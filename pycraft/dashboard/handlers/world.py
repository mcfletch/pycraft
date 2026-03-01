"""World, block, and entity endpoints"""
import logging

from aiohttp import web

from pycraft.server import final
from pycraft.server.world import Location, Vector

from ..serialization import serialize

log = logging.getLogger(__name__)


async def get_world_entities(request):
    """GET /api/worlds/{name}/entities — list entities in a world"""
    services = request.app['services']
    channel = services.channel
    world_name = request.match_info['name']
    try:
        world = final.World(name=world_name)
        entities = await world.getEntities()
        result = [serialize(e) for e in entities]
        return web.json_response(result)
    except Exception as err:
        return web.json_response({'error': str(err)}, status=500)


async def spawn_entity(request):
    """POST /api/worlds/{name}/entities/spawn — spawn entity at location"""
    services = request.app['services']
    channel = services.channel
    world_name = request.match_info['name']
    try:
        data = await request.json()
    except Exception:
        return web.json_response({'error': 'Invalid JSON body'}, status=400)
    for field in ('type', 'x', 'y', 'z'):
        if field not in data:
            return web.json_response({'error': f'Missing field: {field}'}, status=400)
    try:
        loc = Location([world_name, float(data['x']), float(data['y']), float(data['z'])])
        world = final.World(name=world_name)
        entity = await world.spawnEntity(loc, data['type'])
        return web.json_response({'status': 'ok', 'entity': serialize(entity)})
    except Exception as err:
        return web.json_response({'error': str(err)}, status=500)


Y_RANGE = 30  # scan this many blocks above and below center Y
CHUNK_SIZE = 32  # max blocks per RPC call in x and z

AIR_BLOCKS = frozenset({
    'minecraft:air',
    'minecraft:cave_air',
    'minecraft:void_air',
})


def _is_air(cell):
    """Check if a block cell is any type of air."""
    base = cell.split('[')[0] if isinstance(cell, str) else cell
    return base in AIR_BLOCKS


def _find_surface_block(layers, x_idx, z_idx, num_y, center_y_idx):
    """Find the visible floor/surface block at this x,z column.

    Algorithm (per the user's specification):
    - Check the block at center_y_idx
    - If AIR: scan DOWN to find the first non-air block (the floor beneath us)
    - If SOLID: scan UP to find the first air block, then use the block below
      it (the surface we'd see looking up)
    - If we exhaust the search depth without finding a transition, render
      whatever is at center_y_idx
    """
    center_y_idx = max(0, min(center_y_idx, num_y - 1))
    center_cell = layers[center_y_idx][z_idx][x_idx]

    if _is_air(center_cell):
        # In air — scan downward to find the floor
        for y_idx in range(center_y_idx - 1, -1, -1):
            cell = layers[y_idx][z_idx][x_idx]
            if not _is_air(cell):
                base = cell.split('[')[0] if isinstance(cell, str) else cell
                return base
        # Hit bottom of slab without finding solid — return air
        return 'minecraft:air'
    else:
        # In solid — scan upward to find air, return the block just below air
        for y_idx in range(center_y_idx + 1, num_y):
            cell = layers[y_idx][z_idx][x_idx]
            if _is_air(cell):
                # The block below this air is the surface
                surface = layers[y_idx - 1][z_idx][x_idx]
                base = surface.split('[')[0] if isinstance(surface, str) else surface
                return base
        # Hit top of slab without finding air — return the block at center
        base = center_cell.split('[')[0] if isinstance(center_cell, str) else center_cell
        return base


