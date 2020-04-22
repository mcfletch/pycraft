"""Expose commands via chat on a minecraft instance"""
from mcpi import minecraft, block
import threading, logging, inspect, operator
import re, time, ast
import contextlib, functools
log = logging.getLogger('chatcommands')
COMMAND_FINDER = re.compile(
    r'^[ ]*(?P<function>[a-zA-z][a-zA-Z0-9]*)[(](?P<args>.*)[)][ ]*$',
    re.I|re.U
)
MC_LOCK = threading.RLock()
@contextlib.contextmanager
def locked():
    MC_LOCK.acquire(True)
    yield MC_LOCK
    MC_LOCK.release()

class Event(object):
    def __init__(self, listener, user, message, args, named):
        self.listener = listener
        self.user = user 
        self.message = message 
        self.args = args 
        self.named = named
    

DEFAULT_COMMANDS = {

}
def expose(command_set=None):
    command_set = command_set or DEFAULT_COMMANDS
    def wrapper(function):
        function_name = function.__name__
        signature = list(inspect.signature(function).parameters)
        if not (signature and signature[0] == 'event'):
            raise TypeError(
                'Exposed functions should have a parameter `mc` as the first parameter: %s'%(
                    function,
                )
            )
        command_set[function_name] = function
        @functools.wraps(function)
        def final_function(*args,**named):
            result = function(*args,**named)
            if result is not None:
                log.debug('%s(*%r,**named) => %r', function_name,args,named)
        return final_function
    return wrapper

@expose()
def echo(event,message):
    """Return the message to the user"""
    return f'{event.user}: {message}'

class ChatListener(object):
    wanted = True
    def __init__(self, mc, commands = None):
        self.mc = mc 
        self.namespace = commands or DEFAULT_COMMANDS
        self.name_cache = {}
    
    def get_entity_name(self, entity):
        """Get username for the given user"""
        current = self.name_cache.get(entity)
        if not current:
            with locked():
                current = self.name_cache[entity] = self.mc.entity.getName(
                    entity
                )
                log.debug("Entity %s => %s", entity, current)
        return current

    
    def poll(self):
        """Poll for chat messages and see if we recognise them"""
        while self.wanted:
            with locked():
                messages = self.mc.events.pollChatPosts()
            for message in messages:
                match = COMMAND_FINDER.match(message.message)
                if match:
                    response = self.interpret(message)
                    if response:
                        self.mc.postToChat(str(response))
            if not messages:
                time.sleep(1)
    
    def interpret(self,message):
        """Interpret a command from our queue"""
        sender = self.get_entity_name(message.entityId)
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
            func = self.get_function(call,self.namespace)
            args,named = self.get_call_args(call, self.namespace)
            event = Event(
                self,
                sender,
                message,
                args,
                named,
            )
            result = func(event,*args,**named)
            return result

            # return f'Would call {function} with {args}'
            # node = top.children[0]
            # log.debug('Expression %s',node)
            # for child in ast.iter_child_nodes(node):
            #     log.debug('Node: %s',node)
            #     if isinstance(child,ast.Call):
            #         log.info(
            #             "Call parsed to %s, %s", 
            #             ast.get_source_segment(child.func),
            #             ast.get_source_segment(child.args),
            #         )
            #     else:
            #         print(child)
        except Exception:
            log.exception('Failed during parsing')
            return 'Error'
    def get_function(self, call, namespace):
        """Lookup a function in namespace for the given call"""
        func = call.func
        if not isinstance(func,ast.Name):
            raise TypeError("Function not called by name")
        name = func.id 
        if name not in self.namespace:
            raise NameError("I don't know the name %r"%( name))
        function = self.namespace.get(name)
        if not hasattr(function,'__call__'):
            raise NameError("Sorry, %r isn't a function, it is a %s"%(name,type(function)))
        return function
    def get_call_args(self, call, namespace):
        args,named = [],{}
        for arg in call.args:
            value = self.interpret_expr(arg,self.namespace)
            args.append(value)
        return args, named
    def interpret_call(self, call, namespace):
        func = self.get_function(call,self.namespace)
        args,named = self.get_call_args(call, self.namespace)
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
        if isinstance(arg,ast.Name):
            if arg.id in self.namespace:
                return self.namespace[arg.id]
            raise NameError(arg.id)
        elif isinstance(arg,ast.BinOp):
            left,op,right = arg.left,arg.op,arg.right
            first,second = (
                self.interpret_expr(left,namespace), 
                self.interpret_expr(right,namespace)
            )
            impl = self.BINOP_TO_OPERATOR[op.__class__]
            return impl(first,second)
        elif isinstance(arg,ast.Call):
            return self.interpret_call(arg,namespace)
        else:
            return ast.literal_eval(ast.Expression(body=arg))


def main():
    mc = minecraft.Minecraft.create()
    # players = [1,2,3]
    listener = ChatListener(mc)
    listener.poll()
    
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()
