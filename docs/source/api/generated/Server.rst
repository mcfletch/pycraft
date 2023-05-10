.. currentmodule:: pycraft.server.final

Server
======

Inheritance
------------
* pycraft.server.final.Server
* :py:class:`pycraft.server.world.Server`
* :py:class:`pycraft.server.final.PluginMessageRecipient`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.Server <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Server.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Server(self, **named)
   :canonical: pycraft.server.final.Server

   Proxy for the server API

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: addRecipe(self, _0:Recipe) -> bool
      :async:


   .. py:method:: advancementIterator(self) -> :py:class:`Iterator`
      :async:


   .. py:method:: audiences(self) -> :py:class:`Iterable`
      :async:


   .. py:method:: banIP(self, _0:String) -> None
      :async:


   .. py:method:: broadcast

       .. py:method:: broadcast(self, _0:BaseComponent[]) -> None
          :async:
          :noindex:

       .. py:method:: broadcast(self, _0:Component) -> int
          :async:
          :noindex:

       .. py:method:: broadcast(self, _0:BaseComponent) -> None
          :async:
          :noindex:

       .. py:method:: broadcast(self, _0:String, _1:String) -> int
          :async:
          :noindex:

       .. py:method:: broadcast(self, _0:Component, _1:String) -> int
          :async:
          :noindex:


   .. py:method:: broadcastMessage(self, _0:String) -> int
      :async:


   .. py:method:: clearRecipes(self) -> None
      :async:


   .. py:method:: clearTitle(self) -> None
      :async:


   .. py:method:: craftItem(self, _0:ItemStack[], _1:World, _2:Player) -> :py:class:`ItemStack`
      :async:


   .. py:method:: createBlockData

       .. py:method:: createBlockData(self, _0:String) -> :py:class:`BlockData`
          :async:
          :noindex:

       .. py:method:: createBlockData(self, _0:Material) -> :py:class:`BlockData`
          :async:
          :noindex:

       .. py:method:: createBlockData(self, _0:Material, _1:String) -> :py:class:`BlockData`
          :async:
          :noindex:

       .. py:method:: createBlockData(self, _0:Material, _1:Consumer) -> :py:class:`BlockData`
          :async:
          :noindex:


   .. py:method:: createBossBar

       .. py:method:: createBossBar(self, _0:String, _1:BarColor, _2:BarStyle, _3:BarFlag[]) -> :py:class:`BossBar`
          :async:
          :noindex:

       .. py:method:: createBossBar(self, _0:NamespacedKey, _1:String, _2:BarColor, _3:BarStyle, _4:BarFlag[]) -> :py:class:`KeyedBossBar`
          :async:
          :noindex:


   .. py:method:: createChunkData(self, _0:World) -> :py:class:`ChunkData`
      :async:


   .. py:method:: createCommandSender(self, _0:Consumer) -> :py:class:`CommandSender`
      :async:


   .. py:method:: createExplorerMap

       .. py:method:: createExplorerMap(self, _0:World, _1:Location, _2:StructureType) -> :py:class:`ItemStack`
          :async:
          :noindex:

       .. py:method:: createExplorerMap(self, _0:World, _1:Location, _2:StructureType, _3:int, _4:boolean) -> :py:class:`ItemStack`
          :async:
          :noindex:


   .. py:method:: createInventory

       .. py:method:: createInventory(self, _0:InventoryHolder, _1:InventoryType) -> :py:class:`Inventory`
          :async:
          :noindex:

       .. py:method:: createInventory(self, _0:InventoryHolder, _1:int) -> :py:class:`Inventory`
          :async:
          :noindex:

       .. py:method:: createInventory(self, _0:InventoryHolder, _1:int, _2:Component) -> :py:class:`Inventory`
          :async:
          :noindex:

       .. py:method:: createInventory(self, _0:InventoryHolder, _1:InventoryType, _2:String) -> :py:class:`Inventory`
          :async:
          :noindex:

       .. py:method:: createInventory(self, _0:InventoryHolder, _1:InventoryType, _2:Component) -> :py:class:`Inventory`
          :async:
          :noindex:

       .. py:method:: createInventory(self, _0:InventoryHolder, _1:int, _2:String) -> :py:class:`Inventory`
          :async:
          :noindex:


   .. py:method:: createMap(self, _0:World) -> :py:class:`MapView`
      :async:


   .. py:method:: createMerchant

       .. py:method:: createMerchant(self, _0:Component) -> :py:class:`Merchant`
          :async:
          :noindex:

       .. py:method:: createMerchant(self, _0:String) -> :py:class:`Merchant`
          :async:
          :noindex:


   .. py:method:: createPlayerProfile

       .. py:method:: createPlayerProfile(self, _0:String) -> :py:class:`PlayerProfile`
          :async:
          :noindex:

       .. py:method:: createPlayerProfile(self, _0:UUID) -> :py:class:`PlayerProfile`
          :async:
          :noindex:

       .. py:method:: createPlayerProfile(self, _0:UUID, _1:String) -> :py:class:`PlayerProfile`
          :async:
          :noindex:


   .. py:method:: createProfile

       .. py:method:: createProfile(self, _0:UUID) -> :py:class:`PlayerProfile`
          :async:
          :noindex:

       .. py:method:: createProfile(self, _0:String) -> :py:class:`PlayerProfile`
          :async:
          :noindex:

       .. py:method:: createProfile(self, _0:UUID, _1:String) -> :py:class:`PlayerProfile`
          :async:
          :noindex:


   .. py:method:: createProfileExact(self, _0:UUID, _1:String) -> :py:class:`PlayerProfile`
      :async:


   .. py:method:: createVanillaChunkData(self, _0:World, _1:int, _2:int) -> :py:class:`ChunkData`
      :async:


   .. py:method:: createWorld(self, _0:WorldCreator) -> :py:class:`World`
      :async:


   .. py:method:: createWorldBorder(self) -> :py:class:`WorldBorder`
      :async:


   .. py:method:: deleteMessage

       .. py:method:: deleteMessage(self, _0:Signature) -> None
          :async:
          :noindex:

       .. py:method:: deleteMessage(self, _0:SignedMessage) -> None
          :async:
          :noindex:


   .. py:method:: dispatchCommand(self, _0:CommandSender, _1:String) -> bool
      :async:


   .. py:method:: filterAudience(self, _0:Predicate) -> :py:class:`Audience`
      :async:


   .. py:method:: forEachAudience(self, _0:Consumer) -> None
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: get(self, _0:Pointer) -> :py:class:`Optional`
      :async:


   .. py:method:: getAdvancement(self, _0:NamespacedKey) -> :py:class:`Advancement`
      :async:


   .. py:method:: getAllowEnd(self) -> bool
      :async:


   .. py:method:: getAllowFlight(self) -> bool
      :async:


   .. py:method:: getAllowNether(self) -> bool
      :async:


   .. py:method:: getAmbientSpawnLimit(self) -> int
      :async:


   .. py:method:: getAnimalSpawnLimit(self) -> int
      :async:


   .. py:method:: getAverageTickTime(self) -> float
      :async:


   .. py:method:: getBanList(self, _0:Type) -> :py:class:`BanList`
      :async:


   .. py:method:: getBannedPlayers(self) -> typing.List[:py:class:`OfflinePlayer`]
      :async:


   .. py:method:: getBossBar(self, _0:NamespacedKey) -> :py:class:`KeyedBossBar`
      :async:


   .. py:method:: getBossBars(self) -> :py:class:`Iterator`
      :async:


   .. py:method:: getBukkitVersion(self) -> str
      :async:


   .. py:method:: getCommandAliases(self) -> :py:class:`Map`
      :async:


   .. py:method:: getCommandMap(self) -> :py:class:`CommandMap`
      :async:


   .. py:method:: getConnectionThrottle(self) -> :py:class:`long`
      :async:


   .. py:method:: getConsoleSender(self) -> :py:class:`ConsoleCommandSender`
      :async:


   .. py:method:: getCraftingRecipe(self, _0:ItemStack[], _1:World) -> :py:class:`Recipe`
      :async:


   .. py:method:: getCurrentTick(self) -> int
      :async:


   .. py:method:: getDatapackManager(self) -> :py:class:`DatapackManager`
      :async:


   .. py:method:: getDefaultGameMode(self) -> :py:class:`GameMode`
      :async:


   .. py:method:: getEntity(self, _0:UUID) -> :py:class:`Entity`
      :async:


   .. py:method:: getGenerateStructures(self) -> bool
      :async:


   .. py:method:: getHelpMap(self) -> :py:class:`HelpMap`
      :async:


   .. py:method:: getHideOnlinePlayers(self) -> bool
      :async:


   .. py:method:: getIPBans(self) -> typing.List[str]
      :async:


   .. py:method:: getIdleTimeout(self) -> int
      :async:


   .. py:method:: getIp(self) -> str
      :async:


   .. py:method:: getItemFactory(self) -> :py:class:`ItemFactory`
      :async:


   .. py:method:: getListeningPluginChannels(self) -> typing.List[str]
      :async:


   .. py:method:: getLogger(self) -> :py:class:`Logger`
      :async:


   .. py:method:: getLootTable(self, _0:NamespacedKey) -> :py:class:`LootTable`
      :async:


   .. py:method:: getMap(self, _0:int) -> :py:class:`MapView`
      :async:


   .. py:method:: getMaxChainedNeighborUpdates(self) -> int
      :async:


   .. py:method:: getMaxPlayers(self) -> int
      :async:


   .. py:method:: getMaxWorldSize(self) -> int
      :async:


   .. py:method:: getMessenger(self) -> :py:class:`Messenger`
      :async:


   .. py:method:: getMinecraftVersion(self) -> str
      :async:


   .. py:method:: getMobGoals(self) -> :py:class:`MobGoals`
      :async:


   .. py:method:: getMonsterSpawnLimit(self) -> int
      :async:


   .. py:method:: getMotd(self) -> str
      :async:


   .. py:method:: getName(self) -> str
      :async:


   .. py:method:: getOfflinePlayer

       .. py:method:: getOfflinePlayer(self, _0:String) -> :py:class:`OfflinePlayer`
          :async:
          :noindex:

       .. py:method:: getOfflinePlayer(self, _0:UUID) -> :py:class:`OfflinePlayer`
          :async:
          :noindex:


   .. py:method:: getOfflinePlayerIfCached(self, _0:String) -> :py:class:`OfflinePlayer`
      :async:


   .. py:method:: getOfflinePlayers(self) -> typing.List[:py:class:`OfflinePlayer`]
      :async:


   .. py:method:: getOnlineMode(self) -> bool
      :async:


   .. py:method:: getOnlinePlayers(self) -> typing.List[:py:class:`? extends org.bukkit.entity.Player`]
      :async:


   .. py:method:: getOperators(self) -> typing.List[:py:class:`OfflinePlayer`]
      :async:


   .. py:method:: getOrDefault(self, _0:Pointer, _1:Object) -> :py:class:`Object`
      :async:


   .. py:method:: getOrDefaultFrom(self, _0:Pointer, _1:Supplier) -> :py:class:`Object`
      :async:


   .. py:method:: getPermissionMessage(self) -> str
      :async:


   .. py:method:: getPlayer

       .. py:method:: getPlayer(self, _0:String) -> :py:class:`Player`
          :async:
          :noindex:

       .. py:method:: getPlayer(self, _0:UUID) -> :py:class:`Player`
          :async:
          :noindex:


   .. py:method:: getPlayerExact(self, _0:String) -> :py:class:`Player`
      :async:


   .. py:method:: getPlayerUniqueId(self, _0:String) -> uuid.UUID
      :async:


   .. py:method:: getPluginCommand(self, _0:String) -> :py:class:`PluginCommand`
      :async:


   .. py:method:: getPluginManager(self) -> :py:class:`PluginManager`
      :async:


   .. py:method:: getPluginsFolder(self) -> :py:class:`File`
      :async:


   .. py:method:: getPort(self) -> int
      :async:


   .. py:method:: getPotionBrewer(self) -> :py:class:`PotionBrewer`
      :async:


   .. py:method:: getRecipe(self, _0:NamespacedKey) -> :py:class:`Recipe`
      :async:


   .. py:method:: getRecipesFor(self, _0:ItemStack) -> typing.List[:py:class:`Recipe`]
      :async:


   .. py:method:: getRegistry(self, _0:Class) -> :py:class:`Registry`
      :async:


   .. py:method:: getResourcePack(self) -> str
      :async:


   .. py:method:: getResourcePackHash(self) -> str
      :async:


   .. py:method:: getResourcePackPrompt(self) -> str
      :async:


   .. py:method:: getScheduler(self) -> :py:class:`BukkitScheduler`
      :async:


   .. py:method:: getScoreboardCriteria(self, _0:String) -> :py:class:`Criteria`
      :async:


   .. py:method:: getScoreboardManager(self) -> :py:class:`ScoreboardManager`
      :async:


   .. py:method:: getServerIcon(self) -> :py:class:`CachedServerIcon`
      :async:


   .. py:method:: getServicesManager(self) -> :py:class:`ServicesManager`
      :async:


   .. py:method:: getShutdownMessage(self) -> str
      :async:


   .. py:method:: getSimulationDistance(self) -> int
      :async:


   .. py:method:: getSpawnLimit(self, _0:SpawnCategory) -> int
      :async:


   .. py:method:: getSpawnRadius(self) -> int
      :async:


   .. py:method:: getStructureManager(self) -> :py:class:`StructureManager`
      :async:


   .. py:method:: getTPS(self) -> typing.List[float]
      :async:


   .. py:method:: getTag(self, _0:String, _1:NamespacedKey, _2:Class) -> :py:class:`Tag`
      :async:


   .. py:method:: getTags(self, _0:String, _1:Class) -> :py:class:`Iterable`
      :async:


   .. py:method:: getTickTimes(self) -> typing.List[:py:class:`long`]
      :async:


   .. py:method:: getTicksPerAmbientSpawns(self) -> int
      :async:


   .. py:method:: getTicksPerAnimalSpawns(self) -> int
      :async:


   .. py:method:: getTicksPerMonsterSpawns(self) -> int
      :async:


   .. py:method:: getTicksPerSpawns(self, _0:SpawnCategory) -> int
      :async:


   .. py:method:: getTicksPerWaterAmbientSpawns(self) -> int
      :async:


   .. py:method:: getTicksPerWaterSpawns(self) -> int
      :async:


   .. py:method:: getTicksPerWaterUndergroundCreatureSpawns(self) -> int
      :async:


   .. py:method:: getUnsafe(self) -> :py:class:`UnsafeValues`
      :async:


   .. py:method:: getUpdateFolder(self) -> str
      :async:


   .. py:method:: getUpdateFolderFile(self) -> :py:class:`File`
      :async:


   .. py:method:: getVersion(self) -> str
      :async:


   .. py:method:: getViewDistance(self) -> int
      :async:


   .. py:method:: getWarningState(self) -> :py:class:`WarningState`
      :async:


   .. py:method:: getWaterAmbientSpawnLimit(self) -> int
      :async:


   .. py:method:: getWaterAnimalSpawnLimit(self) -> int
      :async:


   .. py:method:: getWaterUndergroundCreatureSpawnLimit(self) -> int
      :async:


   .. py:method:: getWhitelistedPlayers(self) -> typing.List[:py:class:`OfflinePlayer`]
      :async:


   .. py:method:: getWorld

       .. py:method:: getWorld(self, _0:UUID) -> :py:class:`World`
          :async:
          :noindex:

       .. py:method:: getWorld(self, _0:String) -> :py:class:`World`
          :async:
          :noindex:

       .. py:method:: getWorld(self, _0:NamespacedKey) -> :py:class:`World`
          :async:
          :noindex:


   .. py:method:: getWorldContainer(self) -> :py:class:`File`
      :async:


   .. py:method:: getWorldType(self) -> str
      :async:


   .. py:method:: getWorlds(self) -> typing.List[:py:class:`World`]
      :async:


   .. py:method:: get_key(self)
      

      Get the key to lookup the server (literal 'server')


   .. py:method:: hasWhitelist(self) -> bool
      :async:


   .. py:method:: hideBossBar(self, _0:BossBar) -> None
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isEnforcingSecureProfiles(self) -> bool
      :async:


   .. py:method:: isHardcore(self) -> bool
      :async:


   .. py:method:: isPrimaryThread(self) -> bool
      :async:


   .. py:method:: isResourcePackRequired(self) -> bool
      :async:


   .. py:method:: isStopping(self) -> bool
      :async:


   .. py:method:: isTickingWorlds(self) -> bool
      :async:


   .. py:method:: isWhitelistEnforced(self) -> bool
      :async:


   .. py:method:: loadServerIcon

       .. py:method:: loadServerIcon(self, _0:File) -> :py:class:`CachedServerIcon`
          :async:
          :noindex:

       .. py:method:: loadServerIcon(self, _0:BufferedImage) -> :py:class:`CachedServerIcon`
          :async:
          :noindex:


   .. py:method:: matchPlayer(self, _0:String) -> typing.List[:py:class:`Player`]
      :async:


   .. py:method:: motd(self) -> :py:class:`Component`
      :async:


   .. py:method:: openBook

       .. py:method:: openBook(self, _0:Book) -> None
          :async:
          :noindex:

       .. py:method:: openBook(self, _0:Builder) -> None
          :async:
          :noindex:


   .. py:method:: permissionMessage(self) -> :py:class:`Component`
      :async:


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


   .. py:method:: recipeIterator(self) -> :py:class:`Iterator`
      :async:


   .. py:method:: reload(self) -> None
      :async:


   .. py:method:: reloadCommandAliases(self) -> bool
      :async:


   .. py:method:: reloadData(self) -> None
      :async:


   .. py:method:: reloadPermissions(self) -> None
      :async:


   .. py:method:: reloadWhitelist(self) -> None
      :async:


   .. py:method:: removeBossBar(self, _0:NamespacedKey) -> bool
      :async:


   .. py:method:: removeRecipe(self, _0:NamespacedKey) -> bool
      :async:


   .. py:method:: resetRecipes(self) -> None
      :async:


   .. py:method:: resetTitle(self) -> None
      :async:


   .. py:method:: savePlayers(self) -> None
      :async:


   .. py:method:: selectEntities(self, _0:CommandSender, _1:String) -> typing.List[:py:class:`Entity`]
      :async:


   .. py:method:: sendActionBar

       .. py:method:: sendActionBar(self, _0:Component) -> None
          :async:
          :noindex:

       .. py:method:: sendActionBar(self, _0:ComponentLike) -> None
          :async:
          :noindex:


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


   .. py:method:: setDefaultGameMode(self, _0:GameMode) -> None
      :async:


   .. py:method:: setIdleTimeout(self, _0:int) -> None
      :async:


   .. py:method:: setMaxPlayers(self, _0:int) -> None
      :async:


   .. py:method:: setSpawnRadius(self, _0:int) -> None
      :async:


   .. py:method:: setWhitelist(self, _0:boolean) -> None
      :async:


   .. py:method:: setWhitelistEnforced(self, _0:boolean) -> None
      :async:


   .. py:method:: shouldSendChatPreviews(self) -> bool
      :async:


   .. py:method:: showBossBar(self, _0:BossBar) -> None
      :async:


   .. py:method:: showTitle(self, _0:Title) -> None
      :async:


   .. py:method:: shutdown(self) -> None
      :async:


   .. py:method:: shutdownMessage(self) -> :py:class:`Component`
      :async:


   .. py:method:: stopSound

       .. py:method:: stopSound(self, _0:SoundStop) -> None
          :async:
          :noindex:

       .. py:method:: stopSound(self, _0:Sound) -> None
          :async:
          :noindex:


   .. py:method:: suggestPlayerNamesWhenNullTabCompletions(self) -> bool
      :async:


   .. py:method:: unbanIP(self, _0:String) -> None
      :async:


   .. py:method:: unloadWorld

       .. py:method:: unloadWorld(self, _0:String, _1:boolean) -> bool
          :async:
          :noindex:

       .. py:method:: unloadWorld(self, _0:World, _1:boolean) -> bool
          :async:
          :noindex:

