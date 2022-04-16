"""Clear (create) a set of blocks in front of the player"""
import numpy as np
import logging
from .server.world import Vector, Location
from .server import final
from . import expose
from .directions import roughly_forward, as_cube, forward_and_cross

log = logging.getLogger(__name__)


@expose.expose()
async def bulldoze(
    depth=10,
    width=6,
    height=2,
    material='minecraft:air',
    location=None,
    *,
    player=None,
    world=None,
):
    """Set blocks ahead of the player to the given material

    This (loosely) aligns the block of material with the direction
    the player is currently facing, so it wipes out whatever
    is in front of you.
    """
    # x, y, z = position = player.position[:3]
    direction = player.direction
    if location is not None:
        position = location
    else:
        position = player.position.block_location()
        log.info("Raw position: %s and direction %s", position, direction)

    forward, cross = forward_and_cross(direction)

    log.info("Forward: %s Cross: %s", forward, cross)

    start = position + forward + (-cross * (width // 2))
    stop = (
        start
        + (cross * (width - 1))
        + (forward * (depth - 1))
        + (Vector(0, 1, 0) * (height - 1))
    )
    log.info("Start: %s Stop: %s", start, stop)

    start, size = as_cube(start, stop)

    log.info("Start: %s Size: %s", start, size)

    if material:
        await world.setBlocks(
            start,
            size,
            material,
        )
    else:
        await world.breakBlocks(
            start,
            size,
        )


@expose.expose()
async def strip_mine(depth=50, offset=7, *, player=None, world=None):
    """Set explosive charges every step steps forward"""
    position = player.position
    direction = player.direction
    forward = one_step = roughly_forward(direction)
    forward = Vector(forward.x, forward.y, forward.z)
    current = position + (forward * offset)
    for i in range(offset):
        current = current + forward
    start, size = as_cube(current, current + forward * depth)
    await world.setBlocks(start, size, 'tnt')
    in_front = current - one_step
    await final.Block(location=in_front).setBlockData('redstone_torch')
    return "Fire in the hold!"
