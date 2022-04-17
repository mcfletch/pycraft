"""Common commands exposed over chat server"""
from .expose import expose, command_details, command_list
from .directions import roughly_forward
from .server import proxyobjects
from typing import List
from .server import world
from .server import final
from .server.world import (
    Vector,
)
import time, re, os, json
import numpy as np
import asyncio
import logging

from pycraft import directions

log = logging.getLogger(__name__)

Vec3 = Vector


@expose()
def echo(message, *, player=None):
    """Return the message to the player"""
    return message


@expose()
def help(value):
    """Try to get help about the object"""
    import inspect

    doc = inspect.getdoc(value)
    if callable(value):
        params = inspect.signature(value)
        if doc:
            return '%s%s\n%s' % (value.__name__, params, doc)
        else:
            return '%s%s' % (value.__name__, params)
    elif doc:
        return doc
    else:
        return '%s instance with members %s' % (
            value.__class__,
            dir(value),
        )


@expose(name='dir')
def dir_(*args, namespace=None):
    """Look at the argument and describe what members it has"""
    if args:
        return dir(args[0])
    else:
        return sorted(namespace.keys())


@expose()
async def spawn(
    type_name, position=None, *, player: world.Player = None, world: world.World = None
):
    """Spawn a new entity of type_id at position (default in front of player)

    type_name -- full minecraft ID for the entity to spawn
    """
    if position is None:
        position = player.position + player.direction
    if not ':' in type_name:
        type_name = 'minecraft:%s' % (type_name,)
    await world.spawnEntity(position, type_name)


@expose()
async def spawn_drop(type_id, height=50, *, player=None, world=None):
    """Spawn an entity 50m overhead dropping onto your location

    Use this to e.g. drop a creeper to their death and generate gunpowder
    """
    position = player.position + Vector(0, height, 0)
    return await spawn(type_id, position=position, player=player, world=world)


@expose()
async def spawn_shower(type_id, count=30, height=50, *, player=None, world=None):
    """Spawn an entity 50m overhead dropping onto your location

    Use this to e.g. drop a creeper to their death and generate gunpowder
    """

    async def do_shower():
        position = player.position + player.direction + Vector(0, height, 0)
        for i in range(count):
            await spawn(type_id, position=position, player=player, world=world)
            await asyncio.sleep(0.1)
        return count

    asyncio.ensure_future(do_shower())


@expose()
async def block(type_name, position=None, offset=(0, 0, 0), *, player=None):
    """Create a block with the given type_id at position"""
    if position is None:
        position = player.location + player.location.direction
    if offset:
        position = position + offset
    if not ':' in type_name:
        type_name = 'minecraft:%s' % (type_name,)
    block = await position.getBlock()
    return await block.setBlockData(type_name)


# @expose()
# def click_create(type_id, *, clicks=None, player=None):
#     """When you right-click with a sword, create block-type there"""
#     typ = blocks.Block.as_instance(type_id)

#     def on_click(event):
#         target = V(event.pos) + V(event.direction)
#         mc.setBlock(*target, typ)

#     return clicks.register_user(player, on_click)


# @expose()
# def click_delete(*, clicks=None, player=None):
#     typ = blocks.Block.as_instance('AIR')

#     def on_click(event):
#         target = V(event.pos)
#         mc.setBlock(*target, typ)

#     return clicks.register_user(player, on_click)


# # @expose()
# # def click_describe(*,clicks=None,player=None):
# #     def on_click(event):
# #         try:
# #             target = event.pos
# #             description = 'Unavailable'
# #             for i in range(2):
# #                 try:
# #                     description = mc.getBlockWithData(event.pos)
# #                 except Exception as err:
# #                     pass
# #             print('Block at %s => %s'%(
# #                 event.pos,
# #                 description,
# #             ))
# #         except Exception as err:
# #             print("Failed: %s", err)
# #     return clicks.register_user(player,on_click)


# @expose()
# def click_cancel(*, clicks=None, player=None):
#     """Cancel click operations"""
#     clicks.register_user(player, None)


@expose()
async def find_blocks(name):
    """Find blocks with names similar to the given name

    find_blocks('granite') => ['GRANITE','POLISHED_GRANITE']
    """
    return [x.key for x in await final.Material.loosely_match(name)]


@expose()
async def find_entities(name):
    """Find entities with names similar to name

    find_entities( 'creep' ) => ['CREEPER']
    """
    return [e.key for e in await final.EntityType.loosely_match(name)]


@expose()
def users(*, world=None):
    return world.getPlayers()


# @expose()
# def last_hit(index=-1, *, player=None, clicks=None):
#     """Return the index-th last click by the sending player

#     If we don't have that click, will return None
#     """
#     try:
#         click = clicks.user_clicks(player)[index]
#         return click
#     except IndexError:
#         return None


@expose()
async def getblocks(depth=5, width=5, height=5, *, player=None, world=None):

    return await world.getBlocks(
        list(player.location[:3]), list((player.location + (depth, height, width))[:3])
    )


