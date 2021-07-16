"""Create building-like structures for players"""
from pycraft.directions import as_cube
import numpy as np
import random, os
import logging
from . import expose, directions, randomchoice
from .server.world import World, Vector

HERE = os.path.dirname(os.path.abspath(__file__))
log = logging.getLogger(__name__)


@expose.expose()
async def pyramid(
    position=None,
    width=15,
    depth=15,
    material='iron_block',
    ystep=1,
    hollow=False,
    *,
    player=None,
):
    """Create a pyramid in front of the player

    position -- where to create it, the pyramid's top will be in front of this position
    width -- size in the x direction
    depth -- size in the y direction
    material -- name of the material to use
    zstep -- 1 for upward, -1 for downward
    """
    if position is None:
        position = player.position + player.direction
    forward, cross = directions.forward_and_cross(Vector(player.direction))
    current = position - (cross * width // 2)
    for i in range(0, min(width, depth), 2):
        start, size = as_cube(current, current + forward * depth + cross * width)
        await World(name=position.world).setBlocks(start, size, material)
        if hollow:
            await World(name=position.world).setBlocks(
                start + Vector(1, 0, 1), size - Vector(2, 0, 2), 'air'
            )
        current = current + forward + cross + Vector(0, ystep, 0)
        width = width - 2
        depth = depth - 2


@expose.expose()
async def hall(
    position=None,
    width=8,
    depth=13,
    height=4,
    wall_material='minecraft:polished_andesite',
    floor_material='minecraft:stone_bricks',
    carpet_material='minecraft:red_carpet',
    roof_material='minecraft:red_glazed_terracotta',
    *,
    player=None,
):
    if position is None:
        position = player.position
    x, y, z = [int(c) for c in position[:3]]
    left = x - width // 2
    right = left + width
    front = z - depth // 2
    back = front + depth
    bottom = y - 1
    top = y + height
    world = World(name=position.world)

    # clear
    await world.oldSetBlocks(
        left + 1,
        bottom + 1,
        front + 1,
        right - 1,
        top,
        back - 1,
        'air',
    )
    # subfloor...
    await world.oldSetBlocks(
        left,
        bottom - 1,
        front,
        right,
        bottom,
        back,
        floor_material,
    )
    if width > 4 and depth > 4:
        # Carpet on top...
        await world.oldSetBlocks(
            left + 2,
            bottom,
            front + 2,
            right - 2,
            bottom,
            back - 2,
            carpet_material,
        )
    # walls...
    for start, stop in [
        ((left, bottom, front), (right, top, front)),
        ((left, bottom, front), (left, top, back)),
        ((left, bottom, back), (right, top, back)),
        ((right, bottom, front), (right, top, back)),
    ]:
        await world.oldSetBlocks(
            *start,
            *stop,
            wall_material,
        )
    # front doorway
    front_blocks = width - 1
    log.info("Front blocks: %s", front_blocks)
    if front_blocks % 2:
        doorwidth = 1
    else:
        doorwidth = 2
    log.info("Width of %s means door width is %s", width, doorwidth)
    delta = (front_blocks - doorwidth) // 2
    log.info("delta %s", delta)
    doorleft = left + delta + 1
    await world.oldSetBlocks(
        doorleft,
        bottom + 1,
        front,
        doorleft + (doorwidth - 1),
        bottom + 2,
        front,
        'air',
    )
    await world.setBlock(
        doorleft,
        bottom + 1,
        front,
        'minecraft:dark_oak_door[facing=north,half=lower,hinge=right,open=false,powered=false]',
    )  # facing North
    await world.setBlock(
        doorleft,
        bottom + 2,
        front,
        'minecraft:dark_oak_door[facing=north,half=upper,hinge=right,open=false,powered=false]',
    )  # upper part
    # Cornice...
    roofstart, roofstop = left - 1, right + 1
    roofy = top
    while roofstart <= roofstop:
        await world.oldSetBlocks(
            roofstart,
            roofy,
            front - 1,
            roofstart,
            roofy,
            back + 1,
            roof_material,
        )
        await world.oldSetBlocks(
            roofstop,
            roofy,
            front - 1,
            roofstop,
            roofy,
            back + 1,
            roof_material,
        )
        await world.oldSetBlocks(
            roofstart + 1,
            roofy,
            front,
            roofstop - 1,
            roofy,
            front,
            wall_material,
        )
        await world.oldSetBlocks(
            roofstart + 1,
            roofy,
            back,
            roofstop - 1,
            roofy,
            back,
            wall_material,
        )
        roofstart += 1
        roofstop -= 1
        roofy += 1

    # Torches...
    torches = []
    for step in range(front + 2, back - 2, 3):
        torches.append(step)
        await world.setBlock(
            left + 1,
            bottom + 3,
            step,
            'minecraft:wall_torch[facing=east]',
        )
        await world.setBlock(
            right - 1,
            bottom + 3,
            step,
            'minecraft:wall_torch[facing=west]',
        )
        await world.oldSetBlocks(
            left + 1,
            top + 1,
            step,
            right - 1,
            top + 1,
            step,
            'minecraft:dark_oak_log[axis=x]',
        )
    glass_material = randomchoice.RANDOM_STAINED_GLASS
    for step in range(front + 1, back - 1):
        if not step in torches:
            await world.oldSetBlocks(
                left,
                bottom + 1,
                step,
                left,
                top - 1,
                step,
                glass_material,
            )
            await world.oldSetBlocks(
                right,
                bottom + 1,
                step,
                right,
                top - 1,
                step,
                glass_material,
            )
    await world.setBlock(left + 2, bottom, back - 4, 'minecraft:air')
    await world.setBlock(left + 2, bottom, back - 5, 'minecraft:air')

    await world.setBlock(
        left + 2,
        bottom,
        back - 4,
        'minecraft:cyan_bed[facing=south,occupied=false,part=head]',
    )
    await world.setBlock(
        left + 2,
        bottom,
        back - 5,
        'minecraft:cyan_bed[facing=south,occupied=false,part=foot]',
    )

    crafting = left + (width // 2)
    await world.setBlock(
        crafting,
        bottom,
        back - 1,
        'crafting_table',
    )
    await world.setBlock(
        crafting - 1,
        bottom,
        back - 1,
        'furnace',
    )
    await world.setBlock(
        crafting + 1,
        bottom,
        back - 1,
        'chest',
    )
    await world.setBlock(
        crafting + 2,
        bottom,
        back - 1,
        'enchanting_table',
    )
    await world.setBlock(
        crafting - 2,
        bottom,
        back - 1,
        'brewing_stand',
    )
    await world.setBlock(
        crafting - 2,
        bottom,
        back - 2,
        'anvil',
    )


@expose.expose()
async def temple(
    position=None,
    width=17,
    depth=23,
    height=4,  # column/room height
    wall_material='minecraft:quartz_block',
    floor_material='minecraft:smooth_quartz',
    column_material='minecraft:quartz_pillar',
    roof_material='minecraft:white_glazed_terracotta',
    beam_material='minecraft:dark_oak',
    *,
    player=None,
    world=None,
):
    if position is None:
        position = player.position
    if position is None:
        position = player.position + player.direction
    forward, cross = directions.forward_and_cross(Vector(player.direction))

    blocks, positions = [], []

    # plinth

    def block(start, width, depth, height, material):
        """Create a block of width,depth,height starting at start"""
        current = start
        for y in range(height):
            slice = start + (0, y, 0)
            for z in range(depth):
                tranche = slice + (forward * z)
                for x in range(width):
                    block = tranche + (cross * x)
                    blocks.append(material)
                    positions.append(block)

    current = (position + forward + (cross * -(width // 2))).block_location()
    block(current, width, depth, 1, floor_material)
    block(
        current + forward + cross + (0, 1, 0), width - 2, depth - 2, 1, floor_material
    )

    # columns, offset 1m from edge of plinth and 4m high
    def column(start, height=height):
        for i in range(height):
            blocks.append(column_material)
            positions.append(start + (0, i, 0))

    # front row of columns...
    front_left = current + (forward * 2) + (cross * 2) + (0, 2, 0)
    for x in range(0, (width - 5) // 2, 2):
        column(front_left + (cross * x))

    for z in range(0, (depth - 4), 2):
        column(front_left + (forward * z))

    # left wall, behind the columns...
    block(
        front_left + (cross * 2) + (forward * 2),
        width=1,
        depth=(depth - 8),
        height=height,
        material=wall_material,
    )
    half_width = (width - 4) // 2

    front_right = current + (forward * 2) + (cross * (width - 3)) + (0, 2, 0)
    for x in range(0, half_width, 2):
        column(front_right + (cross * -x))

    for z in range(0, (depth - 4), 2):
        column(front_right + (forward * z))

    # right wall, behind the columns...
    block(
        front_right + (cross * -2) + (forward * 2),
        width=1,
        depth=(depth - 8),
        height=height,
        material=wall_material,
    )

    # front wall, leaving a 1-wide opening for the door
    block(
        front_left + (forward * 2) + (cross * 2),
        width=half_width - 3,
        depth=1,
        height=height,
        material=wall_material,
    )
    block(
        front_right + (forward * 2) + (cross * -2) - (cross * (half_width - 4)),
        width=half_width - 3,
        depth=1,
        height=height,
        material=wall_material,
    )

    # back wall
    block(
        front_left + (cross * 2) + (forward * (depth - 7)),
        width=width - 8,
        depth=1,
        height=height,
        material=wall_material,
    )

    # create it
    await world.setBlockList(positions, blocks)
