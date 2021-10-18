"""Expose commands via chat on a minecraft instance"""
import asyncio
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
EntityAirChangeEvent
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

            interpreter = default_interpreter.AInterpreter(channel)
        self.interpreter = interpreter

    async def listen(self):
        """Arrang to run our chat processing operations in the background"""
        self.request_queue = await self.channel.subscribe("AsyncPlayerChatEvent")
        asyncio.ensure_future(self.process_chat_queue(self.request_queue))
        for interaction in [
            'BlockPlaceEvent',
            'BlockBreakEvent',
            'PlayerInteractEvent',
            'PlayerInteractEntityEvent',
        ]:

            queue = await self.channel.subscribe(interaction)
            asyncio.ensure_future(self.process_interact_queue(queue, interaction))

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

    async def process_interact_queue(self, queue, interaction):
        """Process queue of events from interactions"""
        while self.wanted:
            log.info("Getting %s...", interaction)
            message = await queue.get()
            log.debug("Message: %s", message)
