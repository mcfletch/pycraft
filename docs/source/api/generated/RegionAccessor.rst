.. currentmodule:: pycraft.server.final

RegionAccessor
==============

Inheritance
------------
* pycraft.server.final.RegionAccessor
* :py:class:`pycraft.server.proxyobjects.KeyedServerObjectEnum`
* :py:class:`pycraft.server.proxyobjects.ServerObjectEnum`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.RegionAccessor <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/RegionAccessor.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: RegionAccessor(self, key)
   :canonical: pycraft.server.final.RegionAccessor

   Namespaced/keyed enumerations

   .. py:method:: __init__(self, key)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: cached_values()
      :async:

      Get the cached values for the given enumeration


   .. py:method:: from_server(key)
      

      Convert server-side structure to local object


   .. py:method:: generateTree

       .. py:method:: generateTree(self, _0:Location, _1:Random, _2:TreeType) -> bool
          :async:
          :noindex:

       .. py:method:: generateTree(self, _0:Location, _1:Random, _2:TreeType, _3:Predicate) -> bool
          :async:
          :noindex:

       .. py:method:: generateTree(self, _0:Location, _1:Random, _2:TreeType, _3:Consumer) -> bool
          :async:
          :noindex:


   .. py:method:: getBiome

       .. py:method:: getBiome(self, _0:Location) -> :py:class:`Biome`
          :async:
          :noindex:

       .. py:method:: getBiome(self, _0:int, _1:int, _2:int) -> :py:class:`Biome`
          :async:
          :noindex:


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


   .. py:method:: getComputedBiome(self, _0:int, _1:int, _2:int) -> :py:class:`Biome`
      :async:


   .. py:method:: getEntities(self) -> typing.List[:py:class:`Entity`]
      :async:


   .. py:method:: getEntitiesByClass(self, _0:Class) -> typing.List[:py:class:`T`]
      :async:


   .. py:method:: getEntitiesByClasses(self, _0:Class[]) -> typing.List[:py:class:`Entity`]
      :async:


   .. py:method:: getKey(self) -> :py:class:`NamespacedKey`
      :async:


   .. py:method:: getLivingEntities(self) -> typing.List[:py:class:`LivingEntity`]
      :async:


   .. py:method:: getMoonPhase(self) -> :py:class:`MoonPhase`
      :async:


   .. py:method:: getType

       .. py:method:: getType(self, _0:Location) -> :py:class:`Material`
          :async:
          :noindex:

       .. py:method:: getType(self, _0:int, _1:int, _2:int) -> :py:class:`Material`
          :async:
          :noindex:


   .. py:method:: get_key(self)
      

   .. py:method:: hasCollisionsIn(self, _0:BoundingBox) -> bool
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: key(self) -> :py:class:`Key`
      :async:


   .. py:method:: lineOfSightExists(self, _0:Location, _1:Location) -> bool
      :async:


   .. py:method:: loosely_match(name)
      :async:

   .. py:method:: setBiome

       .. py:method:: setBiome(self, _0:Location, _1:Biome) -> None
          :async:
          :noindex:

       .. py:method:: setBiome(self, _0:int, _1:int, _2:int, _3:Biome) -> None
          :async:
          :noindex:


   .. py:method:: setBlockData

       .. py:method:: setBlockData(self, _0:Location, _1:BlockData) -> None
          :async:
          :noindex:

       .. py:method:: setBlockData(self, _0:int, _1:int, _2:int, _3:BlockData) -> None
          :async:
          :noindex:


   .. py:method:: setType

       .. py:method:: setType(self, _0:Location, _1:Material) -> None
          :async:
          :noindex:

       .. py:method:: setType(self, _0:int, _1:int, _2:int, _3:Material) -> None
          :async:
          :noindex:


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


   .. py:method:: values()
      :async:

      Get the enumerated values in this class

