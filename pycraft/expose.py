"""Command namespace exposure and core commands"""
from mcpi import minecraft, entity as mc_entity
from mcpi.vec3 import Vec3
from . import blocks, entity, fuzzymatch
import threading, logging, inspect, operator
import re, time, ast, inspect
import contextlib, functools
from .lockedmc import locked
import numpy as np

_range = range


def range(*args):
    """Produce sequences of integers args [start],stop,[step]"""
    return list(_range(*args))


BLOCK_NAMESPACE = fuzzymatch.FuzzyNamespace(blocks.BLOCK_NAMES)
ENTITY_NAMESPACE = fuzzymatch.FuzzyNamespace(entity.ENTITY_NAMES)

DEFAULT_NAMESPACE = {
    'sin': np.sin,
    'cos': np.cos,
    'arange': np.arange,
    'tuple': tuple,
    'list': list,
    'range': range,
    'pi': np.pi,
    'blocks': BLOCK_NAMESPACE,
    'entities': ENTITY_NAMESPACE,
    'int': int,
    'float': float,
    'str': str,
    'bool': bool,
    'sqrt': np.sqrt,
}
DEFAULT_COMMANDS = {}


def expose(command_set=None, name=None):
    """Registers a function as being externally callable"""
    command_set = command_set or DEFAULT_COMMANDS

    def wrapper(function):
        function_name = name or function.__name__
        command_set[function_name] = function
        return function

    return wrapper


def command_list():
    """Produce a command list"""
    result = []
    for name, function in sorted(DEFAULT_COMMANDS.items()):
        docs = inspect.getdoc(function)
        if docs:
            doc_line = docs.splitlines()[0]
        else:
            doc_line = 'Undocumented'
        result.append(f'{name} -- {doc_line}')
    return result


def command_details(name):
    function = DEFAULT_COMMANDS.get(name)
    if function:
        docs = inspect.getdoc(function) or 'Undocumented'
        return [
            f'{name}{inspect.formatargspec(*inspect.getfullargspec(function))}',
        ] + [f'    {line}' for line in docs.splitlines()]
    else:
        names = sorted(
            fuzzymatch.similar_names(
                name,
                DEFAULT_COMMANDS,
            )
        )
        if names:
            return [
                f'Do not know any function named {name}, did you mean: {", ".join(names)}',
            ]
        return [
            f'Do not know any function named {name}',
        ]
