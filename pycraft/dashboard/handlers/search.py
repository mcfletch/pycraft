"""Search endpoints for materials, entity types, and other enums"""
from aiohttp import web

from pycraft.server import final


async def search_blocks(request):
    """GET /api/search/blocks?q= — search Material names"""
    query = request.query.get('q', '').strip().lower()
    if not query:
        return web.json_response({'error': 'Missing query parameter q'}, status=400)
    try:
        materials = await final.Material.cached_values()
        matches = []
        for m in materials:
            key = getattr(m, 'key', str(m))
            if query in key.lower():
                matches.append(key)
        matches.sort()
        return web.json_response({'results': matches[:50]})
    except Exception as err:
        return web.json_response({'error': str(err)}, status=500)


async def search_entities(request):
    """GET /api/search/entities?q= — search EntityType names"""
    query = request.query.get('q', '').strip().lower()
    if not query:
        return web.json_response({'error': 'Missing query parameter q'}, status=400)
    try:
        entity_types = await final.EntityType.cached_values()
        matches = []
        for e in entity_types:
            key = getattr(e, 'key', str(e))
            if query in key.lower():
                matches.append(key)
        matches.sort()
        return web.json_response({'results': matches[:50]})
    except Exception as err:
        return web.json_response({'error': str(err)}, status=500)
