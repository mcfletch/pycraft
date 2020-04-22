import unittest
import chatcommands
import ast
import numpy as np

class TestChatCommands(unittest.TestCase):
    def setUp(self):
        self.listener = chatcommands.ChatListener(None)
    def test_expressions(self):
        namespace = chatcommands.DEFAULT_NAMESPACE
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
        ]:
            parsed = ast.parse(
                statement,
                'chat.py',
                'eval',
            )
            result = self.listener.interpret_expr(parsed, namespace)
            assert result==expected,(statement,result)