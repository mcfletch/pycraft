import logging, asyncio, pprint
from pycraft.server.proxyobjects import ProxyMethod, type_coerce
from .channel import Channel
from .world import (
    World,
    Player,
    Server,
    Entity,
    Material,
    BlockData,
    Location,
    Inventory,
    Block,
    ItemStack,
    Enchantment,
)


log = logging.getLogger(__name__)

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
        minecraft:silk_touch
        minecraft:quick_charge
        minecraft:projectile_protection
        minecraft:impaling
        minecraft:feather_falling
        minecraft:power
        minecraft:infinity""".splitlines()
]


async def enchanted(stack):
    """Enchant the item stack with all available enchantments"""
    for enchantment in DESIRABLE_ENCHANTMENTS:
        ench = Enchantment(enchantment)
        if await ench.canEnchantItem(stack):
            await stack.addEnchantment(
                ench,
                await ench.getMaxLevel(),
            )


async def nice_sword(inventoryHolder):
    """Give the player a nice sword for running about"""
    return await nice_item(inventoryHolder, 'minecraft:netherite_sword')


async def nice_pickaxe(inventoryHolder):
    return await nice_item(inventoryHolder, 'minecraft:netherite_pickaxe')


async def nice_item(inventory, item, index=None, count=1):
    """Add a nice item to the given inventory, assumes content is up to date"""
    if not isinstance(inventory, Inventory):
        inventory = await inventory.getInventory()
    assert isinstance(inventory, Inventory), inventory
    if index is None:
        empty = inventory.empty_slots()
        if not empty:
            raise RuntimeError("Inventory is full")
        else:
            index = empty[0]
    await inventory.setItem(index, [item, count])
    stack = inventory.get_stack(index)
    inventory.contents[index] = stack
    await enchanted(stack)


async def nice_armour(player):
    for item in [
        'minecraft:netherite_helmet',
        'minecraft:netherite_chestplate',
        'minecraft:netherite_leggings',
        'minecraft:netherite_boots',
    ]:
        await nice_item(player, item)
        inventory = await player.getInventory()


async def show_enum(cls):
    print("Instances of %s" % cls.__name__)
    for instance in await cls.values():
        print(instance.get_key())


async def copy_block(world, start, stop):
    blocks = world.getBlocks([0, 0, 0], [10, 10, 10])
    print(blocks)


async def block(player, blockdata):
    location = player.location + player.direction
    block = await location.getBlock()
    await block.setBlockData(blockdata)


async def fill_inventory(player, material, count):
    inventory = await player.getInventory()
    while inventory.firstEmpty > -1:
        await inventory.setItem(inventory.firstEmpty, [material, count])
        inventory = await player.getInventory()


async def test_api():

    server = Channel(debug=True)
    await server.open()
    await server.introspect()

    # worlds = await Server(name="server").getWorlds()

    # log.info("getWorlds => %s", worlds)

    from .. import acommands, bulldozer
    from . import proxyobjects

    for player in await World(name='world').getPlayers():
        if player.name == 'VRPlumber':
            # await acommands.give('iron_ingot', count=64, player=player)
            # await acommands.give('emerald', count=64, player=player)
            await bulldozer.bulldoze(depth=50, width=1, height=3, player=player)

    # loc = Location(['world', [0, 0, 0]])
    # await acommands.bed(position=loc, direction=(0, 0, 1))

    # # bed = proxyobjects.PROXY_TYPES['Bed'](location=loc)
    # bed = await Block(location=loc).getBlockData()
    # # from Bed
    # assert hasattr(bed, 'isOccupied'), bed
    # # from BlockData
    # assert hasattr(bed, 'getMaterial'), bed
    # print('Bed Material', await bed.getMaterial())
    # queue,queue_id = await server.subscribe("AsyncPlayerChatEvent")
    # while True:
    #     event = await queue.get()
    #     print('Event: %s', event)
    # await server.close()


def main():
    logging.basicConfig(level=logging.DEBUG)
    asyncio.get_event_loop().run_until_complete(test_api())


if __name__ == "__main__":
    main()
