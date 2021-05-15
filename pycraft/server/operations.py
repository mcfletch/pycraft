import logging, asyncio
from .channel import Channel
from .world import (
    World,
    Player,
    Server,
    Entity,
    BlockData,
    Location,
    Inventory,
    Block,
    ItemStack,
    Enchantment,
)

log = logging.getLogger(__name__)


async def nice_sword(player):
    """Give the player a nice sword for running about"""
    inventory = await player.getInventory()
    assert isinstance(inventory, Inventory), inventory
    await inventory.setItem(inventory.firstEmpty, ['minecraft:netherite_sword', 1])
    stack = inventory.get_stack(inventory.firstEmpty)
    for enchantment in [
        'minecraft:sharpness',
        'minecraft:knockback',
        'minecraft:fire_aspect',
        'minecraft:smite',
    ]:
        await stack.addEnchantment(
            enchantment,
            await Enchantment(enchantment).getMaxLevel(),
        )


async def test_api():

    server = Channel()
    await server.open()
    await server.introspect()

    import pprint

    worlds = await Server(name="server").getWorlds()

    # worlds = await server.call_remote("Server.getWorlds", "server")
    log.info("getWorlds => %s", worlds)
    for world in worlds:
        if world.name == 'world':  # default world name...
            print("Materials")
            for material in await server.call_remote(
                "World.getMaterialTypes",
            ):
                print(material)
            print("Enchantments")
            for enchantment in await server.call_remote("Enchantment.values"):
                print(enchantment)
        for player in world.players:
            # print(await structured.getBlockAt([structured.name, 0, 0, 0]))
            if player.name == 'VRPlumber':
                await nice_sword(player)

        #         location = player.location.block_location() + (0, -1, 0)
        #         await world.setBlock(
        #             list(location.vector[:3]), 'minecraft:netherite_block'
        #         )
        # await server.call_remote(
        #     "Inventory.setItem",
        #     str(player.uuid),
        #     0,
        #     'minecraft:elytra',
        # )

        # await world.spawnEntity(player.location, 'SHEEP')
        # await world.setStorm(True)
        # await world.setThundering(True)

        # await world.spawnEntity(player.location, 'minecraft:pufferfish')

        # await world.strikeLightning(player.location)
        # await world.strikeLightningEffect(player.location)
        # await player.sendMessage("Hello from the new api")

        # for player in world.get('players'):
        #     if player.get('name') != 'VRPlumber':
        #         continue
        #     items = [
        #         'minecraft:netherite_axe',
        #         'minecraft:netherite_sword',
        #         'minecraft:netherite_hoe',
        #         'minecraft:netherite_helmet',
        #         'minecraft:netherite_chestplate',
        #         'minecraft:netherite_leggings',
        #         'minecraft:netherite_boots',
        #         'minecraft:trident',
        #     ]
        #     for index, item in enumerate(items):
        #         await server.call_remote(
        #             "Inventory.setItem",
        #             player['uuid'],
        #             index,
        #             item,
        #         )
        #         # if index in [0, 1]:
        #         #     await server.call_remote(
        #         #         "ItemStack.addEnchantment",
        #         #         [index, player['uuid']],
        #         #         'minecraft:fire_aspect',
        #         #         1,
        #         #     )

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
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(test_api())


if __name__ == "__main__":
    main()
