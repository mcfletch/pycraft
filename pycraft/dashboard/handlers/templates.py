"""Template list, detail, and paste endpoints for the dashboard"""
import json
import logging

import numpy as np
from aiohttp import web

from pycraft import copypaste, rotations
from pycraft.server import final
from pycraft.server.world import Location, Vector

log = logging.getLogger(__name__)


async def list_templates(request):
    """GET /api/templates — list available templates with metadata"""
    try:
        names = copypaste.list_templates()
        result = []
        for name in sorted(names):
            template = copypaste.load_template(None, name)
            if not template:
                continue
            blocks = template.get('blocks', [])
            height = len(blocks)
            depth = len(blocks[0]) if height else 0
            width = len(blocks[0][0]) if depth else 0
            result.append({
                'name': name,
                'author': template.get('author', ''),
                'description': template.get('description', ''),
                'width': width,
                'depth': depth,
                'height': height,
            })
        return web.json_response(result)
    except Exception as err:
        log.exception("Failed to list templates")
        return web.json_response({'error': str(err)}, status=500)


async def get_template(request):
    """GET /api/templates/{name} — full template data for preview"""
    name = request.match_info['name']
    try:
        template = copypaste.load_template(None, name)
        if not template:
            return web.json_response({'error': f'Template {name} not found'}, status=404)

        blocks = template.get('blocks', [])
        height = len(blocks)
        depth = len(blocks[0]) if height else 0
        width = len(blocks[0][0]) if depth else 0

        # Build a top-down footprint: for each x,z column, find the topmost non-air block
        footprint = []
        for z in range(depth):
            row = []
            for x in range(width):
                material = None
                for y in range(height - 1, -1, -1):
                    cell = blocks[y][z][x]
                    if cell is None:
                        continue
                    mat = cell if isinstance(cell, str) else cell.get('material', '') if isinstance(cell, dict) else str(cell)
                    base = mat.split('[')[0]
                    if base and base not in ('minecraft:air', 'air'):
                        material = base
                        break
                row.append(material)
            footprint.append(row)

        return web.json_response({
            'name': name,
            'author': template.get('author', ''),
            'description': template.get('description', ''),
            'width': width,
            'depth': depth,
            'height': height,
            'offset': template.get('offset'),
            'footprint': footprint,
        })
    except Exception as err:
        log.exception("Failed to get template %s", name)
        return web.json_response({'error': str(err)}, status=500)


def _rotate_footprint(footprint, steps):
    """Rotate a 2D footprint grid by steps * 90 degrees CW.

    footprint is [z][x] (rows of columns).
    Uses numpy rot90 which rotates CCW, so we negate steps.
    """
    if steps == 0:
        return footprint
    arr = np.array(footprint, dtype=object)
    rotated = np.rot90(arr, -steps)
    return rotated.tolist()


def _rotate_blocks(blocks, steps):
    """Rotate a 3D blocks array [y][z][x] by steps * 90 degrees CW.

    Applies both spatial rotation and material facing rotation.
    """
    if steps == 0:
        return blocks
    result = []
    for layer in blocks:
        arr = np.array(layer, dtype=object)
        rotated = np.rot90(arr, -steps)
        # Rotate material facing properties
        rotated_mats = []
        for row in rotated.tolist():
            new_row = []
            for cell in row:
                if cell is None:
                    new_row.append(None)
                elif isinstance(cell, str):
                    new_row.append(rotations.rotate(cell, steps))
                elif isinstance(cell, dict):
                    new_cell = cell.copy()
                    new_cell['material'] = rotations.rotate(cell.get('material', ''), steps)
                    new_row.append(new_cell)
                else:
                    new_row.append(cell)
            rotated_mats.append(new_row)
        result.append(rotated_mats)
    return result


async def paste_template(request):
    """POST /api/worlds/{name}/paste — paste a template at absolute coordinates"""
    world_name = request.match_info['name']
    try:
        data = await request.json()
    except Exception:
        return web.json_response({'error': 'Invalid JSON body'}, status=400)

    template_name = data.get('template_name')
    if not template_name:
        return web.json_response({'error': 'Missing template_name'}, status=400)

    for field in ('x', 'y', 'z'):
        if field not in data:
            return web.json_response({'error': f'Missing field: {field}'}, status=400)

    try:
        template = copypaste.load_template(None, template_name)
        if not template:
            return web.json_response({'error': f'Template {template_name} not found'}, status=404)

        rotation = int(data.get('rotation', 0)) % 4
        template_blocks = template.get('blocks', [])
        if not template_blocks:
            return web.json_response({'error': 'Template has no blocks'}, status=400)

        if rotation:
            template_blocks = _rotate_blocks(template_blocks, rotation)

        height = len(template_blocks)
        depth = len(template_blocks[0]) if height else 0
        width = len(template_blocks[0][0]) if depth else 0

        # Position is the center of the base — compute start corner
        base_x = int(data['x']) - width // 2
        base_y = int(data['y'])
        base_z = int(data['z']) - depth // 2

        # Apply template offset if present
        offset = template.get('offset')
        if offset:
            base_x += int(offset[0]) if len(offset) > 0 else 0
            base_y += int(offset[1]) if len(offset) > 1 else 0
            base_z += int(offset[2]) if len(offset) > 2 else 0

        world = final.World(name=world_name)
        locations = []
        blocks = []

        for y_idx, layer in enumerate(template_blocks):
            for z_idx, row in enumerate(layer):
                for x_idx, cell in enumerate(row):
                    if cell is None:
                        continue
                    if isinstance(cell, dict):
                        mat = cell.get('material', '')
                    elif isinstance(cell, str):
                        mat = cell
                    else:
                        continue
                    base = mat.split('[')[0] if mat else ''
                    if base in ('minecraft:air', 'air', ''):
                        continue
                    # Apply data updates (renamed blocks)
                    mat = copypaste.DATA_UPDATES.get(
                        f'minecraft:{mat}' if ':' not in mat else mat, mat
                    )
                    wx = base_x + x_idx
                    wy = base_y + y_idx
                    wz = base_z + z_idx
                    locations.append(Location([world_name, float(wx), float(wy), float(wz)]))
                    blocks.append(mat)

        count = await world.setBlockList(locations, blocks)
        return web.json_response({
            'status': 'ok',
            'blocks_placed': len(blocks),
            'count': count,
        })
    except Exception as err:
        log.exception("Failed to paste template %s", template_name)
        return web.json_response({'error': str(err)}, status=500)
