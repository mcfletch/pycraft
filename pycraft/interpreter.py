from mcpi import minecraft, block, connection
from mcpi.vec3 import Vec3
import threading, logging, inspect, operator
import re, time, ast, traceback
from collections import deque
import contextlib, functools
from .expose import (
    DEFAULT_COMMANDS,
    DEFAULT_NAMESPACE,
    expose,
)
import queue, time
from . import entity
import numpy as np
log = logging.getLogger(__name__)

class Interpreter(object):
    """Provide basic python expression interpretation"""
    def __init__(self, mc ):
        self.mc = mc
        self.entities = entity.EntityAPI(self.mc)
        self.user_namespaces = {}
        self.clicks = ClickTracker()

    def base_namespace(self, message=None, sender=None, **kwargs):
        namespace = DEFAULT_NAMESPACE.copy()
        namespace.update(DEFAULT_COMMANDS)
        namespace['mc'] = self.mc
        namespace['event'] = message
        namespace['user'] = sender
        namespace['clicks'] = self.clicks
        return namespace
    def user_namespace(self, sender):
        """Get the user's personal namespace"""
        current = self.user_namespaces.get(sender.id)
        if current is None:
            self.user_namespaces[sender.id] = current = {
            }
        return current
    
    def interpret(self,message):
        """Interpret a command from our queue"""
        sender = entity.Entity(
            message.entityId,
            type_id=0,
            type_name='Player',
            api=self.entities
        )
        if isinstance(message,minecraft.BlockEvent):
            message.sender = sender 
            log.info(
                "%s clicked on %s (%s)",
                message.sender,
                message.pos,
                message.face,
            )
            responses = list(self.clicks.notify(message))
            log.debug('Responses to click: %s', responses)
            return responses
        log.info("Call from %s: %r", sender, message)
        try:
            # expr
            namespace = self.base_namespace(message,sender)
            user_namespace = self.user_namespace(sender)
            log.debug('user namespace %r',user_namespace)
            def user_storage():
                return user_namespace
            namespace['user_storage'] = user_storage
            namespace.update(user_namespace)
            try:
                top = ast.parse(message.message,'chat.py','eval')
            except SyntaxError as err:
                if err.offset >= len(err.text):
                    return Response(
                        error = True,
                        message = message,
                        value = f"Something missing at the end here...\n{err.text}",
                        sender=sender,
                    )
                else:
                    spaced = (' '*(err.offset-1))+'^'
                    return Response(
                        error = True,
                        message = message,
                        value = f"This doesn't seem right\n{err.text}\n{spaced}",
                        sender=sender,
                    )
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
        elif isinstance(arg,ast.GeneratorExp):
            return self.interpret_generator(arg,namespace)
        elif isinstance(arg,ast.ListComp):
            return self.interpret_listcomp(arg,namespace)
        elif isinstance(arg, ast.DictComp):
            return self.interpret_dictcomp(arg, namespace)
        elif isinstance(arg, ast.SetComp):
            return self.interpret_setcomp(arg, namespace)
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
    def iterate_generator(self, gen, namespace):
        """Iterate a single ast generator evalulation within a namespace"""
        source = self.interpret_expr(gen.iter, namespace)
        log.info('Source %s', source)
        for item in source:
            passes = True
            update = self.unpack_target(gen.target,item)
            namespace.update(update)
            if gen.ifs:
                for test in gen.ifs:
                    if not self.interpret_expr(test,namespace):
                        passes = False
                        break 
            if passes:
                yield update

    def unpack_target(self,target,value):
        """Unpack ast generator target into a namespace update from value"""
        if isinstance(target,ast.Name):
            return {target.id:value}
        elif isinstance(target,ast.Tuple):
            if len(value) != len(target.elts):
                raise TypeError(
                    value,
                    'Expected value with %s items, got %s'
                    %(
                        len(value),
                        len(target.elts)
                    )
                )
            update = {}
            for subtarget,subitem in zip(target.elts,value):
                update.update(self.unpack_target(subtarget,subitem))
            return update
        else:
            raise ValueError(
                'Unsupported list comprehension target type',
                ast.dump(target),
            )

    def interpret_generator(self, gen, namespace):
        """Iterate over a set of generators from a comprehension"""
        working = namespace.copy()
        dc = isinstance(gen,ast.DictComp)
        for update in self.iterate_generator_updates(gen.generators, namespace):
            log.info("Update %s", update)
            working.update(update)
            if dc:
                yield (
                    self.interpret_expr(gen.key, working),
                    self.interpret_expr(gen.value, working),
                )
            else:
                yield self.interpret_expr(gen.elt, working)

    def iterate_generator_updates(self, generators, namespace):
        if generators:
            # import ipdb;ipdb.set_trace()
            this,rest = generators[0],generators[1:]
            working = namespace.copy()
            for update in self.iterate_generator(generators[0],working):
                # log.info("Update: %s", update)
                working.update(update)
                if rest:
                    for subupdate in self.iterate_generator_updates(rest,working):
                        update.update(subupdate)
                        yield update
                else:
                    yield update

    def interpret_dictcomp(self, dc, namespace):
        return dict(self.interpret_generator(dc,namespace))
    def interpret_listcomp(self, lc, namespace):
        return list(self.interpret_generator(lc,namespace))
    def interpret_setcomp(self, sc, namespace):
        return set(self.interpret_generator(sc,namespace))

