"""Player listing and detail endpoints"""
from aiohttp import web

from ..serialization import serialize


async def get_players(request):
    """GET /api/players — list all online players"""
    services = request.app['services']
    channel = services.channel
    try:
        players = await channel.server.getOnlinePlayers()
        result = [serialize(p) for p in players]
        return web.json_response(result)
    except Exception as err:
        return web.json_response({'error': str(err)}, status=500)
