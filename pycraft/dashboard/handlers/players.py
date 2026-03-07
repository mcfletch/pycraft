"""Player listing, detail, inventory, teleport, give, and enchant endpoints"""
import logging

from aiohttp import web

from pycraft.server import final
from pycraft.server.world import Location

from ..serialization import serialize

log = logging.getLogger(__name__)

DESIRABLE_ENCHANTMENTS = [
    'minecraft:fire_protection',
    'minecraft:sharpness',
    'minecraft:flame',
    'minecraft:soul_speed',
    'minecraft:aqua_affinity',
    'minecraft:punch',
    'minecraft:loyalty',
    'minecraft:depth_strider',
    'minecraft:unbreaking',
    'minecraft:knockback',
    'minecraft:luck_of_the_sea',
    'minecraft:fortune',
    'minecraft:protection',
    'minecraft:efficiency',
    'minecraft:mending',
    'minecraft:frost_walker',
    'minecraft:lure',
    'minecraft:looting',
    'minecraft:piercing',
    'minecraft:blast_protection',
    'minecraft:smite',
    'minecraft:multishot',
    'minecraft:fire_aspect',
    'minecraft:channeling',
    'minecraft:thorns',
    'minecraft:bane_of_arthropods',
    'minecraft:respiration',
    'minecraft:quick_charge',
    'minecraft:projectile_protection',
    'minecraft:impaling',
    'minecraft:feather_falling',
    'minecraft:power',
    'minecraft:infinity',
]
DESIRABLE_SET = frozenset(DESIRABLE_ENCHANTMENTS)

# Known PotionEffectType names (Bukkit 1.21 API).
# The server enum doesn't deserialize properly, so we hardcode the names.
POTION_EFFECT_TYPES = [
    'SPEED',
    'SLOWNESS',
    'HASTE',
    'MINING_FATIGUE',
    'STRENGTH',
    'INSTANT_HEALTH',
    'INSTANT_DAMAGE',
    'JUMP_BOOST',
    'NAUSEA',
    'REGENERATION',
    'RESISTANCE',
    'FIRE_RESISTANCE',
    'WATER_BREATHING',
    'INVISIBILITY',
    'BLINDNESS',
    'NIGHT_VISION',
    'HUNGER',
    'WEAKNESS',
    'POISON',
    'WITHER',
    'HEALTH_BOOST',
    'ABSORPTION',
    'SATURATION',
    'GLOWING',
    'LEVITATION',
    'LUCK',
    'UNLUCK',
    'SLOW_FALLING',
    'CONDUIT_POWER',
    'DOLPHINS_GRACE',
    'BAD_OMEN',
    'HERO_OF_THE_VILLAGE',
    'DARKNESS',
    'TRIAL_OMEN',
    'RAID_OMEN',
    'WIND_CHARGED',
    'WEAVING',
    'OOZING',
    'INFESTED',
]

# Materials that are potions (can have potion metadata)
POTION_MATERIALS = frozenset([
    'minecraft:potion',
    'minecraft:splash_potion',
    'minecraft:lingering_potion',
    'minecraft:tipped_arrow',
])

# Cache for enchantment metadata (key → {max_level})
_enchantment_cache = None
_potion_type_cache = None


async def _find_player(channel, uuid_str):
    """Find an online player by UUID string"""
    players = await channel.server.getOnlinePlayers()
    for p in players:
        if str(getattr(p, 'uuid', '')) == uuid_str:
            return p
    return None


async def get_players(request):
    """GET /api/players — list all known players with online/offline status.

    Returns {online: [...], offline: [...]} where each entry has player fields.
    Query param ?online_only=1 returns just the flat online list (legacy compat).
    """
    services = request.app['services']
    channel = services.channel
    online_only = request.query.get('online_only')
    try:
        online_players = await channel.server.getOnlinePlayers()
        online_uuids = {str(getattr(p, 'uuid', '')) for p in online_players}
        online_list = [serialize(p) for p in online_players]
        # Mark all online players explicitly
        for p in online_list:
            p['online'] = True
        if online_only:
            return web.json_response(online_list)
        # Get all players who have ever logged in
        try:
            all_players = await channel.server.getOfflinePlayers()
        except Exception:
            all_players = []
        offline_list = []
        for p in all_players:
            uid = str(getattr(p, 'uuid', ''))
            if uid not in online_uuids:
                s = serialize(p)
                s['online'] = False
                offline_list.append(s)
        return web.json_response({
            'online': online_list,
            'offline': offline_list,
        })
    except Exception as err:
        return web.json_response({'error': str(err)}, status=500)


