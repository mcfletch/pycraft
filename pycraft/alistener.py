"""Expose commands via chat on a minecraft instance"""
import asyncio
from asyncio.events import get_event_loop
import logging, typing
import re, time, weakref
from .expose import (
    DEFAULT_COMMANDS,
    DEFAULT_NAMESPACE,
    expose,
)

import numpy as np
from .server import world

log = logging.getLogger(__name__)
COMMAND_FINDER = re.compile(
    r'^[ ]*(?P<function>[a-zA-z][_.a-zA-Z0-9]*)[(](?P<args>.*)[)][ ]*$', re.I | re.U
)
ASSIGNMENT_FINDER = re.compile(
    r'^[ ]*(?P<name>[a-zA-z][_a-zA-Z0-9]*)[ ]*[=](?P<expr>.*)[ ]*$',
    re.I | re.U,
)

KNOWN_EVENTS = '''AsyncPlayerPreLoginEvent
PlayerAdvancementDoneEvent
PlayerAnimationEvent
PlayerArmorStandManipulateEvent
PlayerBedEnterEvent
PlayerBedLeaveEvent
PlayerBucketEmptyEvent
PlayerBucketFillEvent
PlayerChangedMainHandEvent
PlayerChangedWorldEvent
PlayerChannelEvent
PlayerCommandPreprocessEvent
PlayerDropItemEvent
PlayerEditBookEvent
PlayerEggThrowEvent
PlayerExpChangeEvent
PlayerFishEvent
PlayerGameModeChangeEvent
PlayerInteractAtEntityEvent
PlayerInteractEntityEvent
PlayerInteractEvent
PlayerItemBreakEvent
PlayerItemConsumeEvent
PlayerItemDamageEvent
PlayerItemHeldEvent
PlayerJoinEvent
PlayerKickEvent
PlayerLevelChangeEvent
PlayerLocaleChangeEvent
PlayerLoginEvent
PlayerMoveEvent
PlayerPickupArrowEvent
PlayerPortalEvent
PlayerQuitEvent
PlayerRegisterChannelEvent
PlayerResourcePackStatusEvent
PlayerRespawnEvent
PlayerShearEntityEvent
PlayerStatisticIncrementEvent
PlayerSwapHandItemsEvent
PlayerTeleportEvent
PlayerToggleFlightEvent
PlayerToggleSneakEvent
PlayerToggleSprintEvent
PlayerUnleashEntityEvent
PlayerUnregisterChannelEvent
PlayerVelocityEvent
BlockBreakEvent
BlockBurnEvent
BlockCanBuildEvent
BlockDamageEvent
BlockDispenseEvent
BlockExpEvent
BlockExplodeEvent
BlockFadeEvent
BlockFormEvent
BlockFromToEvent
BlockGrowEvent
BlockIgniteEvent
BlockMultiPlaceEvent
BlockPhysicsEvent
BlockPistonExtendEvent
BlockPistonRetractEvent
BlockPlaceEvent
BlockRedstoneEvent
BlockSpreadEvent
CauldronLevelChangeEvent
EntityBlockFormEvent
LeavesDecayEvent
NotePlayEvent
SignChangeEvent
AreaEffectCloudApplyEvent
CreatureSpawnEvent
CreeperPowerEvent
EnderDragonChangePhaseEvent
EntityBreakDoorEvent
EntityBreedEvent
EntityChangeBlockEvent
EntityCombustByBlockEvent
EntityCombustByEntityEvent
EntityCombustEvent
EntityDamageByBlockEvent
EntityDamageByEntityEvent
EntityDamageEvent
EntityDeathEvent
EntityExplodeEvent
EntityInteractEvent
EntityPickupItemEvent
EntityPortalEnterEvent
EntityPortalEvent
EntityPortalExitEvent
EntityRegainHealthEvent
EntityResurrectEvent
EntityShootBowEvent
EntitySpawnEvent
EntityTameEvent
EntityTargetEvent
EntityTargetLivingEntityEvent
EntityTeleportEvent
EntityToggleGlideEvent
EntityUnleashEvent
ExpBottleEvent
ExplosionPrimeEvent
FireworkExplodeEvent
FoodLevelChangeEvent
HorseJumpEvent
ItemDespawnEvent
ItemMergeEvent
ItemSpawnEvent
LingeringPotionSplashEvent
PigZapEvent
PlayerDeathEvent
PlayerLeashEntityEvent
PotionSplashEvent
ProjectileHitEvent
ProjectileLaunchEvent
SheepDyeWoolEvent
SheepRegrowWoolEvent
SlimeSplitEvent
SpawnerSpawnEvent
VillagerAcquireTradeEvent
VillagerReplenishTradeEvent
HangingBreakByEntityEvent
HangingBreakEvent
HangingPlaceEvent
BrewEvent
BrewingStandFuelEvent
CraftItemEvent
FurnaceBurnEvent
FurnaceExtractEvent
FurnaceSmeltEvent
InventoryClickEvent
InventoryCloseEvent
InventoryCreativeEvent
InventoryDragEvent
InventoryInteractEvent
InventoryMoveItemEvent
InventoryOpenEvent
PrepareAnvilEvent
PrepareItemCraftEvent
VehicleBlockCollisionEvent
VehicleCreateEvent
VehicleDamageEvent
VehicleDestroyEvent
VehicleEnterEvent
VehicleEntityCollisionEvent
VehicleExitEvent
VehicleMoveEvent
VehicleUpdateEvent
LightningStrikeEvent
ThunderChangeEvent
WeatherChangeEvent
ChunkLoadEvent
ChunkPopulateEvent
ChunkUnloadEvent
PortalCreateEvent
SpawnChangeEvent
StructureGrowEvent
WorldInitEvent
WorldLoadEvent
WorldSaveEvent
WorldUnloadEvent'''.split()