class Response(object):
    """A response to send to the chat"""
    def __init__(self, message, sender, value, error=False, handler=None):
        self.message = message
        self.sender = sender
        self.value = value
        self.error = error
        self.handler = handler
    def __eq__(self, rhs):
        return self.value == rhs
    def chat_messages(self):
        formatted = str(self.value)
        for line in formatted.splitlines():
            if self.error:
                yield f'ERR> {line}'
            else:
                yield f'Out> {line}'

    def __repr__(self):
        return '%r (%s)'%(
            self.value,
            self.value.__class__,
        )
class ClickTracker(object):
    """Track clicks by all users"""
    MAX_LENGTH = 200
    DIRECTION_MAP = {
        # Maps face-id to the direction of the block on that side

        0: Vec3(0,-1,0,),
        1: Vec3(0,1,0),
        2: Vec3(0,0,-1),
        3: Vec3(0,0,1),
        4: Vec3(-1,0,0),
        5: Vec3(1,0,0),
    }
    def __init__(self):
        self.clicks = list()
        self.handlers = {}
    def user_clicks(self, user):
        """Get the user's clicks in reverse order"""
        id = getattr(user,'id',user)
        return [
            click for click in self.clicks 
            if click.entityId == user
        ]
    def any_clicks(self):
        """Get any click by any user"""
        return self.clicks 
    def dispatch(self, event):
        """Dispatch event to any handlers"""
        for typ,handlerset in self.handlers.items():
            keyfunc = handlerset.get(None)
            key = keyfunc(event)
            handlers = handlerset.get(key,())
            if handlers:
                to_handle = handlers[:]
                for handler in to_handle:
                    try:
                        result = handler(event)
                    except Exception as err:
                        yield Response(
                            message=event,
                            sender=event.sender,
                            value=err,
                            error=True,
                            handler=handler,
                        )
                    else:
                        if result is not None:
                            yield Response(
                                message=event,
                                sender=event.sender,
                                value=result,
                                error=False,
                                handler=handler,
                            )
                remaining = [
                    h for h in to_handle if not h.one_shot
                ]
                handlers[:len(to_handle)] = remaining

    def notify(self, event):
        """Record and notify handlers about events"""
        self.clicks.insert(0,event)
        event.direction = self.DIRECTION_MAP.get(event.face)
        del self.clicks[self.MAX_LENGTH:]
        for response in self.dispatch(event):
            yield response

    def pos_key(self, event):
        return tuple(event.pos)
    def user_key(self,event):
        return int(event.entityId)

    def register_block(self, position, callback, *, one_shot=False):
        """Register the given block for a callback operation"""
        return self.register(
            'pos',
            tuple(position),
            callback,
            one_shot=one_shot,
            key_func=self.pos_key,
        )
    def register_user(self, user, callback, *, one_shot=False):
        """Register the given block for a callback operation"""
        return self.register(
            'user',
            int(getattr(user,'id',user)),
            callback,
            one_shot=one_shot,
            key_func=self.user_key,
        )
    def register(self, type, key, callback, *, one_shot=False,key_func=None):
        """Register a generic callback for event clicks"""
        if key is None:
            raise ValueError("Cannot register for an even with a key of None")
        registry = self.handlers.get(type)
        if callback is None:
            if registry:
                try:
                    del registry[key]
                except KeyError:
                    pass
            return
        if registry is None:
            self.handlers[type] = registry = {None:key_func}
        handler = Handler(type,key,callback,one_shot=one_shot)
        # for now, we're just going to allow one handler per user or block
        registry[key] = [handler]
        return handler

class Handler(object):
    def __init__(self, type, key, callback, one_shot=False):
        self.type=type
        self.key = key 
        self.callback = callback
        self.one_shot = one_shot 
    def __call__(self, event):
        event.current_handler = self # TODO: yuck
        return self.callback(event)
