.. currentmodule:: pycraft.server.final

Biome
=====

Inheritance
------------
* pycraft.server.final.Biome
* :py:class:`pycraft.server.world.Biome`
* :py:class:`pycraft.server.proxyobjects.KeyedServerObjectEnum`
* :py:class:`pycraft.server.proxyobjects.ServerObjectEnum`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.block.Biome <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/block/Biome.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Biome(self, key)
   :canonical: pycraft.server.final.Biome

   Namespaced/keyed enumerations

   .. py:method:: __init__(self, key)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: cached_values()
      :async:

      Get the cached values for the given enumeration


   .. py:method:: compareTo

       .. py:method:: compareTo(self, _0:Object) -> int
          :async:
          :noindex:

       .. py:method:: compareTo(self, _0:Enum) -> int
          :async:
          :noindex:


   .. py:method:: describeConstable(self) -> :py:class:`Optional`
      :async:


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: from_server(key)
      

      Convert server-side structure to local object


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getDeclaringClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getKey(self) -> :py:class:`NamespacedKey`
      :async:


   .. py:method:: get_key(self)
      

   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: key(self) -> :py:class:`Key`
      :async:


   .. py:method:: loosely_match(name)
      :async:

   .. py:method:: name(self) -> str
      :async:


   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: ordinal(self) -> int
      :async:


   .. py:method:: toString(self) -> str
      :async:


   .. py:method:: translationKey(self) -> str
      :async:


   .. py:method:: valueOf

       .. py:method:: valueOf(cls, _0:String) -> :py:class:`Biome`
          :async:
          :classmethod:
          :noindex:

       .. py:method:: valueOf(cls, _0:Class, _1:String) -> :py:class:`Enum`
          :async:
          :classmethod:
          :noindex:


   .. py:method:: values(cls) -> typing.List[:py:class:`Biome`]
      :async:
      :classmethod:


Values
-------

* minecraft:ocean
* minecraft:plains
* minecraft:desert
* minecraft:windswept_hills
* minecraft:forest
* minecraft:taiga
* minecraft:swamp
* minecraft:mangrove_swamp
* minecraft:river
* minecraft:nether_wastes
* minecraft:the_end
* minecraft:frozen_ocean
* minecraft:frozen_river
* minecraft:snowy_plains
* minecraft:mushroom_fields
* minecraft:beach
* minecraft:jungle
* minecraft:sparse_jungle
* minecraft:deep_ocean
* minecraft:stony_shore
* minecraft:snowy_beach
* minecraft:birch_forest
* minecraft:dark_forest
* minecraft:snowy_taiga
* minecraft:old_growth_pine_taiga
* minecraft:windswept_forest
* minecraft:savanna
* minecraft:savanna_plateau
* minecraft:badlands
* minecraft:wooded_badlands
* minecraft:small_end_islands
* minecraft:end_midlands
* minecraft:end_highlands
* minecraft:end_barrens
* minecraft:warm_ocean
* minecraft:lukewarm_ocean
* minecraft:cold_ocean
* minecraft:deep_lukewarm_ocean
* minecraft:deep_cold_ocean
* minecraft:deep_frozen_ocean
* minecraft:the_void
* minecraft:sunflower_plains
* minecraft:windswept_gravelly_hills
* minecraft:flower_forest
* minecraft:ice_spikes
* minecraft:old_growth_birch_forest
* minecraft:old_growth_spruce_taiga
* minecraft:windswept_savanna
* minecraft:eroded_badlands
* minecraft:bamboo_jungle
* minecraft:soul_sand_valley
* minecraft:crimson_forest
* minecraft:warped_forest
* minecraft:basalt_deltas
* minecraft:dripstone_caves
* minecraft:lush_caves
* minecraft:deep_dark
* minecraft:meadow
* minecraft:grove
* minecraft:snowy_slopes
* minecraft:frozen_peaks
* minecraft:jagged_peaks
* minecraft:stony_peaks
* minecraft:cherry_grove
* minecraft:custom
