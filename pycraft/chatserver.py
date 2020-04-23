import argparse, logging, threading
from . import (
    chatcommands, expose,
    parabolic,
    bulldozer,
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
    listener.poll()
