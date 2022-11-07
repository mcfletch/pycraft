"""Create building-like structures for players"""
from pycraft.directions import as_cube
import numpy as np
import random, os, typing
import itertools
import logging
from . import expose, directions, randomchoice, rotations
from .server.world import Vector, Block, Location
from .server import final

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
    world=None,
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
        await world.setBlocks(start, size, material)
        if hollow:
            await world.setBlocks(
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
    world=None,
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
    roof_material='minecraft:blue_stained_glass',
    beam_material='minecraft:smooth_quartz',
    beam_support_material='minecraft:smooth_quartz_stairs',
    pediment_top_material='minecraft:green_stained_glass',
    *,
    player=None,
    world=None,
):
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

    left_columns, right_columns, front_columns = [], [], []

    # front row of columns...
    front_left = current + (forward * 2) + (cross * 2) + (0, 2, 0)
    for x in range(0, (width - 5) // 2, 2):
        pos = front_left + (cross * x)
        column(pos)
        front_columns.append(pos)

    for z in range(0, (depth - 4), 2):
        pos = front_left + (forward * z)
        column(pos)
        left_columns.append(pos)

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
        pos = front_right + (cross * -x)
        column(pos)
        front_columns.append(pos)

    for z in range(0, (depth - 4), 2):
        pos = front_right + (forward * z)
        column(pos)
        right_columns.append(pos)

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

    # Cross beams...
    def linprops(base, props):
        if props:
            return '%s[%s]' % (
                base,
                ','.join(['%s=%s' % (k, v) for k, v in props.items()]),
            )
        else:
            return base

    STAIR_DIR = {
        (0, 0, 1): dict(facing='south', half='top'),
        (0, 0, -1): dict(facing='north', half='top'),
        (1, 0, 0): dict(facing='east', half='top'),
        (-1, 0, 0): dict(facing='west', half='top'),
    }
    LEFT = {
        (0, 0, -1): (1, 0, 0),
        (1, 0, 0): (0, 0, 1),
        (0, 0, 1): (-1, 0, 0),
        (-1, 0, 0): (0, 0, -1),
    }
    RIGHT = dict([(v, k) for k, v in LEFT.items()])

    for left, right in zip(left_columns, right_columns):
        start = left + (0, height - 1, 0)
        stop = right + cross + (0, height - 1, 0)
        block(start, width=width - 4, depth=1, height=1, material=beam_material)
        # l_props = STAIR_DIR[LEFT[tuple(forward)]]
        # blocks.append(linprops(beam_support_material, l_props))
        # blocks.append(start)
        # r_props = STAIR_DIR[RIGHT[tuple(forward)]]
        # blocks.append(linprops(beam_support_material, r_props))
        # blocks.append(stop)

    # bottom of the pediment

    facing = STAIR_DIR[tuple(forward)].copy()
    pediment_bottom_material = linprops(beam_support_material, facing)
    left_corner = facing.copy()
    left_corner.update({'shape': 'outer_right'})
    right_corner = facing.copy()
    right_corner.update({'shape': 'outer_left'})
    pediment_left_corner_material = linprops(beam_support_material, left_corner)
    pediment_right_corner_material = linprops(beam_support_material, right_corner)

    front_left_pediment = front_left - cross - (forward * 1) + (0, height - 1, 0)
    block(
        front_left_pediment,
        width=width - 2,
        depth=1,
        height=1,
        material=pediment_bottom_material,
    )
    blocks.append(pediment_left_corner_material)
    positions.append(front_left_pediment)
    blocks.append(pediment_right_corner_material)
    positions.append(front_left_pediment + (cross * (width - 3)))
    # left roof supports

    pediment_left_material = linprops(
        beam_support_material, STAIR_DIR[LEFT[tuple(forward)]].copy()
    )
    pediment_right_material = linprops(
        beam_support_material, STAIR_DIR[RIGHT[tuple(forward)]].copy()
    )

    block(
        front_left_pediment + forward,
        depth=depth - 8,
        width=1,
        height=1,
        material=pediment_left_material,
    )
    block(
        front_left_pediment + forward + (cross * (width - 3)),
        depth=depth - 8,
        width=1,
        height=1,
        material=pediment_right_material,
    )

    # for col in front_columns:
    #     blocks.append(beam_material)
    #     positions.append(col - forward + (0, height - 1, 0))

    # Now the roof
    current = front_left_pediment + (0, 1, 0)
    slice_width = width - 2
    while slice_width > 0:
        tile_width = 2 if slice_width > 1 else 1
        # stone, tile, stone
        block(
            current,
            width=tile_width,
            depth=1,
            height=1,
            material=pediment_top_material,
        )
        block(
            current + forward,
            width=tile_width,
            depth=depth - 2,
            height=1,
            material=roof_material,
        )
        block(
            current + (forward * (depth - 2)),
            width=tile_width,
            depth=1,
            height=1,
            material=pediment_top_material,
        )
        # same, stone, tile, stone

        block(
            current + (cross * (slice_width - tile_width)),
            width=tile_width,
            depth=1,
            height=1,
            material=pediment_top_material,
        )

        block(
            current + (cross * (slice_width - tile_width)),
            width=tile_width,
            depth=depth - 2,
            height=1,
            material=roof_material,
        )
        block(
            current + (cross * (slice_width - tile_width)),
            width=tile_width,
            depth=1,
            height=1,
            material=pediment_top_material,
        )

        slice_width -= 4
        current = current + (cross * 2) + (0, 1, 0)

    # create it
    await world.setBlockList(positions, blocks)


def strip_top_air(materials):
    for item in materials[::-1]:
        item = item[0][0]
        if item == 'minecraft:air':
            del materials[-1]
        else:
            break
    return materials


def until_air(materials):
    for item in materials:
        item = item[0][0]
        if item != 'minecraft:air':
            yield item
        else:
            break


def until_change(materials):
    first = None
    for item in materials:
        item = item[0][0]
        if first is None:
            first = item
        else:
            if item == first:
                yield item
            else:
                break


@expose.expose()
async def column_up(
    material: typing.Union[list, str] = 'chain',
    position=None,
    height: typing.Optional[float] = None,
    to_air: typing.Optional[bool] = False,
    to_surface: typing.Optional[bool] = False,
    *,
    player=None,
    world=None,
):
    """Create a chain in the block in front of you going up to a solid block"""
    if position is None:
        position = player.position + player.direction
    x, y, z = [int(v) for v in position.block_location()[:3]]
    maxHeight = int(await world.getMaxHeight())
    y_height = maxHeight - y - 1
    if y_height < 1:
        return 'At the top of the world'

    above = await world.getBlocks(
        [x, y, z],
        [1, y_height, 1],
    )
    if height:
        above = [layer[0][0] for layer in above[:height]]
    elif to_air:
        above = list(until_air(above))
    elif to_surface:
        above = strip_top_air(above)
        if len(above) < 2:
            return 'Did not find a ceiling'
    else:
        above = list(until_change(above))
        if len(above) < 2:
            return 'Did not find a ceiling'

    if isinstance(material, list):
        next_material = itertools.cycle(material).__next__
    else:

        def next_material():
            return material

    positions, blocks = [position], [next_material()]
    for index, current in enumerate(above[1:]):
        # note that index is -1 from real index
        positions.append(
            position + (0, index + 1, 0)
        )  # one for get offset, one for index offset
        blocks.append(next_material())
    await world.setBlockList(positions, blocks)
    return len(above)


@expose.expose()
async def elevator_up(
    position=None,
    to_surface: typing.Optional[bool] = None,
    height: typing.Optional[float] = None,
    to_air: typing.Optional[bool] = None,
    base: typing.Optional[str] = 'soul_sand',
    *,
    player=None,
    world=None,
):
    """Construct a water-elevator going up"""
    if position is None:
        position = player.position + player.direction
    x, y, z = [int(v) for v in position.block_location()[:3]]
    if to_surface is None and to_air is None and height is None:
        to_air = True
    await world.setBlockList([[position.world, x, y - 1, z]], [base])
    final_height = await column_up(
        material='bubble_column[drag=false]',
        position=position,
        to_air=to_air,
        to_surface=to_surface,
        height=height,
        player=player,
        world=world,
    )
    return final_height


@expose.expose()
async def elevators(
    position=None,
    to_surface: typing.Optional[bool] = None,
    height: typing.Optional[float] = None,
    to_air: typing.Optional[bool] = None,
    walls: typing.Optional[str] = 'glass',
    *,
    player=None,
    world=None,
):
    """Create a full-featured up-and-down bubble elevator with walls as specified

    Bubble elevators let you quickly descend/ascend. The elevator
    here provides a full-featured version of the elevator pattern,
    with one column going up and the other down. The base of the
    elevator column has doors to control the flow of the water.

    To use, go to the base of where you would like to create the
    elevator and face where the doors should be. The options:

    * to_surface -- elevator rises to the top-most piece of land in the column
                    directly in front of you. If there is floating dirt or the
                    like, the elevator will still rise to that level
    * to_air -- elevator rises to the first air-pocket it finds in the column
    * height -- if specified, creates an elevator with an explicit height
                instead of searching for the height

    * walls -- specifies the material used to surround the water columns to
               avoid flooding areas of air through which it passes

    """
    from .acommands import set_sign_text

    forward, cross = directions.forward_and_cross(player.direction)
    up_pos = player.position + forward + forward
    down_pos = up_pos - cross
    if to_surface is None and to_air is None and height is None:
        # default to to_surface because otherwise you wind up with
        # single-block elevators far more often than not...
        to_surface = True
    height = await elevator_up(
        position=up_pos,
        player=player,
        world=world,
        to_surface=to_surface,
        to_air=to_air,
        height=height,
        base='soul_sand',
    )
    assert height, height
    await elevator_up(
        position=down_pos,
        player=player,
        world=world,
        height=height,
        base='magma_block',
    )
    await column_up(
        walls,
        position=up_pos + cross,
        height=height,
        player=player,
        world=world,
    )
    await column_up(
        walls,
        position=down_pos - cross,
        height=height,
        player=player,
        world=world,
    )
    await column_up(
        [walls] * 10 + ['soul_lantern'],
        position=up_pos + forward,
        height=height,
        player=player,
        world=world,
    )
    await column_up(
        [walls] * 10 + ['lantern'],
        position=down_pos + forward,
        height=height,
        player=player,
        world=world,
    )
    await column_up(
        walls,
        position=up_pos - forward + cross,
        height=height,
        player=player,
        world=world,
    )
    await column_up(
        walls,
        position=down_pos - forward - cross,
        height=height,
        player=player,
        world=world,
    )
    await column_up(
        walls,
        position=up_pos - forward + (0, 2, 0),
        height=height - 2,
        player=player,
        world=world,
    )
    await column_up(
        walls,
        position=down_pos - forward + (0, 2, 0),
        height=height - 2,
        player=player,
        world=world,
    )
    # Now need doors or signs at the bottom...
    left = rotations.NESW_NAMES.get(tuple(-cross))
    right = rotations.NESW_NAMES.get(tuple(cross))
    signs = [
        (
            up_pos - forward,
            'oak_wall_sign[facing=%(left)s]' % locals(),
            ['Mind the Sand', 'As you Enter'],
            'BLUE',
        ),
        (
            up_pos - forward + (0, 1, 0),
            'oak_wall_sign[facing=%(left)s]' % locals(),
            'Elevator Up',
            'BLUE',
        ),
        (
            down_pos - forward,
            'oak_wall_sign[facing=%(right)s]' % locals(),
            ['Please', 'Keep Clear', 'Of the Exits'],
            'RED',
        ),
        (
            down_pos - forward + (0, 1, 0),
            'oak_wall_sign[facing=%(right)s]' % locals(),
            'Elevator Down',
            'RED',
        ),
    ]

    await world.setBlockList([sign[0] for sign in signs], [sign[1] for sign in signs])

    for sign_info in signs:
        sign_block = await final.Location(sign_info[0]).getBlock()
        await set_sign_text(sign_info[0], sign_info[2], color=sign_info[3])


@expose.expose()
async def torch_tower(
    position=None,
    height: typing.Optional[float] = None,
    to_air: typing.Optional[bool] = False,
    to_surface: typing.Optional[bool] = False,
    *,
    player=None,
    world=None,
):
    """Construct a redstone torch tower to transmit redstone signal upward"""
    return await column_up(
        [
            'dirt',
            'redstone_torch',
        ],
        position=position,
        height=height,
        to_air=to_air,
        to_surface=to_surface,
        player=player,
        world=world,
    )


@expose.expose()
async def torch_cascade(
    position=None,
    height=None,
    to_air=False,
    to_surface=False,
    *,
    player=None,
    world=None,
):
    forward, cross = directions.forward_and_cross(player.direction)
    position = player.position + forward
    await column_up(
        [
            'dirt',
            'redstone_wire[north=none,west=none,east=none,south=none]',
            'redstone_wall_torch[facing=east]',
            'air',
        ],
        position=position,
        height=height,
        to_air=to_air,
        to_surface=to_surface,
        player=player,
        world=world,
    )
    position = position - (1, 0, 0) + (0, 2, 0)
    await column_up(
        [
            'dirt',
            'redstone_wire[north=none,west=none,east=none,south=none]',
            'redstone_wall_torch[facing=west]',
            'air',
        ],
        position=position,
        height=height if height is None else height - 2,
        to_air=to_air,
        to_surface=to_surface,
        player=player,
        world=world,
    )
