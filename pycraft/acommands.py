"""Common commands exposed over chat server"""
from .expose import expose, command_details, command_list
from .directions import roughly_forward
from .server import proxyobjects
import typing
from .server import world
from .server import final
from .chatmessage import ChatMessage
from . import parsematerial
from . import rotations
from .server.world import (
    Vector,
    Location,
    Block,
)
import time, re, os, json
import numpy as np
import asyncio
import logging
import random

from pycraft import directions

log = logging.getLogger(__name__)

Vec3 = Vector


@expose()
def echo(message, *, player=None):
    """Return the message to the player"""
    return message


@expose()
async def print(*args, sep=' ', end=''):
    """Format the arguments as a raw message

    Print outputs a ChatMessage that doesn't get turned into a
    code-like representation, it just gets output as provided.

    Print takes any number of arguments and converts them
    to strings, joins them with :py:param:`sep` and adds
    :py:param:`end` to the result.

    Example usage::

        <VRPlumberMagic> print(2+3)
        5
        <VRPlumberMagic> print("hello" * 3)
        hellohellohello
        <VRPlumberMagic> print(1,2,3)
        1 2 3
        <VRPlumberMagic> print((1,2,3))
        (1, 2, 3)
        <VRPlumberMagic> print(player.location)
        ['world',2673.9915696040616,119.0,-1091.0867856973955,-120.993355,-0.15053184]
        <VRPlumberMagic> print(player.name)
        VRPlumberMagic
    """
    formatted = []
    for item in args:
        if isinstance(item, typing.Coroutine):
            item = await item
        formatted.append(str(item))
    return ChatMessage(sep.join(formatted) + end)


@expose()
async def list_players(*, server):
    """Print out a friendly list of player name, uuid and status"""
    for player in await server.getOfflinePlayers():
        if isinstance(player, final.Player):
            return await print(
                f'{repr(player.name)} {player.uuid} {"banned" if player.banned else ""} {"whitelisted" if player.whitelisted else ""} currently at {player.location}'
            )
        else:
            return await print(
                f'{repr(player.name)} {player.uuid} {"banned" if player.banned else ""} {"whitelisted" if player.whitelisted else ""}'
            )


@expose(name='dir')
def dir_(*args, namespace=None) -> typing.List[str]:
    """Give a directory of the namespace or of an object

    dir() -- show all names in the namespace
    dir('test') -- show all names in the namespace with 'test' in them
    dir(object) -- show all names in the given object

    returns
    """
    if args:
        if args and isinstance(args[0], str):
            test = args[0].lower()
            return [item for item in sorted(namespace.keys()) if test in item.lower()]
        return dir(args[0])
    else:
        return sorted(namespace.keys())


@expose()
async def spawn(
    type_name, position=None, *, player: world.Player = None, world: world.World = None
):
    """Spawn a new entity of type_id at position (default in front of player)

    type_name -- full minecraft ID for the entity to spawn

    returns :py:class:`pycraft.server.final.Entity` subclass
    """
    if position is None:
        position = player.position + player.direction
    if not ':' in type_name:
        type_name = 'minecraft:%s' % (type_name,)
    return await world.spawnEntity(position, type_name)


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
async def block(type_name, position=None, offset=(0, 0, 0), *, player=None, world=None):
    """Create a block with the given type_id at position

    returns position of the block
    """
    if position is None:
        position = player.location + player.forward
    if offset:
        position = position + offset
    if not ':' in type_name:
        type_name = 'minecraft:%s' % (type_name,)
    await final.World(position.world).setBlockList([position], [type_name])
    return position


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
    """Find block-types with names similar to the given name

    find_blocks('granite') => ['GRANITE','POLISHED_GRANITE']
    """
    return [x.key for x in await final.Material.loosely_match(name)]


@expose()
async def find_entities(name):
    """Find entity-types with names similar to name

    find_entities( 'creep' ) => ['CREEPER']
    """
    return [e.key for e in await final.EntityType.loosely_match(name)]


def matching_players(players: typing.List[world.Player], player_name: str):
    """Filters the list of players to those matching player_name"""
    player_name = player_name.lower()
    for other in players:
        if player_name == '*':
            yield other
        elif player_name in other.name.lower():
            yield other


