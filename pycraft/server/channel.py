"""Communications channel for interacting with Pycraft Server"""
import asyncio
import json
from json import encoder
import logging
from functools import lru_cache

from json.encoder import JSONEncoder
from . import proxyobjects

log = logging.getLogger(__name__)


class ProxyEncoder(JSONEncoder):
    def default(self, o):
        """If o has a __json__ method, return the encoded result of o.__json__()"""
        if hasattr(o, '__json__'):
            return o.__json__()
        raise TypeError("No __json__ on type %s" % (o.__class__,))


class MethodInvocationError(RuntimeError):
    """Raised on all invocation failures"""


class Channel(object):
    def __init__(self, host='localhost', port=4712):
        self.address = (host, port)
        self.reader = None
        self.writer = None
        self.outgoing_queue = asyncio.Queue()
        self.incoming_queue = asyncio.Queue()
        self.wanted = True
        self.count = 0
        self.timeout = 30
        self.pending = {}
        self.subscriptions = {}
        self.method_cache = {}
        self.method_cache_lock = asyncio.Lock()

    async def open(self):
        self.wanted = True
        self.reader, self.writer = await asyncio.open_connection(
            *self.address, limit=1024 * 1024 * 5
        )
        asyncio.ensure_future(self.write_to_socket(self.outgoing_queue, self.writer))
        asyncio.ensure_future(self.read_from_socket(self.incoming_queue, self.reader))
        asyncio.ensure_future(self.process_incoming_queue(self.incoming_queue))
        proxyobjects.ProxyMethod.set_channel(self)

    async def close(self):
        if proxyobjects.ProxyMethod.channel is self:
            proxyobjects.ProxyMethod.set_channel(None)
        self.wanted = False
        self.writer.close()
        await self.outgoing_queue.put(None)
        await self.incoming_queue.put(None)
        await self.writer.wait_closed()

    async def write_to_socket(self, queue, writer):
        while self.wanted:
            message = await queue.get()
            if message is None:
                break
            if isinstance(message, str):
                message = message.encode('utf-8')
            log.info("Writing message: %r", message)
            self.writer.write(message)
            self.writer.write(b"\n")

    async def read_from_socket(self, queue, reader):
        while self.wanted:
            try:
                line = await reader.readline()
                if not line:
                    break
                try:
                    message_id, error_flag, payload = line.decode('utf-8').split(',', 2)
                except (ValueError, TypeError) as err:
                    log.error("Invalid header/format: %r", line)
                    continue
                try:
                    message_id, error_flag, payload = (
                        int(message_id),
                        int(error_flag),
                        json.loads(payload),
                    )
                except Exception as err:
                    log.exception("Error reading from socket with %r", line)
                log.info("Read message: %r,%r,%r", message_id, error_flag, payload)
                await queue.put((message_id, error_flag, payload))
            except Exception as err:
                log.exception("Error reading from socket")
                # if reader.connection.isClosed():
                break

    async def process_incoming_queue(self, queue):
        while self.wanted:
            record = await queue.get()
            if record is None:
                break
            message_id, error_flag, payload = record
            try:
                pending = self.pending.pop(message_id)
            except KeyError as err:
                pending = None
            if not pending:
                if error_flag == 2:
                    # subscription
                    queue = self.subscriptions.get(message_id)
                    if queue:
                        await queue.put(payload)
            else:
                if error_flag == 1:
                    pending.set_exception(MethodInvocationError(*payload))
                else:
                    pending.set_result(payload)

    async def call_remote(self, method, *args):
        """1:1 RPC call to the remote server"""
        self.count += 1
        id = self.count
        message = "%s,%s,%s" % (
            id,
            method,
            json.dumps(
                args,
                cls=ProxyEncoder,
            ),
        )
        await self.outgoing_queue.put(message)
        log.info("Outgoing message queued")
        self.pending[id] = asyncio.Future()
        return await asyncio.wait_for(self.pending[id], self.timeout)

    async def subscribe(self, EventClass):
        """Subscribe to an Event Type from the server

        Returns an awaitable queue producing event records,
        a None in the queue indicates deletion
        """
        self.subscriptions[EventClass] = asyncio.Queue()
        await self.call_remote("subscribe", EventClass, True)
        return self.subscriptions[EventClass]

    async def unsubscribe(self, EventClass):
        """Unsubscribe to an Event Type from the server"""
        queue = self.subscriptions.get(EventClass)
        if queue:
            await queue.put(None)
            del self.subscriptions[EventClass]
        return await self.call_remote("subscribe", EventClass, False)

    async def get_methods(self, namespace=None):
        """Get the methods/names in the given namespace

        Caches results to avoid constantly re-querying the server
        """
        await self.method_cache_lock.acquire()
        try:
            if namespace in self.method_cache:
                return self.method_cache[namespace]
            response = await self.call_remote(
                "%s.__methods__" % (namespace,) if namespace else '__methods__'
            )
            self.method_cache[namespace] = response
            return response
        finally:
            self.method_cache_lock.release()


async def test_api():
    from .world import World, Player, Server, Entity, BlockData, Location

    server = Channel()
    await server.open()
    Server.inject_methods(server, await server.get_methods('Server'))
    World.inject_methods(server, await server.get_methods('World'))
    Player.inject_methods(server, await server.get_methods('Player'))
    Entity.inject_methods(server, await server.get_methods('Player'))

    import pprint

    pprint.pprint(
        sorted(
            [
                x
                for x in proxyobjects.RETURN_TYPES.keys()
                if not proxyobjects.type_name_to_type(x)
            ]
        )
    )

    worlds = await Server(name="server").getWorlds()

    # worlds = await server.call_remote("Server.getWorlds", "server")
    log.info("getWorlds => %s", worlds)
    # for world in worlds:
    #     structured = World.from_server(world)
    #     for player in structured.players:
    #         # print(await structured.getBlockAt([structured.name, 0, 0, 0]))
    #         if player.name == 'VRPlumber':
    #             print(dir(structured))
    #             # await structured.spawn(player.location, 'minecraft:sheep')
    #             # await structured.setStorm(True)
    #             # await structured.setThundering(True)

    #             # await structured.spawnEntity(player.location, 'minecraft:pufferfish')

    #             # await structured.strikeLightning(player.location)
    #             # await structured.strikeLightningEffect(player.location)
    #             await player.sendMessage("Hello from the new api")

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
    # if world.get('name') == 'world':  # default world name...
    #     # for material in await server.call_remote(
    #     #     "World.getMaterialTypes",
    #     # ):
    #     #     print(material)
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
