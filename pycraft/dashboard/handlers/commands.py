"""Code evaluation endpoint — wraps AInterpreter for web use"""
import ast
import io
import logging
import sys
import traceback as tb_module
from typing import Coroutine

from aiohttp import web

from pycraft.ainterpreter import AInterpreter
from pycraft.expose import get_base_namespace
from pycraft.server import world as world_module

from ..serialization import serialize

log = logging.getLogger(__name__)


class FakeMapPlayer:
    """A synthetic player-like object anchored at the map's focus point, always facing north.

    Used when no real player is selected in the dashboard map, so that exposed
    functions that depend on a player's position and direction still work correctly.
    North in Minecraft corresponds to yaw=180 (-Z direction).
    """

    name = '<map>'
    is_real_player = False

    def __init__(self, x, y, z, world_name):
        # yaw=180 → facing north (-Z direction)
        self.location = world_module.Location([world_name, float(x), float(y), float(z), 180.0, 0.0])

    @property
    def position(self):
        return self.location

    @property
    def direction(self):
        return self.location.direction

    @property
    def forward_and_cross(self):
        from pycraft import directions
        return directions.forward_and_cross(self.direction)

    @property
    def forward(self):
        return self.forward_and_cross[0]

    @property
    def back(self):
        return -self.forward_and_cross[0]

    @property
    def backward(self):
        return -self.forward_and_cross[0]

    @property
    def left(self):
        return -self.forward_and_cross[1]

    @property
    def right(self):
        return self.forward_and_cross[1]

    @property
    def tile_position(self):
        return self.location.__floor__() - (0, 1, 0)


async def _build_namespace(channel, interpreter, player_uuid=None, map_context=None):
    """Build a pycraft namespace with optional player context"""
    namespace = get_base_namespace()
    namespace['mc'] = channel
    namespace['server'] = channel.server
    namespace['interpreter'] = interpreter

    if player_uuid:
        players = await channel.server.getOnlinePlayers()
        for p in players:
            if str(getattr(p, 'uuid', '')) == player_uuid:
                namespace['player'] = p
                namespace['user'] = p
                try:
                    namespace['world'] = p.location.get_world()
                except Exception:
                    pass
                break

    if 'player' not in namespace:
        # No real player — inject a FakeMapPlayer so position/direction-based commands work
        if map_context:
            x = map_context.get('x', 0)
            y = map_context.get('y', 64)
            z = map_context.get('z', 0)
            world_name = map_context.get('world', '')
        else:
            # No map context (e.g. standalone code editor): use world spawn or defaults
            x, y, z, world_name = 0, 64, 0, ''
            try:
                worlds = await channel.server.getWorlds()
                if worlds:
                    world_name = worlds[0].name
            except Exception:
                pass
        fake = FakeMapPlayer(x=x, y=y, z=z, world_name=world_name)
        namespace['player'] = fake
        namespace['user'] = fake

    if 'world' not in namespace:
        try:
            namespace['world'] = namespace['player'].location.get_world()
        except Exception:
            pass

    return namespace