@expose()
async def find_player(player_name='*', *, server=None):
    """Find the first player whose name matches the given name (if *, finds first player)

    returns :py:class:`pycraft.server.final.Player` or raises KeyError if no Player is found
    """
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
async def players(player_name='*', *, world=None):
    """Get the list of players whose name matches player_name (all if *)

    returns list of :py:class:`pycraft.server.final.Player` instances
    """
    players = await server.getOnlinePlayers()
    result = list(await matching_players(players, player_name))
    return result


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
async def give(item, count=1, *, player=None):
    """Add a (stack of) item(s) to the player's inventory

    item -- item-type-name, such as "cooked_beef" or "netherite_sword"
    count -- number of items to have in the stack

    returns :py:class:`pycraft.server.final.ItemStack` instance
    """
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
    """Add a nice item to the given inventory

    give() the item, then call enchanted() on it

    returns :py:class:`pycraft.server.final.ItemStack`
    """
    stack = await give(item, count=count, player=player)
    return await enchanted(stack)


@expose()
async def nice_gear(material='netherite', *, player=None):
    """Given the calling player a collection of very nice items for adventuring

    Included:
    * helmet
    * chestplate
    * leggings
    * boots
    * shield
    * sword
    * pickaxe
    * shovel
    * bow
    * 64 arrows

    material -- determines the material for the gear, supported are iron, netherite and diamond,
                as those are the only materials with versions of all supported items
    """
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
    """Enchant the item stack with all available desirable enchantments"""
    for enchantment in enchantments:
        ench = final.Enchantment(enchantment)
        if await ench.canEnchantItem(stack):
            await stack.addEnchantment(
                ench,
                await ench.getMaxLevel(),
            )
    return stack


@expose()
async def bed(position=None, direction=None, color='cyan', *, player=None, world=None):
    """Create a bed in front of the player"""
    if direction is None:
        direction = player.direction
    if position is None:
        position = player.position

    forward = roughly_forward(direction)
    facing = rotations.direction_name(forward)

    await final.Block(location=position + forward + forward).setBlockData(
        f'minecraft:{color}_bed[facing={facing},occupied=false,part=head]'
    )
    await final.Block(location=position + forward).setBlockData(
        f'minecraft:{color}_bed[facing={facing},occupied=false,part=foot]'
    )


@expose()
async def killall(name, *, player=None, world=None):
    """Kill all entities with exactly "name" as their name"""
    count = 0
    for entity in await findall(name, world=world):
        try:
            await entity.remove()
            count += 1
        except Exception as err:
            pass
    return count


@expose()
async def findall(name, *, world=None):
    """Search for all entities with precisely name

    returns a list of :py:class:`pycraft.server.final.Entity`
    subclasses
    """
    result = []
    for entity in await world.getEntities():
        if entity.name == name:
            result.append(entity)
    return result


@expose()
async def help(command=None, *args, player=None):
    """Help, a command list if no command specified, otherwise per-command details

    help() => Show list of available commands
    help(command) => show detailed usage for the given command
    help('entity-list') => Show list of available entitity names
    help('entity-list', 'name') => Show list of available entitity names matching name
    help('block-list') => Show list of available block names (including *item* names)
    help('block-list', 'name') => Show list of available block names matching name
    """
    if not command:
        output = command_list()
    elif command == 'entity-list':
        names = []
        for entityType in await final.EntityType.cached_values():
            names.append(entityType.key)
        return ", ".join(sorted(names))
    elif command == 'block-list':
        names = []
        for entityType in await final.Material.cached_values():
            names.append(entityType.key)
        if args:
            names = [n for n in names if args[0] in n]
        return ", ".join(sorted(names))
    else:
        output = command_details(command)
    return ChatMessage("\n".join(output))