async def get_blocks(request):
    """GET /api/worlds/{name}/blocks — top-down surface view for a region.

    Fetches a vertical slab (y +/- 30) and collapses each x,z column
    to the nearest floor block around center Y.  A floor block is a non-air
    block with air above it, searched outward from the center so caves show
    the floor the player is standing on rather than the ceiling.
    """
    services = request.app['services']
    channel = services.channel
    world_name = request.match_info['name']
    try:
        x1 = int(request.query.get('x1', 0))
        z1 = int(request.query.get('z1', 0))
        x2 = int(request.query.get('x2', x1 + 16))
        z2 = int(request.query.get('z2', z1 + 16))
        y = int(request.query.get('y', 64))
        # Clamp horizontal size to prevent server overload
        max_size = 128
        x2 = min(x2, x1 + max_size)
        z2 = min(z2, z1 + max_size)
    except (ValueError, TypeError) as err:
        return web.json_response({'error': f'Invalid query params: {err}'}, status=400)
    try:
        world = final.World(name=world_name)
        y_lo = max(-64, y - Y_RANGE)
        y_hi = min(319, y + Y_RANGE)
        center_y_idx = y - y_lo
        total_w = x2 - x1
        total_h = z2 - z1
        # Pre-allocate the output grid
        blocks = [['minecraft:air'] * total_h for _ in range(total_w)]
        # Fetch in CHUNK_SIZE x CHUNK_SIZE tiles to avoid overwhelming MC server
        for cx in range(x1, x2, CHUNK_SIZE):
            cx_end = min(cx + CHUNK_SIZE, x2)
            for cz in range(z1, z2, CHUNK_SIZE):
                cz_end = min(cz + CHUNK_SIZE, z2)
                start = Vector(cx, y_lo, cz)
                stop = Vector(cx_end - 1, y_hi, cz_end - 1)
                try:
                    layers = await world.getBlockArray(start, stop)
                except Exception:
                    log.debug("Chunk fetch failed for [%d,%d]-[%d,%d]", cx, cz, cx_end, cz_end, exc_info=True)
                    continue
                num_y = len(layers)
                num_z = len(layers[0]) if num_y else 0
                num_x = len(layers[0][0]) if num_z else 0
                # Collapse each column and write into the output grid
                for lx in range(num_x):
                    for lz in range(num_z):
                        material = _find_surface_block(
                            layers, lx, lz, num_y, center_y_idx
                        )
                        blocks[cx - x1 + lx][cz - z1 + lz] = material
        # Fetch entities in the region (best-effort)
        entities = []
        try:
            all_entities = await world.getEntities()
            for e in all_entities:
                es = serialize(e)
                loc = es.get('location')
                if not loc:
                    continue
                ex, ey, ez = loc.get('x', 0), loc.get('y', 0), loc.get('z', 0)
                if x1 <= ex < x2 and z1 <= ez < z2 and ey >= y - Y_RANGE:
                    entities.append(es)
        except Exception:
            log.debug("Failed to fetch entities for blocks overlay", exc_info=True)
        return web.json_response({
            'world': world_name,
            'y': y,
            'x1': x1,
            'z1': z1,
            'x2': x2,
            'z2': z2,
            'blocks': blocks,
            'entities': entities,
        })
    except Exception as err:
        log.exception("get_blocks failed for world=%s", world_name)
        return web.json_response({'error': str(err)}, status=500)


async def get_surface_y(request):
    """GET /api/worlds/{name}/surface?x=&z= — get highest non-air block Y at x,z"""
    services = request.app['services']
    channel = services.channel
    world_name = request.match_info['name']
    try:
        x = int(request.query['x'])
        z = int(request.query['z'])
    except (KeyError, ValueError, TypeError) as err:
        return web.json_response({'error': f'Need integer x and z params: {err}'}, status=400)
    try:
        world = final.World(name=world_name)
        y = await world.getHighestBlockYAt(x, z)
        return web.json_response({'x': x, 'z': z, 'y': int(y)})
    except Exception as err:
        return web.json_response({'error': str(err)}, status=500)


async def set_blocks(request):
    """POST /api/worlds/{name}/blocks — set blocks at locations"""
    services = request.app['services']
    channel = services.channel
    world_name = request.match_info['name']
    try:
        data = await request.json()
    except Exception:
        return web.json_response({'error': 'Invalid JSON body'}, status=400)
    if 'locations' not in data or 'material' not in data:
        return web.json_response(
            {'error': 'Missing fields: locations and material required'}, status=400
        )
    try:
        locations = []
        for loc_data in data['locations']:
            locations.append(
                Location([world_name, float(loc_data['x']), float(loc_data['y']), float(loc_data['z'])])
            )
        material = data['material']
        materials = [material] * len(locations)
        world = final.World(name=world_name)
        # Single bulk RPC call
        count = await world.setBlockList(locations, materials)
        return web.json_response({'status': 'ok', 'count': count})
    except Exception as err:
        return web.json_response({'error': str(err)}, status=500)
