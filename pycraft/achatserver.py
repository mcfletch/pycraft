import argparse, logging, threading, asyncio
from .server import channel
from . import (
    alistener,
    # expose,
    # commands,
    parabolic,
    bulldozer,
    buildings,
    # farm,
    # tunnels,
    # copypaste,
)

# from mcpi import minecraft

log = logging.getLogger(__name__)


def get_options():
    parser = argparse.ArgumentParser(
        description='Run minecraft mcpi chat-command server'
    )
    parser.add_argument(
        '-H',
        '--host',
        help='Host (server) ip to which to connect, default 127.0.0.1',
        default='127.0.0.1',
    )
    parser.add_argument(
        '-p',
        '--port',
        type=int,
        help='Host (server) port to which to connect, default 4712',
        default=4712,
    )
    parser.add_argument(
        '-v',
        '--verbose',
        default=False,
        help='If specified, do verbose API logging',
        action='store_true',
    )
    parser.add_argument(
        '--hot-reload',
        default=False,
        action='store_true',
        help='If specified, watch the pychart directory for changes and reload when seen (requires inotify-tools package)',
    )
    return parser


async def run(options):
    if options.verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
    server = channel.Channel(host=options.host, port=options.port, debug=True)
    await server.open()
    await server.introspect()

    worlds = await server.server.getWorlds()

    log.info("getWorlds => %s", worlds)

    # players = [1,2,3]
    listen = alistener.AListener(server)

    def shutdown():
        listen.wanted = False
        try:
            log.info("Closing chat socket")
            server.close()
        except Exception as err:
            pass

    if options.hot_reload:
        # raise RuntimeError('Not yet working')
        from . import hotreload

        t = threading.Thread(
            target=hotreload.hot_reload,
            kwargs=dict(
                callback=shutdown,
            ),
            daemon=True,
        )
        t.start()
    try:
        log.info("Trying to subscribe to chat")
        await listen.listen()
        log.info("Listening to chat now")
    except asyncio.TimeoutError as err:
        log.warning("Timed out listening to connection")
        raise


def main():
    logging.basicConfig(level=logging.DEBUG)
    options = get_options().parse_args()
    asyncio.ensure_future(run(options))
    asyncio.get_event_loop().run_forever()
