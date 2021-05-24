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

    worlds = await Server(name="server").getWorlds()

    log.info("getWorlds => %s", worlds)
    for world in worlds:
        # if world.name == 'world':
        #     await armoury_chest(['world', -136, 63, 91])
        # blocks = await world.getBlocks([0, 0, 0], [5, 5, 5])
        # pprint.pprint(blocks)
        # if world.name == 'world':  # default world name...
        #     print("Materials")
        #     for material in await server.call_remote(
        #         "World.getMaterialTypes",
        #     ):
        #         print(material)
        #     print("Enchantments")
        #     for enchantment in await server.call_remote("Enchantment.values"):
        #         print(enchantment)
        for player in world.players:
            #     #     # print(await structured.getBlockAt([structured.name, 0, 0, 0]))
            #     #     # if player.name == 'VRPlumber':
            #     if player.name == 'BlockBrave':
            #         #         # await nice_item(player, 'minecraft:elytra')
            #         await nice_item(player, 'minecraft:trident')
            # await nice_sword(player)
            # await nice_armour(player)
            # await nice_pickaxe(player)
            # await nice_item(player, 'minecraft:bow')
            if player.name == 'BlockBrave':
                await nice_item(player, 'minecraft:diamond_horse_armor')
                pass
                # await nice_item(player, 'minecraft:wooden_hoe')
                # if player.name == 'VRPlumber':
                # if player.name in ('BlockPlumber', 'VRPlumber'):
                # await nice_item(player, 'minecraft:elytra')
                # inventory = await player.getInventory()
                # await inventory.setItem(inventory.firstEmpty, ['minecraft:salmon', 64])

                # await nice_item(player, 'minecraft:netherite_boots')
                # await nice_item(player, 'minecraft:bow')
                # await nice_armour(player)
                # await nice_sword(player)
                # await nice_pickaxe(player)
                # await nice_item(player, 'minecraft:shield')
                # inventory = await player.getInventory()
                # await inventory.setItem(inventory.firstEmpty, ['minecraft:arrow', 64])
                # inventory = await player.getInventory()
                # await inventory.setItem(
                #     inventory.firstEmpty, ['minecraft:flint_and_steel', 1]
                # )
                # inventory = await player.getInventory()
                # await nice_item(player, 'minecraft:golden_boots')
                # await inventory.setItem(inventory.firstEmpty, ['minecraft:shield', 1])
                # await inventory.setItem(
                #     inventory.firstEmpty, ['minecraft:obsidian', 64]
                # )
                # await nice_item(player, 'minecraft:netherite_shovel')
                # inventory = await player.getInventory()
                # await inventory.setItem(inventory.firstEmpty, ['minecraft:arrow', 64])
                # inventory = await player.getInventory()
                # await inventory.setItem(
                #     inventory.firstEmpty, ['minecraft:firework_rocket', 64]
                # )

                # for material in [
                #     # 'minecraft:obsidian',
                #     # 'minecraft:smooth_quartz_stairs',
                #     # 'minecraft:arrow',
                #     # 'minecraft:diamond',
                #     # 'minecraft:stick',
                #     # 'minecraft:soul_sand',
                #     'minecraft:water_bucket',
                # ]:
                #     inventory = await player.getInventory()
                #     await inventory.setItem(inventory.firstEmpty, [material, 1])
                # await fill_inventory(player, material = 'minecraft:water_bucket',count=1)

        # await block(player, 'netherite_block')
        # for item in [
        #     'minecraft:netherite_axe',
        #     'minecraft:netherite_sword',
        #     'minecraft:netherite_hoe',
        #     'minecraft:netherite_shovel',
        # ]:
        #     await nice_item(player, item)
        # await nice_item(player, 'minecraft:crossbow')

        # location = player.location.block_location() + (0, -1, 0)
        # await world.setBlock(
        #     list(location.vector[:3]), 'minecraft:netherite_block'
        # )

        # await world.spawnEntity(player.location, 'SHEEP')
        # await world.setStorm(True)
        # await world.setThundering(True)

        # await world.spawnEntity(player.location, 'minecraft:pufferfish')

        # await world.strikeLightning(player.location)
        # await world.strikeLightningEffect(player.location)
        # await player.sendMessage("Hello from the new api")

        # for player in world.players:
        #     #     # print(await structured.getBlockAt([structured.name, 0, 0, 0]))
        #     #     # if player.name == 'VRPlumber':
        #     if player.name == 'VRPlumber':
        #         #         # await nice_item(player, 'minecraft:elytra')
        #         await block(player, 'minecraft:netherite_block')

        # response = await server.call_remote("World.getBlock", [world, 0, 0, 0])
        # log.info("%s block(0,0,0) => %s", world, response)
        # response = await server.call_remote(
        #     "World.setBlock", [world, 0, 74, 0], 'minecraft:netherite_block'
        # )
    #     # for entity in await server.call_remote("World.getEntityTypes"):
    #     #     print(entity)
    #     for i in range(1, 5):
    #         response = await server.call_remote(
    #             "World.setBlock",
    #             [
    #                 'world',
    #                 193,
    #                 110 + i,
    #                 277,
    #             ],
    #             "minecraft:netherite_block",
    #         )

    # for entity in await server.call_remote("World.getEntities", world):
    #     print(entity)
    #     if entity.get('type') == 'SKELETON':
    #         await server.call_remote("Entity.remove", entity['uuid'])
    queue = await server.subscribe("AsyncPlayerChatEvent")
    while True:
        event = await queue.get()
        print('Event: %s', event)
    await server.close()


def main():
    logging.basicConfig(level=logging.DEBUG)
    asyncio.get_event_loop().run_until_complete(test_api())


if __name__ == "__main__":
    main()
