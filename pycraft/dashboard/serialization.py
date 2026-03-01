"""Convert pycraft proxy objects to JSON-serializable dicts"""
import json
import uuid as uuid_mod
import numpy as np
from pycraft.server import world


def serialize(obj):
    """Recursively serialize a proxy object to a JSON-safe dict/list/primitive"""
    if obj is None:
        return None
    if isinstance(obj, (str, int, float, bool)):
        return obj
    if isinstance(obj, uuid_mod.UUID):
        return str(obj)
    if isinstance(obj, np.integer):
        return int(obj)
    if isinstance(obj, np.floating):
        return float(obj)
    if isinstance(obj, np.ndarray):
        return [serialize(v) for v in obj]
    if isinstance(obj, world.Location):
        return {
            'world': obj.world,
            'x': float(obj.x),
            'y': float(obj.y),
            'z': float(obj.z),
            'yaw': float(obj.yaw),
            'pitch': float(obj.pitch),
        }
    if isinstance(obj, world.Vector):
        return {
            'x': float(obj.x),
            'y': float(obj.y),
            'z': float(obj.z),
        }
    if isinstance(obj, world.Player):
        return {
            'uuid': str(obj.uuid) if hasattr(obj, 'uuid') else None,
            'name': getattr(obj, 'name', None),
            'display_name': getattr(obj, 'display_name', None),
            'location': serialize(getattr(obj, 'location', None)),
            'type': getattr(obj, 'type', None),
            'online': getattr(obj, 'online', None),
            'banned': getattr(obj, 'banned', None),
            'whitelisted': getattr(obj, 'whitelisted', None),
        }
    if isinstance(obj, world.Entity):
        return {
            'uuid': str(obj.uuid) if hasattr(obj, 'uuid') else None,
            'name': getattr(obj, 'name', None),
            'display_name': getattr(obj, 'display_name', None),
            'type': getattr(obj, 'type', None),
            'location': serialize(getattr(obj, 'location', None)),
        }
    if isinstance(obj, world.World):
        return {
            'name': obj.name,
            'players': serialize(getattr(obj, 'players', [])),
        }
    if isinstance(obj, world.ItemStack):
        return {
            'material': getattr(obj, 'material', None),
            'amount': getattr(obj, 'amount', 0),
            'enchantments': serialize(getattr(obj, 'enchantments', {})),
            'key': getattr(obj, 'key', None),
        }
    if isinstance(obj, world.Inventory):
        return {
            'size': getattr(obj, 'size', 0),
            'contents': serialize(getattr(obj, 'contents', [])),
            'type': getattr(obj, 'type', None),
        }
    if isinstance(obj, world.Event):
        result = {'type': getattr(obj, 'type', None)}
        if hasattr(obj, 'player') and obj.player is not None:
            result['player'] = serialize(obj.player)
        if hasattr(obj, 'message') and obj.message is not None:
            result['message'] = obj.message
        if hasattr(obj, 'block') and obj.block is not None:
            result['block'] = serialize(obj.block)
        if hasattr(obj, 'entity') and obj.entity is not None:
            result['entity'] = serialize(obj.entity)
        return result
    if isinstance(obj, world.Block):
        return {
            'location': serialize(getattr(obj, 'location', None)),
            'data': serialize(getattr(obj, 'data', None)),
        }
    if isinstance(obj, world.BlockData):
        return getattr(obj, 'string_value', None)
    if isinstance(obj, dict):
        return {str(k): serialize(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [serialize(item) for item in obj]
    # Fallback: try __dict__ for other proxy objects
    if hasattr(obj, '__dict__') and obj.__dict__:
        return {k: serialize(v) for k, v in obj.__dict__.items() if not k.startswith('_')}
    return str(obj)


def to_json(obj):
    """Serialize a proxy object to a JSON string"""
    return json.dumps(serialize(obj))
