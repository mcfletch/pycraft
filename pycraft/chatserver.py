import argparse, logging, threading
from . import (
    listener, 
    expose,
    commands,
    parabolic,
    bulldozer,
    buildings,
    farm,
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
        type=int,
        help='Host (server) port to which to connect, default 4711',
        default=4711,
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
        help ='If specified, watch the pychart directory for changes and reload when seen (requires inotify-tools package)',
    )
    return parser

def main():
    options = get_options().parse_args()
    if options.verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
    mc = minecraft.Minecraft.create(
        options.host,
        port=options.port
    )
    # players = [1,2,3]
    listen = listener.Listener(mc)
    def shutdown():
        listen.wanted = False
        try:
            log.info("Closing chat socket")
            listen.mc.socket.close()
        except Exception as err:
            pass
    threading.Thread(target=listen.interpreter,daemon=True).start()
    threading.Thread(target=listen.responder,daemon=True).start()
    if options.hot_reload:
        # raise RuntimeError('Not yet working')
        from . import hotreload
        t = threading.Thread(
            target=hotreload.hot_reload,
            kwargs=dict(
                callback = shutdown,
            ),
            daemon=True,
        )
        t.start()
    log.info("Listening to chat now")
    listen.poll()

    