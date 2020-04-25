import unittest
from pycraft import chatcommands
from pycraft import expose
from pycraft import blocks
import ast
import numpy as np
from mcpi import vec3
class FakeUser(object):
    position = vec3.Vec3(0,0,0)
class FakeMessage(object):
    def __init__(self, attrs):
        self.__dict__.update(attrs)
class FakeEntities(object):
    def get_entity_name(self, id):
        return 'Moo'
    def get_entity_position(self, id):
        return vec3.Vec3(42,42,42)

class TestChatCommands(unittest.TestCase):
    def setUp(self):
        self.listener = chatcommands.ChatListener(None)
        self.namespace = self.listener.base_namespace()
        self.namespace['user'] = FakeUser()
        self.listener.entities = FakeEntities()
    def test_expressions(self):
        for statement,expected in [
            ("'this'",'this'),
            ('23',23),
            ('(1,2,3)',(1,2,3)),
            ('sin(3)',np.sin(3)),
            ('cos(3)',np.cos(3)),
            ('(1,2,3)+(3,4,5)',(1,2,3,3,4,5)),
            ('"""those"""', 'those'),
            ('[1,2,3]',[1,2,3]),
            ('[1,2,3][2]',3),
            ('[1,2,3,4][::2]',[1,3]),
            ('[sin(2)+1,3]',[np.sin(2)+1,3]),
            ('blocks.AIR',blocks.AIR),
            ('entities.ENDER_C',expose.entities.ENDER_CRYSTAL),
            ('range(3)',np.arange(3)),
            ('user.position+V(0,1,0)',vec3.Vec3(0,1,0)),
            ('V(z=3)',vec3.Vec3(0,0,3)),
            # ('[sin(x) for x in [1,2,3]]',[np.sin(x) for x in [1,2,3]]),
        ]:
            parsed = ast.parse(
                statement,
                'chat.py',
                'eval',
            )
            print(ast.dump(parsed))
            result = self.listener.interpret_expr(parsed, self.namespace)
            if isinstance(expected, np.ndarray):
                assert np.allclose(result,expected)
            else:
                assert result==expected,(statement,result)
    
    def test_failures(self):
        for statement,expected in [
            ('[32',SyntaxError),
            ('[int(i) for i in [1,2,3]]',ValueError),
            ('[1,2,3].__module__',ValueError),
        ]:
            try:
                parsed = ast.parse(
                    statement,
                    'chat.py',
                    'eval',
                )
                print(ast.dump(parsed))
                result = self.listener.interpret_expr(parsed, self.namespace)
                assert False, "Should have raised an error"
            except Exception as err:
                assert isinstance(err, expected), (statement, err)
    def test_V(self):
        V = chatcommands.V
        for i,(result,expected) in enumerate([
            (
                V([1,2,3]),
                vec3.Vec3(1,2,3),
            ),
            (
                V(1),
                vec3.Vec3(1),
            ),
            (
                V(z=1),
                vec3.Vec3(0,0,1),
            ),
            (
                V((1,2,3)),
                vec3.Vec3(1,2,3),
            ),
        ]):
            assert result==expected,(i,result,expected)
    
    def test_assignment(self):
        message = FakeMessage({
            'message': '3',
            'entityId': 4,
            'assignment': 'a',
        })
        self.listener.interpret(message)
        assert self.listener.user_namespaces == {
            4: {'a':3},
        }
        assert self.listener.interpret(FakeMessage({
            'message': 'echo(a)',
            'entityId': 4,
        })) == 'Moo: 3'
    def test_resolve(self):
        for name,expected in [
            ('bed',blocks.BED),
            ('CRACKED_STONE_BRICKS',blocks.CRACKED_STONE_BRICKS),
            ('white concrete',blocks.WHITE_CONCRETE)
        ]:
            result = expose.as_block(name)
            assert result == expected, (name,result)
        