class AListener(object):
    """Asyncio compatible listening service

    The AListener is responsible for:
    * listening to events from the server
    * using a :py:class:`ainterpreter.AInterpreter` to interpret the events
    * sending commands back to the server
    """

    channel: 'pycraft.channel.Channel'
    wanted = True

    def __init__(self, channel, interpreter=None, scripts=None):
        self.channel = channel
        self.request_queue = None
        self.request_queue_id = None
        if interpreter is None:
            from . import ainterpreter as default_interpreter

            interpreter = default_interpreter.AInterpreter(
                channel, self, scripts=scripts
            )
        self.interpreter = interpreter
        self.event_watchers = {}

    async def listen(self):
        """Arrang to run our chat processing operations in the background"""
        self.request_queue, self.request_queue_id = await self.channel.subscribe(
            "AsyncPlayerChatEvent"
        )
        asyncio.create_task(
            self.process_chat_queue(self.request_queue), name='chat-queue'
        )
        asyncio.create_task(self.interpreter.scripts_shovel(), name='scripts-shovel')

    async def process_chat_queue(self, queue):
        """Process chat events from the queue"""
        try:
            while self.wanted:
                log.info("Getting message...")
                message = await queue.get()
                log.debug("Message: %s", message)
                match = COMMAND_FINDER.match(message.message)
                if match:
                    asyncio.ensure_future(self.process_command(message))
                else:
                    match = ASSIGNMENT_FINDER.match(message.message)
                    if match:
                        message.assignment = match.group('name')
                        message.message = match.group('expr').strip()
                        asyncio.ensure_future(self.process_command(message))
            log.info("Wanted False, exiting process chat queue")
        except Exception as err:
            log.exception("Failure during process chat queue, will restart")
            asyncio.ensure_future(self.process_chat_queue(queue))

    async def process_command(self, message):
        """Process a command that does not make an assignment"""
        response = await self.interpreter.interpret(message)
        if response is not None:
            await self.channel.server.broadcastMessage(str(response))

    async def process_interact_queue(
        self, queue: asyncio.Queue, event_type: str, watchers: list, queue_id: int
    ):
        """Process queue of events from interactions"""

        def remove(watcher):
            watchers.remove(watcher)

        while self.wanted and watchers:
            log.info("Getting %s...", event_type)
            message = await queue.get()
            log.info("Message: %s", message)
            for watcher in watchers:
                try:
                    matched = watcher(message)
                except Exception as err:
                    log.exception(
                        'Failure processing message: %s with %s', message, watcher
                    )
                    matched = True
                else:
                    log.debug('Result of %s: %s', watcher, matched)
        if not watchers:
            del self.event_watchers[event_type]
        log.info("Unsubscribing from %s", event_type)
        await self.channel.unsubscribe(event_type, queue_id)

    def _filters_from_named(self, named):
        for key in ['player', 'entity']:
            if key in named:
                value = named[key]
                if isinstance(value, str):
                    return [1, value]
                elif hasattr(value, 'uuid'):
                    return [1, value.uuid]
                elif hasattr(value, 'name'):
                    return [1, value.name]
        if 'location' in named:
            value = named['location']
            if isinstance(value, (list, tuple)):
                return [2, value, value]
            elif hasattr(value, '__floor__'):
                return [2, value.__floor__()[:3], value.__floor__()[:3]]
            raise ValueError("Unrecognised location type: %r" % (value,))
        if 'block' in named:
            value = named['block']
            return self._filters_from_named(
                {'location': value.location if hasattr(value, 'location') else value}
            )
        if 'area' in named:
            value = named['area']
            first, last = value
            fx, fy, fz = first[:3]
            lx, ly, lz = last[:3]
            fx, lx = min((fx, lx)), max((fx, lx))
            fy, ly = min((fy, ly)), max((fy, ly))
            fx, lz = min((fz, lz)), max((fz, lz))
            return [2, (fx, fy, fz), (lx, ly, lz)]
        return None

    async def wait_for_events(
        self,
        event_type: str = 'PlayerInteractEvent',
        filters: typing.Optional[list] = None,
        timeout: int = 30,
        max_count: int = 0,
        **named
    ):
        """Wait for events, yielding each as it occurs

        event_type -- Java Bukkit API name for the event

        filters -- definition of a filter to be applied to the events
                   [1, name] -- filter to entity name
                   [1, uuid] -- filter to entity uuid
                   [2, [0,0,0],[1,1,1]] -- filter to blocks in the (inclusive) area

        timeout -- timeout in seconds after which we stop

        max_count -- number of events after which we exit

        named -- parameters to construct a filter:
                 player/entity -- str or Entity to match
                 location/block -- location or block to match
                 area -- 2 locations for inclusive area match

        returns async generator producing events matching the filters
        """
        if not filters:
            filters = self._filters_from_named(named)
        queue, queue_id = await self.channel.subscribe(event_type, *(filters or []))
        log.info("Subscribed %s for %s", event_type, queue_id)
        final_ts = time.time() + timeout
        try:
            count = 0
            while True:
                try:
                    event = await asyncio.wait_for(
                        queue.get(), timeout=final_ts - time.time()
                    )
                except asyncio.TimeoutError as err:
                    log.info("Timeout waiting for %s for %s", event_type, queue_id)
                    break
                count += 1
                yield event
                if max_count and count >= max_count:
                    break
        finally:
            log.info("Unsubscribing %s for %s", event_type, queue_id)
            await self.channel.unsubscribe(event_type, queue_id)

    async def wait_for_event(
        self,
        event_type: str = 'PlayerInteractEvent',
        filters: typing.Optional[list] = None,
        timeout: int = 30,
        **named
    ):
        """Wait for a single event, exiting when it is received...

        See wait_for_events for the parameters, this call merely
        does an async_for over the events returning the first result
        """
        async for event in self.wait_for_events(
            event_type=event_type,
            filters=filters,
            timeout=timeout,
            max_count=1,
            **named
        ):
            return event


