"""Common commands exposed over chat server"""
from . import entity, blocks, fuzzymatch
from .expose import expose, command_details, command_list
from .lockedmc import locked
from mcpi.vec3 import Vec3
import time, re, os, json
import numpy as np


@expose()
def echo(message, *, user=None):
    """Return the message to the user"""
    return message


@expose()
def help(value):
    """Try to get help about the object"""
    import inspect

    doc = inspect.getdoc(value)
    if callable(value):
        params = inspect.signature(value)
        if doc:
            return '%s%s\n%s' % (value.__name__, params, doc)
        else:
            return '%s%s' % (value.__name__, params)
    elif doc:
        return doc
    else:
        return '%s instance with members %s' % (
            value.__class__,
            dir(value),
        )


@expose(name='dir')
def dir_(*args, namespace=None):
    """Look at the argument and describe what members it has"""
    if args:
        return dir(args[0])
    else:
        return sorted(namespace.keys())


@expose()
def spawn(type_id, position=None, *, mc=None, user=None):
    """Spawn a new entity of type_id at position (default in front of user)"""
    if position is None:
        position = user.position + user.direction + Vec3(0, 1, 0)
    if isinstance(type_id, int):
        with locked(mc):
            return mc.spawnEntity(
                *position,
                type_id,
            )
    else:
        typ = entity.Entity.as_instance(type_id)
        with locked(mc):
            return mc.spawnEntity(
                *position,
                typ,
            )


@expose()
def spawn_drop(type_id, *, mc=None, user=None):
    """Spawn an entity 50m overhead dropping onto your location

    Use this to e.g. drop a creeper to their death and generate gunpowder
    """
    position = user.position + user.direction + Vec3(0, 50, 0)
    return spawn(type_id, position=position, mc=mc, user=user)


@expose()
def spawn_shower(type_id, count=30, height=50, *, mc=None, user=None):
    """Spawn an entity 50m overhead dropping onto your location

    Use this to e.g. drop a creeper to their death and generate gunpowder
    """
    position = user.position + user.direction + Vec3(0, height, 0)
    for i in range(count):
        spawn(type_id, position=position, mc=mc, user=user)
        time.sleep(0.1)
    return count


@expose()
def block(type_id, position=None, *, mc=None, user=None):
    """Create a block with the given type_id at position"""
    if position is None:
        position = user.position + user.direction + Vec3(0, 1, 0)
    typ = blocks.Block.as_instance(type_id)
    with locked(mc):
        return mc.setBlock(
            *position,
            typ.id,
        )


@expose()
def click_create(type_id, *, clicks=None, mc=None, user=None):
    """When you right-click with a sword, create block-type there"""
    typ = blocks.Block.as_instance(type_id)

    def on_click(event):
        target = V(event.pos) + V(event.direction)
        mc.setBlock(*target, typ)

    return clicks.register_user(user, on_click)


@expose()
def click_delete(*, clicks=None, mc=None, user=None):
    typ = blocks.Block.as_instance('AIR')

    def on_click(event):
        target = V(event.pos)
        mc.setBlock(*target, typ)

    return clicks.register_user(user, on_click)


# @expose()
# def click_describe(*,clicks=None,mc=None,user=None):
#     def on_click(event):
#         try:
#             target = event.pos
#             description = 'Unavailable'
#             for i in range(2):
#                 try:
#                     description = mc.getBlockWithData(event.pos)
#                 except Exception as err:
#                     pass
#             print('Block at %s => %s'%(
#                 event.pos,
#                 description,
#             ))
#         except Exception as err:
#             print("Failed: %s", err)
#     return clicks.register_user(user,on_click)


@expose()
def click_cancel(*, clicks=None, user=None):
    """Cancel click operations"""
    clicks.register_user(user, None)


@expose()
def find_blocks(name):
    """Find blocks with names similar to the given name

    find_blocks('granite') => ['GRANITE','POLISHED_GRANITE']
    """
    return sorted(
        fuzzymatch.similar_names(
            fuzzymatch.as_constant(
                name,
            ),
            blocks.BLOCK_NAMES,
        )
    )


