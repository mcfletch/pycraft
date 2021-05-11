"""Communications channel for interacting with Pycraft Server"""
import asyncio
import json
import logging

log = logging.getLogger(__name__)


class MethodInvocationError(RuntimeError):
    """Raised on all invocation failures"""


class Server(object):
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

    async def open(self):
        self.wanted = True
        self.reader, self.writer = await asyncio.open_connection(*self.address)
        asyncio.ensure_future(self.write_to_socket(self.outgoing_queue, self.writer))
        asyncio.ensure_future(self.read_from_socket(self.incoming_queue, self.reader))
        asyncio.ensure_future(self.process_incoming_queue(self.incoming_queue))

    async def close(self):
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
                message_id, error_flag, payload = (
                    int(message_id),
                    int(error_flag),
                    json.loads(payload),
                )
                log.info("Read message: %r,%r,%r", message_id, error_flag, payload)
                await queue.put((message_id, error_flag, payload))
            except Exception as err:
                log.exception("Error reading from socket")
                # if reader.connection.isClosed():
                import pdb

                pdb.set_trace()
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
            json.dumps(args),
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


async def test_api():
    server = Server()
    await server.open()
    worlds = await server.call_remote("World.getWorlds")
    log.info("getWorlds => %s", worlds)
    for world in worlds:
        response = await server.call_remote("World.getPlayers", world)
        log.info("getPlayers(%r) => %s", world, response)
        response = await server.call_remote("World.getBlock", [world, 0, 0, 0])
        log.info("%s block(0,0,0) => %s", world, response)
        response = await server.call_remote(
            "World.setBlock", [world, 0, 74, 0], 'minecraft:netherite_block'
        )
        if world == 'world':  # default world name...
            for material in await server.call_remote(
                "World.getMaterialTypes",
            ):
                print(material)
            for entity in await server.call_remote("World.getEntityTypes"):
                print(entity)

        for entity in await server.call_remote("World.getEntities", world):
            print(entity)
            if entity.get('type') == 'SKELETON':
                await server.call_remote("Entity.remove", entity['uuid'])
    queue = await server.subscribe("AsyncPlayerChatEvent")
    while True:
        event = await queue.get()
        print('Event: %s', event)
    await server.close()


def main():
    asyncio.get_event_loop().run_until_complete(test_api())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