async def get_player_detail(request):
    """GET /api/players/{uuid} — full player detail"""
    services = request.app['services']
    channel = services.channel
    uuid_str = request.match_info['uuid']
    try:
        player = await _find_player(channel, uuid_str)
        if not player:
            return web.json_response({'error': 'Player not found'}, status=404)
        result = serialize(player)
        # Add extra detail fields
        try:
            result['health'] = float(await player.getHealth())
        except Exception:
            pass
        try:
            result['food_level'] = int(await player.getFoodLevel())
        except Exception:
            pass
        try:
            gm = await player.getGameMode()
            if gm:
                # Extract the key attribute (e.g. "SURVIVAL")
                result['game_mode'] = getattr(gm, 'key', str(gm))
        except Exception:
            pass
        try:
            result['level'] = int(await player.getLevel())
        except Exception:
            pass
        return web.json_response(result)
    except Exception as err:
        return web.json_response({'error': str(err)}, status=500)


async def get_player_inventory(request):
    """GET /api/players/{uuid}/inventory — player inventory contents"""
    services = request.app['services']
    channel = services.channel
    uuid_str = request.match_info['uuid']
    try:
        player = await _find_player(channel, uuid_str)
        if not player:
            return web.json_response({'error': 'Player not found'}, status=404)
        inventory = await player.getInventory()
        result = serialize(inventory)
        return web.json_response(result)
    except Exception as err:
        return web.json_response({'error': str(err)}, status=500)


async def _safe_teleport_y(world_name, x, y, z, max_scan=200):
    """Scan upward from y to find the first position with two passable blocks (safe to stand)."""
    world_obj = final.World(name=world_name)
    x_int = int(x)
    z_int = int(z)
    y_int = int(y)
    for dy in range(max_scan):
        check_y = y_int + dy
        b_feet = await world_obj.getBlockAt(x_int, check_y, z_int)
        b_head = await world_obj.getBlockAt(x_int, check_y + 1, z_int)
        if await b_feet.isPassable() and await b_head.isPassable():
            return check_y
    return y_int  # fallback: couldn't find safe position


async def teleport_player(request):
    """POST /api/players/{uuid}/teleport — teleport player to location"""
    services = request.app['services']
    channel = services.channel
    uuid_str = request.match_info['uuid']
    try:
        data = await request.json()
    except Exception:
        return web.json_response({'error': 'Invalid JSON body'}, status=400)
    for field in ('world', 'x', 'y', 'z'):
        if field not in data:
            return web.json_response({'error': f'Missing field: {field}'}, status=400)
    try:
        player = await _find_player(channel, uuid_str)
        if not player:
            return web.json_response({'error': 'Player not found'}, status=404)
        world_name = data['world']
        x = float(data['x'])
        y = float(data['y'])
        z = float(data['z'])
        if data.get('safe', True):
            y = await _safe_teleport_y(world_name, x, y, z)
        loc = Location([world_name, x, y, z])
        await player.teleport(loc)
        return web.json_response({'status': 'ok'})
    except Exception as err:
        return web.json_response({'error': str(err)}, status=500)


