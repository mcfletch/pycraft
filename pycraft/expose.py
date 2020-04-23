"""Command namespace exposure and core commands"""
from mcpi import minecraft, block, entity as mc_entity
from mcpi.vec3 import Vec3
from . import blocks, entity
import threading, logging, inspect, operator
import re, time, ast
import contextlib, functools
from .lockedmc import locked
import numpy as np

def V(*args,**named):
    """Construct an mcpi.vec3.Vec3 from a list, tuple or 3 values"""
    if named:
        return Vec3(*args,**named)
    if len(args) == 1 and isinstance(args[0],(list,tuple,Vec3,np.ndarray)):
        return Vec3(*args[0])
    else:
        return Vec3(*args)
_range = range
def range(*args):
    """Produce sequences of integers args [start],stop,[step]"""
    return list(_range(*args))

DEFAULT_NAMESPACE = {
    'sin': np.sin,
    'cos': np.cos,
    'arange': np.arange,
    'range': np.arange,
    'pi': np.pi,
    'block': blocks.BLOCK_NAMES,
    'entity': entity.ENTITY_NAMES,
    'int': int,
    'float': float,
    'str': str,
    'bool': bool,
    'sqrt': np.sqrt,
    'V': V,
}
DEFAULT_COMMANDS = {}
def expose(command_set=None,name=None):
    """Registers a function as being externally callable"""
    command_set = command_set or DEFAULT_COMMANDS
    def wrapper(function):
        function_name = name or function.__name__
        command_set[function_name] = function
        return function
    return wrapper

@expose()
def echo(message, *, user=None):
    """Return the message to the user"""
    return f'{user}: {message}'
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

def resolve_name(name,lookup_space):
    """Fuzzy lookup of name in name-space"""
    if hasattr(name,'id'):
        return name.id 
    elif isinstance(name,int):
        return name 
    elif isinstance(name, str):
        name = name.upper()
        if name in lookup_space:
            return lookup_space[name]
        possible = []
        for key in lookup_space:
            if name in key:
                possible.append(key)
        if len(possible) == 1:
            return lookup_space[key]
        elif possible:
            raise NameError(
                name,
                'Possibly you meant: %s'%(
                    ', '.join(sorted(possible))
                )
            )
        else:
            raise NameError(
                name,'Available: %s'%(
                ', '.join(sorted(lookup_space.keys()))
                )
            )
    raise NameError(name,'Known names: %s'%(
        sorted(lookup_space.keys())
    ))


@expose()
def spawn(type_id,position=None,*,mc=None,user=None):
    """Spawn a new entity of type_id at position (default in front of user)"""
    if position is None:
        position = user.position + user.direction + Vec3(0,1,0)
    typ = resolve_name(type_id,entity.ENTITY_NAMES)
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
    typ = resolve_name(type_id,blocks.BLOCK_NAMES)
    with locked(mc):
        return mc.setBlock(
            *position,
            typ, 
        )