class QIter(object):
    def __init__(self, queue, max_count=0, timeout=0, cleanup=None):
        self.queue = queue
        self.max_count = max_count
        self.count = 0
        if timeout:
            asyncio.get_event_loop().call_later(timeout, self.timedout)
        # cleanup should be called when we exit the loop...
        self._cleanup_ref = weakref.ref(self, cleanup)

    async def timedout(self):
        log.info("Doing timeout check: %s", self.count)
        if not self.count:
            await self.queue.put(
                StopAsyncIteration('Timed out waiting for first message')
            )
            # if self.cleanup:
            #     log.info("Cleaning up on timeout")
            #     await self.cleanup()

    async def __anext__(self):
        self.count += 1
        log.info("anext: %s", self.count)
        if self.max_count and self.count > self.max_count:
            # if self.cleanup:
            #     await self.cleanup()
            log.info("Max count %s reached, stopping iteration")
            raise StopAsyncIteration('Reached max count')
        item = await self.queue.get()
        log.info("  item: %s", item)
        if isinstance(item, Exception):
            # if self.cleanup:
            #     await self.cleanup()
            raise item
        else:
            return item

    def __aiter__(self):
        return self


def player_test(player):
    return 1, player.uuid


def action_test(interaction_type):
    """Test that the interaction is specified type"""

    def test(message):
        incoming = getattr(message, 'action', None)
        if incoming == interaction_type:
            return True
        return False

    test.__name__ = 'action_eq_%s' % (interaction_type)
    return test
