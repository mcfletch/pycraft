"""Rotation calculations based on NESW cardinal directions

Combined with parsematerial allows you to issue rotation
operations on material properties to correctly re-align
facing items to the correct orientations.
"""
from functools import lru_cache
import numpy as np


NESW_ROTS = next = {
    'north': 'east',
    'south': 'west',
    'east': 'south',
    'west': 'north',
    'up': 'up',
    'down': 'down',
}
NESW_DIRS = [
    (0, 0, -1),  # north
    (1, 0, 0),  # east
    (0, 0, 1),  # south
    (-1, 0, 0),  # west
]
NESW_NAMES = dict(zip(NESW_DIRS, ['north', 'east', 'south', 'west']))


def direction_name(direction):
    """Get the direction name for a given 3-element direction"""
    key = tuple(direction[:3])
    return NESW_NAMES.get(key)


def _news_steps():
    i = 0
    for i in range(12):
        yield NESW_DIRS[i % len(NESW_DIRS)]


@lru_cache(maxsize=16)
def steps_between(direction, other):
    """Calculate the NESW rotations needed to map direction onto other"""
    if direction == other:
        return 0
    assert direction in NESW_DIRS, "Must be a cardinal direction"
    assert other in NESW_DIRS, "Must be a cardinal direction"
    start = -1
    for i, value in enumerate(_news_steps()):
        if value == direction:
            start = i
        if start > -1 and value == other:
            return i - start
    raise ValueError(f"Did not find direction {direction} in the NESW directions")


def rotate_struct(material, steps=1):
    """Rotate the material struct through N NESW rotations"""
    if material is None:
        return material
    mat = material.copy()
    mat['properties'] = props = material['properties'].copy()
    if 'facing' in props:
        props['facing'] = _rotate_dir(mat['properties']['facing'], steps)

    prop_rot = {}
    for key in ['north', 'south', 'east', 'west']:
        if key in props:
            prop_rot[_rotate_dir(key, steps)] = props.pop(key)
    for key in ['axis']:
        if key in props:
            if steps in (1, 3):
                props[key] = {'x': 'z', 'z': 'x'}.get(props[key], props[key])

    props.update(prop_rot)

    return mat


def _rotate_dir(direction, count):
    for i in range(count):
        direction = NESW_ROTS[direction]
    return direction


@lru_cache(maxsize=256)
def rotate(material, steps=1):
    """Rotate a material through given number of NESW rotations (clockwise from the top)"""
    from .parsematerial import parse_material, unparse_material

    if isinstance(material, str):
        material = parse_material(material)
    result = rotate_struct(material, steps=steps)
    return unparse_material(result)
