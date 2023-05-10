.. currentmodule:: pycraft.server.final

Bukkit
======

Inheritance
------------
* pycraft.server.final.Bukkit
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.Bukkit <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Bukkit.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Bukkit(self, **named)
   :canonical: pycraft.server.final.Bukkit

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: addRecipe(cls, _0:Recipe) -> bool
      :async:
      :classmethod:


   .. py:method:: advancementIterator(cls) -> :py:class:`Iterator`
      :async:
      :classmethod:


   .. py:method:: banIP(cls, _0:String) -> None
      :async:
      :classmethod:


   .. py:method:: broadcast

       .. py:method:: broadcast(cls, _0:BaseComponent) -> None
          :async:
          :classmethod:
          :noindex:

       .. py:method:: broadcast(cls, _0:Component) -> int
          :async:
          :classmethod:
          :noindex:

       .. py:method:: broadcast(cls, _0:BaseComponent[]) -> None
          :async:
          :classmethod:
          :noindex:

       .. py:method:: broadcast(cls, _0:Component, _1:String) -> int
          :async:
          :classmethod:
          :noindex:

       .. py:method:: broadcast(cls, _0:String, _1:String) -> int
          :async:
          :classmethod:
          :noindex:


   .. py:method:: broadcastMessage(cls, _0:String) -> int
      :async:
      :classmethod:


   .. py:method:: clearRecipes(cls) -> None
      :async:
      :classmethod:


   .. py:method:: craftItem(cls, _0:ItemStack[], _1:World, _2:Player) -> :py:class:`ItemStack`
      :async:
      :classmethod:


   .. py:method:: createBlockData

       .. py:method:: createBlockData(cls, _0:String) -> :py:class:`BlockData`
          :async:
          :classmethod:
          :noindex:

       .. py:method:: createBlockData(cls, _0:Material) -> :py:class:`BlockData`
          :async:
          :classmethod:
          :noindex:

       .. py:method:: createBlockData(cls, _0:Material, _1:String) -> :py:class:`BlockData`
          :async:
          :classmethod:
          :noindex:

       .. py:method:: createBlockData(cls, _0:Material, _1:Consumer) -> :py:class:`BlockData`
          :async:
          :classmethod:
          :noindex:


   .. py:method:: createBossBar

       .. py:method:: createBossBar(cls, _0:String, _1:BarColor, _2:BarStyle, _3:BarFlag[]) -> :py:class:`BossBar`
          :async:
          :classmethod:
          :noindex:

       .. py:method:: createBossBar(cls, _0:NamespacedKey, _1:String, _2:BarColor, _3:BarStyle, _4:BarFlag[]) -> :py:class:`KeyedBossBar`
          :async:
          :classmethod:
          :noindex:


   .. py:method:: createChunkData(cls, _0:World) -> :py:class:`ChunkData`
      :async:
      :classmethod:


   .. py:method:: createCommandSender(cls, _0:Consumer) -> :py:class:`CommandSender`
      :async:
      :classmethod:


   .. py:method:: createExplorerMap

       .. py:method:: createExplorerMap(cls, _0:World, _1:Location, _2:StructureType) -> :py:class:`ItemStack`
          :async:
          :classmethod:
          :noindex:

       .. py:method:: createExplorerMap(cls, _0:World, _1:Location, _2:StructureType, _3:int, _4:boolean) -> :py:class:`ItemStack`
          :async:
          :classmethod:
          :noindex:


   .. py:method:: createInventory

       .. py:method:: createInventory(cls, _0:InventoryHolder, _1:InventoryType) -> :py:class:`Inventory`
          :async:
          :classmethod:
          :noindex:

       .. py:method:: createInventory(cls, _0:InventoryHolder, _1:int) -> :py:class:`Inventory`
          :async:
          :classmethod:
          :noindex:

       .. py:method:: createInventory(cls, _0:InventoryHolder, _1:int, _2:String) -> :py:class:`Inventory`
          :async:
          :classmethod:
          :noindex:

       .. py:method:: createInventory(cls, _0:InventoryHolder, _1:InventoryType, _2:Component) -> :py:class:`Inventory`
          :async:
          :classmethod:
          :noindex:

       .. py:method:: createInventory(cls, _0:InventoryHolder, _1:int, _2:Component) -> :py:class:`Inventory`
          :async:
          :classmethod:
          :noindex:

       .. py:method:: createInventory(cls, _0:InventoryHolder, _1:InventoryType, _2:String) -> :py:class:`Inventory`
          :async:
          :classmethod:
          :noindex:


   .. py:method:: createMap(cls, _0:World) -> :py:class:`MapView`
      :async:
      :classmethod:


   .. py:method:: createMerchant

       .. py:method:: createMerchant(cls, _0:Component) -> :py:class:`Merchant`
          :async:
          :classmethod:
          :noindex:

       .. py:method:: createMerchant(cls, _0:String) -> :py:class:`Merchant`
          :async:
          :classmethod:
          :noindex:


   .. py:method:: createPlayerProfile

       .. py:method:: createPlayerProfile(cls, _0:String) -> :py:class:`PlayerProfile`
          :async:
          :classmethod:
          :noindex:

       .. py:method:: createPlayerProfile(cls, _0:UUID) -> :py:class:`PlayerProfile`
          :async:
          :classmethod:
          :noindex:

       .. py:method:: createPlayerProfile(cls, _0:UUID, _1:String) -> :py:class:`PlayerProfile`
          :async:
          :classmethod:
          :noindex:


   .. py:method:: createProfile

       .. py:method:: createProfile(cls, _0:UUID) -> :py:class:`PlayerProfile`
          :async:
          :classmethod:
          :noindex:

       .. py:method:: createProfile(cls, _0:String) -> :py:class:`PlayerProfile`
          :async:
          :classmethod:
          :noindex:

       .. py:method:: createProfile(cls, _0:UUID, _1:String) -> :py:class:`PlayerProfile`
          :async:
          :classmethod:
          :noindex:


   .. py:method:: createProfileExact(cls, _0:UUID, _1:String) -> :py:class:`PlayerProfile`
      :async:
      :classmethod:


   .. py:method:: createVanillaChunkData(cls, _0:World, _1:int, _2:int) -> :py:class:`ChunkData`
      :async:
      :classmethod:


   .. py:method:: createWorld(cls, _0:WorldCreator) -> :py:class:`World`
      :async:
      :classmethod:


   .. py:method:: createWorldBorder(cls) -> :py:class:`WorldBorder`
      :async:
      :classmethod:


   .. py:method:: dispatchCommand(cls, _0:CommandSender, _1:String) -> bool
      :async:
      :classmethod:


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getAdvancement(cls, _0:NamespacedKey) -> :py:class:`Advancement`
      :async:
      :classmethod:


   .. py:method:: getAllowEnd(cls) -> bool
      :async:
      :classmethod:


   .. py:method:: getAllowFlight(cls) -> bool
      :async:
      :classmethod:


   .. py:method:: getAllowNether(cls) -> bool
      :async:
      :classmethod:


   .. py:method:: getAmbientSpawnLimit(cls) -> int
      :async:
      :classmethod:


   .. py:method:: getAnimalSpawnLimit(cls) -> int
      :async:
      :classmethod:


   .. py:method:: getAverageTickTime(cls) -> float
      :async:
      :classmethod:


   .. py:method:: getBanList(cls, _0:Type) -> :py:class:`BanList`
      :async:
      :classmethod:


   .. py:method:: getBannedPlayers(cls) -> typing.List[:py:class:`OfflinePlayer`]
      :async:
      :classmethod:


   .. py:method:: getBossBar(cls, _0:NamespacedKey) -> :py:class:`KeyedBossBar`
      :async:
      :classmethod:


   .. py:method:: getBossBars(cls) -> :py:class:`Iterator`
      :async:
      :classmethod:


   .. py:method:: getBukkitVersion(cls) -> str
      :async:
      :classmethod:


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getCommandAliases(cls) -> :py:class:`Map`
      :async:
      :classmethod:


   .. py:method:: getCommandMap(cls) -> :py:class:`CommandMap`
      :async:
      :classmethod:


   .. py:method:: getConnectionThrottle(cls) -> :py:class:`long`
      :async:
      :classmethod:


   .. py:method:: getConsoleSender(cls) -> :py:class:`ConsoleCommandSender`
      :async:
      :classmethod:


   .. py:method:: getCraftingRecipe(cls, _0:ItemStack[], _1:World) -> :py:class:`Recipe`
      :async:
      :classmethod:


   .. py:method:: getCurrentTick(cls) -> int
      :async:
      :classmethod:


   .. py:method:: getDatapackManager(cls) -> :py:class:`DatapackManager`
      :async:
      :classmethod:


   .. py:method:: getDefaultGameMode(cls) -> :py:class:`GameMode`
      :async:
      :classmethod:


   .. py:method:: getEntity(cls, _0:UUID) -> :py:class:`Entity`
      :async:
      :classmethod:


   .. py:method:: getGenerateStructures(cls) -> bool
      :async:
      :classmethod:


   .. py:method:: getHelpMap(cls) -> :py:class:`HelpMap`
      :async:
      :classmethod:


   .. py:method:: getHideOnlinePlayers(cls) -> bool
      :async:
      :classmethod:


   .. py:method:: getIPBans(cls) -> typing.List[str]
      :async:
      :classmethod:


   .. py:method:: getIdleTimeout(cls) -> int
      :async:
      :classmethod:


   .. py:method:: getIp(cls) -> str
      :async:
      :classmethod:


   .. py:method:: getItemFactory(cls) -> :py:class:`ItemFactory`
      :async:
      :classmethod:


   .. py:method:: getLogger(cls) -> :py:class:`Logger`
      :async:
      :classmethod:


   .. py:method:: getLootTable(cls, _0:NamespacedKey) -> :py:class:`LootTable`
      :async:
      :classmethod:


   .. py:method:: getMap(cls, _0:int) -> :py:class:`MapView`
      :async:
      :classmethod:


   .. py:method:: getMaxChainedNeighborUpdates(cls) -> int
      :async:
      :classmethod:


   .. py:method:: getMaxPlayers(cls) -> int
      :async:
      :classmethod:


   .. py:method:: getMaxWorldSize(cls) -> int
      :async:
      :classmethod:


   .. py:method:: getMessenger(cls) -> :py:class:`Messenger`
      :async:
      :classmethod:


   .. py:method:: getMinecraftVersion(cls) -> str
      :async:
      :classmethod:


   .. py:method:: getMobGoals(cls) -> :py:class:`MobGoals`
      :async:
      :classmethod:


   .. py:method:: getMonsterSpawnLimit(cls) -> int
      :async:
      :classmethod:


   .. py:method:: getMotd(cls) -> str
      :async:
      :classmethod:


   .. py:method:: getName(cls) -> str
      :async:
      :classmethod:


   .. py:method:: getOfflinePlayer

       .. py:method:: getOfflinePlayer(cls, _0:UUID) -> :py:class:`OfflinePlayer`
          :async:
          :classmethod:
          :noindex:

       .. py:method:: getOfflinePlayer(cls, _0:String) -> :py:class:`OfflinePlayer`
          :async:
          :classmethod:
          :noindex:


   .. py:method:: getOfflinePlayerIfCached(cls, _0:String) -> :py:class:`OfflinePlayer`
      :async:
      :classmethod:


   .. py:method:: getOfflinePlayers(cls) -> typing.List[:py:class:`OfflinePlayer`]
      :async:
      :classmethod:


   .. py:method:: getOnlineMode(cls) -> bool
      :async:
      :classmethod:


   .. py:method:: getOnlinePlayers(cls) -> typing.List[:py:class:`? extends org.bukkit.entity.Player`]
      :async:
      :classmethod:


   .. py:method:: getOperators(cls) -> typing.List[:py:class:`OfflinePlayer`]
      :async:
      :classmethod:


   .. py:method:: getPermissionMessage(cls) -> str
      :async:
      :classmethod:


   .. py:method:: getPlayer

       .. py:method:: getPlayer(cls, _0:UUID) -> :py:class:`Player`
          :async:
          :classmethod:
          :noindex:

       .. py:method:: getPlayer(cls, _0:String) -> :py:class:`Player`
          :async:
          :classmethod:
          :noindex:


   .. py:method:: getPlayerExact(cls, _0:String) -> :py:class:`Player`
      :async:
      :classmethod:


   .. py:method:: getPlayerUniqueId(cls, _0:String) -> uuid.UUID
      :async:
      :classmethod:


   .. py:method:: getPluginCommand(cls, _0:String) -> :py:class:`PluginCommand`
      :async:
      :classmethod:


   .. py:method:: getPluginManager(cls) -> :py:class:`PluginManager`
      :async:
      :classmethod:


   .. py:method:: getPluginsFolder(cls) -> :py:class:`File`
      :async:
      :classmethod:


   .. py:method:: getPort(cls) -> int
      :async:
      :classmethod:


   .. py:method:: getPotionBrewer(cls) -> :py:class:`PotionBrewer`
      :async:
      :classmethod:


   .. py:method:: getRecipe(cls, _0:NamespacedKey) -> :py:class:`Recipe`
      :async:
      :classmethod:


   .. py:method:: getRecipesFor(cls, _0:ItemStack) -> typing.List[:py:class:`Recipe`]
      :async:
      :classmethod:


   .. py:method:: getRegistry(cls, _0:Class) -> :py:class:`Registry`
      :async:
      :classmethod:


   .. py:method:: getResourcePack(cls) -> str
      :async:
      :classmethod:


   .. py:method:: getResourcePackHash(cls) -> str
      :async:
      :classmethod:


   .. py:method:: getResourcePackPrompt(cls) -> str
      :async:
      :classmethod:


   .. py:method:: getScheduler(cls) -> :py:class:`BukkitScheduler`
      :async:
      :classmethod:


   .. py:method:: getScoreboardCriteria(cls, _0:String) -> :py:class:`Criteria`
      :async:
      :classmethod:


   .. py:method:: getScoreboardManager(cls) -> :py:class:`ScoreboardManager`
      :async:
      :classmethod:


   .. py:method:: getServer(cls) -> :py:class:`Server`
      :async:
      :classmethod:


   .. py:method:: getServerIcon(cls) -> :py:class:`CachedServerIcon`
      :async:
      :classmethod:


   .. py:method:: getServicesManager(cls) -> :py:class:`ServicesManager`
      :async:
      :classmethod:


   .. py:method:: getShutdownMessage(cls) -> str
      :async:
      :classmethod:


   .. py:method:: getSimulationDistance(cls) -> int
      :async:
      :classmethod:


   .. py:method:: getSpawnLimit(cls, _0:SpawnCategory) -> int
      :async:
      :classmethod:


   .. py:method:: getSpawnRadius(cls) -> int
      :async:
      :classmethod:


   .. py:method:: getStructureManager(cls) -> :py:class:`StructureManager`
      :async:
      :classmethod:


   .. py:method:: getTPS(cls) -> typing.List[float]
      :async:
      :classmethod:


   .. py:method:: getTag(cls, _0:String, _1:NamespacedKey, _2:Class) -> :py:class:`Tag`
      :async:
      :classmethod:


   .. py:method:: getTags(cls, _0:String, _1:Class) -> :py:class:`Iterable`
      :async:
      :classmethod:


   .. py:method:: getTickTimes(cls) -> typing.List[:py:class:`long`]
      :async:
      :classmethod:


   .. py:method:: getTicksPerAmbientSpawns(cls) -> int
      :async:
      :classmethod:


   .. py:method:: getTicksPerAnimalSpawns(cls) -> int
      :async:
      :classmethod:


   .. py:method:: getTicksPerMonsterSpawns(cls) -> int
      :async:
      :classmethod:


   .. py:method:: getTicksPerSpawns(cls, _0:SpawnCategory) -> int
      :async:
      :classmethod:


   .. py:method:: getTicksPerWaterAmbientSpawns(cls) -> int
      :async:
      :classmethod:


   .. py:method:: getTicksPerWaterSpawns(cls) -> int
      :async:
      :classmethod:


   .. py:method:: getTicksPerWaterUndergroundCreatureSpawns(cls) -> int
      :async:
      :classmethod:


   .. py:method:: getUnsafe(cls) -> :py:class:`UnsafeValues`
      :async:
      :classmethod:


   .. py:method:: getUpdateFolder(cls) -> str
      :async:
      :classmethod:


   .. py:method:: getUpdateFolderFile(cls) -> :py:class:`File`
      :async:
      :classmethod:


   .. py:method:: getVersion(cls) -> str
      :async:
      :classmethod:


   .. py:method:: getVersionMessage(cls) -> str
      :async:
      :classmethod:


   .. py:method:: getViewDistance(cls) -> int
      :async:
      :classmethod:


   .. py:method:: getWarningState(cls) -> :py:class:`WarningState`
      :async:
      :classmethod:


   .. py:method:: getWaterAmbientSpawnLimit(cls) -> int
      :async:
      :classmethod:


   .. py:method:: getWaterAnimalSpawnLimit(cls) -> int
      :async:
      :classmethod:


   .. py:method:: getWaterUndergroundCreatureSpawnLimit(cls) -> int
      :async:
      :classmethod:


   .. py:method:: getWhitelistedPlayers(cls) -> typing.List[:py:class:`OfflinePlayer`]
      :async:
      :classmethod:


   .. py:method:: getWorld

       .. py:method:: getWorld(cls, _0:NamespacedKey) -> :py:class:`World`
          :async:
          :classmethod:
          :noindex:

       .. py:method:: getWorld(cls, _0:String) -> :py:class:`World`
          :async:
          :classmethod:
          :noindex:

       .. py:method:: getWorld(cls, _0:UUID) -> :py:class:`World`
          :async:
          :classmethod:
          :noindex:


   .. py:method:: getWorldContainer(cls) -> :py:class:`File`
      :async:
      :classmethod:


   .. py:method:: getWorldType(cls) -> str
      :async:
      :classmethod:


   .. py:method:: getWorlds(cls) -> typing.List[:py:class:`World`]
      :async:
      :classmethod:


   .. py:method:: hasWhitelist(cls) -> bool
      :async:
      :classmethod:


   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isEnforcingSecureProfiles(cls) -> bool
      :async:
      :classmethod:


   .. py:method:: isHardcore(cls) -> bool
      :async:
      :classmethod:


   .. py:method:: isPrimaryThread(cls) -> bool
      :async:
      :classmethod:


   .. py:method:: isResourcePackRequired(cls) -> bool
      :async:
      :classmethod:


   .. py:method:: isStopping(cls) -> bool
      :async:
      :classmethod:


   .. py:method:: isTickingWorlds(cls) -> bool
      :async:
      :classmethod:


   .. py:method:: isWhitelistEnforced(cls) -> bool
      :async:
      :classmethod:


   .. py:method:: loadServerIcon

       .. py:method:: loadServerIcon(cls, _0:BufferedImage) -> :py:class:`CachedServerIcon`
          :async:
          :classmethod:
          :noindex:

       .. py:method:: loadServerIcon(cls, _0:File) -> :py:class:`CachedServerIcon`
          :async:
          :classmethod:
          :noindex:


   .. py:method:: matchPlayer(cls, _0:String) -> typing.List[:py:class:`Player`]
      :async:
      :classmethod:


   .. py:method:: motd(cls) -> :py:class:`Component`
      :async:
      :classmethod:


   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: permissionMessage(cls) -> :py:class:`Component`
      :async:
      :classmethod:


   .. py:method:: recipeIterator(cls) -> :py:class:`Iterator`
      :async:
      :classmethod:


   .. py:method:: reload(cls) -> None
      :async:
      :classmethod:


   .. py:method:: reloadCommandAliases(cls) -> bool
      :async:
      :classmethod:


   .. py:method:: reloadData(cls) -> None
      :async:
      :classmethod:


   .. py:method:: reloadPermissions(cls) -> None
      :async:
      :classmethod:


   .. py:method:: reloadWhitelist(cls) -> None
      :async:
      :classmethod:


   .. py:method:: removeBossBar(cls, _0:NamespacedKey) -> bool
      :async:
      :classmethod:


   .. py:method:: removeRecipe(cls, _0:NamespacedKey) -> bool
      :async:
      :classmethod:


   .. py:method:: resetRecipes(cls) -> None
      :async:
      :classmethod:


   .. py:method:: savePlayers(cls) -> None
      :async:
      :classmethod:


   .. py:method:: selectEntities(cls, _0:CommandSender, _1:String) -> typing.List[:py:class:`Entity`]
      :async:
      :classmethod:


   .. py:method:: setDefaultGameMode(cls, _0:GameMode) -> None
      :async:
      :classmethod:


   .. py:method:: setIdleTimeout(cls, _0:int) -> None
      :async:
      :classmethod:


   .. py:method:: setMaxPlayers(cls, _0:int) -> None
      :async:
      :classmethod:


   .. py:method:: setServer(cls, _0:Server) -> None
      :async:
      :classmethod:


   .. py:method:: setSpawnRadius(cls, _0:int) -> None
      :async:
      :classmethod:


   .. py:method:: setWhitelist(cls, _0:boolean) -> None
      :async:
      :classmethod:


   .. py:method:: setWhitelistEnforced(cls, _0:boolean) -> None
      :async:
      :classmethod:


   .. py:method:: shouldSendChatPreviews(cls) -> bool
      :async:
      :classmethod:


   .. py:method:: shutdown(cls) -> None
      :async:
      :classmethod:


   .. py:method:: shutdownMessage(cls) -> :py:class:`Component`
      :async:
      :classmethod:


   .. py:method:: suggestPlayerNamesWhenNullTabCompletions(cls) -> bool
      :async:
      :classmethod:


   .. py:method:: toString(self) -> str
      :async:


   .. py:method:: unbanIP(cls, _0:String) -> None
      :async:
      :classmethod:


   .. py:method:: unloadWorld

       .. py:method:: unloadWorld(cls, _0:String, _1:boolean) -> bool
          :async:
          :classmethod:
          :noindex:

       .. py:method:: unloadWorld(cls, _0:World, _1:boolean) -> bool
          :async:
          :classmethod:
          :noindex:

