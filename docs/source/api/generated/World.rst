.. currentmodule:: pycraft.server.final

World
=====

Inheritance
------------
* pycraft.server.final.World
* :py:class:`pycraft.server.world.World`
* :py:class:`pycraft.server.final.WorldInfo`
* :py:class:`pycraft.server.final.PluginMessageRecipient`
* :py:class:`pycraft.server.final.Metadatable`
* :py:class:`pycraft.server.final.PersistentDataHolder`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.World <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/World.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: World(self, name=None, **named)
   :canonical: pycraft.server.final.World

   A particular world on the server

   Worlds are referenced by their name, with the common worlds being:

   * 'world' -- known as the Overworld, this is the main world you start in
   * 'world_nether' -- the Nether is full of lava, magma and Piglins
   * 'world_the_end' -- the End is the boss-level for the Ender Dragon and is full of Endermen

   When referring to a world, you can use the string name of the world,
   or get a world with :py:meth:`pycraft.server.final.Server.getWorld`
   or :py:meth:`pycraft.server.final.Server.getWorlds`

   Example usage:

       server.getWorld('world')

   .. py:method:: __init__(self, name=None, **named)
      

      Initialise the world record, normally by name


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: addPluginChunkTicket(self, _0:int, _1:int, _2:Plugin) -> bool
      :async:


   .. py:method:: audiences(self) -> :py:class:`Iterable`
      :async:


   .. py:method:: breakBlocks(self, _0:World, _1:Vector, _2:Vector) -> None
      :async:


   .. py:method:: canGenerateStructures(self) -> bool
      :async:


   .. py:method:: clearTitle(self) -> None
      :async:


   .. py:method:: createExplosion

       .. py:method:: createExplosion(self, _0:Entity, _1:float) -> bool
          :async:
          :noindex:

       .. py:method:: createExplosion(self, _0:Location, _1:float) -> bool
          :async:
          :noindex:

       .. py:method:: createExplosion(self, _0:Entity, _1:Location, _2:float) -> bool
          :async:
          :noindex:

       .. py:method:: createExplosion(self, _0:Location, _1:float, _2:boolean) -> bool
          :async:
          :noindex:

       .. py:method:: createExplosion(self, _0:Entity, _1:float, _2:boolean) -> bool
          :async:
          :noindex:

       .. py:method:: createExplosion(self, _0:double, _1:double, _2:double, _3:float) -> bool
          :async:
          :noindex:

       .. py:method:: createExplosion(self, _0:Location, _1:float, _2:boolean, _3:boolean) -> bool
          :async:
          :noindex:

       .. py:method:: createExplosion(self, _0:Entity, _1:float, _2:boolean, _3:boolean) -> bool
          :async:
          :noindex:

       .. py:method:: createExplosion(self, _0:Entity, _1:Location, _2:float, _3:boolean) -> bool
          :async:
          :noindex:

       .. py:method:: createExplosion(self, _0:double, _1:double, _2:double, _3:float, _4:boolean) -> bool
          :async:
          :noindex:

       .. py:method:: createExplosion(self, _0:Location, _1:float, _2:boolean, _3:boolean, _4:Entity) -> bool
          :async:
          :noindex:

       .. py:method:: createExplosion(self, _0:Entity, _1:Location, _2:float, _3:boolean, _4:boolean) -> bool
          :async:
          :noindex:

       .. py:method:: createExplosion(self, _0:double, _1:double, _2:double, _3:float, _4:boolean, _5:boolean) -> bool
          :async:
          :noindex:

       .. py:method:: createExplosion(self, _0:double, _1:double, _2:double, _3:float, _4:boolean, _5:boolean, _6:Entity) -> bool
          :async:
          :noindex:


   .. py:method:: deleteMessage

       .. py:method:: deleteMessage(self, _0:Signature) -> None
          :async:
          :noindex:

       .. py:method:: deleteMessage(self, _0:SignedMessage) -> None
          :async:
          :noindex:


   .. py:method:: doesBedWork(self) -> bool
      :async:


   .. py:method:: doesRespawnAnchorWork(self) -> bool
      :async:


   .. py:method:: dropItem

       .. py:method:: dropItem(self, _0:Location, _1:ItemStack) -> :py:class:`Item`
          :async:
          :noindex:

       .. py:method:: dropItem(self, _0:Location, _1:ItemStack, _2:Consumer) -> :py:class:`Item`
          :async:
          :noindex:


   .. py:method:: dropItemNaturally

       .. py:method:: dropItemNaturally(self, _0:Location, _1:ItemStack) -> :py:class:`Item`
          :async:
          :noindex:

       .. py:method:: dropItemNaturally(self, _0:Location, _1:ItemStack, _2:Consumer) -> :py:class:`Item`
          :async:
          :noindex:


   .. py:method:: filterAudience(self, _0:Predicate) -> :py:class:`Audience`
      :async:


   .. py:method:: findLightningRod(self, _0:Location) -> :py:class:`Location`
      :async:


   .. py:method:: findLightningTarget(self, _0:Location) -> :py:class:`Location`
      :async:


   .. py:method:: forEachAudience(self, _0:Consumer) -> None
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: generateTree

       .. py:method:: generateTree(self, _0:Location, _1:TreeType) -> bool
          :async:
          :noindex:

       .. py:method:: generateTree(self, _0:Location, _1:TreeType, _2:BlockChangeDelegate) -> bool
          :async:
          :noindex:

       .. py:method:: generateTree(self, _0:Location, _1:Random, _2:TreeType) -> bool
          :async:
          :noindex:

       .. py:method:: generateTree(self, _0:Location, _1:Random, _2:TreeType, _3:Predicate) -> bool
          :async:
          :noindex:

       .. py:method:: generateTree(self, _0:Location, _1:Random, _2:TreeType, _3:Consumer) -> bool
          :async:
          :noindex:


   .. py:method:: get(self, _0:Pointer) -> :py:class:`Optional`
      :async:


   .. py:method:: getAllowAnimals(self) -> bool
      :async:


   .. py:method:: getAllowMonsters(self) -> bool
      :async:


   .. py:method:: getAmbientSpawnLimit(self) -> int
      :async:


   .. py:method:: getAnimalSpawnLimit(self) -> int
      :async:


   .. py:method:: getBiome

       .. py:method:: getBiome(self, _0:Location) -> :py:class:`Biome`
          :async:
          :noindex:

       .. py:method:: getBiome(self, _0:int, _1:int) -> :py:class:`Biome`
          :async:
          :noindex:

       .. py:method:: getBiome(self, _0:int, _1:int, _2:int) -> :py:class:`Biome`
          :async:
          :noindex:


   .. py:method:: getBiomeProvider(self) -> :py:class:`BiomeProvider`
      :async:


   .. py:method:: getBlockArray(self, start, end)
      :async:

      Get block array by start and end coordinates


   .. py:method:: getBlockAt

       .. py:method:: getBlockAt(self, _0:Location) -> :py:class:`Block`
          :async:
          :noindex:

       .. py:method:: getBlockAt(self, _0:int, _1:int, _2:int) -> :py:class:`Block`
          :async:
          :noindex:


   .. py:method:: getBlockAtKey(self, _0:long) -> :py:class:`Block`
      :async:


   .. py:method:: getBlockData

       .. py:method:: getBlockData(self, _0:Location) -> :py:class:`BlockData`
          :async:
          :noindex:

       .. py:method:: getBlockData(self, _0:int, _1:int, _2:int) -> :py:class:`BlockData`
          :async:
          :noindex:


   .. py:method:: getBlockState

       .. py:method:: getBlockState(self, _0:Location) -> :py:class:`BlockState`
          :async:
          :noindex:

       .. py:method:: getBlockState(self, _0:int, _1:int, _2:int) -> :py:class:`BlockState`
          :async:
          :noindex:


   .. py:method:: getBlocks(self, _0:World, _1:Vector, _2:Vector) -> typing.List[[[BlockData,BlockData,...]]]
      :async:


   .. py:method:: getChunkAt

       .. py:method:: getChunkAt(self, _0:Location) -> :py:class:`Chunk`
          :async:
          :noindex:

       .. py:method:: getChunkAt(self, _0:Block) -> :py:class:`Chunk`
          :async:
          :noindex:

       .. py:method:: getChunkAt(self, _0:long) -> :py:class:`Chunk`
          :async:
          :noindex:

       .. py:method:: getChunkAt(self, _0:int, _1:int) -> :py:class:`Chunk`
          :async:
          :noindex:


   .. py:method:: getChunkAtAsync

       .. py:method:: getChunkAtAsync(self, _0:Block) -> :py:class:`CompletableFuture`
          :async:
          :noindex:

       .. py:method:: getChunkAtAsync(self, _0:Location) -> :py:class:`CompletableFuture`
          :async:
          :noindex:

       .. py:method:: getChunkAtAsync(self, _0:Location, _1:Consumer) -> None
          :async:
          :noindex:

       .. py:method:: getChunkAtAsync(self, _0:Block, _1:Consumer) -> None
          :async:
          :noindex:

       .. py:method:: getChunkAtAsync(self, _0:Block, _1:ChunkLoadCallback) -> None
          :async:
          :noindex:

       .. py:method:: getChunkAtAsync(self, _0:Block, _1:boolean) -> :py:class:`CompletableFuture`
          :async:
          :noindex:

       .. py:method:: getChunkAtAsync(self, _0:int, _1:int) -> :py:class:`CompletableFuture`
          :async:
          :noindex:

       .. py:method:: getChunkAtAsync(self, _0:Location, _1:ChunkLoadCallback) -> None
          :async:
          :noindex:

       .. py:method:: getChunkAtAsync(self, _0:Location, _1:boolean) -> :py:class:`CompletableFuture`
          :async:
          :noindex:

       .. py:method:: getChunkAtAsync(self, _0:Location, _1:boolean, _2:Consumer) -> None
          :async:
          :noindex:

       .. py:method:: getChunkAtAsync(self, _0:Block, _1:boolean, _2:Consumer) -> None
          :async:
          :noindex:

       .. py:method:: getChunkAtAsync(self, _0:int, _1:int, _2:ChunkLoadCallback) -> None
          :async:
          :noindex:

       .. py:method:: getChunkAtAsync(self, _0:int, _1:int, _2:Consumer) -> None
          :async:
          :noindex:

       .. py:method:: getChunkAtAsync(self, _0:int, _1:int, _2:boolean) -> :py:class:`CompletableFuture`
          :async:
          :noindex:

       .. py:method:: getChunkAtAsync(self, _0:int, _1:int, _2:boolean, _3:boolean) -> :py:class:`CompletableFuture`
          :async:
          :noindex:

       .. py:method:: getChunkAtAsync(self, _0:int, _1:int, _2:boolean, _3:Consumer) -> None
          :async:
          :noindex:


   .. py:method:: getChunkAtAsyncUrgently

       .. py:method:: getChunkAtAsyncUrgently(self, _0:Block) -> :py:class:`CompletableFuture`
          :async:
          :noindex:

       .. py:method:: getChunkAtAsyncUrgently(self, _0:Location) -> :py:class:`CompletableFuture`
          :async:
          :noindex:

       .. py:method:: getChunkAtAsyncUrgently(self, _0:Location, _1:boolean) -> :py:class:`CompletableFuture`
          :async:
          :noindex:

       .. py:method:: getChunkAtAsyncUrgently(self, _0:Block, _1:boolean) -> :py:class:`CompletableFuture`
          :async:
          :noindex:

       .. py:method:: getChunkAtAsyncUrgently(self, _0:int, _1:int) -> :py:class:`CompletableFuture`
          :async:
          :noindex:


   .. py:method:: getChunkCount(self) -> int
      :async:


   .. py:method:: getClearWeatherDuration(self) -> int
      :async:


   .. py:method:: getComputedBiome(self, _0:int, _1:int, _2:int) -> :py:class:`Biome`
      :async:


   .. py:method:: getCoordinateScale(self) -> float
      :async:


   .. py:method:: getDifficulty(self) -> :py:class:`Difficulty`
      :async:


   .. py:method:: getEmptyChunkSnapshot(self, _0:int, _1:int, _2:boolean, _3:boolean) -> :py:class:`ChunkSnapshot`
      :async:


   .. py:method:: getEnderDragonBattle(self) -> :py:class:`DragonBattle`
      :async:


   .. py:method:: getEntities(self) -> typing.List[:py:class:`Entity`]
      :async:


   .. py:method:: getEntitiesByClass

       .. py:method:: getEntitiesByClass(self, _0:Class[]) -> typing.List[:py:class:`T`]
          :async:
          :noindex:

       .. py:method:: getEntitiesByClass(self, _0:Class) -> typing.List[:py:class:`T`]
          :async:
          :noindex:


   .. py:method:: getEntitiesByClasses(self, _0:Class[]) -> typing.List[:py:class:`Entity`]
      :async:


   .. py:method:: getEntity(self, _0:UUID) -> :py:class:`Entity`
      :async:


   .. py:method:: getEntityCount(self) -> int
      :async:


   .. py:method:: getEnvironment(self) -> :py:class:`Environment`
      :async:


   .. py:method:: getForceLoadedChunks(self) -> typing.List[:py:class:`Chunk`]
      :async:


   .. py:method:: getFullTime(self) -> :py:class:`long`
      :async:


   .. py:method:: getGameRuleDefault(self, _0:GameRule) -> :py:class:`Object`
      :async:


   .. py:method:: getGameRuleValue

       .. py:method:: getGameRuleValue(self, _0:GameRule) -> :py:class:`Object`
          :async:
          :noindex:

       .. py:method:: getGameRuleValue(self, _0:String) -> str
          :async:
          :noindex:


   .. py:method:: getGameRules(self) -> typing.List[str]
      :async:


   .. py:method:: getGameTime(self) -> :py:class:`long`
      :async:


   .. py:method:: getGenerator(self) -> :py:class:`ChunkGenerator`
      :async:


   .. py:method:: getHighestBlockAt

       .. py:method:: getHighestBlockAt(self, _0:Location) -> :py:class:`Block`
          :async:
          :noindex:

       .. py:method:: getHighestBlockAt(self, _0:Location, _1:HeightMap) -> :py:class:`Block`
          :async:
          :noindex:

       .. py:method:: getHighestBlockAt(self, _0:Location, _1:HeightmapType) -> :py:class:`Block`
          :async:
          :noindex:

       .. py:method:: getHighestBlockAt(self, _0:int, _1:int) -> :py:class:`Block`
          :async:
          :noindex:

       .. py:method:: getHighestBlockAt(self, _0:int, _1:int, _2:HeightMap) -> :py:class:`Block`
          :async:
          :noindex:

       .. py:method:: getHighestBlockAt(self, _0:int, _1:int, _2:HeightmapType) -> :py:class:`Block`
          :async:
          :noindex:


   .. py:method:: getHighestBlockYAt

       .. py:method:: getHighestBlockYAt(self, _0:Location) -> int
          :async:
          :noindex:

       .. py:method:: getHighestBlockYAt(self, _0:int, _1:int) -> int
          :async:
          :noindex:

       .. py:method:: getHighestBlockYAt(self, _0:Location, _1:HeightMap) -> int
          :async:
          :noindex:

       .. py:method:: getHighestBlockYAt(self, _0:Location, _1:HeightmapType) -> int
          :async:
          :noindex:

       .. py:method:: getHighestBlockYAt(self, _0:int, _1:int, _2:HeightMap) -> int
          :async:
          :noindex:

       .. py:method:: getHighestBlockYAt(self, _0:int, _1:int, _2:HeightmapType) -> int
          :async:
          :noindex:


   .. py:method:: getHumidity

       .. py:method:: getHumidity(self, _0:int, _1:int) -> float
          :async:
          :noindex:

       .. py:method:: getHumidity(self, _0:int, _1:int, _2:int) -> float
          :async:
          :noindex:


   .. py:method:: getInfiniburn(self) -> typing.List[:py:class:`Material`]
      :async:


   .. py:method:: getKeepSpawnInMemory(self) -> bool
      :async:


   .. py:method:: getKey(self) -> :py:class:`NamespacedKey`
      :async:


   .. py:method:: getListeningPluginChannels(self) -> typing.List[str]
      :async:


   .. py:method:: getLivingEntities(self) -> typing.List[:py:class:`LivingEntity`]
      :async:


   .. py:method:: getLoadedChunks(self) -> typing.List[:py:class:`Chunk`]
      :async:


   .. py:method:: getLocationAtKey(self, _0:long) -> :py:class:`Location`
      :async:


   .. py:method:: getLogicalHeight(self) -> int
      :async:


   .. py:method:: getMaxHeight(self) -> int
      :async:


   .. py:method:: getMetadata(self, _0:String) -> typing.List[:py:class:`MetadataValue`]
      :async:


   .. py:method:: getMinHeight(self) -> int
      :async:


   .. py:method:: getMonsterSpawnLimit(self) -> int
      :async:


   .. py:method:: getMoonPhase(self) -> :py:class:`MoonPhase`
      :async:


   .. py:method:: getName(self) -> str
      :async:


   .. py:method:: getNearbyEntities

       .. py:method:: getNearbyEntities(self, _0:BoundingBox) -> typing.List[:py:class:`Entity`]
          :async:
          :noindex:

       .. py:method:: getNearbyEntities(self, _0:BoundingBox, _1:Predicate) -> typing.List[:py:class:`Entity`]
          :async:
          :noindex:

       .. py:method:: getNearbyEntities(self, _0:Location, _1:double, _2:double, _3:double) -> typing.List[:py:class:`Entity`]
          :async:
          :noindex:

       .. py:method:: getNearbyEntities(self, _0:Location, _1:double, _2:double, _3:double, _4:Predicate) -> typing.List[:py:class:`Entity`]
          :async:
          :noindex:


   .. py:method:: getNearbyEntitiesByType

       .. py:method:: getNearbyEntitiesByType(self, _0:Class, _1:Location, _2:double) -> typing.List[:py:class:`T`]
          :async:
          :noindex:

       .. py:method:: getNearbyEntitiesByType(self, _0:Class, _1:Location, _2:double, _3:double) -> typing.List[:py:class:`T`]
          :async:
          :noindex:

       .. py:method:: getNearbyEntitiesByType(self, _0:Class, _1:Location, _2:double, _3:Predicate) -> typing.List[:py:class:`T`]
          :async:
          :noindex:

       .. py:method:: getNearbyEntitiesByType(self, _0:Class, _1:Location, _2:double, _3:double, _4:double) -> typing.List[:py:class:`T`]
          :async:
          :noindex:

       .. py:method:: getNearbyEntitiesByType(self, _0:Class, _1:Location, _2:double, _3:double, _4:Predicate) -> typing.List[:py:class:`T`]
          :async:
          :noindex:

       .. py:method:: getNearbyEntitiesByType(self, _0:Class, _1:Location, _2:double, _3:double, _4:double, _5:Predicate) -> typing.List[:py:class:`T`]
          :async:
          :noindex:


   .. py:method:: getNearbyLivingEntities

       .. py:method:: getNearbyLivingEntities(self, _0:Location, _1:double) -> typing.List[:py:class:`LivingEntity`]
          :async:
          :noindex:

       .. py:method:: getNearbyLivingEntities(self, _0:Location, _1:double, _2:double) -> typing.List[:py:class:`LivingEntity`]
          :async:
          :noindex:

       .. py:method:: getNearbyLivingEntities(self, _0:Location, _1:double, _2:Predicate) -> typing.List[:py:class:`LivingEntity`]
          :async:
          :noindex:

       .. py:method:: getNearbyLivingEntities(self, _0:Location, _1:double, _2:double, _3:double) -> typing.List[:py:class:`LivingEntity`]
          :async:
          :noindex:

       .. py:method:: getNearbyLivingEntities(self, _0:Location, _1:double, _2:double, _3:Predicate) -> typing.List[:py:class:`LivingEntity`]
          :async:
          :noindex:

       .. py:method:: getNearbyLivingEntities(self, _0:Location, _1:double, _2:double, _3:double, _4:Predicate) -> typing.List[:py:class:`LivingEntity`]
          :async:
          :noindex:


   .. py:method:: getNearbyPlayers

       .. py:method:: getNearbyPlayers(self, _0:Location, _1:double) -> typing.List[:py:class:`Player`]
          :async:
          :noindex:

       .. py:method:: getNearbyPlayers(self, _0:Location, _1:double, _2:double) -> typing.List[:py:class:`Player`]
          :async:
          :noindex:

       .. py:method:: getNearbyPlayers(self, _0:Location, _1:double, _2:Predicate) -> typing.List[:py:class:`Player`]
          :async:
          :noindex:

       .. py:method:: getNearbyPlayers(self, _0:Location, _1:double, _2:double, _3:double) -> typing.List[:py:class:`Player`]
          :async:
          :noindex:

       .. py:method:: getNearbyPlayers(self, _0:Location, _1:double, _2:double, _3:Predicate) -> typing.List[:py:class:`Player`]
          :async:
          :noindex:

       .. py:method:: getNearbyPlayers(self, _0:Location, _1:double, _2:double, _3:double, _4:Predicate) -> typing.List[:py:class:`Player`]
          :async:
          :noindex:


   .. py:method:: getNoTickViewDistance(self) -> int
      :async:


   .. py:method:: getOrDefault(self, _0:Pointer, _1:Object) -> :py:class:`Object`
      :async:


   .. py:method:: getOrDefaultFrom(self, _0:Pointer, _1:Supplier) -> :py:class:`Object`
      :async:


   .. py:method:: getPVP(self) -> bool
      :async:


   .. py:method:: getPersistentDataContainer(self) -> :py:class:`PersistentDataContainer`
      :async:


   .. py:method:: getPlayerCount(self) -> int
      :async:


   .. py:method:: getPlayers(self) -> typing.List[:py:class:`Player`]
      :async:


   .. py:method:: getPluginChunkTickets

       .. py:method:: getPluginChunkTickets(self) -> :py:class:`Map`
          :async:
          :noindex:

       .. py:method:: getPluginChunkTickets(self, _0:int, _1:int) -> typing.List[:py:class:`Plugin`]
          :async:
          :noindex:


   .. py:method:: getPopulators(self) -> typing.List[:py:class:`BlockPopulator`]
      :async:


   .. py:method:: getRaids(self) -> typing.List[:py:class:`Raid`]
      :async:


   .. py:method:: getSeaLevel(self) -> int
      :async:


   .. py:method:: getSeed(self) -> :py:class:`long`
      :async:


   .. py:method:: getSendViewDistance(self) -> int
      :async:


   .. py:method:: getSimulationDistance(self) -> int
      :async:


   .. py:method:: getSpawnLimit(self, _0:SpawnCategory) -> int
      :async:


   .. py:method:: getSpawnLocation(self) -> :py:class:`Location`
      :async:


   .. py:method:: getTemperature

       .. py:method:: getTemperature(self, _0:int, _1:int) -> float
          :async:
          :noindex:

       .. py:method:: getTemperature(self, _0:int, _1:int, _2:int) -> float
          :async:
          :noindex:


   .. py:method:: getThunderDuration(self) -> int
      :async:


   .. py:method:: getTickableTileEntityCount(self) -> int
      :async:


   .. py:method:: getTicksPerAmbientSpawns(self) -> :py:class:`long`
      :async:


   .. py:method:: getTicksPerAnimalSpawns(self) -> :py:class:`long`
      :async:


   .. py:method:: getTicksPerMonsterSpawns(self) -> :py:class:`long`
      :async:


   .. py:method:: getTicksPerSpawns(self, _0:SpawnCategory) -> :py:class:`long`
      :async:


   .. py:method:: getTicksPerWaterAmbientSpawns(self) -> :py:class:`long`
      :async:


   .. py:method:: getTicksPerWaterSpawns(self) -> :py:class:`long`
      :async:


   .. py:method:: getTicksPerWaterUndergroundCreatureSpawns(self) -> :py:class:`long`
      :async:


   .. py:method:: getTileEntityCount(self) -> int
      :async:


   .. py:method:: getTime(self) -> :py:class:`long`
      :async:


   .. py:method:: getType

       .. py:method:: getType(self, _0:Location) -> :py:class:`Material`
          :async:
          :noindex:

       .. py:method:: getType(self, _0:int, _1:int, _2:int) -> :py:class:`Material`
          :async:
          :noindex:


   .. py:method:: getUID(self) -> uuid.UUID
      :async:


   .. py:method:: getViewDistance(self) -> int
      :async:


   .. py:method:: getWaterAmbientSpawnLimit(self) -> int
      :async:


   .. py:method:: getWaterAnimalSpawnLimit(self) -> int
      :async:


   .. py:method:: getWaterUndergroundCreatureSpawnLimit(self) -> int
      :async:


   .. py:method:: getWeatherDuration(self) -> int
      :async:


   .. py:method:: getWorldBorder(self) -> :py:class:`WorldBorder`
      :async:


   .. py:method:: getWorldFolder(self) -> :py:class:`File`
      :async:


   .. py:method:: getWorldType(self) -> :py:class:`WorldType`
      :async:


   .. py:method:: get_key(self)
      

      Get the unique value which looks up the world (name)


   .. py:method:: hasBedrockCeiling(self) -> bool
      :async:


   .. py:method:: hasCeiling(self) -> bool
      :async:


   .. py:method:: hasCollisionsIn(self, _0:BoundingBox) -> bool
      :async:


   .. py:method:: hasMetadata(self, _0:String) -> bool
      :async:


   .. py:method:: hasRaids(self) -> bool
      :async:


   .. py:method:: hasSkyLight(self) -> bool
      :async:


   .. py:method:: hasSkylight(self) -> bool
      :async:


   .. py:method:: hasStorm(self) -> bool
      :async:


   .. py:method:: hideBossBar(self, _0:BossBar) -> None
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isAutoSave(self) -> bool
      :async:


   .. py:method:: isBedWorks(self) -> bool
      :async:


   .. py:method:: isChunkForceLoaded(self, _0:int, _1:int) -> bool
      :async:


   .. py:method:: isChunkGenerated

       .. py:method:: isChunkGenerated(self, _0:long) -> bool
          :async:
          :noindex:

       .. py:method:: isChunkGenerated(self, _0:int, _1:int) -> bool
          :async:
          :noindex:


   .. py:method:: isChunkInUse(self, _0:int, _1:int) -> bool
      :async:


   .. py:method:: isChunkLoaded

       .. py:method:: isChunkLoaded(self, _0:Chunk) -> bool
          :async:
          :noindex:

       .. py:method:: isChunkLoaded(self, _0:int, _1:int) -> bool
          :async:
          :noindex:


   .. py:method:: isClearWeather(self) -> bool
      :async:


   .. py:method:: isDayTime(self) -> bool
      :async:


   .. py:method:: isFixedTime(self) -> bool
      :async:


   .. py:method:: isGameRule(self, _0:String) -> bool
      :async:


   .. py:method:: isHardcore(self) -> bool
      :async:


   .. py:method:: isNatural(self) -> bool
      :async:


   .. py:method:: isPiglinSafe(self) -> bool
      :async:


   .. py:method:: isRespawnAnchorWorks(self) -> bool
      :async:


   .. py:method:: isThundering(self) -> bool
      :async:


   .. py:method:: isUltraWarm(self) -> bool
      :async:


   .. py:method:: isUltrawarm(self) -> bool
      :async:


   .. py:method:: key(self) -> :py:class:`Key`
      :async:


   .. py:method:: lineOfSightExists(self, _0:Location, _1:Location) -> bool
      :async:


   .. py:method:: loadChunk

       .. py:method:: loadChunk(self, _0:Chunk) -> None
          :async:
          :noindex:

       .. py:method:: loadChunk(self, _0:int, _1:int) -> None
          :async:
          :noindex:

       .. py:method:: loadChunk(self, _0:int, _1:int, _2:boolean) -> bool
          :async:
          :noindex:


   .. py:method:: locateNearestBiome

       .. py:method:: locateNearestBiome(self, _0:Location, _1:Biome, _2:int) -> :py:class:`Location`
          :async:
          :noindex:

       .. py:method:: locateNearestBiome(self, _0:Location, _1:Biome, _2:int, _3:int) -> :py:class:`Location`
          :async:
          :noindex:


   .. py:method:: locateNearestRaid(self, _0:Location, _1:int) -> :py:class:`Raid`
      :async:


   .. py:method:: locateNearestStructure

       .. py:method:: locateNearestStructure(self, _0:Location, _1:StructureType, _2:int, _3:boolean) -> :py:class:`StructureSearchResult`
          :async:
          :noindex:

       .. py:method:: locateNearestStructure(self, _0:Location, _1:StructureType, _2:int, _3:boolean) -> :py:class:`Location`
          :async:
          :noindex:

       .. py:method:: locateNearestStructure(self, _0:Location, _1:Structure, _2:int, _3:boolean) -> :py:class:`StructureSearchResult`
          :async:
          :noindex:


   .. py:method:: oldSetBlocks(self, sx, sy, sz, ex, ey, ez, material)
      :async:

      Use old style code for mcpi setBlocks

      Note: there is a far more flexible mechanism in
      async world.setBlockList(locations, materials) which
      should likely be preferred for any non-trivial tasks.


   .. py:method:: openBook

       .. py:method:: openBook(self, _0:Book) -> None
          :async:
          :noindex:

       .. py:method:: openBook(self, _0:Builder) -> None
          :async:
          :noindex:


   .. py:method:: playEffect

       .. py:method:: playEffect(self, _0:Location, _1:Effect, _2:Object) -> None
          :async:
          :noindex:

       .. py:method:: playEffect(self, _0:Location, _1:Effect, _2:int) -> None
          :async:
          :noindex:

       .. py:method:: playEffect(self, _0:Location, _1:Effect, _2:Object, _3:int) -> None
          :async:
          :noindex:

       .. py:method:: playEffect(self, _0:Location, _1:Effect, _2:int, _3:int) -> None
          :async:
          :noindex:


   .. py:method:: playSound

       .. py:method:: playSound(self, _0:Sound) -> None
          :async:
          :noindex:

       .. py:method:: playSound(self, _0:Sound, _1:Emitter) -> None
          :async:
          :noindex:

       .. py:method:: playSound(self, _0:Entity, _1:String, _2:float, _3:float) -> None
          :async:
          :noindex:

       .. py:method:: playSound(self, _0:Entity, _1:Sound, _2:float, _3:float) -> None
          :async:
          :noindex:

       .. py:method:: playSound(self, _0:Location, _1:Sound, _2:float, _3:float) -> None
          :async:
          :noindex:

       .. py:method:: playSound(self, _0:Location, _1:String, _2:float, _3:float) -> None
          :async:
          :noindex:

       .. py:method:: playSound(self, _0:Sound, _1:double, _2:double, _3:double) -> None
          :async:
          :noindex:

       .. py:method:: playSound(self, _0:Location, _1:String, _2:SoundCategory, _3:float, _4:float) -> None
          :async:
          :noindex:

       .. py:method:: playSound(self, _0:Entity, _1:Sound, _2:SoundCategory, _3:float, _4:float) -> None
          :async:
          :noindex:

       .. py:method:: playSound(self, _0:Entity, _1:String, _2:SoundCategory, _3:float, _4:float) -> None
          :async:
          :noindex:

       .. py:method:: playSound(self, _0:Location, _1:Sound, _2:SoundCategory, _3:float, _4:float) -> None
          :async:
          :noindex:


   .. py:method:: pointers(self) -> :py:class:`Pointers`
      :async:


   .. py:method:: rayTrace(self, _0:Location, _1:Vector, _2:double, _3:FluidCollisionMode, _4:boolean, _5:double, _6:Predicate) -> :py:class:`RayTraceResult`
      :async:


   .. py:method:: rayTraceBlocks

       .. py:method:: rayTraceBlocks(self, _0:Location, _1:Vector, _2:double) -> :py:class:`RayTraceResult`
          :async:
          :noindex:

       .. py:method:: rayTraceBlocks(self, _0:Location, _1:Vector, _2:double, _3:FluidCollisionMode) -> :py:class:`RayTraceResult`
          :async:
          :noindex:

       .. py:method:: rayTraceBlocks(self, _0:Location, _1:Vector, _2:double, _3:FluidCollisionMode, _4:boolean) -> :py:class:`RayTraceResult`
          :async:
          :noindex:


   .. py:method:: rayTraceEntities

       .. py:method:: rayTraceEntities(self, _0:Location, _1:Vector, _2:double) -> :py:class:`RayTraceResult`
          :async:
          :noindex:

       .. py:method:: rayTraceEntities(self, _0:Location, _1:Vector, _2:double, _3:double) -> :py:class:`RayTraceResult`
          :async:
          :noindex:

       .. py:method:: rayTraceEntities(self, _0:Location, _1:Vector, _2:double, _3:Predicate) -> :py:class:`RayTraceResult`
          :async:
          :noindex:

       .. py:method:: rayTraceEntities(self, _0:Location, _1:Vector, _2:double, _3:double, _4:Predicate) -> :py:class:`RayTraceResult`
          :async:
          :noindex:


   .. py:method:: refreshChunk(self, _0:int, _1:int) -> bool
      :async:


   .. py:method:: regenerateChunk(self, _0:int, _1:int) -> bool
      :async:


   .. py:method:: removeMetadata(self, _0:String, _1:Plugin) -> None
      :async:


   .. py:method:: removePluginChunkTicket(self, _0:int, _1:int, _2:Plugin) -> bool
      :async:


   .. py:method:: removePluginChunkTickets(self, _0:Plugin) -> None
      :async:


   .. py:method:: resetTitle(self) -> None
      :async:


   .. py:method:: save(self) -> None
      :async:


   .. py:method:: sendActionBar

       .. py:method:: sendActionBar(self, _0:Component) -> None
          :async:
          :noindex:

       .. py:method:: sendActionBar(self, _0:ComponentLike) -> None
          :async:
          :noindex:


   .. py:method:: sendGameEvent(self, _0:Entity, _1:GameEvent, _2:Vector) -> None
      :async:


   .. py:method:: sendMessage

       .. py:method:: sendMessage(self, _0:Component) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:ComponentLike) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:SignedMessage, _1:Bound) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:Component, _1:Bound) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:Identity, _1:Component) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:ComponentLike, _1:Bound) -> None
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


   .. py:method:: sendTitlePart(self, _0:TitlePart, _1:Object) -> None
      :async:


   .. py:method:: setAmbientSpawnLimit(self, _0:int) -> None
      :async:


   .. py:method:: setAnimalSpawnLimit(self, _0:int) -> None
      :async:


   .. py:method:: setAutoSave(self, _0:boolean) -> None
      :async:


   .. py:method:: setBiome

       .. py:method:: setBiome(self, _0:Location, _1:Biome) -> None
          :async:
          :noindex:

       .. py:method:: setBiome(self, _0:int, _1:int, _2:Biome) -> None
          :async:
          :noindex:

       .. py:method:: setBiome(self, _0:int, _1:int, _2:int, _3:Biome) -> None
          :async:
          :noindex:


   .. py:method:: setBlock(self, x, y, z, material_or_blockdata)
      :async:

      Set a specific block in this world to given material (blockdata)

      Note: there is a far more flexible mechanism in
      async world.setBlockList(locations, materials) which
      should likely be preferred for any non-trivial tasks.


   .. py:method:: setBlockData

       .. py:method:: setBlockData(self, _0:Location, _1:BlockData) -> None
          :async:
          :noindex:

       .. py:method:: setBlockData(self, _0:int, _1:int, _2:int, _3:BlockData) -> None
          :async:
          :noindex:


   .. py:method:: setBlockList(self, _0:World, _1:Location[], _2:BlockData[]) -> int
      :async:


   .. py:method:: setBlocks(self, _0:World, _1:Vector, _2:Vector, _3:BlockData) -> :py:class:`BlockData`
      :async:


   .. py:method:: setChunkForceLoaded(self, _0:int, _1:int, _2:boolean) -> None
      :async:


   .. py:method:: setClearWeatherDuration(self, _0:int) -> None
      :async:


   .. py:method:: setDifficulty(self, _0:Difficulty) -> None
      :async:


   .. py:method:: setFullTime(self, _0:long) -> None
      :async:


   .. py:method:: setGameRule(self, _0:GameRule, _1:Object) -> bool
      :async:


   .. py:method:: setGameRuleValue(self, _0:String, _1:String) -> bool
      :async:


   .. py:method:: setHardcore(self, _0:boolean) -> None
      :async:


   .. py:method:: setKeepSpawnInMemory(self, _0:boolean) -> None
      :async:


   .. py:method:: setMetadata(self, _0:String, _1:MetadataValue) -> None
      :async:


   .. py:method:: setMonsterSpawnLimit(self, _0:int) -> None
      :async:


   .. py:method:: setNoTickViewDistance(self, _0:int) -> None
      :async:


   .. py:method:: setPVP(self, _0:boolean) -> None
      :async:


   .. py:method:: setSendViewDistance(self, _0:int) -> None
      :async:


   .. py:method:: setSimulationDistance(self, _0:int) -> None
      :async:


   .. py:method:: setSpawnFlags(self, _0:boolean, _1:boolean) -> None
      :async:


   .. py:method:: setSpawnLimit(self, _0:SpawnCategory, _1:int) -> None
      :async:


   .. py:method:: setSpawnLocation

       .. py:method:: setSpawnLocation(self, _0:Location) -> bool
          :async:
          :noindex:

       .. py:method:: setSpawnLocation(self, _0:int, _1:int, _2:int) -> bool
          :async:
          :noindex:

       .. py:method:: setSpawnLocation(self, _0:int, _1:int, _2:int, _3:float) -> bool
          :async:
          :noindex:


   .. py:method:: setStorm(self, _0:boolean) -> None
      :async:


   .. py:method:: setThunderDuration(self, _0:int) -> None
      :async:


   .. py:method:: setThundering(self, _0:boolean) -> None
      :async:


   .. py:method:: setTicksPerAmbientSpawns(self, _0:int) -> None
      :async:


   .. py:method:: setTicksPerAnimalSpawns(self, _0:int) -> None
      :async:


   .. py:method:: setTicksPerMonsterSpawns(self, _0:int) -> None
      :async:


   .. py:method:: setTicksPerSpawns(self, _0:SpawnCategory, _1:int) -> None
      :async:


   .. py:method:: setTicksPerWaterAmbientSpawns(self, _0:int) -> None
      :async:


   .. py:method:: setTicksPerWaterSpawns(self, _0:int) -> None
      :async:


   .. py:method:: setTicksPerWaterUndergroundCreatureSpawns(self, _0:int) -> None
      :async:


   .. py:method:: setTime(self, _0:long) -> None
      :async:


   .. py:method:: setType

       .. py:method:: setType(self, _0:Location, _1:Material) -> None
          :async:
          :noindex:

       .. py:method:: setType(self, _0:int, _1:int, _2:int, _3:Material) -> None
          :async:
          :noindex:


   .. py:method:: setViewDistance(self, _0:int) -> None
      :async:


   .. py:method:: setWaterAmbientSpawnLimit(self, _0:int) -> None
      :async:


   .. py:method:: setWaterAnimalSpawnLimit(self, _0:int) -> None
      :async:


   .. py:method:: setWaterUndergroundCreatureSpawnLimit(self, _0:int) -> None
      :async:


   .. py:method:: setWeatherDuration(self, _0:int) -> None
      :async:


   .. py:method:: showBossBar(self, _0:BossBar) -> None
      :async:


   .. py:method:: showTitle(self, _0:Title) -> None
      :async:


   .. py:method:: spawn

       .. py:method:: spawn(self, _0:Location, _1:Class) -> :py:class:`Entity`
          :async:
          :noindex:

       .. py:method:: spawn(self, _0:Location, _1:Class, _2:SpawnReason) -> :py:class:`Entity`
          :async:
          :noindex:

       .. py:method:: spawn(self, _0:Location, _1:Class, _2:Consumer) -> :py:class:`Entity`
          :async:
          :noindex:

       .. py:method:: spawn(self, _0:Location, _1:Class, _2:SpawnReason, _3:Consumer) -> :py:class:`Entity`
          :async:
          :noindex:

       .. py:method:: spawn(self, _0:Location, _1:Class, _2:Consumer, _3:SpawnReason) -> :py:class:`Entity`
          :async:
          :noindex:

       .. py:method:: spawn(self, _0:Location, _1:Class, _2:boolean, _3:Consumer) -> :py:class:`Entity`
          :async:
          :noindex:


   .. py:method:: spawnArrow

       .. py:method:: spawnArrow(self, _0:Location, _1:Vector, _2:float, _3:float) -> :py:class:`Arrow`
          :async:
          :noindex:

       .. py:method:: spawnArrow(self, _0:Location, _1:Vector, _2:float, _3:float, _4:Class) -> :py:class:`AbstractArrow`
          :async:
          :noindex:


   .. py:method:: spawnEntity

       .. py:method:: spawnEntity(self, _0:Location, _1:EntityType) -> :py:class:`Entity`
          :async:
          :noindex:

       .. py:method:: spawnEntity(self, _0:Location, _1:EntityType, _2:SpawnReason) -> :py:class:`Entity`
          :async:
          :noindex:

       .. py:method:: spawnEntity(self, _0:Location, _1:EntityType, _2:boolean) -> :py:class:`Entity`
          :async:
          :noindex:

       .. py:method:: spawnEntity(self, _0:Location, _1:EntityType, _2:SpawnReason, _3:Consumer) -> :py:class:`Entity`
          :async:
          :noindex:


   .. py:method:: spawnFallingBlock

       .. py:method:: spawnFallingBlock(self, _0:Location, _1:MaterialData) -> :py:class:`FallingBlock`
          :async:
          :noindex:

       .. py:method:: spawnFallingBlock(self, _0:Location, _1:BlockData) -> :py:class:`FallingBlock`
          :async:
          :noindex:

       .. py:method:: spawnFallingBlock(self, _0:Location, _1:Material, _2:byte) -> :py:class:`FallingBlock`
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

       .. py:method:: spawnParticle(self, _0:Particle, _1:Location, _2:int, _3:double, _4:double, _5:double, _6:double) -> None
          :async:
          :noindex:

       .. py:method:: spawnParticle(self, _0:Particle, _1:Location, _2:int, _3:double, _4:double, _5:double, _6:Object) -> None
          :async:
          :noindex:

       .. py:method:: spawnParticle(self, _0:Particle, _1:Location, _2:int, _3:double, _4:double, _5:double, _6:double, _7:Object) -> None
          :async:
          :noindex:

       .. py:method:: spawnParticle(self, _0:Particle, _1:double, _2:double, _3:double, _4:int, _5:double, _6:double, _7:double) -> None
          :async:
          :noindex:

       .. py:method:: spawnParticle(self, _0:Particle, _1:double, _2:double, _3:double, _4:int, _5:double, _6:double, _7:double, _8:double) -> None
          :async:
          :noindex:

       .. py:method:: spawnParticle(self, _0:Particle, _1:Location, _2:int, _3:double, _4:double, _5:double, _6:double, _7:Object, _8:boolean) -> None
          :async:
          :noindex:

       .. py:method:: spawnParticle(self, _0:Particle, _1:double, _2:double, _3:double, _4:int, _5:double, _6:double, _7:double, _8:Object) -> None
          :async:
          :noindex:

       .. py:method:: spawnParticle(self, _0:Particle, _1:double, _2:double, _3:double, _4:int, _5:double, _6:double, _7:double, _8:double, _9:Object) -> None
          :async:
          :noindex:

       .. py:method:: spawnParticle(self, _0:Particle, _1:double, _2:double, _3:double, _4:int, _5:double, _6:double, _7:double, _8:double, _9:Object, _10:boolean) -> None
          :async:
          :noindex:

       .. py:method:: spawnParticle(self, _0:Particle, _1:List, _2:Player, _3:double, _4:double, _5:double, _6:int, _7:double, _8:double, _9:double, _10:double, _11:Object) -> None
          :async:
          :noindex:

       .. py:method:: spawnParticle(self, _0:Particle, _1:List, _2:Player, _3:double, _4:double, _5:double, _6:int, _7:double, _8:double, _9:double, _10:double, _11:Object, _12:boolean) -> None
          :async:
          :noindex:


   .. py:method:: stopSound

       .. py:method:: stopSound(self, _0:SoundStop) -> None
          :async:
          :noindex:

       .. py:method:: stopSound(self, _0:Sound) -> None
          :async:
          :noindex:


   .. py:method:: strikeLightning(self, _0:Location) -> :py:class:`LightningStrike`
      :async:


   .. py:method:: strikeLightningEffect(self, _0:Location) -> :py:class:`LightningStrike`
      :async:


   .. py:method:: unloadChunk

       .. py:method:: unloadChunk(self, _0:Chunk) -> bool
          :async:
          :noindex:

       .. py:method:: unloadChunk(self, _0:int, _1:int) -> bool
          :async:
          :noindex:

       .. py:method:: unloadChunk(self, _0:int, _1:int, _2:boolean) -> bool
          :async:
          :noindex:


   .. py:method:: unloadChunkRequest(self, _0:int, _1:int) -> bool
      :async:


   .. py:method:: vanillaBiomeProvider(self) -> :py:class:`BiomeProvider`
      :async:

