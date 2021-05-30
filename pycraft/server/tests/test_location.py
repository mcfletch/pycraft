from pycraft.server import world
import numpy as np


def test_location_operations():
    player = world.Player(
        __namespace__='Player',
        __type__='CraftPlayer',
        name='VRPlumber',
        last_played=1621136158590.0,
        location=[
            'world',
            -136.70730311379822,
            63.0,
            91.53075199115258,
            0,
            0,
        ],
        type='minecraft:player',
        display_name='VRPlumber',
        uuid='a57d84d6-02eb-354d-90ec-25e6779b2400',
    )
    assert np.allclose(
        player.location[:3], [-136.7073, 63, 95.5307], rtol=0.1, atol=0.01
    )
    forward = player.location + player.direction
    assert np.allclose(forward[:3], [-136.7073, 63, 96.5307], rtol=0.1, atol=0.01)

    block = player.location.block_location()
    assert np.allclose(block[:3], [-136, 63, 96], rtol=0.1, atol=0.01)