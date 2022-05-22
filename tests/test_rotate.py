from pycraft import rotations


def test_rotate():
    mat = 'minecraft:smooth_quartz_stairs[facing=west,half=bottom,shape=straight,waterlogged=false]'
    for count, expected in [
        (
            1,
            'minecraft:smooth_quartz_stairs[facing=north,half=bottom,shape=straight,waterlogged=false]',
        ),
        (
            2,
            'minecraft:smooth_quartz_stairs[facing=east,half=bottom,shape=straight,waterlogged=false]',
        ),
        (
            3,
            'minecraft:smooth_quartz_stairs[facing=south,half=bottom,shape=straight,waterlogged=false]',
        ),
    ]:
        result = rotations.rotate(mat, count)
        assert (
            result == expected
        ), f"Rotate failure for {count} expected {expected} got {result}"
