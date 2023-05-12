"""Overall runner script for the pycraft-chat-server command"""
import argparse, logging, asyncio, logging.handlers, os, time
from .server import channel
from . import (
    alistener,
    scriptloader,
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
    parser.add_argument(
        '--log-dir',
        default=None,
        help='If specified, log chat messages to the given directory, defaults to the calling directory',
    )
    parser.add_argument(
        '--scripts',
        default='/var/pycraft/scripts',
        help='A pathsep (%s) separated set of full paths to script-files to load into the interpreter namespace',
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
    scripts = scriptloader.ScriptLoader(options.scripts)
    asyncio.create_task(scripts.main(), name='script-loader')
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

            listen = alistener.AListener(server, scripts=scripts)
            try:
                log.info("Trying to subscribe to chat")
                await listen.listen()
                log.info("Listening to chat now")
            except asyncio.TimeoutError as err:
                log.warning("Timed out listening to connection")
                raise
            else:
                break


def chat_log_setup(directory):
    chat_log = logging.getLogger('chat-log')
    chat_log.setLevel(logging.INFO)
    # chat_log.propagate = False
    chat_handler = logging.handlers.RotatingFileHandler(
        os.path.join(directory, 'chatserver.log'),
        maxBytes=1024 * 1024,
    )
    chat_formatter = logging.Formatter('%(message)s')
    chat_handler.setFormatter(chat_formatter)
    chat_log.addHandler(chat_handler)
    chat_log.info("Chat Server Started %s", time.strftime('%Y-%m-%d %H:%M:%S'))
    return chat_log


def main():
    logging.basicConfig(level=logging.DEBUG)
    options = get_options().parse_args()
    chat_log_setup(options.log_dir or '.')
    asyncio.ensure_future(chatserver(options))
    asyncio.get_event_loop().run_forever()