@expose()
async def give(item, count=1, *, player=None):
    inventory = await player.getInventory()
    empty = inventory.empty_slots()
    if not empty:
        raise RuntimeError("Inventory is full")
    else:
        index = empty[0]
    await inventory.setItem(index, [item, count])
    stack = inventory.get_stack(index)
    inventory.contents[index] = stack
    return stack


@expose()
async def nice_item(item, count=1, *, player=None):
    """Add a nice item to the given inventory, assumes content is up to date"""
    stack = await give(item, count=count, player=player)
    await enchanted(stack)


@expose()
async def nice_gear(material='netherite', *, player=None):
    for item in [
        'minecraft:%(material)s_helmet',
        'minecraft:%(material)s_chestplate',
        'minecraft:%(material)s_leggings',
        'minecraft:%(material)s_boots',
        'minecraft:shield',
        'minecraft:%(material)s_sword',
        'minecraft:%(material)s_pickaxe',
        'minecraft:%(material)s_shovel',
        'minecraft:bow',
    ]:
        await nice_item(item % locals(), player=player)
    await give('arrow', 64, player=player)


DESIRABLE_ENCHANTMENTS = [
    x.strip()
    for x in """minecraft:fire_protection
        minecraft:sharpness
        minecraft:flame
        minecraft:soul_speed
        minecraft:aqua_affinity
        minecraft:punch
        minecraft:loyalty
        minecraft:depth_strider
        minecraft:unbreaking
        minecraft:knockback
        minecraft:luck_of_the_sea
        minecraft:fortune
        minecraft:protection
        minecraft:efficiency
        minecraft:mending
        minecraft:frost_walker
        minecraft:lure
        minecraft:looting
        minecraft:piercing
        minecraft:blast_protection
        minecraft:smite
        minecraft:multishot
        minecraft:fire_aspect
        minecraft:channeling
        minecraft:sweeping
        minecraft:thorns
        minecraft:bane_of_arthropods
        minecraft:respiration
        minecraft:quick_charge
        minecraft:projectile_protection
        minecraft:impaling
        minecraft:feather_falling
        minecraft:power
        minecraft:infinity""".splitlines()
]


@expose()
async def enchanted(stack, enchantments=DESIRABLE_ENCHANTMENTS):
    """Enchant the item stack with all available enchantments"""
    for enchantment in enchantments:
        ench = final.Enchantment(enchantment)
        if await ench.canEnchantItem(stack):
            await stack.addEnchantment(
                ench,
                await ench.getMaxLevel(),
            )


@expose()
async def bed(position=None, direction=None, color='cyan', *, player=None, world=None):
    """Create a bed in front of the player"""
    if direction is None:
        direction = player.direction
    if position is None:
        position = player.position + direction

    await final.Block(location=position + Vector(0, 0, 1)).setBlockData(
        f'minecraft:{color}_bed[facing=south,occupied=false,part=head]'
    )
    await final.Block(location=position).setBlockData(
        f'minecraft:{color}_bed[facing=south,occupied=false,part=foot]'
    )


@expose()
async def killall(name, *, player=None, world=None):
    """Kill all entities with exactly "name" as their name"""
    for entity in await world.getEntities():
        if entity.name == name:
            try:
                await final.Entity(uuid=entity.uuid).remove()
            except Exception as err:
                pass


@expose()
async def findall(name, *, world=None):
    result = []
    for entity in await world.getEntities():
        if entity.name == name:
            result.append(entity)
    return result


# @expose()
# async def help(command=None, *args, player=None):
#     """Help, a command list if no command specified, otherwise per-command details

#     help() => Show list of available commands
#     help('command') => show detailed usage for the given command
#     help('entity-list') => Show list of available entitity names
#     help('entity-list', 'name') => Show list of available entitity names matching name
#     help('block-list') => Show list of available block names
#     help('block-list', 'name') => Show list of available block names matching name
#     """
#     if not command:
#         output = command_list()
#     elif command == 'entity-list':
#         names = []
#         for entityType in await EntityType.cached_values():
#             names.append(entityType.key)
#         return ", ".join(sorted(names))
#     elif command == 'block-list':
#         names = []
#         for entityType in await EntityType.cached_values():
#             names.append(entityType.key)
#         if args:
#             names = [n for n in names if args[0] in n]
#         return ", ".join(sorted(names))
#     else:
#         output = command_details(command)
#     return "\n".join(output)


@expose()
async def stairs(
    depth=10,
    ystep=1,
    clearance=3,
    position=None,
    direction=None,
    material='minecraft:obsidian',
    *,
    player=None,
    world=None,
):
    """Create an ascending or descending staircase (based on ystep)"""

    if direction is None:
        direction = player.direction
    direction = roughly_forward(direction)

    if not direction:
        raise RuntimeError("Unable to find direction")

    step = Vector(direction.x, ystep, direction.z)
    if position is None:
        position = player.tile_position + (step if ystep < 0 else direction)

    current = position
    air = 'minecraft:air'
    working = position
    locations, materials = [], []
    for i in range(depth):
        locations.append(current)
        materials.append(material)
        for clear in range(1, clearance + 1):
            locations.append(current + (0, clear, 0))
            materials.append('air')
        current = current + step
    await world.setBlockList(locations, materials)


