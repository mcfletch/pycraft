"""Expose commands via chat on a minecraft instance"""
from mcpi import minecraft, block
import threading, logging, inspect
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
                return False
            call = top.body 
            if not isinstance(call,ast.Call):
                log.debug("Not a call: %r", message.message)
                return False 
            func = call.func
            if not isinstance(func,ast.Name):
                log.debug("Function not called by name", message.message)
                return False 
            name = func.id 
            log.info('Top level %s',ast.dump(call,True,True))
            if name not in self.namespace:
                return "%s: Sorry, I don't know the function %r"%(sender,name)
            function = self.namespace.get(name)
            if not hasattr(function,'__call__'):
                return "%s: Sorry, that isn't a function %r"%(sender,name)
            args = []
            for arg in call.args:
                if isinstance(arg,ast.Name):
                    if arg.id in self.namespace:
                        args.append(self.namespace[arg.id])
                    else:
                        return "%s: Could not find %r"%(sender,name)
                else:
                    value = ast.literal_eval(ast.Expr(arg))
                    args.append(value)
            named = {}
            event = Event(
                self,
                sender,
                message,
                args[:],
                named,
            )
            result = function(event,*args,**named)
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

def main():
    mc = minecraft.Minecraft.create()
    # players = [1,2,3]
    listener = ChatListener(mc)
    listener.poll()
    
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()
