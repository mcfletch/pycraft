"""Command namespace exposure and core commands"""
from mcpi import minecraft, block
from mcpi.vec3 import Vec3
import threading, logging, inspect, operator
import re, time, ast
import contextlib, functools
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
    'range': range,
    'pi': np.pi,
    'block': block,
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