@expose()
async def get_blocks(
    depth=10,
    width=10,
    height=10,
    position=None,
    direction=None,
    *,
    world=None,
    player=None,
):
    if direction is None:
        direction = player.direction
    if position is None:
        position = player.position
    forward, cross = directions.forward_and_cross(direction)
    start = position + forward - (cross * (width // 2))
    end = (
        start
        + (forward * (depth - 1))
        + (cross * (width - 1))
        + (Vector(0, 1, 0) * (height - 1))
    )

    return await world.getBlockArray(start[:3], end[:3])


@expose()
async def get_click(*, listener=None, player=None):
    """Await the next (right) click by the player on a block"""
    event = await listener.wait_for_event(player=player.name)
    return str(event)


@expose()
async def midas_touch(
    material='minecraft:gold_block',
    count=25,
    *,
    listener=None,
    player=None,
    interpreter=None,
):
    async def run_midas():
        converted = set()
        if not interpreter:
            return
        async for event in listener.wait_for_events(
            event_type='PlayerInteractEvent',
            player=player,
            count=count,
        ):
            if event.action == 'RIGHT_CLICK_BLOCK':
                block: final.Block = event.block_clicked
                location: final.Location = block.location
                key = location.world, int(location.x), int(location.y), int(location.z)
                if key in converted:
                    continue
                converted.add(key)
                await final.Block(location=location).setType(material)
            elif event.action == 'LEFT_CLICK_BLOCK':
                break
        await interpreter.broadcast_chat('Finished midas_touch')

    asyncio.ensure_future(run_midas())
    return 'Right click blocks with your empty hand to convert them'


def matching_players(players: List[world.Player], player_name: str):
    player_name = player_name.lower()
    for other in players:
        if player_name == '*':
            yield other
        elif other.name.lower().startswith(player_name):
            yield other


UNJOIN_KEY = 'join.jump_back'


@expose()
async def find_player(player_name='*', *, server=None):
    players = await server.getOnlinePlayers()
    for other in matching_players(players, player_name):
        return other
    raise KeyError(
        'No player with name %s found, found: %s'
        % (
            player_name,
            sorted([p.name for p in players]),
        )
    )


@expose()
async def unjoin(*, player=None, interpreter=None):
    """Return the the last location before you were brought or joined another player"""
    join_stack = interpreter.user_namespace(player).setdefault(UNJOIN_KEY, [])
    if join_stack:
        location = join_stack.pop()
        await player.set_location(location)
        return location


@expose()
async def bring(player_name='*', *, player=None, server=None, interpreter=None):
    """Gather other users (or one other user by name) to your location"""
    players = await server.getOnlinePlayers()
    for other in matching_players(players, player_name):
        if other.name != player.name:
            join_stack = interpreter.user_namespace(other).setdefault(UNJOIN_KEY, [])
            join_stack.append(other.location)
            del join_stack[:-20]
            await other.set_location(player.location)


@expose()
async def join(player_name, *, player=None, server=None, interpreter=None):
    """Join (teleport to) another user by name, use unjoin() to return to your location"""
    players = await server.getOnlinePlayers()
    for other in matching_players(players, player_name):
        if other.name != player.name:
            join_stack = interpreter.user_namespace(player).setdefault(UNJOIN_KEY, [])
            join_stack.append(player.location)
            del join_stack[:-20]
            await player.set_location(other.location)
            break


@expose()
async def back_to_bed(*, player=None):
    """Send the player back to their bed spawn location (last place they slept)"""
    location = await player.getBedSpawnLocation()
    if location:
        await player.set_location(location)
    else:
        return 'No bed spawn location found (bed destroyed?)'


@expose()
async def keep_inventory(keep=True, *, player=None, world=None):
    """Enable keep inventory for this world (e.g. the overworld, the nether, the end)"""
    if await world.isGameRule('keepInventory'):
        await world.setGameRule('keepInventory', keep)
        return keep
    else:
        return 'Unknown rule for this world'


@expose()
async def potion_of(
    type='water_breathing',
    *extra,
    player=None,
    world=None,
    server=None,
    PotionMeta=None,
):
    """Give a potion of base with extras as specified"""
    stack = await give('potion', player=player)
    metadata = await stack.getMeta()
    if not metadata:
        raise ValueError("No metadata on the stack %s", stack)
    base = await metadata.getBasePotionData()
    base.type = type
    base.upgraded = True
    base.extended = True
    await metadata.setBasePotionData(base)
    base = await metadata.getBasePotionData()
    print(base)