async def _eval_statements(interpreter, code, namespace):
    """Execute multi-statement code, returning the result of the last expression.

    Splits the code into individual statements. Each statement is evaluated:
    - Assignments update the namespace
    - Expressions are evaluated and the last one's result is returned
    - Print output is captured
    """
    tree = ast.parse(code, 'web.py', 'exec')
    result = None
    output = io.StringIO()

    # Inject a print function that captures to our buffer
    original_print = namespace.get('print', print)

    def captured_print(*args, **kwargs):
        kwargs.setdefault('file', output)
        original_print(*args, **kwargs)

    namespace['print'] = captured_print

    for node in tree.body:
        if isinstance(node, ast.Expr):
            # Pure expression — evaluate it
            result = await interpreter.interpret_expr(node.value, namespace=namespace)
        elif isinstance(node, ast.Assign):
            # Assignment: evaluate RHS, assign to LHS names
            value = await interpreter.interpret_expr(node.value, namespace=namespace)
            for target in node.targets:
                if isinstance(target, ast.Name):
                    namespace[target.id] = value
                elif isinstance(target, ast.Tuple):
                    for i, elt in enumerate(target.elts):
                        if isinstance(elt, ast.Name):
                            namespace[elt.id] = value[i]
            result = value
        elif isinstance(node, ast.AugAssign):
            # Augmented assignment (+=, etc.)
            current = await interpreter.interpret_expr(node.target, namespace=namespace)
            value = await interpreter.interpret_expr(node.value, namespace=namespace)
            op_map = {
                ast.Add: lambda a, b: a + b,
                ast.Sub: lambda a, b: a - b,
                ast.Mult: lambda a, b: a * b,
                ast.Div: lambda a, b: a / b,
            }
            op_func = op_map.get(type(node.op))
            if op_func:
                new_value = op_func(current, value)
            else:
                raise ValueError(f'Unsupported augmented assignment operator: {type(node.op).__name__}')
            if isinstance(node.target, ast.Name):
                namespace[node.target.id] = new_value
            result = new_value
        elif isinstance(node, ast.For):
            # Simple for loop
            iterable = await interpreter.interpret_expr(node.iter, namespace=namespace)
            for item in iterable:
                if isinstance(node.target, ast.Name):
                    namespace[node.target.id] = item
                elif isinstance(node.target, ast.Tuple):
                    for i, elt in enumerate(node.target.elts):
                        if isinstance(elt, ast.Name):
                            namespace[elt.id] = item[i]
                for body_node in node.body:
                    if isinstance(body_node, ast.Expr):
                        result = await interpreter.interpret_expr(body_node.value, namespace=namespace)
                    elif isinstance(body_node, ast.Assign):
                        value = await interpreter.interpret_expr(body_node.value, namespace=namespace)
                        for target in body_node.targets:
                            if isinstance(target, ast.Name):
                                namespace[target.id] = value
                        result = value
        elif isinstance(node, ast.If):
            test_val = await interpreter.interpret_expr(node.test, namespace=namespace)
            branch = node.body if test_val else node.orelse
            for body_node in branch:
                if isinstance(body_node, ast.Expr):
                    result = await interpreter.interpret_expr(body_node.value, namespace=namespace)
                elif isinstance(body_node, ast.Assign):
                    value = await interpreter.interpret_expr(body_node.value, namespace=namespace)
                    for target in body_node.targets:
                        if isinstance(target, ast.Name):
                            namespace[target.id] = value
                    result = value

    captured = output.getvalue()
    return result, captured


async def eval_code(request):
    """POST /api/eval — evaluate Python code in the pycraft namespace

    Supports single expressions (eval mode) and multi-statement scripts (exec mode).
    """
    services = request.app['services']
    channel = services.channel
    try:
        data = await request.json()
    except Exception:
        return web.json_response({'error': 'Invalid JSON body'}, status=400)
    code = data.get('code', '').strip()
    if not code:
        return web.json_response({'error': 'No code provided'}, status=400)
    player_uuid = data.get('player_uuid')
    map_context = data.get('map_context')

    try:
        interpreter = AInterpreter(channel)
        namespace = await _build_namespace(channel, interpreter, player_uuid, map_context)

        # Try eval mode first (single expression)
        try:
            top = ast.parse(code, 'web.py', 'eval')
            result = await interpreter.interpret_expr(top, namespace=namespace)
            serialized = serialize(result)
            return web.json_response({'result': serialized})
        except SyntaxError:
            pass

        # Fall back to exec mode (multi-statement)
        try:
            result, captured = await _eval_statements(interpreter, code, namespace)
            response = {}
            if captured:
                response['output'] = captured
            if result is not None:
                response['result'] = serialize(result)
            if not response:
                response['result'] = None
            return web.json_response(response)
        except SyntaxError as err:
            return web.json_response({
                'error': f'Syntax error: {err.msg}',
                'line': err.lineno,
                'offset': err.offset,
            })
    except Exception as err:
        log.exception("Error evaluating code: %s", code)
        return web.json_response({'error': str(err), 'traceback': tb_module.format_exc()})
