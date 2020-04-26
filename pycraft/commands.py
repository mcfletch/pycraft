"""Common commands exposed over chat server"""
from . import entity, blocks, fuzzymatch
from .expose import expose
from .lockedmc import locked
from mcpi.vec3 import Vec3
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
            return '%s%s\n%s'%(value.__name__,params,doc) 
        else:
            return '%s%s'%(value.__name__,params)
    elif doc:
        return doc
    else:
        return '%s instance with members %s'%(
            value.__class__,
            dir(value),
        )

@expose(name='dir')
def dir_(*args,namespace=None):
    """Look at the argument and describe what members it has"""
    if args:
        return dir(args[0])
    else:
        return sorted(namespace.keys())


@expose()
def spawn(type_id,position=None,*,mc=None,user=None):
    """Spawn a new entity of type_id at position (default in front of user)"""
    if position is None:
        position = user.position + user.direction + Vec3(0,1,0)
    typ = entity.Entity.as_instance(type_id)
    with locked(mc):
        return mc.spawnEntity(
            *position,
            typ, 
        )

@expose()
def block(type_id,position=None,*,mc=None,user=None):
    """Create a block with the given type_id at position"""
    if position is None:
        position = user.position + user.direction + Vec3(0,1,0)
    typ = blocks.Block.as_instance(type_id)
    with locked(mc):
        return mc.setBlock(
            *position,
            typ, 
        )
@expose()
def click_create(type_id,*,clicks=None,mc=None,user=None):
    """When you right-click with a sword, create block-type there"""
    typ = blocks.Block.as_instance(type_id)
    def on_click(event):
        target = V(event.pos) + V(event.direction)
        mc.setBlock(
            *target,
            typ
        )
    return clicks.register_user(user,on_click)
@expose()
def click_delete(*,clicks=None,mc=None,user=None):
    typ = blocks.Block.as_instance('AIR')
    def on_click(event):
        target = V(event.pos)
        mc.setBlock(
            *target,
            typ
        )
    return clicks.register_user(user,on_click)
@expose()
def click_cancel(*,clicks=None,user=None):
    """Cancel click operations"""
    clicks.register_user(user,None)


@expose()
def find_blocks(name):
    """Find blocks with names similar to the given name

        find_blocks('granite') => ['GRANITE','POLISHED_GRANITE']
    """
    return sorted(fuzzymatch.similar_names(
        fuzzymatch.as_constant(
            name,
        ),
        blocks.BLOCK_NAMES,
    ))
@expose()
def find_entities(name):
    """Find entities with names similar to name

        find_entities( 'creep' ) => ['CREEPER']
    """
    return sorted(fuzzymatch.similar_names(
        fuzzymatch.as_constant(
            name,
        ),
        entity.ENTITY_NAMES,
    ))

@expose()
def clear(type=-1,distance=100,*,user=None) -> 'List[str]':
    """Clear all entities near the user of given type

        clear( 'creeper', 200 ) => ['CREEPER','CREEPER']

    if type == -1 then *all* entities are cleared, including
    things such as cats, dogs, mine-carts, etc.
    
    returns a list of the names of the removed entities
    """
    user.remove_nearby_entities(
        type_id=type,
        distance=distance,
    )

@expose()
def users(*,user=None):
    return user.api.players()

@expose()
def V(*args,**named):
    """Construct a Vector from a list, tuple or 3 values
    
    Vectors represent (X,Y,Z) coordinates in 3D space,
    with X (East => West), Y (Down => Up), Z (South => North)
    """
    if named:
        return Vec3(*args,**named)
    if len(args) == 1 and isinstance(args[0],(list,tuple,Vec3,np.ndarray)):
        return Vec3(*args[0])
    else:
        return Vec3(*args)

@expose()
def last_hit(index=-1,*,mc=None,user=None,clicks=None):
    """Return the index-th last click by the sending user
    
    If we don't have that click, will return None
    """
    try:
        import ipdb;ipdb.set_trace()
        click = clicks.user_clicks(user)[index]
        return click
    except IndexError:
        return None