async def give_item(request):
    """POST /api/players/{uuid}/inventory/give — give item to player"""
    services = request.app['services']
    channel = services.channel
    uuid_str = request.match_info['uuid']
    try:
        data = await request.json()
    except Exception:
        return web.json_response({'error': 'Invalid JSON body'}, status=400)
    if 'material' not in data:
        return web.json_response({'error': 'Missing field: material'}, status=400)
    try:
        player = await _find_player(channel, uuid_str)
        if not player:
            return web.json_response({'error': 'Player not found'}, status=404)
        inventory = await player.getInventory()
        material = data['material']
        count = int(data.get('count', 1))
        # Find first empty slot and set the item
        first_empty = inventory.firstEmpty
        if first_empty < 0:
            return web.json_response({'error': 'Inventory is full'}, status=400)
        await inventory.setItem(first_empty, [material, count])
        stack = inventory.get_stack(first_empty)
        result = {'status': 'ok', 'slot': first_empty}

        # Apply potion metadata if this is a potion-type item
        potion_type = data.get('potion_type')
        potion_effects = data.get('potion_effects')  # [{type, duration_seconds, amplifier}]
        potion_name = data.get('potion_name')
        if potion_type or potion_effects or potion_name:
            applied_effects = await _apply_potion_meta(
                stack, potion_type, potion_effects, potion_name
            )
            result['potion_effects_applied'] = applied_effects

        # Apply enchantments
        enchant = data.get('enchant', False)
        if enchant:
            ench_list = data.get('enchantments')  # optional [{key, level}]
            applied = await _enchant_stack(stack, ench_list)
            result['enchantments_applied'] = applied

        return web.json_response(result)
    except Exception as err:
        log.exception("Failed to give item to %s", uuid_str)
        return web.json_response({'error': str(err)}, status=500)


async def _enchant_stack(stack, enchantments=None):
    """Apply enchantments to an item stack. Returns list of applied enchantment keys.

    enchantments can be:
    - None: apply DESIRABLE_ENCHANTMENTS at max level
    - list of strings: apply those keys at max level
    - list of {key, level} dicts: apply at specified levels
    """
    if enchantments is None:
        enchantments = DESIRABLE_ENCHANTMENTS
    applied = []
    for item in enchantments:
        if isinstance(item, str):
            key, level = item, None
        else:
            key, level = item['key'], item.get('level')
        try:
            ench = final.Enchantment(key)
            if await ench.canEnchantItem(stack):
                if level is None:
                    level = await ench.getMaxLevel()
                await stack.addEnchantment(ench, int(level))
                applied.append(key)
        except Exception:
            log.debug("Failed to apply enchantment %s", key, exc_info=True)
    return applied


async def _apply_potion_meta(stack, potion_type=None, effects=None, name=None):
    """Apply potion metadata to an item stack.

    potion_type: base PotionType key (e.g. 'NIGHT_VISION')
    effects: list of {type, duration_seconds, amplifier} dicts for custom effects
    name: optional display name for the potion
    Returns list of applied effect type names.
    """
    metadata = await stack.getItemMeta()
    if not metadata:
        return []
    if potion_type:
        # The Java side expects just the bare enum name (e.g. 'NIGHT_VISION'),
        # not the namespaced key (e.g. 'minecraft:NIGHT_VISION')
        name = potion_type.split(':')[-1] if ':' in potion_type else potion_type
        await metadata.setBasePotionType(name.upper())
    applied = []
    for effect in (effects or []):
        try:
            # Bukkit 1.21 PotionEffectType uses namespaced keys (e.g. minecraft:instant_health)
            etype = effect['type'].lower()
            if ':' not in etype:
                etype = f'minecraft:{etype}'
            duration_ticks = int(float(effect.get('duration_seconds', 60)) * 20)
            amplifier = int(effect.get('amplifier', 0))
            await metadata.addCustomEffect(
                {'type': etype, 'duration': duration_ticks, 'amplifier': amplifier},
                True,
            )
            applied.append(etype)
        except Exception:
            log.debug("Failed to apply potion effect %s", effect, exc_info=True)
    if name:
        await metadata.setDisplayName(name)
    await stack.setItemMeta(metadata)
    return applied


async def enchant_item(request):
    """POST /api/players/{uuid}/inventory/enchant — enchant item in slot"""
    services = request.app['services']
    channel = services.channel
    uuid_str = request.match_info['uuid']
    try:
        data = await request.json()
    except Exception:
        return web.json_response({'error': 'Invalid JSON body'}, status=400)
    if 'slot' not in data:
        return web.json_response({'error': 'Missing field: slot'}, status=400)
    try:
        player = await _find_player(channel, uuid_str)
        if not player:
            return web.json_response({'error': 'Player not found'}, status=404)
        inventory = await player.getInventory()
        slot = int(data['slot'])
        stack = inventory.get_stack(slot)
        if stack is None:
            return web.json_response({'error': f'Slot {slot} is empty'}, status=400)
        result = {'status': 'ok'}
        enchantments = data.get('enchantments')  # optional list of specific enchantment keys
        applied = await _enchant_stack(stack, enchantments)
        result['applied'] = applied
        # Apply potion metadata if provided
        potion_type = data.get('potion_type')
        potion_effects = data.get('potion_effects')
        potion_name = data.get('potion_name')
        if potion_type or potion_effects or potion_name:
            applied_effects = await _apply_potion_meta(
                stack, potion_type, potion_effects, potion_name
            )
            result['potion_effects_applied'] = applied_effects
        return web.json_response(result)
    except Exception as err:
        return web.json_response({'error': str(err)}, status=500)


