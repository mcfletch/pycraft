.. currentmodule:: pycraft.server.final

WaterMob
========

Inheritance
------------
* pycraft.server.final.WaterMob
* :py:class:`pycraft.server.final.Creature`
* :py:class:`pycraft.server.final.Mob`
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
* :py:class:`pycraft.server.final.Lootable`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.entity.WaterMob <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/entity/WaterMob.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: WaterMob(self, **named)
   :canonical: pycraft.server.final.WaterMob

   A particular entity, such as a mob, or item stack on the server

   .. py:property:: direction
      Get the direction (3-value array) the entity is facing

   .. py:property:: tile_position

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


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


   .. py:method:: asHoverEvent

       .. py:method:: asHoverEvent(self) -> :py:class:`HoverEvent`
          :async:
          :noindex:

       .. py:method:: asHoverEvent(self, _0:UnaryOperator) -> :py:class:`HoverEvent`
          :async:
          :noindex:


   .. py:method:: attack(self, _0:Entity) -> None
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


   .. py:method:: clearActiveItem(self) -> None
      :async:


   .. py:method:: clearLootTable(self) -> None
      :async:


   .. py:method:: clearTitle(self) -> None
      :async:


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


   .. py:method:: deleteMessage

       .. py:method:: deleteMessage(self, _0:Signature) -> None
          :async:
          :noindex:

       .. py:method:: deleteMessage(self, _0:SignedMessage) -> None
          :async:
          :noindex:


   .. py:method:: eject(self) -> bool
      :async:


   .. py:method:: filterAudience(self, _0:Predicate) -> :py:class:`Audience`
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


   .. py:method:: getAmbientSound(self) -> :py:class:`Sound`
      :async:


   .. py:method:: getArrowCooldown(self) -> int
      :async:


   .. py:method:: getArrowsInBody(self) -> int
      :async:


   .. py:method:: getArrowsStuck(self) -> int
      :async:


   .. py:method:: getAttribute(self, _0:Attribute) -> :py:class:`AttributeInstance`
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


   .. py:method:: getCollidableExemptions(self) -> typing.List[uuid.UUID]
      :async:


   .. py:method:: getCustomName(self) -> str
      :async:


   .. py:method:: getDeathSound(self) -> :py:class:`Sound`
      :async:


   .. py:method:: getDrinkingSound(self, _0:ItemStack) -> :py:class:`Sound`
      :async:


   .. py:method:: getEatingSound(self, _0:ItemStack) -> :py:class:`Sound`
      :async:


   .. py:method:: getEffectivePermissions(self) -> typing.List[:py:class:`PermissionAttachmentInfo`]
      :async:


   .. py:method:: getEntityId(self) -> int
      :async:


   .. py:method:: getEntitySpawnReason(self) -> :py:class:`SpawnReason`
      :async:


   .. py:method:: getEquipment(self) -> :py:class:`EntityEquipment`
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


   .. py:method:: getFreezeTicks(self) -> int
      :async:


   .. py:method:: getFrictionState(self) -> :py:class:`TriState`
      :async:


   .. py:method:: getHandRaised(self) -> :py:class:`EquipmentSlot`
      :async:


   .. py:method:: getHandRaisedTime(self) -> int
      :async:


   .. py:method:: getHeadRotationSpeed(self) -> int
      :async:


   .. py:method:: getHealth(self) -> float
      :async:


   .. py:method:: getHeight(self) -> float
      :async:


   .. py:method:: getHurtDirection(self) -> float
      :async:


   .. py:method:: getHurtSound(self) -> :py:class:`Sound`
      :async:


   .. py:method:: getItemUseRemainingTime(self) -> int
      :async:


   .. py:method:: getKiller(self) -> :py:class:`Player`
      :async:


   .. py:method:: getLastDamage(self) -> float
      :async:


   .. py:method:: getLastDamageCause(self) -> :py:class:`EntityDamageEvent`
      :async:


   .. py:method:: getLastTwoTargetBlocks(self, _0:Set, _1:int) -> typing.List[:py:class:`Block`]
      :async:


   .. py:method:: getLeashHolder(self) -> :py:class:`Entity`
      :async:


   .. py:method:: getLineOfSight(self, _0:Set, _1:int) -> typing.List[:py:class:`Block`]
      :async:


   .. py:method:: getLocation

       .. py:method:: getLocation(self) -> :py:class:`Location`
          :async:
          :noindex:

       .. py:method:: getLocation(self, _0:Location) -> :py:class:`Location`
          :async:
          :noindex:


   .. py:method:: getLootTable(self) -> :py:class:`LootTable`
      :async:


   .. py:method:: getMaxFireTicks(self) -> int
      :async:


   .. py:method:: getMaxFreezeTicks(self) -> int
      :async:


   .. py:method:: getMaxHeadPitch(self) -> int
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


   .. py:method:: getPathfinder(self) -> :py:class:`Pathfinder`
      :async:


   .. py:method:: getPersistentDataContainer(self) -> :py:class:`PersistentDataContainer`
      :async:


   .. py:method:: getPistonMoveReaction(self) -> :py:class:`PistonMoveReaction`
      :async:


   .. py:method:: getPortalCooldown(self) -> int
      :async:


   .. py:method:: getPose(self) -> :py:class:`Pose`
      :async:


   .. py:method:: getPotionEffect(self, _0:PotionEffectType) -> :py:class:`PotionEffect`
      :async:


   .. py:method:: getRemainingAir(self) -> int
      :async:


   .. py:method:: getRemoveWhenFarAway(self) -> bool
      :async:


   .. py:method:: getScoreboardTags(self) -> typing.List[str]
      :async:


   .. py:method:: getSeed(self) -> :py:class:`long`
      :async:


   .. py:method:: getServer(self) -> :py:class:`Server`
      :async:


   .. py:method:: getShieldBlockingDelay(self) -> int
      :async:


   .. py:method:: getSpawnCategory(self) -> :py:class:`SpawnCategory`
      :async:


   .. py:method:: getSwimHighSpeedSplashSound(self) -> :py:class:`Sound`
      :async:


   .. py:method:: getSwimSound(self) -> :py:class:`Sound`
      :async:


   .. py:method:: getSwimSplashSound(self) -> :py:class:`Sound`
      :async:


   .. py:method:: getTarget(self) -> :py:class:`LivingEntity`
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


   .. py:method:: getTrackedPlayers(self) -> typing.List[:py:class:`Player`]
      :async:


   .. py:method:: getType(self) -> :py:class:`EntityType`
      :async:


   .. py:method:: getUniqueId(self) -> uuid.UUID
      :async:


   .. py:method:: getVehicle(self) -> :py:class:`Entity`
      :async:


   .. py:method:: getVelocity(self) -> :py:class:`Vector`
      :async:


   .. py:method:: getWidth(self) -> float
      :async:


   .. py:method:: getWorld(self) -> :py:class:`World`
      :async:


   .. py:method:: get_key(self)
      

   .. py:method:: hasAI(self) -> bool
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


   .. py:method:: hasLootTable(self) -> bool
      :async:


   .. py:method:: hasMetadata(self, _0:String) -> bool
      :async:


   .. py:method:: hasPermission

       .. py:method:: hasPermission(self, _0:Permission) -> bool
          :async:
          :noindex:

       .. py:method:: hasPermission(self, _0:String) -> bool
          :async:
          :noindex:


   .. py:method:: hasPotionEffect(self, _0:PotionEffectType) -> bool
      :async:


   .. py:method:: hideBossBar(self, _0:BossBar) -> None
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isAware(self) -> bool
      :async:


   .. py:method:: isClimbing(self) -> bool
      :async:


   .. py:method:: isCollidable(self) -> bool
      :async:


   .. py:method:: isCustomNameVisible(self) -> bool
      :async:


   .. py:method:: isDead(self) -> bool
      :async:


   .. py:method:: isEmpty(self) -> bool
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


   .. py:method:: isInBubbleColumn(self) -> bool
      :async:


   .. py:method:: isInDaylight(self) -> bool
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


   .. py:method:: isLeftHanded(self) -> bool
      :async:


   .. py:method:: isOnGround(self) -> bool
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


   .. py:method:: isRiptiding(self) -> bool
      :async:


   .. py:method:: isSilent(self) -> bool
      :async:


   .. py:method:: isSleeping(self) -> bool
      :async:


   .. py:method:: isSneaking(self) -> bool
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


   .. py:method:: lockFreezeTicks(self, _0:boolean) -> None
      :async:


   .. py:method:: lookAt

       .. py:method:: lookAt(self, _0:Entity) -> None
          :async:
          :noindex:

       .. py:method:: lookAt(self, _0:Location) -> None
          :async:
          :noindex:

       .. py:method:: lookAt(self, _0:Entity, _1:float, _2:float) -> None
          :async:
          :noindex:

       .. py:method:: lookAt(self, _0:double, _1:double, _2:double) -> None
          :async:
          :noindex:

       .. py:method:: lookAt(self, _0:Location, _1:float, _2:float) -> None
          :async:
          :noindex:

       .. py:method:: lookAt(self, _0:double, _1:double, _2:double, _3:float, _4:float) -> None
          :async:
          :noindex:


   .. py:method:: name(self) -> :py:class:`Component`
      :async:


   .. py:method:: openBook

       .. py:method:: openBook(self, _0:Book) -> None
          :async:
          :noindex:

       .. py:method:: openBook(self, _0:Builder) -> None
          :async:
          :noindex:


   .. py:method:: permissionValue

       .. py:method:: permissionValue(self, _0:Permission) -> :py:class:`TriState`
          :async:
          :noindex:

       .. py:method:: permissionValue(self, _0:String) -> :py:class:`TriState`
          :async:
          :noindex:


   .. py:method:: playEffect(self, _0:EntityEffect) -> None
      :async:


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

       .. py:method:: playSound(self, _0:Sound, _1:double, _2:double, _3:double) -> None
          :async:
          :noindex:


   .. py:method:: pointers(self) -> :py:class:`Pointers`
      :async:


   .. py:method:: position(self)
      

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


   .. py:method:: remove(self) -> None
      :async:


   .. py:method:: removeAttachment(self, _0:PermissionAttachment) -> None
      :async:


   .. py:method:: removeMetadata(self, _0:String, _1:Plugin) -> None
      :async:


   .. py:method:: removePassenger(self, _0:Entity) -> bool
      :async:


   .. py:method:: removePotionEffect(self, _0:PotionEffectType) -> None
      :async:


   .. py:method:: removeScoreboardTag(self, _0:String) -> bool
      :async:


   .. py:method:: resetMaxHealth(self) -> None
      :async:


   .. py:method:: resetTitle(self) -> None
      :async:


   .. py:method:: sendActionBar

       .. py:method:: sendActionBar(self, _0:Component) -> None
          :async:
          :noindex:

       .. py:method:: sendActionBar(self, _0:ComponentLike) -> None
          :async:
          :noindex:


   .. py:method:: sendMessage

       .. py:method:: sendMessage(self, _0:BaseComponent[]) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:BaseComponent) -> None
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


   .. py:method:: sendRichMessage(self, _0:String) -> None
      :async:


   .. py:method:: sendTitlePart(self, _0:TitlePart, _1:Object) -> None
      :async:


   .. py:method:: setAI(self, _0:boolean) -> None
      :async:


   .. py:method:: setAbsorptionAmount(self, _0:double) -> None
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


   .. py:method:: setAware(self, _0:boolean) -> None
      :async:


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


   .. py:method:: setCustomName(self, _0:String) -> None
      :async:


   .. py:method:: setCustomNameVisible(self, _0:boolean) -> None
      :async:


   .. py:method:: setFallDistance(self, _0:float) -> None
      :async:


   .. py:method:: setFireTicks(self, _0:int) -> None
      :async:


   .. py:method:: setFreezeTicks(self, _0:int) -> None
      :async:


   .. py:method:: setFrictionState(self, _0:TriState) -> None
      :async:


   .. py:method:: setGliding(self, _0:boolean) -> None
      :async:


   .. py:method:: setGlowing(self, _0:boolean) -> None
      :async:


   .. py:method:: setGravity(self, _0:boolean) -> None
      :async:


   .. py:method:: setHealth(self, _0:double) -> None
      :async:


   .. py:method:: setHurtDirection(self, _0:float) -> None
      :async:


   .. py:method:: setInvisible(self, _0:boolean) -> None
      :async:


   .. py:method:: setInvulnerable(self, _0:boolean) -> None
      :async:


   .. py:method:: setJumping(self, _0:boolean) -> None
      :async:


   .. py:method:: setKiller(self, _0:Player) -> None
      :async:


   .. py:method:: setLastDamage(self, _0:double) -> None
      :async:


   .. py:method:: setLastDamageCause(self, _0:EntityDamageEvent) -> None
      :async:


   .. py:method:: setLeashHolder(self, _0:Entity) -> bool
      :async:


   .. py:method:: setLeftHanded(self, _0:boolean) -> None
      :async:


   .. py:method:: setLootTable

       .. py:method:: setLootTable(self, _0:LootTable) -> None
          :async:
          :noindex:

       .. py:method:: setLootTable(self, _0:LootTable, _1:long) -> None
          :async:
          :noindex:


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


   .. py:method:: setOp(self, _0:boolean) -> None
      :async:


   .. py:method:: setPassenger(self, _0:Entity) -> bool
      :async:


   .. py:method:: setPersistent(self, _0:boolean) -> None
      :async:


   .. py:method:: setPortalCooldown(self, _0:int) -> None
      :async:


   .. py:method:: setRemainingAir(self, _0:int) -> None
      :async:


   .. py:method:: setRemoveWhenFarAway(self, _0:boolean) -> None
      :async:


   .. py:method:: setRotation(self, _0:float, _1:float) -> None
      :async:


   .. py:method:: setSeed(self, _0:long) -> None
      :async:


   .. py:method:: setShieldBlockingDelay(self, _0:int) -> None
      :async:


   .. py:method:: setSilent(self, _0:boolean) -> None
      :async:


   .. py:method:: setSneaking(self, _0:boolean) -> None
      :async:


   .. py:method:: setSwimming(self, _0:boolean) -> None
      :async:


   .. py:method:: setTarget(self, _0:LivingEntity) -> None
      :async:


   .. py:method:: setTicksLived(self, _0:int) -> None
      :async:


   .. py:method:: setVelocity(self, _0:Vector) -> None
      :async:


   .. py:method:: setVisibleByDefault(self, _0:boolean) -> None
      :async:


   .. py:method:: setVisualFire(self, _0:boolean) -> None
      :async:


   .. py:method:: set_location(self, location)
      :async:

      Set the user's position to the given location or vector


   .. py:method:: showBossBar(self, _0:BossBar) -> None
      :async:


   .. py:method:: showTitle(self, _0:Title) -> None
      :async:


   .. py:method:: spawnAt

       .. py:method:: spawnAt(self, _0:Location) -> bool
          :async:
          :noindex:

       .. py:method:: spawnAt(self, _0:Location, _1:SpawnReason) -> bool
          :async:
          :noindex:


   .. py:method:: stopSound

       .. py:method:: stopSound(self, _0:SoundStop) -> None
          :async:
          :noindex:

       .. py:method:: stopSound(self, _0:Sound) -> None
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


   .. py:method:: wouldCollideUsing(self, _0:BoundingBox) -> bool
      :async:

