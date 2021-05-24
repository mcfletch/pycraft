"""Draw a parabolic dome over the player"""
import numpy as np
import logging
from . import expose, uniqueblocks, randomchoice, directions
from .server.world import World, Location, Vector, Block

log = logging.getLogger(__name__)


@expose.expose(name='circle')
async def draw_circle(
    center,
    radius,
    material='stone',
    start_angle=0,
    stop_angle=np.pi * 2,
    steps=None,
):
    """Draw a horizontal circle around center with radius"""
    locations, materials = generate_circle(
        center,
        radius,
        material=material,
        start_angle=start_angle,
        stop_angle=stop_angle,
        steps=steps,
    )
    await World(center.world).setBlockList(locations, materials)


def generate_circle(
    center, radius, material, start_angle=0, stop_angle=np.pi * 2 + 0.01, steps=64
):
    x, y, z = center[:3]
    steps = steps or radius * 20

    def coord(angle):
        return (
            (np.sin(angle) * radius),
            0,
            (np.cos(angle) * radius),
        )

    positions = uniqueblocks.unique_blocks_only(
        [
            coord(angle)
            for angle in np.arange(0, 2 * np.pi + 0.01, (2 * np.pi) / (steps))
        ]
    )
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
    await World(name=center.world).setBlockList(locations, materials)


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
    x, y, z = center
    for h, rad in zip(yes, zes):
        await draw_circle((x, y + height - h, z), rad, material=material)


@expose.expose()
async def solid_circle(
    center=None, radius=10, material=randomchoice.RANDOM_STAINED_GLASS, *, player=None
):
    """Draw a solid circle around center"""
    # make block solid *iff* it's center is inside the circle
    # a point is inside the circle if sin(x)
    if center is None:
        forward = directions.roughly_forward(player.direction)
        center = player.position + (forward * radius)
    for coord in circle_coords(center, radius):
        await Block(location=[center.world, coord]).setBlockData(material)


def circle_coords(center, radius=10):
    """Generate set of center-coords around the middle of the center block"""
    cx, cy, cz = [int(i) + 0.5 for i in center]
    for z in np.arange(cz - radius, cz + radius + 0.1, 1.0):
        for x in np.arange(cx - radius, cx + radius + 0.1, 1.0):
            delta = np.array((x - cx, z - cz), dtype='f')
            distance = np.sqrt(np.sum(delta * delta))
            if distance < radius:
                yield (x, cy, z)
