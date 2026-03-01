"""Route registration for the dashboard API"""
from .handlers import server, players


def setup_routes(app):
    """Register all API routes on the aiohttp application"""
    # Server info
    app.router.add_get('/api/server/info', server.get_server_info)
    app.router.add_get('/api/server/worlds', server.get_worlds)

    # Players
    app.router.add_get('/api/players', players.get_players)

    # SSE events
    async def sse_handler(request):
        return await request.app['services'].sse_manager.add_client(request)

    app.router.add_get('/api/events', sse_handler)
