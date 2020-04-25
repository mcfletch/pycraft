import unittest
from pycraft import blocks

class TestBlock(unittest.TestCase):
    def test_block_names(self):
        assert blocks.AIR.name == 'AIR'
        # import ipdb;ipdb.set_trace()
        assert blocks.Block.as_instance(0).name == 'AIR'
        assert blocks.Block.as_instance('AIR').id == 0
        assert 'AIR' in str(blocks.AIR), str(blocks.AIR)

    def test_eblock_creation(self):
        assert blocks.WHITE_CONCRETE.sub_types
        assert blocks.RED_CONCRETE.sub_types
    
    def test_random_type(self):
        glass = blocks.WHITE_STAINED_GLASS
        rand = glass.random_subtype()
        seen = set()
        for i in range(100):
            seen.add( rand.data )
        assert len(seen) > 1, seen # 100 samples produced 100 of the same value?
        assert  blocks.Block.as_instance(rand) is rand

    