@expose()
async def stairs(
    depth: int = 10,
    ystep: int = 1,
    clearance: int = 3,
    position: typing.Optional['pycraft.server.final.Location'] = None,
    direction: typing.Optional['pycraft.server.final.Vector'] = None,
    material='minecraft:obsidian',
    *,
    player=None,
    world=None,
):
    """Create a staircase forward from player's position for depth steps

    The first step is created such that the player will walk forward
    one block to be standing on top of the step. The blocks `clearance`
    above the stairs are set to air so that a stairway from deep
    underground will allow you to walk to the surface.

    depth -- number of steps to create

    ystep -- amount each step is offset in the y direction

    clearance -- how far above the step to clear to air, 0 to disable

    position -- if provided, used instead of the player's position

    direction -- if provided, used instead of the player's direction,
                 is converted to a cardinal direction using :py:func:`roughly_forward`

    material -- minecraft constant describing the material to use for the base
    """

    if direction is None:
        direction = player.direction
    direction = roughly_forward(direction)

    if not direction:
        raise RuntimeError("Unable to find direction")

    step = Vector(direction.x, ystep, direction.z)
    if position is None:
        position = player.tile_position + direction

    air = 'minecraft:air'
    current = position
    locations, materials = [], []
    for i in range(depth):
        locations.append(current)
        materials.append(material)
        for clear in range(1, clearance + 1):
            locations.append(current + (0, clear, 0))
            materials.append(air)
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
    """Retrieve the materials in a rectangular block in front of you

    returns list of slices of list of lines of materials

        [ # y varies
            [ # z varies
                [ material, material, material] # x varies
            ]

        ]
    """
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


UNJOIN_KEY = 'join.jump_back'


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
        # world.setGameRuleValue('pvp','true')
        return keep
    else:
        return 'Unknown rule for this world'


@expose()
async def mikes_potion(name, *, world=None, player=None):
    """Creates one of a selection of over-powered potions

    * carrots -- night_vision, healing
    * heath -- health, health_boost, regeneration, saturation
    * gopher -- digging, luck, night_vision
    """
    name = name.lower()
    if name == 'carrots':
        return await potion_of(
            'night_vision',
            "Carrot Juice",
            {
                'type': 'heal',
                'duration': 20 * 60 * 8,  # in ticks, so 20 seconds...
                'amplifier': 50,  # likely excessive
            },
            {
                'type': 'saturation',
                'duration': 20 * 60 * 8,  # in ticks, so 20 seconds...
                'amplifier': 1,
            },
            player=player,
            world=world,
        )
    elif name == 'health':
        return await potion_of(
            'instant_heal',
            "Tonic Water",
            {
                'type': 'heal',
                'duration': 20 * 60 * 8,  # in ticks, so 20 seconds...
                'amplifier': 50,  # likely excessive
            },
            {
                'type': 'saturation',
                'duration': 20 * 60 * 8,  # in ticks, so 20 seconds...
                'amplifier': 1,
            },
            {
                'type': 'health_boost',
                'duration': 20 * 60 * 8,  # in ticks, so 20 seconds...
                'amplifier': 40,
            },
            player=player,
            world=world,
        )
    elif name == 'gopher':
        return await potion_of(
            'night_vision',
            "Gopher's Gruel",
            {
                'type': 'fast_digging',
                'duration': 20 * 60 * 8,  # in ticks, so 20 seconds...
                'amplifier': 50,  # likely excessive
            },
            {
                'type': 'luck',
                'duration': 20 * 60 * 8,  # in ticks, so 20 seconds...
                'amplifier': 1,
            },
            player=player,
            world=world,
        )

    return 'Unknown potion %r' % (name,)


@expose()
async def potion_of(
    type='water_breathing',
    name='My Potion',
    *extra,
    player=None,
    world=None,
    server=None,
):
    """Give a potion of base with extras as specified

    Examples::

        # potion that gives you night vision and also heal's you, as carrots do
        potion_of('night_vision','Carrot Juice',{'type':'heal'})

    returns :py:class:`pycraft.server.final.ItemStack`
    """
    stack = await give('potion', player=player)
    metadata = await stack.getItemMeta()
    if not metadata:
        raise ValueError("No metadata on the stack %s", stack)
    print("metadata instance: %s" % (metadata,))
    base = await metadata.getBasePotionData()
    base.type = type
    base.upgraded = True
    base.extended = True
    for effect in extra:
        await metadata.addCustomEffect(
            effect, True
        )  # overwrite existing of this type...
    await metadata.setBasePotionData(base)
    base = await metadata.getBasePotionData()
    await metadata.setDisplayName(name)
    await stack.setItemMeta(metadata)

    return stack


@expose()
async def fill_inventory(entity, item='wheat_seeds', count=64):
    """Fill the inventory of the entity with the given item

    Fills all of the slots of the entity with the given item

    returns the entity
    """
    inventory = await entity.getInventory()
    await inventory.clear()
    for i in range(inventory.size):
        if inventory.contents[i]:
            await inventory.setItem(i, [item, count])
    return entity


