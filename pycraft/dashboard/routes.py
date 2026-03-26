"""Route registration for the dashboard API"""
from . import auth, textures
from .handlers import server, players, world, commands, search, templates


def setup_routes(app):
    """Register all API routes on the aiohttp application"""
    # Authentication
    app.router.add_post('/api/auth/login', auth.login_handler)
    app.router.add_post('/api/auth/logout', auth.logout_handler)
    app.router.add_get('/api/auth/status', auth.status_handler)

    # Server info
    app.router.add_get('/api/server/info', server.get_server_info)
    app.router.add_get('/api/server/worlds', server.get_worlds)

    # Players
    app.router.add_get('/api/players', players.get_players)
    app.router.add_get('/api/players/{uuid}', players.get_player_detail)
    app.router.add_get('/api/players/{uuid}/inventory', players.get_player_inventory)
    app.router.add_post('/api/players/{uuid}/teleport', players.teleport_player)
    app.router.add_post('/api/players/{uuid}/inventory/give', players.give_item)
    app.router.add_post('/api/players/{uuid}/inventory/enchant', players.enchant_item)
    app.router.add_post('/api/players/{uuid}/inventory/drop', players.drop_item)
    app.router.add_post('/api/players/{uuid}/inventory/move', players.move_item)
    app.router.add_get('/api/players/{uuid}/inventory/{slot}/applicable-enchantments', players.applicable_enchantments)

    # World
    app.router.add_get('/api/worlds/{name}/entities', world.get_world_entities)
    app.router.add_post('/api/worlds/{name}/entities/spawn', world.spawn_entity)
    app.router.add_get('/api/worlds/{name}/blocks', world.get_blocks)
    app.router.add_post('/api/worlds/{name}/blocks', world.set_blocks)
    app.router.add_get('/api/worlds/{name}/surface', world.get_surface_y)

    # Enchantments
    app.router.add_get('/api/enchantments', players.list_enchantments)

    # Potions
    app.router.add_get('/api/potion-types', players.list_potion_types)

    # Templates (copy/paste)
    app.router.add_get('/api/templates', templates.list_templates)
    app.router.add_get('/api/templates/{name}', templates.get_template)
    app.router.add_post('/api/worlds/{name}/paste', templates.paste_template)

    # Code evaluation
    app.router.add_post('/api/eval', commands.eval_code)

    # Search
    app.router.add_get('/api/search/blocks', search.search_blocks)
    app.router.add_get('/api/search/entities', search.search_entities)
    app.router.add_get('/api/search/map', search.search_map)

    # SSE events
    async def sse_handler(request):
        return await request.app['services'].sse_manager.add_client(request)

    app.router.add_get('/api/events', sse_handler)

    # Textures (served from Faithful 32x ZIP)
    app.router.add_get('/api/textures', textures.list_textures)
    app.router.add_get('/api/textures/items/{name}', textures.get_item_texture)
    app.router.add_get('/api/textures/side/{name}', textures.get_side_texture)
    app.router.add_get('/api/textures/{name}', textures.get_texture)
