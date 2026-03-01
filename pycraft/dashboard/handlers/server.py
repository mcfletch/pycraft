"""Server info and world listing endpoints"""
from aiohttp import web

from ..serialization import serialize


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
        return web.json_response(
            {
                'version': version if isinstance(version, str) else str(version),
                'worlds': world_list,
            }
        )
    except Exception as err:
        return web.json_response({'error': str(err)}, status=500)


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
