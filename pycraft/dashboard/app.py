"""Pycraft Web Dashboard — aiohttp application factory and entry point"""
import argparse
import asyncio
import logging
import os
import pathlib
import subprocess

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
        default=None,
        help='Minecraft server host (default: auto-detect from docker, fallback to localhost)',
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


async def _do_connect(services):
    """Attempt a single connection to the Minecraft server.

    Returns True on success, False on failure.
    """
    ch = services.channel
    try:
        await ch.open()
        await ch.introspect(cached=True)
        log.info("Connected to Minecraft server, introspection loaded")
        await services.sse_manager.start(ch)
        log.info("SSE event subscriptions active")
        services.connected = True
        return True
    except Exception as err:
        log.warning("MC server connection failed: %s", err)
        services.connected = False
        return False


async def _reconnect_loop(app):
    """Background task that maintains the MC server connection.

    On startup and after disconnects, retries with exponential backoff
    (1s, 2s, 4s, 8s, ... up to 30s).
    """
    services = app['services']
    delay = 1

    # Initial connection attempt
    if await _do_connect(services):
        delay = 1
    else:
        log.info(
            "MC server at %s not available yet — will keep retrying",
            services.channel.address,
        )

    while True:
        try:
            if services.connected:
                # Monitor: check if the channel is still alive
                if services.channel.writer is None or services.channel.writer.is_closing():
                    log.warning("MC server connection lost — reconnecting")
                    services.connected = False
                    await services.sse_manager.stop()
                    try:
                        await services.channel.close()
                    except Exception:
                        pass
                    delay = 1
                else:
                    await asyncio.sleep(5)
                    continue

            # Not connected — wait then retry
            await asyncio.sleep(delay)
            if await _do_connect(services):
                log.info("Reconnected to MC server")
                delay = 1
            else:
                delay = min(delay * 2, 30)
        except asyncio.CancelledError:
            return
        except Exception:
            log.exception("Error in reconnect loop")
            delay = min(delay * 2, 30)
            await asyncio.sleep(delay)


async def connect_to_server(app):
    """Startup hook: start the background reconnect loop"""
    app['reconnect_task'] = asyncio.create_task(_reconnect_loop(app))


async def cleanup(app):
    """Shutdown hook: cancel reconnect loop, close SSE and channel"""
    task = app.get('reconnect_task')
    if task:
        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            pass
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


def find_minecraft_host(container_name='minecraft'):
    """Find the Minecraft server IP via docker inspect.

    Returns the container's IP address, or 'localhost' if the container is not
    found or docker is unavailable.
    """
    try:
        ip = subprocess.check_output(
            [
                'docker', 'inspect', '-f',
                '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}',
                container_name,
            ],
            stderr=subprocess.DEVNULL,
        ).decode('utf-8').strip()
        if ip:
            log.info("Auto-detected Minecraft container '%s' at %s", container_name, ip)
            return ip
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass
    log.info("No Minecraft container found, falling back to localhost")
    return 'localhost'


def main():
    parser = get_options()
    options = parser.parse_args()

    if options.verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    host = options.host or find_minecraft_host()

    app = create_app(
        mc_host=host,
        mc_port=options.port,
        debug=options.verbose,
    )
    log.info(
        "Starting dashboard on %s:%s (MC server: %s:%s)",
        options.listen_host,
        options.listen_port,
        host,
        options.port,
    )
    web.run_app(app, host=options.listen_host, port=options.listen_port)
