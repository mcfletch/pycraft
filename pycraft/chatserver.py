import argparse, logging, threading
from . import (
    chatcommands, expose,
    parabolic,
    bulldozer,
    buildings,
)
from mcpi import minecraft
log = logging.getLogger(__name__)

def get_options():
    parser = argparse.ArgumentParser(
        description='Run minecraft mcpi chat-command server'
    )
    parser.add_argument(
        '-H','--host',
        help='Host (server) ip to which to connect, default 127.0.0.1',
        default='127.0.0.1',
    )
    parser.add_argument(
        '-p','--port',
        help='Host (server) port to which to connect, default 25565',
        default=25565,
    )
    parser.add_argument(
        '-v','--verbose',
        default=False,
        help = 'If specified, do verbose API logging',
        action='store_true',
    )
    parser.add_argument(
        '--hot-reload',
        default=False,
        action='store_true',
        help ='If specified, watch the pychart directory for changes and reload it seen',
    )
    return parser

def main():
    options = get_options().parse_args()
    if options.verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
    mc = minecraft.Minecraft.create()
    # players = [1,2,3]
    listener = chatcommands.ChatListener(mc)
    log.info("Listening to chat now")
    threading.Thread(target=listener.interpreter,daemon=True).start()
    threading.Thread(target=listener.responder,daemon=True).start()
    if options.hot_reload:
        from . import hotreload
        threading.Thread(
            target=hotreload.hot_reload(

            )
        ).start()
    listener.poll()

    