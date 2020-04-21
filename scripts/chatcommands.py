"""Expose commands via chat on a minecraft instance"""
from mcpi import minecraft, block
import threading, logging
import re, time
import contextlib
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


DEFAULT_COMMANDS = {

}
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
                    parsed = match.groupdict()
                    sender = self.get_entity_name(message.entityId)
                    log.debug("User %s => %s(%s)", sender, parsed['function'],parsed['args'])
            if not messages:
                time.sleep(1)
    
    def interpreter(self,queue):
        """Interpret a command from our queue"""

def main():
    mc = minecraft.Minecraft.create()
    # players = [1,2,3]
    listener = ChatListener(mc)
    listener.poll()
    
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()
