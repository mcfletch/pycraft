"""Code evaluation endpoint — wraps AInterpreter for web use"""
import ast
import io
import logging
import sys
from typing import Coroutine

from aiohttp import web

from pycraft.ainterpreter import AInterpreter
from pycraft.expose import get_base_namespace

from ..serialization import serialize

log = logging.getLogger(__name__)


async def _build_namespace(channel, interpreter, player_uuid=None):
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
    else:
        try:
            worlds = await channel.server.getWorlds()
            if worlds:
                namespace['world'] = worlds[0]
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

    try:
        interpreter = AInterpreter(channel)
        namespace = await _build_namespace(channel, interpreter, player_uuid)

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
        return web.json_response({'error': str(err)})
