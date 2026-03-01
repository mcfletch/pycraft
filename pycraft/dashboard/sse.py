"""SSE (Server-Sent Events) manager for broadcasting Minecraft events to browser clients"""
import asyncio
import json
import logging
import time

from aiohttp import web

from .serialization import serialize

log = logging.getLogger(__name__)

# Events to subscribe to on startup
SUBSCRIBED_EVENTS = [
    'PlayerJoinEvent',
    'PlayerQuitEvent',
    'PlayerMoveEvent',
    'AsyncPlayerChatEvent',
    'BlockBreakEvent',
    'BlockPlaceEvent',
    'PlayerDeathEvent',
    'EntityDeathEvent',
]

# Map server event type names to SSE event names
EVENT_TYPE_MAP = {
    'PlayerJoinEvent': 'player_join',
    'PlayerQuitEvent': 'player_quit',
    'PlayerMoveEvent': 'player_move',
    'AsyncPlayerChatEvent': 'chat',
    'BlockBreakEvent': 'block_break',
    'BlockPlaceEvent': 'block_place',
    'PlayerDeathEvent': 'player_death',
    'EntityDeathEvent': 'entity_death',
}

POSITION_FLUSH_INTERVAL = 0.5  # seconds


class SSEManager:
    """Manages SSE client connections and broadcasts events from the Minecraft server"""

    def __init__(self):
        self.clients = set()
        self.position_buffer = {}  # uuid -> latest position data
        self._subscription_tasks = []
        self._flusher_task = None
        self._heartbeat_task = None

    async def start(self, channel):
        """Subscribe to Minecraft events and start background tasks"""
        self.channel = channel
        for event_type in SUBSCRIBED_EVENTS:
            try:
                queue, queue_id = await channel.subscribe(event_type)
                task = asyncio.create_task(
                    self._process_event_queue(queue, event_type, queue_id),
                    name=f'sse-{event_type}',
                )
                self._subscription_tasks.append((task, event_type, queue_id))
                log.info("SSE subscribed to %s (queue_id=%s)", event_type, queue_id)
            except Exception:
                log.exception("Failed to subscribe to %s", event_type)

        self._flusher_task = asyncio.create_task(
            self._position_flusher(), name='sse-position-flusher'
        )
        self._heartbeat_task = asyncio.create_task(
            self._heartbeat(), name='sse-heartbeat'
        )

    async def stop(self):
        """Clean up subscriptions and tasks"""
        for task, event_type, queue_id in self._subscription_tasks:
            task.cancel()
            try:
                await self.channel.unsubscribe(event_type, queue_id)
            except Exception:
                pass
        self._subscription_tasks.clear()
        if self._flusher_task:
            self._flusher_task.cancel()
        if self._heartbeat_task:
            self._heartbeat_task.cancel()
        for client in list(self.clients):
            try:
                await client.write_eof()
            except Exception:
                pass
        self.clients.clear()

    async def add_client(self, request):
        """Create an SSE response for a new client connection"""
        response = web.StreamResponse(
            status=200,
            reason='OK',
            headers={
                'Content-Type': 'text/event-stream',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                'Access-Control-Allow-Origin': '*',
            },
        )
        await response.prepare(request)
        self.clients.add(response)
        log.info("SSE client connected (total: %d)", len(self.clients))
        try:
            # Keep the connection alive until the client disconnects
            while True:
                await asyncio.sleep(1)
                # Check if client is still connected by trying to write
                try:
                    await response.write(b': keepalive\n\n')
                except (ConnectionResetError, ConnectionAbortedError):
                    break
        except asyncio.CancelledError:
            pass
        finally:
            self.clients.discard(response)
            log.info("SSE client disconnected (total: %d)", len(self.clients))
        return response

    async def broadcast(self, event_type, data):
        """Send an event to all connected SSE clients"""
        if not self.clients:
            return
        payload = f"event: {event_type}\ndata: {json.dumps(data)}\n\n".encode('utf-8')
        dead_clients = set()
        for client in self.clients:
            try:
                await client.write(payload)
            except (ConnectionResetError, ConnectionAbortedError, Exception):
                dead_clients.add(client)
        self.clients -= dead_clients

    async def _process_event_queue(self, queue, event_type, queue_id):
        """Read events from a channel subscription queue and broadcast them"""
        sse_event = EVENT_TYPE_MAP.get(event_type, event_type)
        try:
            while True:
                event = await queue.get()
                if event is None:
                    break
                data = serialize(event)

                # Buffer move events instead of broadcasting immediately
                if event_type == 'PlayerMoveEvent':
                    player = getattr(event, 'player', None)
                    if player and hasattr(player, 'uuid'):
                        self.position_buffer[str(player.uuid)] = {
                            'uuid': str(player.uuid),
                            'name': getattr(player, 'name', None),
                            'location': data.get('player', {}).get('location')
                            if isinstance(data, dict)
                            else None,
                        }
                    continue

                await self.broadcast(sse_event, data)
        except asyncio.CancelledError:
            pass
        except Exception:
            log.exception("Error processing %s event queue", event_type)

    async def _position_flusher(self):
        """Periodically flush buffered player positions to SSE clients"""
        try:
            while True:
                await asyncio.sleep(POSITION_FLUSH_INTERVAL)
                if self.position_buffer and self.clients:
                    positions = list(self.position_buffer.values())
                    self.position_buffer.clear()
                    for pos in positions:
                        await self.broadcast('player_move', pos)
        except asyncio.CancelledError:
            pass

    async def _heartbeat(self):
        """Send periodic heartbeat events to keep connections alive"""
        try:
            while True:
                await asyncio.sleep(15)
                await self.broadcast('heartbeat', {})
        except asyncio.CancelledError:
            pass