@expose()
def find_entities(name):
    """Find entities with names similar to name

    find_entities( 'creep' ) => ['CREEPER']
    """
    return sorted(
        fuzzymatch.similar_names(
            fuzzymatch.as_constant(
                name,
            ),
            entity.ENTITY_NAMES,
        )
    )


# @expose()
# def clear(type=-1, distance=100, *, user=None) -> 'List[str]':
#     """Clear all entities near the user of given type

#         clear( 'creeper', 200 ) => ['CREEPER','CREEPER']

#     if type == -1 then *all* entities are cleared, including
#     things such as cats, dogs, mine-carts, etc.

#     returns a list of the names of the removed entities
#     """
#     user.remove_nearby_entities(
#         type_id=type,
#         distance=distance,
#     )


@expose()
def users(*, user=None):
    return user.api.players()


@expose()
def V(*args, **named):
    """Construct a Vector from a list, tuple or 3 values

    Vectors represent (X,Y,Z) coordinates in 3D space,
    with X (East => West), Y (Down => Up), Z (South => North)
    """
    if named:
        return Vec3(*args, **named)
    if len(args) == 1 and isinstance(args[0], (list, tuple, Vec3, np.ndarray)):
        return Vec3(*args[0])
    else:
        return Vec3(*args)


@expose()
def last_hit(index=-1, *, mc=None, user=None, clicks=None):
    """Return the index-th last click by the sending user

    If we don't have that click, will return None
    """
    try:
        click = clicks.user_clicks(user)[index]
        return click
    except IndexError:
        return None


@expose()
def bed(position=None, *, user=None, mc=None):
    if position is None:
        position = user.position + user.direction + V(0, 1, 0)
    x, y, z = position
    # Bed can only be put together from matching
    # directional pieces, here a N/S bed
    mc.setBlock(x, y, z + 1, blocks.BED.id, 8)
    mc.setBlock(x, y, z, blocks.BED.id, 0)


@expose()
def help(command=None, *args, user=None, mc=None):
    """Help, a command list if no command specified, otherwise per-command details

    help() => Show list of available commands
    help('command') => show detailed usage for the given command
    help('entity-list') => Show list of available entitity names
    help('entity-list', 'name') => Show list of available entitity names matching name
    help('block-list') => Show list of available block names
    help('block-list', 'name') => Show list of available block names matching name
    """
    if not command:
        output = command_list()
    elif command == 'entity-list':
        if args:
            entities = find_entities(args[0])
            if not entities:
                return f'No entities matching {args[0]} found'
            else:
                return ", ".join(entities)
        return ", ".join(entity_list())
    elif command == 'block-list':
        if args:
            entities = find_blocks(args[0])
            if not entities:
                return f'No blocks matching {args[0]} found'
            else:
                return ", ".join(entities)
        return ", ".join(block_list())
    else:
        output = command_details(command)
    return "\n".join(output)


def entity_list():
    from .entity import ENTITY_NAMES

    names = sorted(ENTITY_NAMES.keys())
    return " ".join(names)


def block_list(search=None):
    from .blocks import BLOCK_NAMES

    names = sorted(BLOCK_NAMES.keys())
    return " ".join(names)


@expose()
def stairs(
    depth=10,
    ystep=1,
    position=None,
    direction=None,
    material='granite',
    *,
    mc=None,
    user=None,
):
    """Read blocks to create a template that can be stamped elsewhere"""
    from .bulldozer import roughly_forward

    if direction is None:
        direction = user.direction
    direction = roughly_forward(direction)

    if not direction:
        raise RuntimeError("Unable to find direction")

    material = blocks.Block.as_instance(material)

    step = Vec3(direction.x, ystep, direction.z)
    if position is None:
        position = user.tile_position + (step if ystep < 0 else direction)

    current = position
    air = material.as_instance('AIR')
    for i in range(depth):
        mc.setBlock(current.x, current.y, current.z, material)
        mc.setBlock(current.x, current.y + 1, current.z, air)
        mc.setBlock(current.x, current.y + 2, current.z, air)
        mc.setBlock(current.x, current.y + 3, current.z, air)
        current = current + step
