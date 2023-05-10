.. currentmodule:: pycraft.server.final

ChunkSnapshot
=============

Inheritance
------------
* pycraft.server.final.ChunkSnapshot
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.ChunkSnapshot <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/ChunkSnapshot.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: ChunkSnapshot(self, **named)
   :canonical: pycraft.server.final.ChunkSnapshot

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: contains

       .. py:method:: contains(self, _0:Biome) -> bool
          :async:
          :noindex:

       .. py:method:: contains(self, _0:BlockData) -> bool
          :async:
          :noindex:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getBiome

       .. py:method:: getBiome(self, _0:int, _1:int) -> :py:class:`Biome`
          :async:
          :noindex:

       .. py:method:: getBiome(self, _0:int, _1:int, _2:int) -> :py:class:`Biome`
          :async:
          :noindex:


   .. py:method:: getBlockData(self, _0:int, _1:int, _2:int) -> :py:class:`BlockData`
      :async:


   .. py:method:: getBlockEmittedLight(self, _0:int, _1:int, _2:int) -> int
      :async:


   .. py:method:: getBlockSkyLight(self, _0:int, _1:int, _2:int) -> int
      :async:


   .. py:method:: getBlockType(self, _0:int, _1:int, _2:int) -> :py:class:`Material`
      :async:


   .. py:method:: getCaptureFullTime(self) -> :py:class:`long`
      :async:


   .. py:method:: getData(self, _0:int, _1:int, _2:int) -> int
      :async:


   .. py:method:: getHighestBlockYAt(self, _0:int, _1:int) -> int
      :async:


   .. py:method:: getRawBiomeTemperature

       .. py:method:: getRawBiomeTemperature(self, _0:int, _1:int) -> float
          :async:
          :noindex:

       .. py:method:: getRawBiomeTemperature(self, _0:int, _1:int, _2:int) -> float
          :async:
          :noindex:


   .. py:method:: getWorldName(self) -> str
      :async:


   .. py:method:: getX(self) -> int
      :async:


   .. py:method:: getZ(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isSectionEmpty(self, _0:int) -> bool
      :async:

