"""Search endpoints for materials, entity types, and other enums"""
import asyncio
import logging

from aiohttp import web

from pycraft.server import final
from pycraft.server.world import Location
from ..serialization import serialize

log = logging.getLogger(__name__)


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


SEARCH_RADIUS = 1000  # blocks


async def _search_players(query, channel):
    """Search online players by name"""
    results = []
    try:
        players = await channel.server.getOnlinePlayers()
        for p in players:
            name = getattr(p, 'name', '')
            if query in name.lower():
                loc = getattr(p, 'location', None)
                results.append({
                    'type': 'player',
                    'name': name,
                    'location': serialize(loc) if loc else None,
                })
    except Exception:
        log.exception("Player search failed")
    return results


async def _search_structures(query, world_name, origin_x, origin_z):
    """Search for structures matching the query near the origin"""
    results = []
    try:
        structure_types = await final.StructureType.cached_values()
        matching = []
        for st in structure_types:
            key = getattr(st, 'key', str(st))
            if key and query in key.lower():
                matching.append((key, st))
        if not matching:
            return results

        world = final.World(name=world_name)
        origin = Location([world_name, float(origin_x), 64.0, float(origin_z)])

        async def locate_one(name, st):
            try:
                loc = await world.locateNearestStructure(origin, st, SEARCH_RADIUS, False)
                if loc is not None:
                    return {
                        'type': 'structure',
                        'name': name.replace('minecraft:', ''),
                        'location': serialize(loc),
                    }
            except Exception:
                log.debug("Structure locate failed for %s", name, exc_info=True)
            return None

        # Run locate calls concurrently (limit to first 5 matches)
        tasks = [locate_one(name, st) for name, st in matching[:5]]
        for result in await asyncio.gather(*tasks):
            if result:
                results.append(result)
    except Exception:
        log.exception("Structure search failed")
    return results


async def _search_biomes(query, world_name, origin_x, origin_z):
    """Search for biomes matching the query near the origin"""
    results = []
    try:
        biomes = await final.Biome.cached_values()
        matching = []
        for b in biomes:
            key = getattr(b, 'key', str(b))
            if key and query in key.lower():
                matching.append((key, b))
        if not matching:
            return results

        world = final.World(name=world_name)
        origin = Location([world_name, float(origin_x), 64.0, float(origin_z)])

        async def locate_one(name, biome):
            try:
                loc = await world.locateNearestBiome(origin, biome, SEARCH_RADIUS)
                if loc is not None:
                    return {
                        'type': 'biome',
                        'name': name.replace('minecraft:', ''),
                        'location': serialize(loc),
                    }
            except Exception:
                log.debug("Biome locate failed for %s", name, exc_info=True)
            return None

        # Run locate calls concurrently (limit to first 5 matches)
        tasks = [locate_one(name, b) for name, b in matching[:5]]
        for result in await asyncio.gather(*tasks):
            if result:
                results.append(result)
    except Exception:
        log.exception("Biome search failed")
    return results


async def _search_entities_on_map(query, world_name):
    """Search for entities in the world matching the query"""
    results = []
    try:
        world = final.World(name=world_name)
        entities = await world.getEntities()
        # Group by type, track locations
        type_groups = {}
        for e in entities:
            e_type = getattr(e, 'type', None)
            e_name = getattr(e, 'name', '')
            type_key = getattr(e_type, 'key', str(e_type)) if e_type else ''
            display = e_name or type_key
            if query in type_key.lower() or query in (e_name or '').lower():
                if type_key not in type_groups:
                    type_groups[type_key] = {
                        'type': 'entity',
                        'name': type_key.replace('minecraft:', ''),
                        'location': serialize(getattr(e, 'location', None)),
                        'count': 0,
                    }
                type_groups[type_key]['count'] += 1
        results = list(type_groups.values())
    except Exception:
        log.debug("Entity search failed", exc_info=True)
    return results


async def search_map(request):
    """GET /api/search/map?q=...&world=...&x=...&z=... — unified map search

    Searches players, structures, biomes, and entities concurrently.
    """
    query = request.query.get('q', '').strip().lower()
    if len(query) < 2:
        return web.json_response({'results': []})

    world_name = request.query.get('world', 'world')
    try:
        origin_x = float(request.query.get('x', 0))
        origin_z = float(request.query.get('z', 0))
    except (ValueError, TypeError):
        origin_x, origin_z = 0.0, 0.0

    # Run all search categories concurrently
    services = request.app['services']
    channel = services.channel
    player_task = _search_players(query, channel)
    structure_task = _search_structures(query, world_name, origin_x, origin_z)
    biome_task = _search_biomes(query, world_name, origin_x, origin_z)
    entity_task = _search_entities_on_map(query, world_name)

    player_results, structure_results, biome_results, entity_results = await asyncio.gather(
        player_task, structure_task, biome_task, entity_task,
        return_exceptions=True,
    )

    results = []
    for category in (player_results, structure_results, biome_results, entity_results):
        if isinstance(category, list):
            results.extend(category)

    return web.json_response({'results': results})
