"""Server info and world listing endpoints"""
import json
import os
import platform
import sys

from aiohttp import web

from ..serialization import serialize

INTROSPECTION_CACHE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '..', '..', 'server', '.introspection.json',
)


def _get_plugin_info():
    """Read PycraftServer plugin version from introspection cache."""
    try:
        with open(INTROSPECTION_CACHE) as f:
            data = json.load(f)
        plugins = data.get('plugins', {})
        ps = plugins.get('PycraftServer', {})
        return {
            'name': ps.get('name', 'PycraftServer'),
            'version': ps.get('version', 'unknown'),
            'api': ps.get('api', 'unknown'),
        }
    except Exception:
        return {'name': 'PycraftServer', 'version': 'unknown', 'api': 'unknown'}


async def get_server_info(request):
    """GET /api/server/info — server version, worlds, plugin info"""
    services = request.app['services']
    channel = services.channel
    try:
        worlds = await channel.server.getWorlds()
        version = await channel.server.getVersion()
        world_list = []
        for w in worlds:
            players = getattr(w, 'players', [])
            world_list.append(
                {
                    'name': w.name,
                    'player_count': len(players) if players else 0,
                }
            )
        mc_host, mc_port = channel.address
        return web.json_response(
            {
                'version': version if isinstance(version, str) else str(version),
                'worlds': world_list,
                'plugin': _get_plugin_info(),
                'python_version': platform.python_version(),
                'dashboard_host': request.host,
                'mc_server': f'{mc_host}:{mc_port}',
                'connected': services.connected,
            }
        )
    except Exception as err:
        mc_host, mc_port = channel.address
        return web.json_response(
            {
                'error': str(err),
                'plugin': _get_plugin_info(),
                'python_version': platform.python_version(),
                'dashboard_host': request.host,
                'mc_server': f'{mc_host}:{mc_port}',
                'connected': services.connected,
            },
            status=500,
        )


async def get_worlds(request):
    """GET /api/server/worlds — list worlds with player counts"""
    services = request.app['services']
    channel = services.channel
    try:
        worlds = await channel.server.getWorlds()
        result = []
        for w in worlds:
            result.append(serialize(w))
        return web.json_response(result)
    except Exception as err:
        return web.json_response({'error': str(err)}, status=500)
