"""Command namespace exposure and core commands"""
from . import fuzzymatch
import inspect, types
import numpy as np
from pycraft.chatmessage import ChatMessage

_range = range


def range(*args):
    """Produce sequences of integers args [start],stop,[step]"""
    return list(_range(*args))


DEFAULT_NAMESPACE = {
    'sin': np.sin,
    'cos': np.cos,
    'arange': np.arange,
    'tuple': tuple,
    'list': list,
    'range': range,
    'pi': np.pi,
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
        docs = inspect.getdoc(function)
        if docs:
            docs = (
                docs
                + f'''
    
Exposed in chat as **{function_name}**
'''
            )
        function.__doc__ = docs
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


def command_details(name_or_instance):
    if isinstance(name_or_instance, str):
        function = DEFAULT_COMMANDS.get(name_or_instance)
        if not function:
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
    else:
        function = name_or_instance
    docs = inspect.getdoc(function) or 'Undocumented'
    if isinstance(function, (types.FunctionType, types.MethodType)):
        return [
            f'{function.__name__}{inspect.formatargspec(*inspect.getfullargspec(function))}',
        ] + [f'    {line}' for line in docs.splitlines()]
    else:
        return docs.splitlines()


def get_base_namespace():
    """Get base namespace as should be used for any interpreter"""
    from .server import proxyobjects

    namespace = DEFAULT_NAMESPACE.copy()
    namespace.update(proxyobjects.PROXY_TYPES)
    namespace.update(DEFAULT_COMMANDS)
    namespace.update(
        {
            'list': list,
            'set': set,
            'dict': dict,
            'type': lambda x: type(x),
        }
    )
    return namespace
