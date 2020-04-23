"""Expose commands via chat on a minecraft instance"""
from mcpi import minecraft, block
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
from .lockedmc import locked
from . import entity
import numpy as np
log = logging.getLogger(__name__)
COMMAND_FINDER = re.compile(
    r'^[ ]*(?P<function>[a-zA-z][_a-zA-Z0-9]*)[(](?P<args>.*)[)][ ]*$',
    re.I|re.U
)
ASSIGNMENT_FINDER = re.compile(
    r'^[ ]*(?P<name>[a-zA-z][_a-zA-Z0-9]*)[ ]*[=](?P<expr>.*)[ ]*$',
    re.I|re.U,
)

class Response(object):
    """A response to send to the chat"""
    def __init__(self, message, sender, value, error=False):
        self.message = message 
        self.sender = sender 
        self.value = value 
        self.error = error 
    def chat_messages(self):
        formatted = str(self.value)
        for line in formatted.splitlines():
            if self.error:
                yield f'{self.sender}: {line}'
            else:
                yield f'{self.sender}: ERROR {line}'

class ChatListener(object):
    wanted = True
    def __init__(self, mc, commands = None):
        self.mc = mc 
        self.entities = entity.EntityAPI(self.mc)
        self.request_queue = queue.Queue()
        self.response_queue = queue.Queue()
        self.user_namespaces = {}
    
    def poll(self):
        """Poll for chat messages and see if we recognise them"""
        empty_count = 0
        while self.wanted:
            with locked(self.mc):
                messages = self.mc.events.pollChatPosts()
            for message in messages:
                match = COMMAND_FINDER.match(message.message)
                if match:
                    log.debug("Request: %s", message)
                    self.request_queue.put(message)
                else:
                    match = ASSIGNMENT_FINDER.match(message.message)
                    if match:
                        message.assignment = match.group('name')
                        message.message = match.group('expr').strip()
                        self.request_queue.put(message)
            if not messages:
                empty_count += 1
            else:
                empty_count = 0
            if empty_count:
                delay = min((.1*empty_count,2))
                log.debug("Sleep for %ss",delay)
                time.sleep(delay)
    def responder(self):
        """Thread that returns responses to requests via Chat"""
        while self.wanted:
            try:
                response = self.response_queue.get(True,5)
            except queue.Empty:
                continue
            with locked(self.mc):
                for line in response.chat_messages():
                    self.mc.postToChat('Bot > %s'%(line,))
    def interpreter(self):
        while self.wanted:
            try:
                request = self.request_queue.get(True,5)
            except queue.Empty:
                continue
            try:
                response = self.interpret(request)
            except Exception as err:
                log.exception(
                    'Error handling %r',
                    request,
                )
            else:
                self.response_queue.put(response)

    def base_namespace(self, message=None, sender=None):
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
        sender = entity.Entity(self.entities,message.entityId)
        log.info("Call from %s", sender)
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
                # import pdb;pdb.set_trace()
            if getattr(message,'assignment',None):
                log.info(
                    'User %s => %s = %r',
                    sender,
                    message.assignment,
                    result,
                )
                user_namespace[message.assignment] = result
            return result
        except Exception as err:
            log.exception('Failed on %s', message.message)
            return f'{sender}: {err} on {repr(message.message)}'
    def get_function(self, call, namespace):
        """Lookup a function in namespace for the given call"""
        func = call.func
        if not isinstance(func,ast.Name):
            raise TypeError("Function not called by name")
        name = func.id 
        if name not in namespace:
            raise NameError("I don't know the name %r: known %s"%( name, sorted(namespace.keys())))
        function = namespace.get(name)
        if not hasattr(function,'__call__'):
            raise NameError("Sorry, %r isn't a function, it is a %s"%(name,type(function)))
        return function
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


