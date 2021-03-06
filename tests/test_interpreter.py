import unittest
from pycraft import interpreter
from pycraft import expose  
from pycraft import blocks
from pycraft import entity
from pycraft import commands
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

class TestInterpreter(unittest.TestCase):
    def setUp(self):
        self.interpreter = interpreter.Interpreter(None)
        self.namespace = self.interpreter.base_namespace()
        self.namespace['user'] = FakeUser()
        self.interpreter.entities = FakeEntities()
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
            ('entities.ENDER_C',expose.ENTITY_NAMESPACE.ENDER_CRYSTAL),
            ('range(3)',np.arange(3)),
            ('user.position+V(0,1,0)',vec3.Vec3(0,1,0)),
            ('V(z=3)',vec3.Vec3(0,0,3)),
            ('[x*2 for x in range(3)]',[0,2,4]),
            ('[(z,y,x) for (x,y,z) in [(2,3,4)]]', [(4,3,2)]),
            ('[(z,y,x,r) for (x,y,z) in [(2,3,4)] for r in [1,2]]', [(4,3,2,1),(4,3,2,2)]),
            ('[x for y in range(3) for x in range(y)]',[0,0,1]),
            ('tuple(x*2 for x in range(3))',(0,2,4)),
            ('{ x:y for (x,y) in [(1,2),(3,4)]}',{1:2,3:4}),
            ('{ x for (x,y) in [(1,2),(3,4)]}',{1,3}),
            # ('[sin(x) for x in [1,2,3]]',[np.sin(x) for x in [1,2,3]]),
        ]:
            parsed = ast.parse(
                statement,
                'chat.py',
                'eval',
            )
            print(ast.dump(parsed))
            result = self.interpreter.interpret_expr(parsed, self.namespace)
            if isinstance(expected, np.ndarray):
                assert np.allclose(result,expected)
            else:
                assert result==expected,(statement,result)
    
    def test_failures(self):
        for statement,expected in [
            ('[32',SyntaxError),
            ('[1,2,3].__module__',ValueError),
        ]:
            try:
                parsed = ast.parse(
                    statement,
                    'chat.py',
                    'eval',
                )
                print(ast.dump(parsed))
                result = self.interpreter.interpret_expr(parsed, self.namespace)
                assert False, "Should have raised an error"
            except Exception as err:
                assert isinstance(err, expected), (statement, err)
    def test_V(self):
        V = commands.V
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
        self.interpreter.interpret(message)
        assert self.interpreter.user_namespaces == {
            4: {'a':3},
        }
        assert self.interpreter.interpret(FakeMessage({
            'message': 'echo(a)',
            'entityId': 4,
        })) == 3
    def test_resolve(self):
        for name,expected in [
            ('bed',blocks.BED),
            ('CRACKED_STONE_BRICKS',blocks.CRACKED_STONE_BRICKS),
            ('white concrete',blocks.WHITE_CONCRETE)
        ]:
            result = getattr(expose.BLOCK_NAMESPACE,name)
            assert result == expected, (name,result)
        