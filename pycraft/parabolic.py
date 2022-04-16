"""Draw a parabolic dome over the player"""
import numpy as np
import logging
from . import expose, uniqueblocks, randomchoice, directions
from .server import final
from .server.world import Vector

log = logging.getLogger(__name__)


@expose.expose(name='circle')
async def draw_circle(
    center=None,
    radius=4,
    material='stone',
    start_angle=0,
    stop_angle=np.pi * 2,
    steps=None,
    *,
    player=None,
    world=None,
):
    """Draw a horizontal circle around center with radius"""
    if center is None:
        center = player.position
    locations, materials = generate_circle(
        center,
        radius,
        material=material,
        start_angle=start_angle,
        stop_angle=stop_angle,
        steps=steps,
    )
    await world.setBlockList(locations, materials)


def generate_circle(
    center, radius, material, start_angle=0, stop_angle=np.pi * 2, steps=None
):
    x, y, z = center[:3]
    steps = steps or (2 * np.pi * radius)

    def coord(angle):
        return (
            (np.sin(angle) * radius),
            0,
            (np.cos(angle) * radius),
        )

    raw_positions = [
        coord(angle) for angle in np.arange(0, stop_angle + 0.01, (2 * np.pi) / (steps))
    ]
    # log.info('Raw positions: %s', raw_positions)
    # positions = uniqueblocks.unique_blocks_only(raw_positions)
    positions = raw_positions
    locations, materials = [], []
    for position in positions:
        # print([round(x),round(y),round(z)])
        locations.append(center + position)
        materials.append(material)
    return locations, materials


@expose.expose(name='p_dome')
async def parabolic_dome(
    center=None,
    height=10,
    relaxation=4,
    material=randomchoice.RANDOM_STAINED_GLASS,
    start_angle=0,
    stop_angle=np.pi * 2,
    steps=None,
    *,
    player=None,
    world=None,
):
    """Draw a parabolic dome at given bottom-center and height

    A parabolic dome is created with:

        radius = sqrt(y*relaxation)

    where each y-level is rendered with circle() and
    with invert the whole structure to get a dome
    instead of a cup...

    center defaults to the player's current position
    """
    if center is None:
        center = player.position
    yes = np.arange(1, height + 1)
    zes = np.sqrt(yes * relaxation)
    yes = yes
    locations, materials = [], []
    for h, rad in zip(yes, zes):
        slice_loc, slice_mat = generate_circle(
            center + Vector(0, height - h, 0), rad, material=material
        )
        locations.extend(slice_loc)
        materials.extend(slice_mat)
    await world.setBlockList(locations, materials)


@expose.expose()
async def dome(
    center=None,
    radius=10,
    material=randomchoice.RANDOM_STAINED_GLASS,
    start_angle=0,
    stop_angle=np.pi * 2,
    steps=None,
    *,
    player=None,
):
    if center is None:
        center = player.position
    height = radius
    yes = np.arange(1, radius + 1)
    angles = np.arcsin(yes / radius)
    zes = np.cos(angles * radius)
    for h, rad in zip(yes, zes):
        await draw_circle(center + (0, height - h, 0), rad, material=material)


def circle_coords(center, radius=10):
    """Generate set of center-coords around the middle of the center block"""
    cx, cy, cz = [int(i) + 0.5 for i in center]
    for z in np.arange(cz - radius, cz + radius + 0.1, 1.0):
        for x in np.arange(cx - radius, cx + radius + 0.1, 1.0):
            delta = np.array((x - cx, z - cz), dtype='f')
            distance = np.sqrt(np.sum(delta * delta))
            if distance < radius:
                yield (x, cy, z)
