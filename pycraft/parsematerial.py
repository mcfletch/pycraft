"""Parsing of Minecraft namespaced materials with embedded properties"""

import re
import typing


class ParsedMaterial(typing.TypedDict):
    """Type annotation for a dictionary used to represent a parsed material"""

    namespace: str
    name: str
    properties: typing.Dict[str, str]


MATERIAL_MATCHER = re.compile(
    r"(?:(?P<namespace>\w+)[:])?(?P<name>\w+)(?:\[(?P<properties>(\w+?)[=](\w+?)([,]\w+?[=]\w+?)*)\])?"
)


def parse_material(material: str) -> ParsedMaterial:
    """Parse a material string into namespace, name and properties"""
    match = MATERIAL_MATCHER.match(material)
    if not match:
        raise ValueError("Unable to parse %s as a material" % (material,))
    props = match.group("properties") or None
    base: ParsedMaterial = {
        "namespace": match.group("namespace") or "minecraft",
        "name": match.group("name"),
        "properties": {},
    }
    if props:
        for segment in props.split(","):
            key, value = segment.split("=", 1)
            base["properties"][key] = value
    return base


def copy_struct(material: typing.Union[str, ParsedMaterial], **named) -> ParsedMaterial:
    """Given a parsed material, produce a copy with properties updated from named"""
    if isinstance(material, str):
        material = parse_material(material)
    material = material.copy()
    material["properties"] = material["properties"].copy()
    material["properties"].update(named)
    return material


def unparse_material(material: typing.Union[str, ParsedMaterial]) -> str:
    """Given a parsed material, convert to string form"""
    if isinstance(material, dict):
        base = "%(namespace)s:%(name)s" % material
        if material["properties"]:
            props = ",".join(
                [f"{k}={v}" for (k, v) in sorted(material["properties"].items())]
            )
            return f"{base}[{props}]" % locals()
        else:
            return base
    return material
