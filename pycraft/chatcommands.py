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
import numpy as np
log = logging.getLogger(__name__)
COMMAND_FINDER = re.compile(
    r'^[ ]*(?P<function>[a-zA-z][_a-zA-Z0-9]*)[(](?P<args>.*)[)][ ]*$',
    re.I|re.U
)
MC_LOCK = threading.RLock()
@contextlib.contextmanager
def locked(mc):
    if mc:
        mc.lock.acquire(True)
    yield MC_LOCK
    if mc:
        mc.lock.release()

class Entity(object):
    """Hold a reference to an entity id on the listener"""
    def __init__(self, listener, id):
        self.listener = listener
        self.id = id 
    def __str__(self):
        return self.get_name()
    def get_name(self):
        return self.listener.get_entity_name(self.id)
    def get_position(self):
        return self.listener.get_entity_position(self.id)
    def get_direction(self):
        """On Java edition, get the direction the user is facing"""
        return self.listener.get_entity_direction(self.id)
    def set_position(self):
        return self.listener.set_entity_position(self.id)
    name = property(get_name)
    position = property(get_position,set_position)
    direction = property(get_direction,)

class ChatListener(object):
    wanted = True
    def __init__(self, mc, commands = None):
        self.mc = mc 
        if self.mc:
            self.mc.lock = threading.RLock()
        self.name_cache = {}
    
    def get_entity_name(self, entity):
        """Get username for the given user"""
        current = self.name_cache.get(entity)
        if not current:
            with locked(self.mc):
                current = self.name_cache[entity] = self.mc.entity.getName(
                    entity
                )
                log.debug("Entity %s => %s", entity, current)
        return current
    def get_entity_position(self, entity):
        """Get entity position"""
        with locked(self.mc):
            return self.mc.entity.getPos(entity)
    def get_entity_tile_position(self, entity):
        with locked(self.mc):
            return self.mc.entity.getTilePos(entity)
    def get_entity_direction(self, entity):
        with locked(self.mc):
            return self.mc.entity.getDirection(entity)

    
    def poll(self):
        """Poll for chat messages and see if we recognise them"""
        while self.wanted:
            with locked(self.mc):
                messages = self.mc.events.pollChatPosts()
            for message in messages:
                match = COMMAND_FINDER.match(message.message)
                if match:
                    response = self.interpret(message)
                    if response:
                        formatted = str(response)
                        for line in formatted.splitlines()[:6]:
                            self.mc.postToChat('<Bot> %s'%(line,))
            if not messages:
                time.sleep(1)
    
    def interpret(self,message):
        """Interpret a command from our queue"""
        sender = Entity(self,message.entityId)
        log.info("Call from %s", sender)
        try:
            # expr
            top = ast.parse(message.message,'chat.py','eval')
            if not isinstance(top, ast.Expression):
                log.debug("Not an expression: %r", message.message)
                raise TypeError("Not an expression")
            call = top.body 
            if not isinstance(call,ast.Call):
                log.debug("Not a call: %r", message.message)
                raise TypeError("Not a function call")
            log.info('Top level call %s',ast.dump(call,True,True))
            namespace = DEFAULT_NAMESPACE.copy()
            namespace.update(DEFAULT_COMMANDS)
            namespace['event'] = message
            namespace['user'] = sender
            namespace['mc'] = self.mc
            return self.interpret_call(call,namespace)
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


