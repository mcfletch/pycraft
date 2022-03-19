import unittest
from pycraft import bulldozer, uniqueblocks
import ast
import numpy as np


class TestUniqueBlocks(unittest.TestCase):
    def test_unique(self):
        duplicates = np.array(
            [
                [1.2, 1, 0],
                [1.25, 1, 0],
                [1.22, 1.3, 0],
                [1.2, 1, 0.4],
                [1.2, 1.8, 0],
                [1.2, 1.9, 0.2],
            ],
            dtype='f',
        )
        result = list(uniqueblocks.unique_blocks_only(duplicates))
        assert len(result) == 1, result
