"""Sample script for pycraft"""
from pycraft.expose import expose


@expose()
async def hello():
    return "Hello World! Let's Craft"


@expose()
async def whoami(*, player=None):
    """Echo back the user's name"""
    return player.name


@expose()
async def whereami(*, player=None):
    """Echo back the user's location"""
    return player.location


@expose()
async def cat(*, player=None, world=None):
    """Spawn a can in front of the player"""
    await world.spawnEntity(player.location + player.forward, 'minecraft:cat')


@expose()
async def box(material, *, player=None, world=None):
    """Create a 5x5 box around the player"""

    materials, positions = [], []
    # we start from a position 2 blocks left and back from the player's current position
    start = player.position + player.left + player.left + player.back + player.back
    # we want to make three layers
    for layer in start, start + (0, 1, 0), start + (0, 2, 0):
        # for each layer, draw the sides
        for i in range(0, 5):
            # left wall
            materials.append(material)
            positions.append(layer + (player.forward * i))
            # right wall
            materials.append(material)
            positions.append(layer + (player.right * 4) + (player.forward * i))

        # and draw the front and back walls...
        for j in range(1, 4):
            # back-wall
            materials.append(material)
            positions.append(layer + (player.right * j))
            # back-wall
            materials.append(material)
            positions.append(layer + (player.forward * 4) + (player.right * j))

    await world.setBlockList(positions, materials)
