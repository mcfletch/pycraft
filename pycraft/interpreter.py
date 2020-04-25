from mcpi import minecraft, block, connection
from mcpi.vec3 import Vec3
import threading, logging, inspect, operator
import re, time, ast
import contextlib, functools
from .expose import (
    DEFAULT_COMMANDS,
    DEFAULT_NAMESPACE,
    expose,
    V,
)
import queue
from . import entity
import numpy as np
log = logging.getLogger(__name__)

class Interpreter(object):
    """Provide basic python expression interpretation"""
    def __init__(self, mc):
        self.mc = mc
        self.entities = entity.EntityAPI(self.mc)
        self.user_namespaces = {}

    def base_namespace(self, message=None, sender=None, **kwargs):
        namespace = DEFAULT_NAMESPACE.copy()
        namespace.update(DEFAULT_COMMANDS)
        namespace['mc'] = self.mc
        namespace['event'] = message
        namespace['user'] = sender
        return namespace
    def user_namespace(self, sender):
        """Get the user's personal namespace"""
        return self.user_namespaces.setdefault(sender.id,{})
    
    def interpret(self,message):
        """Interpret a command from our queue"""
        sender = entity.Entity(
            message.entityId,
            type_id=0,
            type_name='Player',
            api=self.entities
        )
        log.info("Call from %s: %r", sender, message)
        try:
            # expr
            namespace = self.base_namespace(message,sender)
            user_namespace = self.user_namespace(sender)
            log.debug('user namespace %r',user_namespace)
            namespace.update(user_namespace)
            top = ast.parse(message.message,'chat.py','eval')
            if not isinstance(top, ast.Expression):
                log.debug("Not an expression: %r", message.message)
                raise TypeError("Not an expression")
            result = self.interpret_expr(top,namespace=namespace)
            if getattr(message,'assignment',None):
                log.info(
                    'User %s => %s = %r',
                    sender,
                    message.assignment,
                    result,
                )
                user_namespace[message.assignment] = result
            if result is not None:
                return Response(
                    sender=sender,
                    value=result,
                    error=False,
                    message=message,
                )
        except Exception as err:
            log.exception('Failed on %s', message.message)
            return Response(
                sender=sender,
                value=err,
                error=True,
                message=message,
            )
    def get_function(self, call, namespace):
        """Lookup a function in namespace for the given call"""
        func = self.interpret_expr(call.func,namespace)
        if not hasattr(func,'__call__'):
            raise NameError("Sorry, %r isn't a function, it is a %s"%(func,type(func)))
        return func
    def get_call_args(self, call, namespace):
        args,named = [],{}
        for arg in call.args:
            value = self.interpret_expr(arg,namespace)
            args.append(value)
        for keyword in call.keywords:
            named[keyword.arg] = self.interpret_expr(keyword.value,namespace)
        return args, named
    def interpret_call(self, call, namespace):
        func = self.get_function(call,namespace)
        args,named = self.get_call_args(call, namespace)
        if getattr(func,'__kwdefaults__',None):
            for key,default in func.__kwdefaults__.items():
                if key not in named:
                    if key in namespace:
                        named[key] = namespace[key]
                    elif key == 'namespace':
                        named[key] = namespace
                
        return func(*args,**named)

    BINOP_TO_OPERATOR = {
        ast.Add:operator.add,
        ast.Sub:operator.sub,
        ast.Mult:operator.mul,
        ast.MatMult:operator.matmul,
        ast.Div: operator.truediv,
        ast.Mod: operator.mod,
        ast.Pow: operator.pow,
        ast.LShift: operator.lshift,
        ast.RShift: operator.rshift,
        ast.BitOr: operator.__or__,
        ast.BitXor: operator.__xor__,
        ast.BitAnd: operator.__and__,
        ast.FloorDiv: operator.floordiv,
    }

    def interpret_expr(self, arg, namespace):
        if isinstance(arg, ast.Expression):
            return self.interpret_expr(arg.body,namespace=namespace)
        elif isinstance(arg,ast.Name):
            if arg.id.startswith('_'):
                raise NameError('Names starting with _ are not allowed', arg.id)
            if arg.id in namespace:
                return namespace[arg.id]
            raise NameError(arg.id)
        
        elif isinstance(arg,ast.Subscript):
            value = self.interpret_expr(arg.value,namespace)
            if isinstance(arg.slice,ast.Index):
                return value[self.interpret_expr(arg.slice.value,namespace)]
            elif isinstance(arg.slice,ast.Slice):
                return value[
                    (self.interpret_expr(arg.slice.lower,namespace) if arg.slice.lower else None):
                    (self.interpret_expr(arg.slice.upper,namespace) if arg.slice.upper else None):
                    (self.interpret_expr(arg.slice.step,namespace) if arg.slice.step else None)
                ]
            else:
                raise ValueError(
                    'Do not yet support extended indexing'
                )
        elif isinstance(arg,ast.Attribute):
            parent = self.interpret_expr(arg.value,namespace)
            key = arg.attr 
            if key.startswith('_'):
                raise ValueError("Attributes starting with _ are disallowed", key)
            if isinstance(parent,dict):
                return parent[key]
            else:
                return getattr(parent,key)
        elif isinstance(arg,ast.BinOp):
            left,op,right = arg.left,arg.op,arg.right
            first,second = (
                self.interpret_expr(left,namespace), 
                self.interpret_expr(right,namespace)
            )
            impl = self.BINOP_TO_OPERATOR[op.__class__]
            return impl(first,second)
        elif isinstance(arg,ast.Tuple):
            value = tuple([self.interpret_expr(a,namespace) for a in arg.elts])
            return value
        elif isinstance(arg, ast.List):
            value = [self.interpret_expr(a,namespace) for a in arg.elts]
            return value
        elif isinstance(arg,ast.Call):
            return self.interpret_call(arg,namespace)
        else:
            try:
                return ast.literal_eval(ast.Expression(body=arg))
            except Exception:
                raise ValueError(
                    'Unsupported operation: %s'%(
                        ast.dump(arg)
                    )
                )

class Response(object):
    """A response to send to the chat"""
    def __init__(self, message, sender, value, error=False):
        self.message = message
        self.sender = sender
        self.value = value
        self.error = error
    def __eq__(self, rhs):
        return self.value == rhs
    def chat_messages(self):
        formatted = str(self.value)
        for line in formatted.splitlines():
            if self.error:
                yield f'ERR {self.sender}> {line}'
            else:
                yield f'{self.sender}> {line}'

    def __repr__(self):
        return '%r (%s)'%(
            self.value,
            self.value.__class__,
        )