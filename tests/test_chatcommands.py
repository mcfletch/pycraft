import unittest
from pycraft import chatcommands
import ast
import numpy as np
from mcpi import vec3, block
class FakeUser(object):
    position = vec3.Vec3(0,0,0)

class TestChatCommands(unittest.TestCase):
    def setUp(self):
        self.listener = chatcommands.ChatListener(None)
        self.namespace = chatcommands.DEFAULT_NAMESPACE.copy()
        self.namespace.update(chatcommands.DEFAULT_COMMANDS)
        self.namespace['user'] = FakeUser()
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
            ('block.AIR',chatcommands.block.AIR),
            ('range(3)',list(range(3))),
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
        