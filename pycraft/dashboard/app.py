"""Pycraft Web Dashboard — aiohttp application factory and entry point"""
import argparse
import asyncio
import logging
import os
import pathlib

from aiohttp import web

from pycraft.server import channel

from .routes import setup_routes
from .services import DashboardServices
from .sse import SSEManager

log = logging.getLogger(__name__)

HERE = pathlib.Path(__file__).parent
FRONTEND_DIST = HERE / 'frontend' / 'dist'


def get_options():
    parser = argparse.ArgumentParser(description='Run the Pycraft web dashboard')
    parser.add_argument(
        '-H',
        '--host',
        default='127.0.0.1',
        help='Minecraft server host (default 127.0.0.1)',
    )
    parser.add_argument(
        '-p',
        '--port',
        type=int,
        default=4712,
        help='Minecraft server port (default 4712)',
    )
    parser.add_argument(
        '--listen-host',
        default='0.0.0.0',
        help='Dashboard HTTP listen address (default 0.0.0.0)',
    )
    parser.add_argument(
        '--listen-port',
        type=int,
        default=8080,
        help='Dashboard HTTP listen port (default 8080)',
    )
    parser.add_argument(
        '-v',
        '--verbose',
        default=False,
        action='store_true',
        help='Enable verbose logging',
    )
    return parser


async def connect_to_server(app):
    """Startup hook: connect to Minecraft server and start SSE subscriptions"""
    services = app['services']
    ch = services.channel
    try:
        await ch.open()
        await ch.introspect(cached=True)
        log.info("Connected to Minecraft server, introspection loaded")
        await services.sse_manager.start(ch)
        log.info("SSE event subscriptions active")
    except ConnectionRefusedError:
        log.error(
            "Cannot connect to Minecraft server at %s:%s — is it running?",
            ch.host,
            ch.port,
        )
        raise
    except Exception:
        log.exception("Failed to connect to Minecraft server")
        raise


async def cleanup(app):
    """Shutdown hook: close SSE and channel"""
    services = app['services']
    await services.sse_manager.stop()
    await services.channel.close()
    log.info("Dashboard shut down")


def create_app(mc_host='127.0.0.1', mc_port=4712, debug=False):
    """Create and configure the aiohttp application"""
    app = web.Application()

    ch = channel.Channel(host=mc_host, port=mc_port, debug=debug)
    sse_manager = SSEManager()
    services = DashboardServices(channel=ch, sse_manager=sse_manager)
    app['services'] = services

    setup_routes(app)

    # Serve frontend static files if the dist directory exists
    if FRONTEND_DIST.exists():
        # Serve index.html for the root and any non-API paths (SPA fallback)
        async def index_handler(request):
            return web.FileResponse(FRONTEND_DIST / 'index.html')

        app.router.add_get('/', index_handler)
        app.router.add_static('/assets/', FRONTEND_DIST / 'assets', name='assets')

        # SPA fallback: serve index.html for any path not matched by API routes
        async def spa_fallback(request):
            # Check if the path corresponds to an actual file in dist
            file_path = FRONTEND_DIST / request.path.lstrip('/')
            if file_path.exists() and file_path.is_file():
                return web.FileResponse(file_path)
            return web.FileResponse(FRONTEND_DIST / 'index.html')

        # Add a catch-all route last
        app.router.add_get('/{path:.*}', spa_fallback)

    app.on_startup.append(connect_to_server)
    app.on_cleanup.append(cleanup)

    return app


def main():
    parser = get_options()
    options = parser.parse_args()

    if options.verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    app = create_app(
        mc_host=options.host,
        mc_port=options.port,
        debug=options.verbose,
    )
    log.info(
        "Starting dashboard on %s:%s (MC server: %s:%s)",
        options.listen_host,
        options.listen_port,
        options.host,
        options.port,
    )
    web.run_app(app, host=options.listen_host, port=options.listen_port)
