.. currentmodule:: pycraft.server.final

Player
======

Inheritance
------------
* pycraft.server.final.Player
* :py:class:`pycraft.server.world.Player`
* :py:class:`pycraft.server.final.HumanEntity`
* :py:class:`pycraft.server.final.LivingEntity`
* :py:class:`pycraft.server.final.Attributable`
* :py:class:`pycraft.server.final.Damageable`
* :py:class:`pycraft.server.final.Entity`
* :py:class:`pycraft.server.world.Entity`
* :py:class:`pycraft.server.final.Metadatable`
* :py:class:`pycraft.server.final.CommandSender`
* :py:class:`pycraft.server.final.Permissible`
* :py:class:`pycraft.server.final.ServerOperator`
* :py:class:`pycraft.server.final.PersistentDataHolder`
* :py:class:`pycraft.server.final.ProjectileSource`
* :py:class:`pycraft.server.final.AnimalTamer`
* :py:class:`pycraft.server.final.InventoryHolder`
* :py:class:`pycraft.server.final.Conversable`
* :py:class:`pycraft.server.final.PluginMessageRecipient`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.entity.Player <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/entity/Player.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Player(self, **named)
   :canonical: pycraft.server.final.Player

   A particular player (potentially not currently logged in) on the server

   .. py:property:: back
      The cardinal x,z vector which is most closely aligned to backward from the player's current orientation

   .. py:property:: backward
      The cardinal x,z vector which is most closely aligned to backward from the player's current orientation

   .. py:property:: direction
      Retrieve the direction reported when this record was retrieved (not necessarily the *current* direction)

   .. py:property:: forward
      The cardinal x,z vector which is most closely aligned to forward from the player's current orientation

   .. py:property:: forward_and_cross
      Calculate the ordinal directions ahead and right for block-oriented operations

   .. py:property:: id
      Get our local unique key for referencing (uuid)

   .. py:property:: left
      The cardinal x,z vector which is most closely aligned to left from the player's current orientation

   .. py:property:: position
      Retrieve the location reported when this record was retrieved (not necessarily the *current* location)

   .. py:property:: right
      The cardinal x,z vector which is most closely aligned to left from the player's current orientation

   .. py:property:: tile_position

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: abandonConversation

       .. py:method:: abandonConversation(self, _0:Conversation) -> None
          :async:
          :noindex:

       .. py:method:: abandonConversation(self, _0:Conversation, _1:ConversationAbandonedEvent) -> None
          :async:
          :noindex:


   .. py:method:: acceptConversationInput(self, _0:String) -> None
      :async:


   .. py:method:: addAdditionalChatCompletions(self, _0:Collection) -> None
      :async:


   .. py:method:: addAttachment

       .. py:method:: addAttachment(self, _0:Plugin) -> :py:class:`PermissionAttachment`
          :async:
          :noindex:

       .. py:method:: addAttachment(self, _0:Plugin, _1:int) -> :py:class:`PermissionAttachment`
          :async:
          :noindex:

       .. py:method:: addAttachment(self, _0:Plugin, _1:String, _2:boolean) -> :py:class:`PermissionAttachment`
          :async:
          :noindex:

       .. py:method:: addAttachment(self, _0:Plugin, _1:String, _2:boolean, _3:int) -> :py:class:`PermissionAttachment`
          :async:
          :noindex:


   .. py:method:: addCustomChatCompletions(self, _0:Collection) -> None
      :async:


   .. py:method:: addPassenger(self, _0:Entity) -> bool
      :async:


   .. py:method:: addPotionEffect

       .. py:method:: addPotionEffect(self, _0:PotionEffect) -> bool
          :async:
          :noindex:

       .. py:method:: addPotionEffect(self, _0:PotionEffect, _1:boolean) -> bool
          :async:
          :noindex:


   .. py:method:: addPotionEffects(self, _0:Collection) -> bool
      :async:


   .. py:method:: addScoreboardTag(self, _0:String) -> bool
      :async:


   .. py:method:: applyMending(self, _0:int) -> int
      :async:


   .. py:method:: asHoverEvent

       .. py:method:: asHoverEvent(self) -> :py:class:`HoverEvent`
          :async:
          :noindex:

       .. py:method:: asHoverEvent(self, _0:UnaryOperator) -> :py:class:`HoverEvent`
          :async:
          :noindex:


   .. py:method:: attack(self, _0:Entity) -> None
      :async:


   .. py:method:: banPlayer

       .. py:method:: banPlayer(self, _0:String) -> :py:class:`BanEntry`
          :async:
          :noindex:

       .. py:method:: banPlayer(self, _0:String, _1:String) -> :py:class:`BanEntry`
          :async:
          :noindex:

       .. py:method:: banPlayer(self, _0:String, _1:Date) -> :py:class:`BanEntry`
          :async:
          :noindex:

       .. py:method:: banPlayer(self, _0:String, _1:Date, _2:String) -> :py:class:`BanEntry`
          :async:
          :noindex:

       .. py:method:: banPlayer(self, _0:String, _1:Date, _2:String, _3:boolean) -> :py:class:`BanEntry`
          :async:
          :noindex:


   .. py:method:: banPlayerFull

       .. py:method:: banPlayerFull(self, _0:String) -> :py:class:`BanEntry`
          :async:
          :noindex:

       .. py:method:: banPlayerFull(self, _0:String, _1:String) -> :py:class:`BanEntry`
          :async:
          :noindex:

       .. py:method:: banPlayerFull(self, _0:String, _1:Date) -> :py:class:`BanEntry`
          :async:
          :noindex:

       .. py:method:: banPlayerFull(self, _0:String, _1:Date, _2:String) -> :py:class:`BanEntry`
          :async:
          :noindex:


   .. py:method:: banPlayerIP

       .. py:method:: banPlayerIP(self, _0:String) -> :py:class:`BanEntry`
          :async:
          :noindex:

       .. py:method:: banPlayerIP(self, _0:String, _1:Date) -> :py:class:`BanEntry`
          :async:
          :noindex:

       .. py:method:: banPlayerIP(self, _0:String, _1:String) -> :py:class:`BanEntry`
          :async:
          :noindex:

       .. py:method:: banPlayerIP(self, _0:String, _1:boolean) -> :py:class:`BanEntry`
          :async:
          :noindex:

       .. py:method:: banPlayerIP(self, _0:String, _1:Date, _2:String) -> :py:class:`BanEntry`
          :async:
          :noindex:

       .. py:method:: banPlayerIP(self, _0:String, _1:String, _2:boolean) -> :py:class:`BanEntry`
          :async:
          :noindex:

       .. py:method:: banPlayerIP(self, _0:String, _1:Date, _2:boolean) -> :py:class:`BanEntry`
          :async:
          :noindex:

       .. py:method:: banPlayerIP(self, _0:String, _1:Date, _2:String, _3:boolean) -> :py:class:`BanEntry`
          :async:
          :noindex:


   .. py:method:: beginConversation(self, _0:Conversation) -> bool
      :async:


   .. py:method:: boostElytra(self, _0:ItemStack) -> :py:class:`Firework`
      :async:


   .. py:method:: breakBlock(self, _0:Block) -> bool
      :async:


   .. py:method:: broadcastSlotBreak

       .. py:method:: broadcastSlotBreak(self, _0:EquipmentSlot) -> None
          :async:
          :noindex:

       .. py:method:: broadcastSlotBreak(self, _0:EquipmentSlot, _1:Collection) -> None
          :async:
          :noindex:


   .. py:method:: canBreatheUnderwater(self) -> bool
      :async:


   .. py:method:: canSee

       .. py:method:: canSee(self, _0:Entity) -> bool
          :async:
          :noindex:

       .. py:method:: canSee(self, _0:Player) -> bool
          :async:
          :noindex:


   .. py:method:: chat(self, _0:String) -> None
      :async:


   .. py:method:: clearActiveItem(self) -> None
      :async:


   .. py:method:: clearTitle(self) -> None
      :async:


   .. py:method:: closeInventory

       .. py:method:: closeInventory(self) -> None
          :async:
          :noindex:

       .. py:method:: closeInventory(self, _0:Reason) -> None
          :async:
          :noindex:


   .. py:method:: collidesAt(self, _0:Location) -> bool
      :async:


   .. py:method:: customName

       .. py:method:: customName(self) -> :py:class:`Component`
          :async:
          :noindex:

       .. py:method:: customName(self, _0:Component) -> None
          :async:
          :noindex:


   .. py:method:: damage

       .. py:method:: damage(self, _0:double) -> None
          :async:
          :noindex:

       .. py:method:: damage(self, _0:double, _1:Entity) -> None
          :async:
          :noindex:


   .. py:method:: damageItemStack

       .. py:method:: damageItemStack(self, _0:EquipmentSlot, _1:int) -> None
          :async:
          :noindex:

       .. py:method:: damageItemStack(self, _0:ItemStack, _1:int) -> :py:class:`ItemStack`
          :async:
          :noindex:


   .. py:method:: decrementStatistic

       .. py:method:: decrementStatistic(self, _0:Statistic) -> None
          :async:
          :noindex:

       .. py:method:: decrementStatistic(self, _0:Statistic, _1:EntityType) -> None
          :async:
          :noindex:

       .. py:method:: decrementStatistic(self, _0:Statistic, _1:int) -> None
          :async:
          :noindex:

       .. py:method:: decrementStatistic(self, _0:Statistic, _1:Material) -> None
          :async:
          :noindex:

       .. py:method:: decrementStatistic(self, _0:Statistic, _1:Material, _2:int) -> None
          :async:
          :noindex:

       .. py:method:: decrementStatistic(self, _0:Statistic, _1:EntityType, _2:int) -> None
          :async:
          :noindex:


   .. py:method:: deleteMessage

       .. py:method:: deleteMessage(self, _0:Signature) -> None
          :async:
          :noindex:

       .. py:method:: deleteMessage(self, _0:SignedMessage) -> None
          :async:
          :noindex:


   .. py:method:: discoverRecipe(self, _0:NamespacedKey) -> bool
      :async:


   .. py:method:: discoverRecipes(self, _0:Collection) -> int
      :async:


   .. py:method:: displayName

       .. py:method:: displayName(self) -> :py:class:`Component`
          :async:
          :noindex:

       .. py:method:: displayName(self, _0:Component) -> None
          :async:
          :noindex:


   .. py:method:: dropItem(self, _0:boolean) -> bool
      :async:


   .. py:method:: eject(self) -> bool
      :async:


   .. py:method:: filterAudience(self, _0:Predicate) -> :py:class:`Audience`
      :async:


   .. py:method:: fireworkBoost(self, _0:ItemStack) -> :py:class:`Firework`
      :async:


   .. py:method:: forEachAudience(self, _0:Consumer) -> None
      :async:


   .. py:method:: fromMobSpawner(self) -> bool
      :async:


   .. py:method:: from_server(named)
      

      Convert server-side structure to local object


   .. py:method:: get(self, _0:Pointer) -> :py:class:`Optional`
      :async:


   .. py:method:: getAbsorptionAmount(self) -> float
      :async:


   .. py:method:: getActiveItem(self) -> :py:class:`ItemStack`
      :async:


   .. py:method:: getActivePotionEffects(self) -> typing.List[:py:class:`PotionEffect`]
      :async:


   .. py:method:: getAddress(self) -> :py:class:`InetSocketAddress`
      :async:


   .. py:method:: getAdvancementProgress(self, _0:Advancement) -> :py:class:`AdvancementProgress`
      :async:


   .. py:method:: getAffectsSpawning(self) -> bool
      :async:


   .. py:method:: getAllowFlight(self) -> bool
      :async:


   .. py:method:: getArrowCooldown(self) -> int
      :async:


   .. py:method:: getArrowsInBody(self) -> int
      :async:


   .. py:method:: getArrowsStuck(self) -> int
      :async:


   .. py:method:: getAttackCooldown(self) -> float
      :async:


   .. py:method:: getAttribute(self, _0:Attribute) -> :py:class:`AttributeInstance`
      :async:


   .. py:method:: getBedLocation(self) -> :py:class:`Location`
      :async:


   .. py:method:: getBedSpawnLocation(self) -> :py:class:`Location`
      :async:


   .. py:method:: getBeeStingerCooldown(self) -> int
      :async:


   .. py:method:: getBeeStingersInBody(self) -> int
      :async:


   .. py:method:: getBodyYaw(self) -> float
      :async:


   .. py:method:: getBoundingBox(self) -> :py:class:`BoundingBox`
      :async:


   .. py:method:: getCanPickupItems(self) -> bool
      :async:


   .. py:method:: getCategory(self) -> :py:class:`EntityCategory`
      :async:


   .. py:method:: getChunk(self) -> :py:class:`Chunk`
      :async:


   .. py:method:: getClientBrandName(self) -> str
      :async:


   .. py:method:: getClientOption(self, _0:ClientOption) -> :py:class:`Object`
      :async:


   .. py:method:: getClientViewDistance(self) -> int
      :async:


   .. py:method:: getCollidableExemptions(self) -> typing.List[uuid.UUID]
      :async:


   .. py:method:: getCompassTarget(self) -> :py:class:`Location`
      :async:


   .. py:method:: getCooldown(self, _0:Material) -> int
      :async:


   .. py:method:: getCooldownPeriod(self) -> float
      :async:


   .. py:method:: getCooledAttackStrength(self, _0:float) -> float
      :async:


   .. py:method:: getCustomName(self) -> str
      :async:


   .. py:method:: getDeathSound(self) -> :py:class:`Sound`
      :async:


   .. py:method:: getDiscoveredRecipes(self) -> typing.List[:py:class:`NamespacedKey`]
      :async:


   .. py:method:: getDisplayName(self) -> str
      :async:


   .. py:method:: getDrinkingSound(self, _0:ItemStack) -> :py:class:`Sound`
      :async:


   .. py:method:: getEatingSound(self, _0:ItemStack) -> :py:class:`Sound`
      :async:


   .. py:method:: getEffectivePermissions(self) -> typing.List[:py:class:`PermissionAttachmentInfo`]
      :async:


   .. py:method:: getEnchantmentSeed(self) -> int
      :async:


   .. py:method:: getEnderChest(self) -> :py:class:`Inventory`
      :async:


   .. py:method:: getEntityId(self) -> int
      :async:


   .. py:method:: getEntitySpawnReason(self) -> :py:class:`SpawnReason`
      :async:


   .. py:method:: getEquipment(self) -> :py:class:`EntityEquipment`
      :async:


   .. py:method:: getExhaustion(self) -> float
      :async:


   .. py:method:: getExp(self) -> float
      :async:


   .. py:method:: getExpToLevel(self) -> int
      :async:


   .. py:method:: getEyeHeight

       .. py:method:: getEyeHeight(self) -> float
          :async:
          :noindex:

       .. py:method:: getEyeHeight(self, _0:boolean) -> float
          :async:
          :noindex:


   .. py:method:: getEyeLocation(self) -> :py:class:`Location`
      :async:


   .. py:method:: getFacing(self) -> :py:class:`BlockFace`
      :async:


   .. py:method:: getFallDamageSound(self, _0:int) -> :py:class:`Sound`
      :async:


   .. py:method:: getFallDamageSoundBig(self) -> :py:class:`Sound`
      :async:


   .. py:method:: getFallDamageSoundSmall(self) -> :py:class:`Sound`
      :async:


   .. py:method:: getFallDistance(self) -> float
      :async:


   .. py:method:: getFireTicks(self) -> int
      :async:


   .. py:method:: getFirstPlayed(self) -> :py:class:`long`
      :async:


   .. py:method:: getFishHook(self) -> :py:class:`FishHook`
      :async:


   .. py:method:: getFlySpeed(self) -> float
      :async:


   .. py:method:: getFoodLevel(self) -> int
      :async:


   .. py:method:: getFreezeTicks(self) -> int
      :async:


   .. py:method:: getFrictionState(self) -> :py:class:`TriState`
      :async:


   .. py:method:: getGameMode(self) -> :py:class:`GameMode`
      :async:


   .. py:method:: getHandRaised(self) -> :py:class:`EquipmentSlot`
      :async:


   .. py:method:: getHandRaisedTime(self) -> int
      :async:


   .. py:method:: getHealth(self) -> float
      :async:


   .. py:method:: getHealthScale(self) -> float
      :async:


   .. py:method:: getHeight(self) -> float
      :async:


   .. py:method:: getHurtDirection(self) -> float
      :async:


   .. py:method:: getHurtSound(self) -> :py:class:`Sound`
      :async:


   .. py:method:: getInventory

       .. py:method:: getInventory(self) -> :py:class:`Inventory`
          :async:
          :noindex:

       .. py:method:: getInventory(self) -> :py:class:`PlayerInventory`
          :async:
          :noindex:


   .. py:method:: getItemInHand(self) -> :py:class:`ItemStack`
      :async:


   .. py:method:: getItemInUse(self) -> :py:class:`ItemStack`
      :async:


   .. py:method:: getItemOnCursor(self) -> :py:class:`ItemStack`
      :async:


   .. py:method:: getItemUseRemainingTime(self) -> int
      :async:


   .. py:method:: getKiller(self) -> :py:class:`Player`
      :async:


   .. py:method:: getLastDamage(self) -> float
      :async:


   .. py:method:: getLastDamageCause(self) -> :py:class:`EntityDamageEvent`
      :async:


   .. py:method:: getLastDeathLocation

       .. py:method:: getLastDeathLocation(self) -> :py:class:`Location`
          :async:
          :noindex:

       .. py:method:: getLastDeathLocation(self) -> :py:class:`Location`
          :async:
          :noindex:


   .. py:method:: getLastLogin(self) -> :py:class:`long`
      :async:


   .. py:method:: getLastPlayed(self) -> :py:class:`long`
      :async:


   .. py:method:: getLastSeen(self) -> :py:class:`long`
      :async:


   .. py:method:: getLastTwoTargetBlocks(self, _0:Set, _1:int) -> typing.List[:py:class:`Block`]
      :async:


   .. py:method:: getLeashHolder(self) -> :py:class:`Entity`
      :async:


   .. py:method:: getLevel(self) -> int
      :async:


   .. py:method:: getLineOfSight(self, _0:Set, _1:int) -> typing.List[:py:class:`Block`]
      :async:


   .. py:method:: getListeningPluginChannels(self) -> typing.List[str]
      :async:


   .. py:method:: getLocale(self) -> str
      :async:


   .. py:method:: getLocation

       .. py:method:: getLocation(self) -> :py:class:`Location`
          :async:
          :noindex:

       .. py:method:: getLocation(self, _0:Location) -> :py:class:`Location`
          :async:
          :noindex:


   .. py:method:: getMainHand(self) -> :py:class:`MainHand`
      :async:


   .. py:method:: getMaxFireTicks(self) -> int
      :async:


   .. py:method:: getMaxFreezeTicks(self) -> int
      :async:


   .. py:method:: getMaxHealth(self) -> float
      :async:


   .. py:method:: getMaximumAir(self) -> int
      :async:


   .. py:method:: getMaximumNoDamageTicks(self) -> int
      :async:


   .. py:method:: getMemory(self, _0:MemoryKey) -> :py:class:`Object`
      :async:


   .. py:method:: getMetadata(self, _0:String) -> typing.List[:py:class:`MetadataValue`]
      :async:


   .. py:method:: getName(self) -> str
      :async:


   .. py:method:: getNearbyEntities(self, _0:double, _1:double, _2:double) -> typing.List[:py:class:`Entity`]
      :async:


   .. py:method:: getNoDamageTicks(self) -> int
      :async:


   .. py:method:: getNoTickViewDistance(self) -> int
      :async:


   .. py:method:: getOpenInventory(self) -> :py:class:`InventoryView`
      :async:


   .. py:method:: getOrDefault(self, _0:Pointer, _1:Object) -> :py:class:`Object`
      :async:


   .. py:method:: getOrDefaultFrom(self, _0:Pointer, _1:Supplier) -> :py:class:`Object`
      :async:


   .. py:method:: getOrigin(self) -> :py:class:`Location`
      :async:


   .. py:method:: getPassenger(self) -> :py:class:`Entity`
      :async:


   .. py:method:: getPassengers(self) -> typing.List[:py:class:`Entity`]
      :async:


   .. py:method:: getPersistentDataContainer(self) -> :py:class:`PersistentDataContainer`
      :async:


   .. py:method:: getPing(self) -> int
      :async:


   .. py:method:: getPistonMoveReaction(self) -> :py:class:`PistonMoveReaction`
      :async:


   .. py:method:: getPlayer(self) -> :py:class:`Player`
      :async:


   .. py:method:: getPlayerListFooter(self) -> str
      :async:


   .. py:method:: getPlayerListHeader(self) -> str
      :async:


   .. py:method:: getPlayerListName(self) -> str
      :async:


   .. py:method:: getPlayerProfile(self) -> :py:class:`PlayerProfile`
      :async:


   .. py:method:: getPlayerTime(self) -> :py:class:`long`
      :async:


   .. py:method:: getPlayerTimeOffset(self) -> :py:class:`long`
      :async:


   .. py:method:: getPlayerWeather(self) -> :py:class:`WeatherType`
      :async:


   .. py:method:: getPortalCooldown(self) -> int
      :async:


   .. py:method:: getPose(self) -> :py:class:`Pose`
      :async:


   .. py:method:: getPotentialBedLocation(self) -> :py:class:`Location`
      :async:


   .. py:method:: getPotionEffect(self, _0:PotionEffectType) -> :py:class:`PotionEffect`
      :async:


   .. py:method:: getPreviousGameMode(self) -> :py:class:`GameMode`
      :async:


   .. py:method:: getProtocolVersion(self) -> int
      :async:


   .. py:method:: getRemainingAir(self) -> int
      :async:


   .. py:method:: getRemoveWhenFarAway(self) -> bool
      :async:


   .. py:method:: getResourcePackHash(self) -> str
      :async:


   .. py:method:: getResourcePackStatus(self) -> :py:class:`Status`
      :async:


   .. py:method:: getSaturatedRegenRate(self) -> int
      :async:


   .. py:method:: getSaturation(self) -> float
      :async:


   .. py:method:: getScoreboard(self) -> :py:class:`Scoreboard`
      :async:


   .. py:method:: getScoreboardTags(self) -> typing.List[str]
      :async:


   .. py:method:: getSendViewDistance(self) -> int
      :async:


   .. py:method:: getServer(self) -> :py:class:`Server`
      :async:


   .. py:method:: getShieldBlockingDelay(self) -> int
      :async:


   .. py:method:: getShoulderEntityLeft(self) -> :py:class:`Entity`
      :async:


   .. py:method:: getShoulderEntityRight(self) -> :py:class:`Entity`
      :async:


   .. py:method:: getSimulationDistance(self) -> int
      :async:


   .. py:method:: getSleepTicks(self) -> int
      :async:


   .. py:method:: getSpawnCategory(self) -> :py:class:`SpawnCategory`
      :async:


   .. py:method:: getSpectatorTarget(self) -> :py:class:`Entity`
      :async:


   .. py:method:: getStarvationRate(self) -> int
      :async:


   .. py:method:: getStatistic

       .. py:method:: getStatistic(self, _0:Statistic) -> int
          :async:
          :noindex:

       .. py:method:: getStatistic(self, _0:Statistic, _1:Material) -> int
          :async:
          :noindex:

       .. py:method:: getStatistic(self, _0:Statistic, _1:EntityType) -> int
          :async:
          :noindex:


   .. py:method:: getSwimHighSpeedSplashSound(self) -> :py:class:`Sound`
      :async:


   .. py:method:: getSwimSound(self) -> :py:class:`Sound`
      :async:


   .. py:method:: getSwimSplashSound(self) -> :py:class:`Sound`
      :async:


   .. py:method:: getTargetBlock

       .. py:method:: getTargetBlock(self, _0:int) -> :py:class:`Block`
          :async:
          :noindex:

       .. py:method:: getTargetBlock(self, _0:int, _1:FluidMode) -> :py:class:`Block`
          :async:
          :noindex:

       .. py:method:: getTargetBlock(self, _0:Set, _1:int) -> :py:class:`Block`
          :async:
          :noindex:


   .. py:method:: getTargetBlockExact

       .. py:method:: getTargetBlockExact(self, _0:int) -> :py:class:`Block`
          :async:
          :noindex:

       .. py:method:: getTargetBlockExact(self, _0:int, _1:FluidCollisionMode) -> :py:class:`Block`
          :async:
          :noindex:


   .. py:method:: getTargetBlockFace

       .. py:method:: getTargetBlockFace(self, _0:int) -> :py:class:`BlockFace`
          :async:
          :noindex:

       .. py:method:: getTargetBlockFace(self, _0:int, _1:FluidMode) -> :py:class:`BlockFace`
          :async:
          :noindex:

       .. py:method:: getTargetBlockFace(self, _0:int, _1:FluidCollisionMode) -> :py:class:`BlockFace`
          :async:
          :noindex:


   .. py:method:: getTargetBlockInfo

       .. py:method:: getTargetBlockInfo(self, _0:int) -> :py:class:`TargetBlockInfo`
          :async:
          :noindex:

       .. py:method:: getTargetBlockInfo(self, _0:int, _1:FluidMode) -> :py:class:`TargetBlockInfo`
          :async:
          :noindex:


   .. py:method:: getTargetEntity

       .. py:method:: getTargetEntity(self, _0:int) -> :py:class:`Entity`
          :async:
          :noindex:

       .. py:method:: getTargetEntity(self, _0:int, _1:boolean) -> :py:class:`Entity`
          :async:
          :noindex:


   .. py:method:: getTargetEntityInfo

       .. py:method:: getTargetEntityInfo(self, _0:int) -> :py:class:`TargetEntityInfo`
          :async:
          :noindex:

       .. py:method:: getTargetEntityInfo(self, _0:int, _1:boolean) -> :py:class:`TargetEntityInfo`
          :async:
          :noindex:


   .. py:method:: getTicksLived(self) -> int
      :async:


   .. py:method:: getTotalExperience(self) -> int
      :async:


   .. py:method:: getTrackedPlayers(self) -> typing.List[:py:class:`Player`]
      :async:


   .. py:method:: getType(self) -> :py:class:`EntityType`
      :async:


   .. py:method:: getUniqueId

       .. py:method:: getUniqueId(self) -> uuid.UUID
          :async:
          :noindex:

       .. py:method:: getUniqueId(self) -> uuid.UUID
          :async:
          :noindex:


   .. py:method:: getUnsaturatedRegenRate(self) -> int
      :async:


   .. py:method:: getVehicle(self) -> :py:class:`Entity`
      :async:


   .. py:method:: getVelocity(self) -> :py:class:`Vector`
      :async:


   .. py:method:: getViewDistance(self) -> int
      :async:


   .. py:method:: getVirtualHost(self) -> :py:class:`InetSocketAddress`
      :async:


   .. py:method:: getWalkSpeed(self) -> float
      :async:


   .. py:method:: getWardenTimeSinceLastWarning(self) -> int
      :async:


   .. py:method:: getWardenWarningCooldown(self) -> int
      :async:


   .. py:method:: getWardenWarningLevel(self) -> int
      :async:


   .. py:method:: getWidth(self) -> float
      :async:


   .. py:method:: getWorld(self) -> :py:class:`World`
      :async:


   .. py:method:: getWorldBorder(self) -> :py:class:`WorldBorder`
      :async:


   .. py:method:: get_key(self)
      

      Return our unique key for lookup on the server (uuid)


   .. py:method:: giveExp

       .. py:method:: giveExp(self, _0:int) -> None
          :async:
          :noindex:

       .. py:method:: giveExp(self, _0:int, _1:boolean) -> None
          :async:
          :noindex:


   .. py:method:: giveExpLevels(self, _0:int) -> None
      :async:


   .. py:method:: hasAI(self) -> bool
      :async:


   .. py:method:: hasCooldown(self, _0:Material) -> bool
      :async:


   .. py:method:: hasDiscoveredRecipe(self, _0:NamespacedKey) -> bool
      :async:


   .. py:method:: hasFlyingFallDamage(self) -> :py:class:`TriState`
      :async:


   .. py:method:: hasGravity(self) -> bool
      :async:


   .. py:method:: hasLineOfSight

       .. py:method:: hasLineOfSight(self, _0:Location) -> bool
          :async:
          :noindex:

       .. py:method:: hasLineOfSight(self, _0:Entity) -> bool
          :async:
          :noindex:


   .. py:method:: hasMetadata(self, _0:String) -> bool
      :async:


   .. py:method:: hasPermission

       .. py:method:: hasPermission(self, _0:Permission) -> bool
          :async:
          :noindex:

       .. py:method:: hasPermission(self, _0:String) -> bool
          :async:
          :noindex:


   .. py:method:: hasPlayedBefore(self) -> bool
      :async:


   .. py:method:: hasPotionEffect(self, _0:PotionEffectType) -> bool
      :async:


   .. py:method:: hasResourcePack(self) -> bool
      :async:


   .. py:method:: hasSeenWinScreen(self) -> bool
      :async:


   .. py:method:: hideBossBar(self, _0:BossBar) -> None
      :async:


   .. py:method:: hideEntity(self, _0:Plugin, _1:Entity) -> None
      :async:


   .. py:method:: hidePlayer

       .. py:method:: hidePlayer(self, _0:Player) -> None
          :async:
          :noindex:

       .. py:method:: hidePlayer(self, _0:Plugin, _1:Player) -> None
          :async:
          :noindex:


   .. py:method:: hideTitle(self) -> None
      :async:


   .. py:method:: identity(self) -> :py:class:`Identity`
      :async:


   .. py:method:: increaseWardenWarningLevel(self) -> None
      :async:


   .. py:method:: incrementStatistic

       .. py:method:: incrementStatistic(self, _0:Statistic) -> None
          :async:
          :noindex:

       .. py:method:: incrementStatistic(self, _0:Statistic, _1:Material) -> None
          :async:
          :noindex:

       .. py:method:: incrementStatistic(self, _0:Statistic, _1:EntityType) -> None
          :async:
          :noindex:

       .. py:method:: incrementStatistic(self, _0:Statistic, _1:int) -> None
          :async:
          :noindex:

       .. py:method:: incrementStatistic(self, _0:Statistic, _1:Material, _2:int) -> None
          :async:
          :noindex:

       .. py:method:: incrementStatistic(self, _0:Statistic, _1:EntityType, _2:int) -> None
          :async:
          :noindex:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isAllowingServerListings(self) -> bool
      :async:


   .. py:method:: isBanned(self) -> bool
      :async:


   .. py:method:: isBlocking(self) -> bool
      :async:


   .. py:method:: isClimbing(self) -> bool
      :async:


   .. py:method:: isCollidable(self) -> bool
      :async:


   .. py:method:: isConversing(self) -> bool
      :async:


   .. py:method:: isCustomNameVisible(self) -> bool
      :async:


   .. py:method:: isDead(self) -> bool
      :async:


   .. py:method:: isDeeplySleeping(self) -> bool
      :async:


   .. py:method:: isEmpty(self) -> bool
      :async:


   .. py:method:: isFlying(self) -> bool
      :async:


   .. py:method:: isFreezeTickingLocked(self) -> bool
      :async:


   .. py:method:: isFrozen(self) -> bool
      :async:


   .. py:method:: isGliding(self) -> bool
      :async:


   .. py:method:: isGlowing(self) -> bool
      :async:


   .. py:method:: isHandRaised(self) -> bool
      :async:


   .. py:method:: isHealthScaled(self) -> bool
      :async:


   .. py:method:: isInBubbleColumn(self) -> bool
      :async:


   .. py:method:: isInLava(self) -> bool
      :async:


   .. py:method:: isInPowderedSnow(self) -> bool
      :async:


   .. py:method:: isInRain(self) -> bool
      :async:


   .. py:method:: isInWater(self) -> bool
      :async:


   .. py:method:: isInWaterOrBubbleColumn(self) -> bool
      :async:


   .. py:method:: isInWaterOrRain(self) -> bool
      :async:


   .. py:method:: isInWaterOrRainOrBubbleColumn(self) -> bool
      :async:


   .. py:method:: isInsideVehicle(self) -> bool
      :async:


   .. py:method:: isInvisible(self) -> bool
      :async:


   .. py:method:: isInvulnerable(self) -> bool
      :async:


   .. py:method:: isJumping(self) -> bool
      :async:


   .. py:method:: isLeashed(self) -> bool
      :async:


   .. py:method:: isOnGround(self) -> bool
      :async:


   .. py:method:: isOnline(self) -> bool
      :async:


   .. py:method:: isOp(self) -> bool
      :async:


   .. py:method:: isPermissionSet

       .. py:method:: isPermissionSet(self, _0:String) -> bool
          :async:
          :noindex:

       .. py:method:: isPermissionSet(self, _0:Permission) -> bool
          :async:
          :noindex:


   .. py:method:: isPersistent(self) -> bool
      :async:


   .. py:method:: isPlayerTimeRelative(self) -> bool
      :async:


   .. py:method:: isRiptiding(self) -> bool
      :async:


   .. py:method:: isSilent(self) -> bool
      :async:


   .. py:method:: isSleeping(self) -> bool
      :async:


   .. py:method:: isSleepingIgnored(self) -> bool
      :async:


   .. py:method:: isSneaking(self) -> bool
      :async:


   .. py:method:: isSprinting(self) -> bool
      :async:


   .. py:method:: isSwimming(self) -> bool
      :async:


   .. py:method:: isTicking(self) -> bool
      :async:


   .. py:method:: isUnderWater(self) -> bool
      :async:


   .. py:method:: isValid(self) -> bool
      :async:


   .. py:method:: isVisibleByDefault(self) -> bool
      :async:


   .. py:method:: isVisualFire(self) -> bool
      :async:


   .. py:method:: isWhitelisted(self) -> bool
      :async:


   .. py:method:: kick

       .. py:method:: kick(self) -> None
          :async:
          :noindex:

       .. py:method:: kick(self, _0:Component) -> None
          :async:
          :noindex:

       .. py:method:: kick(self, _0:Component, _1:Cause) -> None
          :async:
          :noindex:


   .. py:method:: kickPlayer(self, _0:String) -> None
      :async:


   .. py:method:: knockback(self, _0:double, _1:double, _2:double) -> None
      :async:


   .. py:method:: launchProjectile

       .. py:method:: launchProjectile(self, _0:Class) -> :py:class:`Projectile`
          :async:
          :noindex:

       .. py:method:: launchProjectile(self, _0:Class, _1:Vector) -> :py:class:`Projectile`
          :async:
          :noindex:

       .. py:method:: launchProjectile(self, _0:Class, _1:Vector, _2:Consumer) -> :py:class:`Projectile`
          :async:
          :noindex:


   .. py:method:: leaveVehicle(self) -> bool
      :async:


   .. py:method:: loadData(self) -> None
      :async:


   .. py:method:: locale(self) -> :py:class:`Locale`
      :async:


   .. py:method:: lockFreezeTicks(self, _0:boolean) -> None
      :async:


   .. py:method:: lookAt

       .. py:method:: lookAt(self, _0:Position, _1:LookAnchor) -> None
          :async:
          :noindex:

       .. py:method:: lookAt(self, _0:Entity, _1:LookAnchor, _2:LookAnchor) -> None
          :async:
          :noindex:

       .. py:method:: lookAt(self, _0:double, _1:double, _2:double, _3:LookAnchor) -> None
          :async:
          :noindex:


   .. py:method:: name(self) -> :py:class:`Component`
      :async:


   .. py:method:: openAnvil(self, _0:Location, _1:boolean) -> :py:class:`InventoryView`
      :async:


   .. py:method:: openBook

       .. py:method:: openBook(self, _0:ItemStack) -> None
          :async:
          :noindex:

       .. py:method:: openBook(self, _0:Book) -> None
          :async:
          :noindex:

       .. py:method:: openBook(self, _0:Builder) -> None
          :async:
          :noindex:


   .. py:method:: openCartographyTable(self, _0:Location, _1:boolean) -> :py:class:`InventoryView`
      :async:


   .. py:method:: openEnchanting(self, _0:Location, _1:boolean) -> :py:class:`InventoryView`
      :async:


   .. py:method:: openGrindstone(self, _0:Location, _1:boolean) -> :py:class:`InventoryView`
      :async:


   .. py:method:: openInventory

       .. py:method:: openInventory(self, _0:InventoryView) -> None
          :async:
          :noindex:

       .. py:method:: openInventory(self, _0:Inventory) -> :py:class:`InventoryView`
          :async:
          :noindex:


   .. py:method:: openLoom(self, _0:Location, _1:boolean) -> :py:class:`InventoryView`
      :async:


   .. py:method:: openMerchant

       .. py:method:: openMerchant(self, _0:Merchant, _1:boolean) -> :py:class:`InventoryView`
          :async:
          :noindex:

       .. py:method:: openMerchant(self, _0:Villager, _1:boolean) -> :py:class:`InventoryView`
          :async:
          :noindex:


   .. py:method:: openSign(self, _0:Sign) -> None
      :async:


   .. py:method:: openSmithingTable(self, _0:Location, _1:boolean) -> :py:class:`InventoryView`
      :async:


   .. py:method:: openStonecutter(self, _0:Location, _1:boolean) -> :py:class:`InventoryView`
      :async:


   .. py:method:: openWorkbench(self, _0:Location, _1:boolean) -> :py:class:`InventoryView`
      :async:


   .. py:method:: performCommand(self, _0:String) -> bool
      :async:


   .. py:method:: permissionValue

       .. py:method:: permissionValue(self, _0:Permission) -> :py:class:`TriState`
          :async:
          :noindex:

       .. py:method:: permissionValue(self, _0:String) -> :py:class:`TriState`
          :async:
          :noindex:


   .. py:method:: playEffect

       .. py:method:: playEffect(self, _0:EntityEffect) -> None
          :async:
          :noindex:

       .. py:method:: playEffect(self, _0:Location, _1:Effect, _2:Object) -> None
          :async:
          :noindex:

       .. py:method:: playEffect(self, _0:Location, _1:Effect, _2:int) -> None
          :async:
          :noindex:


   .. py:method:: playNote

       .. py:method:: playNote(self, _0:Location, _1:byte, _2:byte) -> None
          :async:
          :noindex:

       .. py:method:: playNote(self, _0:Location, _1:Instrument, _2:Note) -> None
          :async:
          :noindex:


   .. py:method:: playPickupItemAnimation

       .. py:method:: playPickupItemAnimation(self, _0:Item) -> None
          :async:
          :noindex:

       .. py:method:: playPickupItemAnimation(self, _0:Item, _1:int) -> None
          :async:
          :noindex:


   .. py:method:: playSound

       .. py:method:: playSound(self, _0:Sound) -> None
          :async:
          :noindex:

       .. py:method:: playSound(self, _0:Sound, _1:Emitter) -> None
          :async:
          :noindex:

       .. py:method:: playSound(self, _0:Location, _1:String, _2:float, _3:float) -> None
          :async:
          :noindex:

       .. py:method:: playSound(self, _0:Location, _1:Sound, _2:float, _3:float) -> None
          :async:
          :noindex:

       .. py:method:: playSound(self, _0:Entity, _1:String, _2:float, _3:float) -> None
          :async:
          :noindex:

       .. py:method:: playSound(self, _0:Entity, _1:Sound, _2:float, _3:float) -> None
          :async:
          :noindex:

       .. py:method:: playSound(self, _0:Sound, _1:double, _2:double, _3:double) -> None
          :async:
          :noindex:

       .. py:method:: playSound(self, _0:Location, _1:String, _2:SoundCategory, _3:float, _4:float) -> None
          :async:
          :noindex:

       .. py:method:: playSound(self, _0:Location, _1:Sound, _2:SoundCategory, _3:float, _4:float) -> None
          :async:
          :noindex:

       .. py:method:: playSound(self, _0:Entity, _1:String, _2:SoundCategory, _3:float, _4:float) -> None
          :async:
          :noindex:

       .. py:method:: playSound(self, _0:Entity, _1:Sound, _2:SoundCategory, _3:float, _4:float) -> None
          :async:
          :noindex:


   .. py:method:: playerListFooter(self) -> :py:class:`Component`
      :async:


   .. py:method:: playerListHeader(self) -> :py:class:`Component`
      :async:


   .. py:method:: playerListName

       .. py:method:: playerListName(self) -> :py:class:`Component`
          :async:
          :noindex:

       .. py:method:: playerListName(self, _0:Component) -> None
          :async:
          :noindex:


   .. py:method:: pointers(self) -> :py:class:`Pointers`
      :async:


   .. py:method:: rayTraceBlocks

       .. py:method:: rayTraceBlocks(self, _0:double) -> :py:class:`RayTraceResult`
          :async:
          :noindex:

       .. py:method:: rayTraceBlocks(self, _0:double, _1:FluidCollisionMode) -> :py:class:`RayTraceResult`
          :async:
          :noindex:


   .. py:method:: rayTraceEntities

       .. py:method:: rayTraceEntities(self, _0:int) -> :py:class:`RayTraceResult`
          :async:
          :noindex:

       .. py:method:: rayTraceEntities(self, _0:int, _1:boolean) -> :py:class:`RayTraceResult`
          :async:
          :noindex:


   .. py:method:: recalculatePermissions(self) -> None
      :async:


   .. py:method:: registerAttribute(self, _0:Attribute) -> None
      :async:


   .. py:method:: releaseLeftShoulderEntity(self) -> :py:class:`Entity`
      :async:


   .. py:method:: releaseRightShoulderEntity(self) -> :py:class:`Entity`
      :async:


   .. py:method:: remove(self) -> None
      :async:


   .. py:method:: removeAdditionalChatCompletions(self, _0:Collection) -> None
      :async:


   .. py:method:: removeAttachment(self, _0:PermissionAttachment) -> None
      :async:


   .. py:method:: removeCustomChatCompletions(self, _0:Collection) -> None
      :async:


   .. py:method:: removeMetadata(self, _0:String, _1:Plugin) -> None
      :async:


   .. py:method:: removePassenger(self, _0:Entity) -> bool
      :async:


   .. py:method:: removePotionEffect(self, _0:PotionEffectType) -> None
      :async:


   .. py:method:: removeScoreboardTag(self, _0:String) -> bool
      :async:


   .. py:method:: resetCooldown(self) -> None
      :async:


   .. py:method:: resetMaxHealth(self) -> None
      :async:


   .. py:method:: resetPlayerTime(self) -> None
      :async:


   .. py:method:: resetPlayerWeather(self) -> None
      :async:


   .. py:method:: resetTitle(self) -> None
      :async:


   .. py:method:: saveData(self) -> None
      :async:


   .. py:method:: sendActionBar

       .. py:method:: sendActionBar(self, _0:String) -> None
          :async:
          :noindex:

       .. py:method:: sendActionBar(self, _0:BaseComponent[]) -> None
          :async:
          :noindex:

       .. py:method:: sendActionBar(self, _0:Component) -> None
          :async:
          :noindex:

       .. py:method:: sendActionBar(self, _0:ComponentLike) -> None
          :async:
          :noindex:

       .. py:method:: sendActionBar(self, _0:char, _1:String) -> None
          :async:
          :noindex:


   .. py:method:: sendBlockChange

       .. py:method:: sendBlockChange(self, _0:Location, _1:BlockData) -> None
          :async:
          :noindex:

       .. py:method:: sendBlockChange(self, _0:Location, _1:Material, _2:byte) -> None
          :async:
          :noindex:


   .. py:method:: sendBlockChanges(self, _0:Collection, _1:boolean) -> None
      :async:


   .. py:method:: sendBlockDamage

       .. py:method:: sendBlockDamage(self, _0:Location, _1:float) -> None
          :async:
          :noindex:

       .. py:method:: sendBlockDamage(self, _0:Location, _1:float, _2:int) -> None
          :async:
          :noindex:


   .. py:method:: sendEquipmentChange

       .. py:method:: sendEquipmentChange(self, _0:LivingEntity, _1:Map) -> None
          :async:
          :noindex:

       .. py:method:: sendEquipmentChange(self, _0:LivingEntity, _1:EquipmentSlot, _2:ItemStack) -> None
          :async:
          :noindex:


   .. py:method:: sendExperienceChange

       .. py:method:: sendExperienceChange(self, _0:float) -> None
          :async:
          :noindex:

       .. py:method:: sendExperienceChange(self, _0:float, _1:int) -> None
          :async:
          :noindex:


   .. py:method:: sendHealthUpdate

       .. py:method:: sendHealthUpdate(self) -> None
          :async:
          :noindex:

       .. py:method:: sendHealthUpdate(self, _0:double, _1:int, _2:float) -> None
          :async:
          :noindex:


   .. py:method:: sendMap(self, _0:MapView) -> None
      :async:


   .. py:method:: sendMessage

       .. py:method:: sendMessage(self, _0:BaseComponent) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:BaseComponent[]) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:String[]) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:String) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:Component) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:ComponentLike) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:ChatMessageType, _1:BaseComponent[]) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:UUID, _1:String) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:UUID, _1:String[]) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:Identity, _1:Component) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:SignedMessage, _1:Bound) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:ComponentLike, _1:Bound) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:Component, _1:Bound) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:Component, _1:MessageType) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:ComponentLike, _1:MessageType) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:Identified, _1:Component) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:Identity, _1:ComponentLike) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:Identified, _1:ComponentLike) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:Identity, _1:Component, _2:MessageType) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:Identified, _1:Component, _2:MessageType) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:Identity, _1:ComponentLike, _2:MessageType) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:Identified, _1:ComponentLike, _2:MessageType) -> None
          :async:
          :noindex:


   .. py:method:: sendMultiBlockChange

       .. py:method:: sendMultiBlockChange(self, _0:Map) -> None
          :async:
          :noindex:

       .. py:method:: sendMultiBlockChange(self, _0:Map, _1:boolean) -> None
          :async:
          :noindex:


   .. py:method:: sendOpLevel(self, _0:byte) -> None
      :async:


   .. py:method:: sendPlainMessage(self, _0:String) -> None
      :async:


   .. py:method:: sendPlayerListFooter

       .. py:method:: sendPlayerListFooter(self, _0:Component) -> None
          :async:
          :noindex:

       .. py:method:: sendPlayerListFooter(self, _0:ComponentLike) -> None
          :async:
          :noindex:


   .. py:method:: sendPlayerListHeader

       .. py:method:: sendPlayerListHeader(self, _0:Component) -> None
          :async:
          :noindex:

       .. py:method:: sendPlayerListHeader(self, _0:ComponentLike) -> None
          :async:
          :noindex:


   .. py:method:: sendPlayerListHeaderAndFooter

       .. py:method:: sendPlayerListHeaderAndFooter(self, _0:Component, _1:Component) -> None
          :async:
          :noindex:

       .. py:method:: sendPlayerListHeaderAndFooter(self, _0:ComponentLike, _1:ComponentLike) -> None
          :async:
          :noindex:


   .. py:method:: sendPluginMessage(self, _0:Plugin, _1:String, _2:byte[]) -> None
      :async:


   .. py:method:: sendRawMessage

       .. py:method:: sendRawMessage(self, _0:String) -> None
          :async:
          :noindex:

       .. py:method:: sendRawMessage(self, _0:UUID, _1:String) -> None
          :async:
          :noindex:


   .. py:method:: sendRichMessage(self, _0:String) -> None
      :async:


   .. py:method:: sendSignChange

       .. py:method:: sendSignChange(self, _0:Location, _1:String[]) -> None
          :async:
          :noindex:

       .. py:method:: sendSignChange(self, _0:Location, _1:List) -> None
          :async:
          :noindex:

       .. py:method:: sendSignChange(self, _0:Location, _1:String[], _2:DyeColor) -> None
          :async:
          :noindex:

       .. py:method:: sendSignChange(self, _0:Location, _1:List, _2:DyeColor) -> None
          :async:
          :noindex:

       .. py:method:: sendSignChange(self, _0:Location, _1:List, _2:boolean) -> None
          :async:
          :noindex:

       .. py:method:: sendSignChange(self, _0:Location, _1:List, _2:DyeColor, _3:boolean) -> None
          :async:
          :noindex:

       .. py:method:: sendSignChange(self, _0:Location, _1:String[], _2:DyeColor, _3:boolean) -> None
          :async:
          :noindex:


   .. py:method:: sendTitle

       .. py:method:: sendTitle(self, _0:Title) -> None
          :async:
          :noindex:

       .. py:method:: sendTitle(self, _0:String, _1:String) -> None
          :async:
          :noindex:

       .. py:method:: sendTitle(self, _0:String, _1:String, _2:int, _3:int, _4:int) -> None
          :async:
          :noindex:


   .. py:method:: sendTitlePart(self, _0:TitlePart, _1:Object) -> None
      :async:


   .. py:method:: serialize(self) -> :py:class:`Map`
      :async:


   .. py:method:: setAI(self, _0:boolean) -> None
      :async:


   .. py:method:: setAbsorptionAmount(self, _0:double) -> None
      :async:


   .. py:method:: setAffectsSpawning(self, _0:boolean) -> None
      :async:


   .. py:method:: setAllowFlight(self, _0:boolean) -> None
      :async:


   .. py:method:: setArrowCooldown(self, _0:int) -> None
      :async:


   .. py:method:: setArrowsInBody

       .. py:method:: setArrowsInBody(self, _0:int) -> None
          :async:
          :noindex:

       .. py:method:: setArrowsInBody(self, _0:int, _1:boolean) -> None
          :async:
          :noindex:


   .. py:method:: setArrowsStuck(self, _0:int) -> None
      :async:


   .. py:method:: setBedSpawnLocation

       .. py:method:: setBedSpawnLocation(self, _0:Location) -> None
          :async:
          :noindex:

       .. py:method:: setBedSpawnLocation(self, _0:Location, _1:boolean) -> None
          :async:
          :noindex:


   .. py:method:: setBeeStingerCooldown(self, _0:int) -> None
      :async:


   .. py:method:: setBeeStingersInBody(self, _0:int) -> None
      :async:


   .. py:method:: setBodyYaw(self, _0:float) -> None
      :async:


   .. py:method:: setCanPickupItems(self, _0:boolean) -> None
      :async:


   .. py:method:: setCollidable(self, _0:boolean) -> None
      :async:


   .. py:method:: setCompassTarget(self, _0:Location) -> None
      :async:


   .. py:method:: setCooldown(self, _0:Material, _1:int) -> None
      :async:


   .. py:method:: setCustomChatCompletions(self, _0:Collection) -> None
      :async:


   .. py:method:: setCustomName(self, _0:String) -> None
      :async:


   .. py:method:: setCustomNameVisible(self, _0:boolean) -> None
      :async:


   .. py:method:: setDisplayName(self, _0:String) -> None
      :async:


   .. py:method:: setEnchantmentSeed(self, _0:int) -> None
      :async:


   .. py:method:: setExhaustion(self, _0:float) -> None
      :async:


   .. py:method:: setExp(self, _0:float) -> None
      :async:


   .. py:method:: setFallDistance(self, _0:float) -> None
      :async:


   .. py:method:: setFireTicks(self, _0:int) -> None
      :async:


   .. py:method:: setFlySpeed(self, _0:float) -> None
      :async:


   .. py:method:: setFlying(self, _0:boolean) -> None
      :async:


   .. py:method:: setFlyingFallDamage(self, _0:TriState) -> None
      :async:


   .. py:method:: setFoodLevel(self, _0:int) -> None
      :async:


   .. py:method:: setFreezeTicks(self, _0:int) -> None
      :async:


   .. py:method:: setFrictionState(self, _0:TriState) -> None
      :async:


   .. py:method:: setGameMode(self, _0:GameMode) -> None
      :async:


   .. py:method:: setGliding(self, _0:boolean) -> None
      :async:


   .. py:method:: setGlowing(self, _0:boolean) -> None
      :async:


   .. py:method:: setGravity(self, _0:boolean) -> None
      :async:


   .. py:method:: setHasSeenWinScreen(self, _0:boolean) -> None
      :async:


   .. py:method:: setHealth(self, _0:double) -> None
      :async:


   .. py:method:: setHealthScale(self, _0:double) -> None
      :async:


   .. py:method:: setHealthScaled(self, _0:boolean) -> None
      :async:


   .. py:method:: setHurtDirection(self, _0:float) -> None
      :async:


   .. py:method:: setInvisible(self, _0:boolean) -> None
      :async:


   .. py:method:: setInvulnerable(self, _0:boolean) -> None
      :async:


   .. py:method:: setItemInHand(self, _0:ItemStack) -> None
      :async:


   .. py:method:: setItemOnCursor(self, _0:ItemStack) -> None
      :async:


   .. py:method:: setJumping(self, _0:boolean) -> None
      :async:


   .. py:method:: setKiller(self, _0:Player) -> None
      :async:


   .. py:method:: setLastDamage(self, _0:double) -> None
      :async:


   .. py:method:: setLastDamageCause(self, _0:EntityDamageEvent) -> None
      :async:


   .. py:method:: setLastDeathLocation(self, _0:Location) -> None
      :async:


   .. py:method:: setLeashHolder(self, _0:Entity) -> bool
      :async:


   .. py:method:: setLevel(self, _0:int) -> None
      :async:


   .. py:method:: setMaxHealth(self, _0:double) -> None
      :async:


   .. py:method:: setMaximumAir(self, _0:int) -> None
      :async:


   .. py:method:: setMaximumNoDamageTicks(self, _0:int) -> None
      :async:


   .. py:method:: setMemory(self, _0:MemoryKey, _1:Object) -> None
      :async:


   .. py:method:: setMetadata(self, _0:String, _1:MetadataValue) -> None
      :async:


   .. py:method:: setNoDamageTicks(self, _0:int) -> None
      :async:


   .. py:method:: setNoTickViewDistance(self, _0:int) -> None
      :async:


   .. py:method:: setOp(self, _0:boolean) -> None
      :async:


   .. py:method:: setPassenger(self, _0:Entity) -> bool
      :async:


   .. py:method:: setPersistent(self, _0:boolean) -> None
      :async:


   .. py:method:: setPlayerListFooter(self, _0:String) -> None
      :async:


   .. py:method:: setPlayerListHeader(self, _0:String) -> None
      :async:


   .. py:method:: setPlayerListHeaderFooter

       .. py:method:: setPlayerListHeaderFooter(self, _0:String, _1:String) -> None
          :async:
          :noindex:

       .. py:method:: setPlayerListHeaderFooter(self, _0:BaseComponent[], _1:BaseComponent[]) -> None
          :async:
          :noindex:

       .. py:method:: setPlayerListHeaderFooter(self, _0:BaseComponent, _1:BaseComponent) -> None
          :async:
          :noindex:


   .. py:method:: setPlayerListName(self, _0:String) -> None
      :async:


   .. py:method:: setPlayerProfile(self, _0:PlayerProfile) -> None
      :async:


   .. py:method:: setPlayerTime(self, _0:long, _1:boolean) -> None
      :async:


   .. py:method:: setPlayerWeather(self, _0:WeatherType) -> None
      :async:


   .. py:method:: setPortalCooldown(self, _0:int) -> None
      :async:


   .. py:method:: setRemainingAir(self, _0:int) -> None
      :async:


   .. py:method:: setRemoveWhenFarAway(self, _0:boolean) -> None
      :async:


   .. py:method:: setResourcePack

       .. py:method:: setResourcePack(self, _0:String) -> None
          :async:
          :noindex:

       .. py:method:: setResourcePack(self, _0:String, _1:byte[]) -> None
          :async:
          :noindex:

       .. py:method:: setResourcePack(self, _0:String, _1:String) -> None
          :async:
          :noindex:

       .. py:method:: setResourcePack(self, _0:String, _1:byte[], _2:String) -> None
          :async:
          :noindex:

       .. py:method:: setResourcePack(self, _0:String, _1:byte[], _2:Component) -> None
          :async:
          :noindex:

       .. py:method:: setResourcePack(self, _0:String, _1:byte[], _2:boolean) -> None
          :async:
          :noindex:

       .. py:method:: setResourcePack(self, _0:String, _1:String, _2:boolean) -> None
          :async:
          :noindex:

       .. py:method:: setResourcePack(self, _0:String, _1:byte[], _2:Component, _3:boolean) -> None
          :async:
          :noindex:

       .. py:method:: setResourcePack(self, _0:String, _1:byte[], _2:String, _3:boolean) -> None
          :async:
          :noindex:

       .. py:method:: setResourcePack(self, _0:String, _1:String, _2:boolean, _3:Component) -> None
          :async:
          :noindex:


   .. py:method:: setRotation(self, _0:float, _1:float) -> None
      :async:


   .. py:method:: setSaturatedRegenRate(self, _0:int) -> None
      :async:


   .. py:method:: setSaturation(self, _0:float) -> None
      :async:


   .. py:method:: setScoreboard(self, _0:Scoreboard) -> None
      :async:


   .. py:method:: setSendViewDistance(self, _0:int) -> None
      :async:


   .. py:method:: setShieldBlockingDelay(self, _0:int) -> None
      :async:


   .. py:method:: setShoulderEntityLeft(self, _0:Entity) -> None
      :async:


   .. py:method:: setShoulderEntityRight(self, _0:Entity) -> None
      :async:


   .. py:method:: setSilent(self, _0:boolean) -> None
      :async:


   .. py:method:: setSimulationDistance(self, _0:int) -> None
      :async:


   .. py:method:: setSleepingIgnored(self, _0:boolean) -> None
      :async:


   .. py:method:: setSneaking(self, _0:boolean) -> None
      :async:


   .. py:method:: setSpectatorTarget(self, _0:Entity) -> None
      :async:


   .. py:method:: setSprinting(self, _0:boolean) -> None
      :async:


   .. py:method:: setStarvationRate(self, _0:int) -> None
      :async:


   .. py:method:: setStatistic

       .. py:method:: setStatistic(self, _0:Statistic, _1:int) -> None
          :async:
          :noindex:

       .. py:method:: setStatistic(self, _0:Statistic, _1:EntityType, _2:int) -> None
          :async:
          :noindex:

       .. py:method:: setStatistic(self, _0:Statistic, _1:Material, _2:int) -> None
          :async:
          :noindex:


   .. py:method:: setSubtitle

       .. py:method:: setSubtitle(self, _0:BaseComponent) -> None
          :async:
          :noindex:

       .. py:method:: setSubtitle(self, _0:BaseComponent[]) -> None
          :async:
          :noindex:


   .. py:method:: setSwimming(self, _0:boolean) -> None
      :async:


   .. py:method:: setTexturePack(self, _0:String) -> None
      :async:


   .. py:method:: setTicksLived(self, _0:int) -> None
      :async:


   .. py:method:: setTitleTimes(self, _0:int, _1:int, _2:int) -> None
      :async:


   .. py:method:: setTotalExperience(self, _0:int) -> None
      :async:


   .. py:method:: setUnsaturatedRegenRate(self, _0:int) -> None
      :async:


   .. py:method:: setVelocity(self, _0:Vector) -> None
      :async:


   .. py:method:: setViewDistance(self, _0:int) -> None
      :async:


   .. py:method:: setVisibleByDefault(self, _0:boolean) -> None
      :async:


   .. py:method:: setVisualFire(self, _0:boolean) -> None
      :async:


   .. py:method:: setWalkSpeed(self, _0:float) -> None
      :async:


   .. py:method:: setWardenTimeSinceLastWarning(self, _0:int) -> None
      :async:


   .. py:method:: setWardenWarningCooldown(self, _0:int) -> None
      :async:


   .. py:method:: setWardenWarningLevel(self, _0:int) -> None
      :async:


   .. py:method:: setWhitelisted(self, _0:boolean) -> None
      :async:


   .. py:method:: setWindowProperty(self, _0:Property, _1:int) -> bool
      :async:


   .. py:method:: setWorldBorder(self, _0:WorldBorder) -> None
      :async:


   .. py:method:: set_location(self, location)
      :async:

      Set the user's position to the given location or vector


   .. py:method:: showBossBar(self, _0:BossBar) -> None
      :async:


   .. py:method:: showDemoScreen(self) -> None
      :async:


   .. py:method:: showElderGuardian

       .. py:method:: showElderGuardian(self) -> None
          :async:
          :noindex:

       .. py:method:: showElderGuardian(self, _0:boolean) -> None
          :async:
          :noindex:


   .. py:method:: showEntity(self, _0:Plugin, _1:Entity) -> None
      :async:


   .. py:method:: showPlayer

       .. py:method:: showPlayer(self, _0:Player) -> None
          :async:
          :noindex:

       .. py:method:: showPlayer(self, _0:Plugin, _1:Player) -> None
          :async:
          :noindex:


   .. py:method:: showTitle

       .. py:method:: showTitle(self, _0:BaseComponent[]) -> None
          :async:
          :noindex:

       .. py:method:: showTitle(self, _0:BaseComponent) -> None
          :async:
          :noindex:

       .. py:method:: showTitle(self, _0:Title) -> None
          :async:
          :noindex:

       .. py:method:: showTitle(self, _0:BaseComponent[], _1:BaseComponent[], _2:int, _3:int, _4:int) -> None
          :async:
          :noindex:

       .. py:method:: showTitle(self, _0:BaseComponent, _1:BaseComponent, _2:int, _3:int, _4:int) -> None
          :async:
          :noindex:


   .. py:method:: showWinScreen(self) -> None
      :async:


   .. py:method:: sleep(self, _0:Location, _1:boolean) -> bool
      :async:


   .. py:method:: spawnAt

       .. py:method:: spawnAt(self, _0:Location) -> bool
          :async:
          :noindex:

       .. py:method:: spawnAt(self, _0:Location, _1:SpawnReason) -> bool
          :async:
          :noindex:


   .. py:method:: spawnParticle

       .. py:method:: spawnParticle(self, _0:Particle, _1:Location, _2:int) -> None
          :async:
          :noindex:

       .. py:method:: spawnParticle(self, _0:Particle, _1:Location, _2:int, _3:Object) -> None
          :async:
          :noindex:

       .. py:method:: spawnParticle(self, _0:Particle, _1:double, _2:double, _3:double, _4:int) -> None
          :async:
          :noindex:

       .. py:method:: spawnParticle(self, _0:Particle, _1:double, _2:double, _3:double, _4:int, _5:Object) -> None
          :async:
          :noindex:

       .. py:method:: spawnParticle(self, _0:Particle, _1:Location, _2:int, _3:double, _4:double, _5:double) -> None
          :async:
          :noindex:

       .. py:method:: spawnParticle(self, _0:Particle, _1:Location, _2:int, _3:double, _4:double, _5:double, _6:Object) -> None
          :async:
          :noindex:

       .. py:method:: spawnParticle(self, _0:Particle, _1:Location, _2:int, _3:double, _4:double, _5:double, _6:double) -> None
          :async:
          :noindex:

       .. py:method:: spawnParticle(self, _0:Particle, _1:Location, _2:int, _3:double, _4:double, _5:double, _6:double, _7:Object) -> None
          :async:
          :noindex:

       .. py:method:: spawnParticle(self, _0:Particle, _1:double, _2:double, _3:double, _4:int, _5:double, _6:double, _7:double) -> None
          :async:
          :noindex:

       .. py:method:: spawnParticle(self, _0:Particle, _1:double, _2:double, _3:double, _4:int, _5:double, _6:double, _7:double, _8:Object) -> None
          :async:
          :noindex:

       .. py:method:: spawnParticle(self, _0:Particle, _1:double, _2:double, _3:double, _4:int, _5:double, _6:double, _7:double, _8:double) -> None
          :async:
          :noindex:

       .. py:method:: spawnParticle(self, _0:Particle, _1:double, _2:double, _3:double, _4:int, _5:double, _6:double, _7:double, _8:double, _9:Object) -> None
          :async:
          :noindex:


   .. py:method:: stopAllSounds(self) -> None
      :async:


   .. py:method:: stopSound

       .. py:method:: stopSound(self, _0:SoundCategory) -> None
          :async:
          :noindex:

       .. py:method:: stopSound(self, _0:String) -> None
          :async:
          :noindex:

       .. py:method:: stopSound(self, _0:Sound) -> None
          :async:
          :noindex:

       .. py:method:: stopSound(self, _0:SoundStop) -> None
          :async:
          :noindex:

       .. py:method:: stopSound(self, _0:Sound) -> None
          :async:
          :noindex:

       .. py:method:: stopSound(self, _0:Sound, _1:SoundCategory) -> None
          :async:
          :noindex:

       .. py:method:: stopSound(self, _0:String, _1:SoundCategory) -> None
          :async:
          :noindex:


   .. py:method:: swingHand(self, _0:EquipmentSlot) -> None
      :async:


   .. py:method:: swingMainHand(self) -> None
      :async:


   .. py:method:: swingOffHand(self) -> None
      :async:


   .. py:method:: teamDisplayName(self) -> :py:class:`Component`
      :async:


   .. py:method:: teleport

       .. py:method:: teleport(self, _0:Entity) -> bool
          :async:
          :noindex:

       .. py:method:: teleport(self, _0:Location) -> bool
          :async:
          :noindex:

       .. py:method:: teleport(self, _0:Location, _1:TeleportFlag[]) -> bool
          :async:
          :noindex:

       .. py:method:: teleport(self, _0:Entity, _1:TeleportCause) -> bool
          :async:
          :noindex:

       .. py:method:: teleport(self, _0:Location, _1:TeleportCause) -> bool
          :async:
          :noindex:

       .. py:method:: teleport(self, _0:Location, _1:TeleportCause, _2:TeleportFlag[]) -> bool
          :async:
          :noindex:


   .. py:method:: teleportAsync

       .. py:method:: teleportAsync(self, _0:Location) -> :py:class:`CompletableFuture`
          :async:
          :noindex:

       .. py:method:: teleportAsync(self, _0:Location, _1:TeleportCause) -> :py:class:`CompletableFuture`
          :async:
          :noindex:


   .. py:method:: tilt(self)
      

      Get the rise/run 1 value float telling how far the entity's gaze rises/falls per unit of run


   .. py:method:: undiscoverRecipe(self, _0:NamespacedKey) -> bool
      :async:


   .. py:method:: undiscoverRecipes(self, _0:Collection) -> int
      :async:


   .. py:method:: updateCommands(self) -> None
      :async:


   .. py:method:: updateInventory(self) -> None
      :async:


   .. py:method:: updateTitle(self, _0:Title) -> None
      :async:


   .. py:method:: wakeup(self, _0:boolean) -> None
      :async:


   .. py:method:: wouldCollideUsing(self, _0:BoundingBox) -> bool
      :async:

