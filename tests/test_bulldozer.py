import unittest
from pycraft import bulldozer, uniqueblocks
import ast
import numpy as np
from mcpi import vec3, block

class TestBulldozer(unittest.TestCase):
    def test_generation(self):
        for step in (.25,.5,1):
            blocks = list(bulldozer.generate_blocks_ahead(
                vec3.Vec3(0,0,0),
                vec3.Vec3(0,0,1),
                depth=1,
                width=2,
                height=2,
                step=step,
            ))
            assert blocks 
            steps = 1/step
            assert len(blocks) == (1*steps)*(2*steps)*(2*steps), len(blocks)
            # assert False, blocks
    def test_unique(self):
        duplicates = np.array([
            [1.2,1,0],
            [1.25,1,0],
            [1.22,1.3,0],
            [1.2,1,0.4],
            [1.2,1.8,0],
            [1.2,1.9,0.2],
        ],dtype='f')
        result = list(uniqueblocks.unique_blocks_only(
            duplicates
        ))
        assert len(result) == 1, result
    