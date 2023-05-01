"""Overall runner script for the pycraft-chat-server command"""
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

log = logging.getLogger(__name__)


def get_options():
    """Gets the command-line argument parser for the chat server program"""
    parser = argparse.ArgumentParser(
        description='Run minecraft pycraft chat-command server'
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
    return parser


async def chatserver(options):
    """Top level driver with recovery from connection failure"""
    if options.verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
    server = channel.Channel(
        host=options.host, port=options.port, debug=options.verbose
    )
    while True:
        try:
            await server.open()
            await server.introspect(cached=True)
        except KeyboardInterrupt:
            return
        except ConnectionRefusedError as err:
            log.warning(
                "Connection to server refused (likely not yet running), waiting"
            )
            await asyncio.sleep(5)
        except Exception as err:
            log.exception("Failure during setup, pausing before reconnection")
            await asyncio.sleep(10)
        else:
            worlds = await server.server.getWorlds()

            log.info("getWorlds => %s", worlds)
            world = worlds[0]
            world_cls = world.__class__

            listen = alistener.AListener(server)
            try:
                log.info("Trying to subscribe to chat")
                await listen.listen()
                log.info("Listening to chat now")
            except asyncio.TimeoutError as err:
                log.warning("Timed out listening to connection")
                raise
            else:
                break


def main():
    logging.basicConfig(level=logging.DEBUG)
    options = get_options().parse_args()
    asyncio.ensure_future(chatserver(options))
    asyncio.get_event_loop().run_forever()
