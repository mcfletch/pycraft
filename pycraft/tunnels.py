"""Create transportation"""
# from mcpi import minecraft, vec3
from pycraft import directions
from .server.world import Vector, World, Block, Location
from . import randomchoice
import numpy as np
import random, os
import logging
from . import expose
from .bulldozer import roughly_forward

HERE = os.path.dirname(os.path.abspath(__file__))
log = logging.getLogger(__name__)


@expose.expose()
async def tunnel(
    depth=25,
    width=3,
    height=3,
    walls='glass',
    floor='glass',
    ceiling='glass',
    position=None,
    direction=None,
    *,
    player=None,
    player_storage=None,
    mc=None,
):
    """Create a pyramid centered at position in material

    position -- start position
    direction -- rough direction to go (must be a unit block direction)
    width -- size in the x direction
    depth -- size in the y direction
    material -- name of the material to use
    zstep -- 1 for upward, -1 for downward
    """
    log.info("Position %s direction %s", position, direction)

    if direction is None and position is None:
        storage = player_storage()
    if direction is None:
        direction = player.direction
    if position is None:
        position = player.position
    direction, cross = directions.forward_and_cross(direction)
    if not direction[1]:
        up = np.array((0, 1, 0), dtype='f')
    else:
        up = np.array([0, 0, 1], dtype='f')

    start = position + direction
    log.info("Start %s direction %s", start, direction)

    # walls...
    left_front_bottom = start + (cross * (-width // 2 - 1)) - up
    right_front_bottom = left_front_bottom + (cross * (width + 2))
    left_back_top = left_front_bottom + (up * (height + 2)) + (direction * depth)
    right_back_top = right_front_bottom + (up * (height + 2)) + (direction * depth)

    world = World(name=player.location.world)

    await world.oldSetBlocks(
        *left_front_bottom[:3],
        *left_back_top[:3],
        walls,
    )
    await world.oldSetBlocks(
        *right_front_bottom[:3],
        *right_back_top[:3],
        walls,
    )
    inner_lfb = left_front_bottom + cross
    inner_lbt = left_back_top + cross
    inner_rfb = right_front_bottom - cross
    inner_rbt = right_back_top - cross
    # floor
    await world.oldSetBlocks(
        *inner_lfb[:3],
        *(inner_rfb + (direction * depth))[:3],
        floor,
    )
    await world.oldSetBlocks(
        *inner_lbt[:3],
        *(inner_rbt - (direction * depth))[:3],
        ceiling,
    )
    # carve out the inner space...
    await world.oldSetBlocks(
        *(inner_lfb + up)[:3],
        *(inner_rbt - up)[:3],
        'air',
    )

    TORCH_DIR = {
        (0, 0, -1): 'wall_torch[facing=west]',
        (0, 0, 1): 'wall_torch[facing=east]',
        (1, 0, 0): 'wall_torch[facing=south]',
        (-1, 0, 0): 'wall_torch[facing=north]',
    }

    # setup some torches every once in a while...
    torch_pos = inner_lbt - (up)  # one below ceiling...
    for step in range(0, depth, 5):
        await Block(location=torch_pos - (direction * step)).setBlockData(
            TORCH_DIR.get(tuple(direction[:3]))
        )

    # setup some windows so the players can see...
    window_pos = left_back_top - (up)  # one below ceiling...
    glass = randomchoice.RANDOM_STAINED_GLASS

    for step in range(1, depth, 5):
        window_depth = window_pos - (direction * step)
        await world.oldSetBlocks(
            *(window_depth[:3]), *(window_depth - (up * 2))[:3], glass
        )
        await world.oldSetBlocks(
            *(window_depth + (cross * (width + 2)))[:3],
            *(window_depth - (up * 2) + (cross * (width + 2)))[:3],
            glass,
        )
    player_storage()[TUNNEL_CONTINUE_KEY] = (
        width,
        height,
        walls,
        floor,
        ceiling,
        start + (direction * depth),
        direction,
    )


TUNNEL_CONTINUE_KEY = '__current_tunnel__'


@expose.expose()
async def tunnel_continue(depth=25, *, player=None, player_storage=None):
    """Continue the previously started tunnel"""
    log.info("Starring")
    storage = player_storage()
    params = storage.get(TUNNEL_CONTINUE_KEY)
    if not params:
        return 'Sorry, I have forgotten where the tunnel was'
    return await tunnel(depth, *params, player=player, player_storage=player_storage)


@expose.expose(name='fr')
async def fast_rail(
    depth=100,
    position=None,
    direction=None,
    base=None,
    *,
    player=None,
    world=None,
):
    """Create a powered railroad going forward from the player's position

    Creates powered rail sections so that your minecart will accelerate down the rail-path
    """
    if direction is None:
        direction = player.direction
    if position is None:
        position = player.tile_position + player.direction
    direction, cross = directions.forward_and_cross(direction)
    if depth < 0:
        direction = direction * np.array((-1, -1, -1))
        depth = -depth

    #     # 0 z-straight
    #     # 1 x-straight
    #     # 2 up-west
    #     # 3 up-east
    #     # 4 up-south
    #     # 5 up-north
    #     # 6 NW join
    #     # 7 NE join
    #     # 8 SE join
    #     # 9 SW join

    if np.abs(direction[2]):  # N/S direction
        shape = 'north_south'
    else:
        shape = 'east_west'

    if base:
        await world.oldSetBlocks(
            *(position[:3]),
            *(position + (direction * depth))[:3],
            base,
        )
    down = Vector(0, -1, 0)

    air_start = position + Vector(0, 1, 0)
    air_end = air_start + (direction * depth) + Vector(0, 1, 0)
    await world.oldSetBlocks(
        *(air_start[:3]),
        *(air_end[:3]),
        'air',
    )

    # Now generate the actual track segments...
    # Always start and end with a powered-rail that has no power...

    locations, blocks = [
        air_start,
        air_start + direction,
    ], [f'powered_rail[shape={shape}]', f'rail[shape={shape}]']

    for offset in range(2, depth - 2, 8):
        for i in range(8):
            locations.append(air_start + (direction * (offset + i)))
            if i <= 4:
                blocks.append(f'powered_rail[shape={shape}]')
            else:
                blocks.append(f'rail[shape={shape}]')
        if base:
            locations.append(air_start + (direction * (offset + 4)) + cross + down)
            blocks.append(base)
        locations.append(air_start + (direction * (offset + 4)) + cross)
        blocks.append('redstone_torch')

    locations.append(air_start + (direction * (depth - 1)))
    blocks.append(f'rail[shape={shape}]')
    locations.append(air_start + (direction * depth))
    blocks.append(f'powered_rail[shape={shape}]')

    await world.setBlockList(locations, blocks)
