"""Communications channel for interacting with Pycraft Server"""
import asyncio
import json
from json import encoder
import uuid
import logging
import time
import numpy as np
from functools import lru_cache

from json.encoder import JSONEncoder
from . import proxyobjects, world

log = logging.getLogger(__name__)


class ProxyEncoder(JSONEncoder):
    def default(self, o):
        """If o has a __json__ method, return the encoded result of o.__json__()"""
        if hasattr(o, '__json__'):
            return o.__json__()
        elif isinstance(o, uuid.UUID):
            return str(o)
        elif isinstance(o, np.ndarray):
            result = []
            for item in o:
                if isinstance(item, np.ndarray):
                    result.append(self.default(item))
                else:
                    result.append(item)
            return result
        raise TypeError("No __json__ on type %s: %s" % (o.__class__, o))


class MethodInvocationError(RuntimeError):
    """Raised on all invocation failures"""


class Channel(object):
    def __init__(self, host='localhost', port=4712, debug=False):
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
        self.debug = debug

    async def open(self):
        self.wanted = True
        self.reader, self.writer = await asyncio.open_connection(
            *self.address, limit=1024 * 1024 * 20
        )
        if self.debug:
            log.info("Opening channel to server: %s", self.address)
        asyncio.ensure_future(self.write_to_socket(self.outgoing_queue, self.writer))
        asyncio.ensure_future(self.read_from_socket(self.incoming_queue, self.reader))
        asyncio.ensure_future(self.process_incoming_queue(self.incoming_queue))
        proxyobjects.ProxyMethod.set_channel(self)

    async def close(self):
        if self.debug:
            log.info("Closing channel to server: %s", self.address)
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
            if self.debug:
                log.debug("Writing message: %r", message)
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
                if self.debug:
                    log.debug("Read message: %r,%r,%r", message_id, error_flag, payload)
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
                # if error_flag == 2:
                # subscription
                sub_queue = self.subscriptions.get(message_id)
                if sub_queue:
                    from . import world, proxyobjects

                    await sub_queue[0].put(
                        proxyobjects.type_coerce(payload, world.AsyncPlayerChatEvent)
                    )
                else:
                    log.info("Stale or unexpected response to %s", record)
            else:
                if error_flag == 1:
                    pending.set_exception(MethodInvocationError(*payload))
                else:
                    pending.set_result(payload)

    async def call_remote(self, method, *args):
        """1:1 RPC call to the remote server"""
        ts = time.time()
        try:
            if self.debug:
                log.info("call remote: %s", method)
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
            if self.debug:
                log.debug("Outgoing message queued")
            self.pending[id] = asyncio.Future()
            return await asyncio.wait_for(self.pending[id], self.timeout)
        finally:
            if self.debug:
                log.debug("%0.2fs for %s call", time.time() - ts, method)

    async def subscribe(self, EventClass):
        """Subscribe to an Event Type from the server

        Returns an awaitable queue producing event records,
        a None in the queue indicates deletion
        """
        queue = asyncio.Queue()
        result = await self.call_remote("subscribe", EventClass, True)
        log.info("Subscribe result: %s", result)
        self.subscriptions[self.count] = (queue, EventClass)
        return queue

    async def unsubscribe(self, EventClass):
        """Unsubscribe to an Event Type from the server"""
        for id, (q, ec) in list(self.subscriptions.items()):
            if ec == EventClass:
                del self.subscriptions[id]
                await q.put(None)
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

    async def introspect(self):
        """Get methods for all registered namespaces"""
        seen = {}
        seen_classes = {}

        automatic = await self.call_remote("__methods__")

        for declarations in automatic.get('commands', []):
            if not isinstance(declarations, dict):
                log.warning("Non dictionary type in declarations: %s", declarations)
                continue
            if declarations.get('type') == 'namespace':
                name = declarations['name']
                cls = proxyobjects.PROXY_TYPES.get(name)
                if cls is None:
                    proxyobjects.PROXY_TYPES[name] = cls = type(
                        name,
                        (proxyobjects.ServerObjectProxy,),
                        {
                            '__namespace__': name,
                        },
                    )
                seen[name] = declarations

        for proxy in proxyobjects.PROXY_TYPES.values():
            if proxy.__namespace__ not in seen:
                if self.debug:
                    log.info("Manual Introspect: %s", proxy.__namespace__)
                try:
                    seen[proxy.__namespace__] = await self.get_methods(
                        proxy.__namespace__
                    )
                except MethodInvocationError as err:
                    log.warning("Unable to introspect: %s %s", proxy.__namespace__, err)
                    continue
            if proxy in seen_classes:
                continue
            seen_classes[proxy] = True
            proxy.inject_methods(self, seen[proxy.__namespace__])

    @property
    def server(self):
        """Get configured server instance for this connection"""
        from .world import Server

        return Server()