async def drop_item(request):
    """POST /api/players/{uuid}/inventory/drop — delete item from slot"""
    services = request.app['services']
    channel = services.channel
    uuid_str = request.match_info['uuid']
    try:
        data = await request.json()
    except Exception:
        return web.json_response({'error': 'Invalid JSON body'}, status=400)
    if 'slot' not in data:
        return web.json_response({'error': 'Missing field: slot'}, status=400)
    try:
        player = await _find_player(channel, uuid_str)
        if not player:
            return web.json_response({'error': 'Player not found'}, status=404)
        inventory = await player.getInventory()
        slot = int(data['slot'])
        await inventory.clear(slot)
        return web.json_response({'status': 'ok', 'slot': slot})
    except Exception as err:
        return web.json_response({'error': str(err)}, status=500)


async def applicable_enchantments(request):
    """GET /api/players/{uuid}/inventory/{slot}/applicable-enchantments

    Returns enchantments that can be applied to the item in the given slot.
    Same shape as list_enchantments but filtered by canEnchantItem.
    """
    services = request.app['services']
    channel = services.channel
    uuid_str = request.match_info['uuid']
    slot = int(request.match_info['slot'])
    try:
        player = await _find_player(channel, uuid_str)
        if not player:
            return web.json_response({'error': 'Player not found'}, status=404)
        inventory = await player.getInventory()
        stack = inventory.get_stack(slot)
        if stack is None:
            return web.json_response({'error': f'Slot {slot} is empty'}, status=400)
        all_enchants = await final.Enchantment.cached_values()
        result = []
        for ench in all_enchants:
            key = ench.get_key()
            try:
                if await ench.canEnchantItem(stack):
                    try:
                        max_level = int(await ench.getMaxLevel())
                    except Exception:
                        max_level = 1
                    result.append({
                        'key': key,
                        'max_level': max_level,
                        'desirable': key in DESIRABLE_SET,
                    })
            except Exception:
                log.debug("Failed to check canEnchantItem for %s", key, exc_info=True)
        result.sort(key=lambda x: (not x['desirable'], x['key']))
        return web.json_response({'enchantments': result})
    except Exception as err:
        return web.json_response({'error': str(err)}, status=500)


async def list_enchantments(request):
    """GET /api/enchantments — list all enchantments with max levels and desirable flag."""
    global _enchantment_cache
    if _enchantment_cache is not None:
        return web.json_response({'enchantments': _enchantment_cache})
    try:
        all_enchants = await final.Enchantment.cached_values()
        result = []
        for ench in all_enchants:
            key = ench.get_key()
            try:
                max_level = int(await ench.getMaxLevel())
            except Exception:
                max_level = 1
            result.append({
                'key': key,
                'max_level': max_level,
                'desirable': key in DESIRABLE_SET,
            })
        result.sort(key=lambda x: (not x['desirable'], x['key']))
        _enchantment_cache = result
        return web.json_response({'enchantments': result})
    except Exception as err:
        return web.json_response({'error': str(err)}, status=500)


async def list_potion_types(request):
    """GET /api/potion-types — list potion types and effect types."""
    global _potion_type_cache
    if _potion_type_cache is not None:
        return web.json_response(_potion_type_cache)
    try:
        potion_types = await final.PotionType.cached_values()
        type_keys = sorted(t.get_key() for t in potion_types)
        _potion_type_cache = {
            'potion_types': type_keys,
            'effect_types': POTION_EFFECT_TYPES,
            'potion_materials': sorted(POTION_MATERIALS),
        }
        return web.json_response(_potion_type_cache)
    except Exception as err:
        return web.json_response({'error': str(err)}, status=500)
