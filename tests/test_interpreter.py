import unittest
from pycraft import ainterpreter as interpreter
from pycraft import expose
from pycraft import acommands as commands
from pycraft.server import world
import pytest
import ast
import numpy as np
import uuid


class FakeServer(object):
    pass


class FakeChannel(object):
    server = FakeServer()


class FakeUser(object):
    position = world.Vector(0, 0, 0)
    location = world.Location(['world', (0, 0, 0)])
    name = 'MooUser'
    uuid = uuid.uuid4()


class FakeMessage(object):
    def __init__(self, attrs):
        self.__dict__.update(attrs)


class FakeEntities(object):
    def get_entity_name(self, id):
        return 'Moo'

    def get_entity_position(self, id):
        return world.Vector(42, 42, 42)


@pytest.fixture
def channel_setup():
    class Self:
        pass

    self = Self()
    self.interpreter = interpreter.AInterpreter(FakeChannel())
    self.namespace = self.interpreter.base_namespace(
        sender=FakeUser(),
    )
    self.namespace['user'] = FakeUser()
    return self


@pytest.mark.asyncio
async def test_expressions(channel_setup):
    for statement, expected in [
        ("'this'", 'this'),
        ('23', 23),
        ('(1,2,3)', (1, 2, 3)),
        ('sin(3)', np.sin(3)),
        ('cos(3)', np.cos(3)),
        ('(1,2,3)+(3,4,5)', (1, 2, 3, 3, 4, 5)),
        ('"""those"""', 'those'),
        ('[1,2,3]', [1, 2, 3]),
        ('[1,2,3][2]', 3),
        ('[1,2,3,4][::2]', [1, 3]),
        ('[sin(2)+1,3]', [np.sin(2) + 1, 3]),
        ('range(3)', np.arange(3)),
        ('[x*2 for x in range(3)]', [0, 2, 4]),
        ('[x*2 for x in range(3) if str(x) == "1"]', [2]),
        ('[(z,y,x) for (x,y,z) in [(2,3,4)]]', [(4, 3, 2)]),
        (
            '[(z,y,x,r) for (x,y,z) in [(2,3,4)] for r in [1,2]]',
            [(4, 3, 2, 1), (4, 3, 2, 2)],
        ),
        ('[x for y in range(3) for x in range(y)]', [0, 0, 1]),
        # Regression here, we used to support this...
        ('tuple(x*2 for x in range(3))', (0, 2, 4)),
        ('{ x:y for (x,y) in [(1,2),(3,4)]}', {1: 2, 3: 4}),
        ('{ x for (x,y) in [(1,2),(3,4)]}', {1, 3}),
        ('[sin(x) for x in [1,2,3]]', [np.sin(x) for x in [1, 2, 3]]),
        ('2 in (1,2,3)', True),
    ]:
        parsed = ast.parse(
            statement,
            'chat.py',
            'eval',
        )
        print(ast.dump(parsed))
        try:
            result = await channel_setup.interpreter.interpret_expr(
                parsed, channel_setup.namespace
            )
        except Exception as err:
            err.args += (statement,)
            raise
        if isinstance(expected, np.ndarray):
            assert np.allclose(result, expected)
        else:
            assert result == expected, (statement, result)


@pytest.mark.asyncio
async def test_failures(channel_setup):
    for statement, expected in [
        ('[32', SyntaxError),
        ('[1,2,3].__module__', ValueError),
    ]:
        try:
            parsed = ast.parse(
                statement,
                'chat.py',
                'eval',
            )
            print(ast.dump(parsed))
            result = await channel_setup.interpreter.interpret_expr(
                parsed, channel_setup.namespace
            )
            assert False, "Should have raised an error"
        except Exception as err:
            assert isinstance(err, expected), (statement, err)


@pytest.mark.asyncio
async def test_assignment(channel_setup):
    message = FakeMessage(
        {
            'message': '3',
            'player': channel_setup.namespace['player'],
            'assignment': 'a',
        },
    )
    await channel_setup.interpreter.interpret(message)
    assert channel_setup.interpreter.user_namespaces == {
        channel_setup.namespace['player'].uuid: {'a': 3},
    }
    assert (
        await channel_setup.interpreter.interpret(
            FakeMessage(
                {
                    'message': 'echo(a)',
                    'player': channel_setup.namespace['player'],
                }
            )
        )
        == 3
    )
