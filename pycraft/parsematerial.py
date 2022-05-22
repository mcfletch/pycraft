"""Rotational operations on material (strings)"""
from functools import lru_cache
import re
from telnetlib import NEW_ENVIRON
from . import rotations

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


def copy_struct(material, **named):
    material = material.copy()
    material['properties'] = material['properties'].copy()
    material['properties'].update(named)
    return material


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
