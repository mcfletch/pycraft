.. currentmodule:: pycraft.server.final

ChunkGenerator
==============

Inheritance
------------
* pycraft.server.final.ChunkGenerator
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.generator.ChunkGenerator <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/generator/ChunkGenerator.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: ChunkGenerator(self, **named)
   :canonical: pycraft.server.final.ChunkGenerator

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: canSpawn(self, _0:World, _1:int, _2:int) -> bool
      :async:


   .. py:method:: createVanillaChunkData(self, _0:World, _1:int, _2:int) -> :py:class:`ChunkData`
      :async:


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: generateBedrock(self, _0:WorldInfo, _1:Random, _2:int, _3:int, _4:ChunkData) -> None
      :async:


   .. py:method:: generateCaves(self, _0:WorldInfo, _1:Random, _2:int, _3:int, _4:ChunkData) -> None
      :async:


   .. py:method:: generateChunkData(self, _0:World, _1:Random, _2:int, _3:int, _4:BiomeGrid) -> :py:class:`ChunkData`
      :async:


   .. py:method:: generateNoise(self, _0:WorldInfo, _1:Random, _2:int, _3:int, _4:ChunkData) -> None
      :async:


   .. py:method:: generateSurface(self, _0:WorldInfo, _1:Random, _2:int, _3:int, _4:ChunkData) -> None
      :async:


   .. py:method:: getBaseHeight(self, _0:WorldInfo, _1:Random, _2:int, _3:int, _4:HeightMap) -> int
      :async:


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getDefaultBiomeProvider(self, _0:WorldInfo) -> :py:class:`BiomeProvider`
      :async:


   .. py:method:: getDefaultPopulators(self, _0:World) -> typing.List[:py:class:`BlockPopulator`]
      :async:


   .. py:method:: getFixedSpawnLocation(self, _0:World, _1:Random) -> :py:class:`Location`
      :async:


   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isParallelCapable(self) -> bool
      :async:


   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: shouldGenerateBedrock(self) -> bool
      :async:


   .. py:method:: shouldGenerateCaves

       .. py:method:: shouldGenerateCaves(self) -> bool
          :async:
          :noindex:

       .. py:method:: shouldGenerateCaves(self, _0:WorldInfo, _1:Random, _2:int, _3:int) -> bool
          :async:
          :noindex:


   .. py:method:: shouldGenerateDecorations

       .. py:method:: shouldGenerateDecorations(self) -> bool
          :async:
          :noindex:

       .. py:method:: shouldGenerateDecorations(self, _0:WorldInfo, _1:Random, _2:int, _3:int) -> bool
          :async:
          :noindex:


   .. py:method:: shouldGenerateMobs

       .. py:method:: shouldGenerateMobs(self) -> bool
          :async:
          :noindex:

       .. py:method:: shouldGenerateMobs(self, _0:WorldInfo, _1:Random, _2:int, _3:int) -> bool
          :async:
          :noindex:


   .. py:method:: shouldGenerateNoise

       .. py:method:: shouldGenerateNoise(self) -> bool
          :async:
          :noindex:

       .. py:method:: shouldGenerateNoise(self, _0:WorldInfo, _1:Random, _2:int, _3:int) -> bool
          :async:
          :noindex:


   .. py:method:: shouldGenerateStructures

       .. py:method:: shouldGenerateStructures(self) -> bool
          :async:
          :noindex:

       .. py:method:: shouldGenerateStructures(self, _0:WorldInfo, _1:Random, _2:int, _3:int) -> bool
          :async:
          :noindex:


   .. py:method:: shouldGenerateSurface

       .. py:method:: shouldGenerateSurface(self) -> bool
          :async:
          :noindex:

       .. py:method:: shouldGenerateSurface(self, _0:WorldInfo, _1:Random, _2:int, _3:int) -> bool
          :async:
          :noindex:


   .. py:method:: toString(self) -> str
      :async:

