"""Expose commands via chat on a minecraft instance"""
import asyncio
from asyncio.events import get_event_loop
import logging
import re, time
from .expose import (
    DEFAULT_COMMANDS,
    DEFAULT_NAMESPACE,
    expose,
)
import queue

# from .lockedmc import locked
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
    """Asyncio compatible listening service"""

    wanted = True

    def __init__(self, channel, interpreter=None):
        self.channel = channel
        if interpreter is None:
            from . import ainterpreter as default_interpreter

            interpreter = default_interpreter.AInterpreter(channel, self)
        self.interpreter = interpreter
        self.event_watchers = {}

    async def listen(self):
        """Arrang to run our chat processing operations in the background"""
        self.request_queue = await self.channel.subscribe("AsyncPlayerChatEvent")
        asyncio.ensure_future(self.process_chat_queue(self.request_queue))
        # for interaction in [
        #     'BlockPlaceEvent',
        #     'BlockBreakEvent',
        #     'PlayerInteractEvent',
        #     'PlayerInteractEntityEvent',
        # ]:

        #     queue = await self.channel.subscribe(interaction)
        #     asyncio.ensure_future(self.process_interact_queue(queue, interaction))

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
        self, queue: asyncio.Queue, interaction: str, watchers: list
    ):
        """Process queue of events from interactions"""

        def remove(watcher):
            watchers.remove(watcher)

        while self.wanted and watchers:
            log.info("Getting %s...", interaction)
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
                if matched and watcher.one_shot:
                    remove(watcher)
        if not watchers:
            del self.event_watchers[interaction]
        log.info("Unsubscribing from %s", interaction)
        await self.channel.unsubscribe(interaction)

    async def wait_for_event(
        self,
        event_type: str = 'PlayerInteractEvent',
        player: world.Player = None,
        action: str = None,
        timeout: int = 30,
        one_shot: bool = True,
    ):
        """Wait for the given user to generate an event of the given type"""
        watchers = self.event_watchers.get(event_type, None)
        event_loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()
        df = event_loop.create_future()

        filters = []
        if player:
            filters.append(player_test(player))
        if action:
            filters.append(action_test(action))

        def watcher(message):
            if df.done():
                log.info("Callback already done...")
                return True
            for filter in filters:
                if not filter(message):
                    log.info("Ingoring due to failing filter %s", filter)
                    return False
            log.info("Matched watcher: %s", watcher)
            df.set_result(message)
            return True

        watcher.one_shot = one_shot

        if watchers is None:
            watchers = self.event_watchers[event_type] = [watcher]
            queue = await self.channel.subscribe(event_type)
            asyncio.ensure_future(
                self.process_interact_queue(queue, event_type, watchers)
            )
        else:
            watchers.append(watcher)

        def timedout():
            if not df.done():
                df.set_exception(
                    TimeoutError(
                        'Timed out waiting for %s from %s' % (event_type, player)
                    )
                )
                watchers.remove(watcher)

        event_loop.call_later(timeout, timedout)
        return await df


def player_test(player):
    def test(message):
        incoming = getattr(message, 'player', None)
        if incoming and (incoming.name == player or incoming.uuid == player):
            return True
        return False

    test.__name__ = 'player_eq_%s' % (player,)
    return test


def action_test(interaction_type):
    """Test that the interaction is specified type"""

    def test(message):
        incoming = getattr(message, 'action', None)
        if incoming == interaction_type:
            return True
        return False

    test.__name__ = 'action_eq_%s' % (interaction_type)
    return test
