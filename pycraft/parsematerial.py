"""Rotational operations on material (strings)"""
from functools import lru_cache
import re
from telnetlib import NEW_ENVIRON

MATERIAL_MATCHER = re.compile(
    r'(?:(?P<namespace>\w+)[:])?(?P<name>\w+)(?:\[(?P<properties>(\w+?)[=](\w+?)([,]\w+?[=]\w+?)*)\])?'
)


def parse_material(material):
    """Parse a material for rotations..."""
    base = MATERIAL_MATCHER.match(material)
    if not base:
        raise ValueError("Unable to parse %s as a material" % (material,))
    props = base.group('properties') or None
    base = {
        'namespace': base.group('namespace') or 'minecraft',
        'name': base.group('name'),
        'properties': {},
    }
    if props:
        for segment in props.split(','):
            key, value = segment.split('=', 1)
            base['properties'][key] = value
    return base


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


@lru_cache(maxsize=16)
def steps_between(direction, other):
    """Calculate the NESW rotations needed to map direction onto other"""
    direction = tuple(direction)
    for i, value in enumerate(NESW_DIRS):
        if value == direction:
            test = NESW_DIRS[i + 1 :] + NESW_DIRS[:i]
            return test.index(tuple(other))
    raise ValueError(f"Did not find direction {direction} in the NESW directions")


@lru_cache(maxsize=256)
def rotate(material, steps=1):
    """Rotate a material through given number of NESW rotations (clockwise from the top)"""
    if isinstance(material, str):
        material = parse_material(material)
    result = rotate_struct(material, steps=steps)
    return unparse_material(result)


def rotate_struct(material, steps=1):
    """Rotate the material through N NESW rotations"""
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


def unparse_material(material):
    if isinstance(material, dict):
        base = '%(namespace)s:%(name)s' % material
        if material['properties']:
            props = ','.join(
                [f'{k}={v}' for (k, v) in sorted(material['properties'].items())]
            )
            return f'{base}[{props}]' % locals()
        else:
            return base
    return material


def test_parse():
    for text, expected in [
        ('air', {'namespace': 'minecraft', 'name': 'air', 'properties': {}}),
        ('minecraft:air', {'namespace': 'minecraft', 'name': 'air', 'properties': {}}),
        (
            'minecraft:smooth_quartz',
            {'namespace': 'minecraft', 'name': 'smooth_quartz', 'properties': {}},
        ),
        (
            'minecraft:smooth_quartz_stairs[facing=west,half=bottom,shape=straight,waterlogged=false]',
            {
                'namespace': 'minecraft',
                'name': 'smooth_quartz_stairs',
                'properties': {
                    'facing': 'west',
                    'half': 'bottom',
                    'shape': 'straight',
                    'waterlogged': 'false',
                },
            },
        ),
    ]:
        result = parse_material(text)
        assert (
            result == expected
        ), f"Parse Failed on {text}\n  got {result}\n  expected {expected}"


def test_unparse():
    for material, expected in [
        ({'namespace': 'minecraft', 'name': 'air', 'properties': {}}, 'minecraft:air'),
        (
            {
                'namespace': 'minecraft',
                'name': 'smooth_quartz_stairs',
                'properties': {
                    'facing': 'west',
                    'half': 'bottom',
                    'shape': 'straight',
                    'waterlogged': 'false',
                },
            },
            'minecraft:smooth_quartz_stairs[facing=west,half=bottom,shape=straight,waterlogged=false]',
        ),
    ]:
        result = unparse_material(material)
        assert (
            result == expected
        ), f"Unparse Failed on {material}\n got {result}\n  expected {expected}"


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
        result = rotate(mat, count)
        assert (
            result == expected
        ), f"Rotate failure for {count} expected {expected} got {result}"
