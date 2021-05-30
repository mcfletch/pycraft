import unittest
from pycraft import randomchoice


class TestBlock(unittest.TestCase):
    def test_random_type(self):
        r = randomchoice.RANDOM_STAINED_GLASS
        choices = set()
        for i in range(1000):
            m = r.__json__()
            choices.add(m)
        assert len(choices) == len(r.choices)
