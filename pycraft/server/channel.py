"""Communications channel for interacting with Pycraft Server"""
import asyncio
import json
import os
from json import encoder
import uuid
import logging
import time
import numpy as np
from functools import lru_cache

from json.encoder import JSONEncoder
from . import proxyobjects, world, final

log = logging.getLogger(__name__)

CACHE_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '.introspection.json'
)


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
        writer, self.writer = self.writer, None
        if writer:
            writer.close()
        await self.outgoing_queue.put(None)
        await self.incoming_queue.put(None)

        if writer:
            await writer.wait_closed()

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
        """Process and dispatch messages coming in on the main input queue"""
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
                        proxyobjects.type_coerce(payload, world.Event)
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

    async def subscribe(self, EventClass, *args):
        """Subscribe to an Event Type from the server

        Returns (queue,queue_id) queue is an awaitable queue producing event records,
        a None in the queue indicates deletion
        """
        queue = asyncio.Queue()
        result = await self.call_remote("subscribe", EventClass, True, *args)
        log.info("Subscribe result: %s", result)
        self.subscriptions[result] = (queue, EventClass)
        return queue, result

    async def unsubscribe(
        self,
        EventClass,
        queue_id,
    ):
        """Unsubscribe to an Event Type from the server for given queue_id"""
        try:
            del self.subscriptions[queue_id]
        except KeyError:
            pass
        return await self.call_remote("subscribe", EventClass, False, queue_id)

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

    DEFAULT_CACHE_TIME = 3600 * 24

    async def load_methods(self, cached=False):
        """Load method metadata, use cache if cached == True"""
        if (
            cached
            and os.path.exists(CACHE_FILE)
            and os.stat(CACHE_FILE).st_mtime > time.time() - self.DEFAULT_CACHE_TIME
        ):
            try:
                log.info("Using cache file: %s", CACHE_FILE)
                return json.loads(open(CACHE_FILE).read())
            except Exception as err:
                log.info(
                    "Unable to load the cached methods, will have to run introspection"
                )
                pass
        automatic = await self.call_remote("__methods__")
        with open(CACHE_FILE + '~', 'w') as fh:
            fh.write(json.dumps(automatic, indent=2, sort_keys=True))
        os.rename(CACHE_FILE + '~', CACHE_FILE)
        return automatic

    async def introspect(self, cached=False):
        """Get methods for all registered namespaces

        Needs to do all of:

            * Query for the (huge) data-structure
            * Figure out dependency resolution orders for classes
            * Generate the final classes

        """
        seen_classes = {}

        automatic = await self.load_methods(cached=cached)

        if 'plugins' in automatic:
            for name, plugin in sorted(automatic['plugins'].items()):
                log.info("Server plugin: %s %s", plugin['name'], plugin['version'])

        await proxyobjects.construct_from_introspection(automatic, self)

    @property
    def server(self):
        """Get configured server instance for this connection"""
        from .final import Server

        return Server()