@expose()
async def this_guy(*, player=None, listener=None, server=None):
    """Listen for an entity with which the player interacts"""
    try:
        async for event in listener.wait_for_events(
            'PlayerInteractEntityEvent',
            count=1,
            timeout=30,
            player=player.uuid,
        ):
            return event.entity
    except asyncio.TimeoutError as err:
        return "Did not click on an entity in time"
    return None


@expose()
async def full_farmer(*, player=None, listener=None, server=None, world=None):
    """Spawn a master farmer whose inventory is full of seeds

    returns :py:class:`pycraft.server.final.Villager`
    """
    name = random.choice(
        [
            'Drop Master Fred',
            'Farmer Don',
            "I'm Full of Seeds",
            "Seedy McFarmer",
            "Planter Fred",
            "Don of the Land",
            "Maester Wheat",
            "Bread Bringer",
            "Sooth Seeder",
            "Thresher Sam",
            "Sammy Planter",
            "Seed Maester Sue",
            "Flour Flowerer",
        ]
    )
    villager = await spawn('villager', player=player, world=world)
    await villager.setCustomName(name)
    await villager.setProfession('FARMER')
    await villager.setVillagerLevel(5)
    await fill_inventory(villager, count=1)
    return villager


@expose()
async def hopper_cascade(
    left=5,
    right=5,
    depth=5,
    position=None,
    direction=None,
    *,
    player=None,
    listener=None,
    server=None,
    world=None,
):
    """Create a cascade of hoppers that feed into the space ahead of you"""
    if direction is None:
        direction = player.direction
    if position is None:
        position = player.position + player.direction
    forward, cross = directions.forward_and_cross(direction)
    forward, cross = directions.forward_and_cross(direction)
    locations, blocks = [position + (0, -1, 0)], [
        'chest[facing=%s]' % (parsematerial.NESW_NAMES[tuple([-x for x in forward])])
    ]
    start = position - (cross * left)
    stop = position + (cross * right) + (forward * depth)
    material = {
        'namespace': 'minecraft',
        'name': 'hopper',
        'properties': {
            'facing': 'east',
        },
    }
    right_material = parsematerial.unparse_material(
        parsematerial.copy_struct(
            material, facing=parsematerial.NESW_NAMES[tuple(cross)]
        )
    )
    left_material = parsematerial.unparse_material(
        parsematerial.copy_struct(
            material, facing=parsematerial.NESW_NAMES[tuple([-x for x in cross])]
        )
    )
    back_material = parsematerial.unparse_material(
        parsematerial.copy_struct(
            material, facing=parsematerial.NESW_NAMES[tuple([-x for x in forward])]
        )
    )
    down_material = parsematerial.unparse_material(
        parsematerial.copy_struct(material, facing='down')
    )
    for row in range(depth):
        for column in range(left + right + 1):
            pos = start + (cross * column) + (forward * row)
            locations.append(pos)
            if row > 0:
                blocks.append(back_material)
            elif column < left:
                blocks.append(right_material)
            elif column == left:
                blocks.append(down_material)
            else:
                blocks.append(left_material)
    await world.setBlockList(locations, blocks)


@expose()
async def set_sign_text(block, text, glowing=True, color=None):
    """Set the text on the passed sign block

    block -- the location of a block or a Block instance from another call
    text -- a string, or list of strings, to set on the sign
    glowing -- whether to make the text glow
    color -- a DyeColor constant such as 'BLUE','PINK','RED', etc

    returns the sign's block on success
    """
    sign_block: final.Block = None
    if isinstance(block, (tuple, Location, list)):
        location = final.Location(block)
        sign_block = await location.getBlock()
    elif isinstance(block, (Block,)):
        sign_block = block
    else:
        raise TypeError('Need a location or a Block reference, not %r' % (block,))

    sign_state: final.Sign = await sign_block.getState()
    if isinstance(sign_state, final.Sign):
        if isinstance(text, str):
            text = [text]
        for index, line in enumerate(text):
            await sign_state.setLine(index, line)
        await sign_state.setGlowingText(True)
        if color:
            await sign_state.setColor(color)
        await sign_state.update()
        return sign_block
    else:
        raise RuntimeError("Not a sign: %s" % (sign_state))
