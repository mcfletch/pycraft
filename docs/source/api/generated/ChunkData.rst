.. currentmodule:: pycraft.server.final

ChunkData
=========

Inheritance
------------
* pycraft.server.final.ChunkData
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.generator.ChunkGenerator.ChunkData <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/generator/ChunkGenerator/ChunkData.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: ChunkData(self, **named)
   :canonical: pycraft.server.final.ChunkData

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getBiome(self, _0:int, _1:int, _2:int) -> :py:class:`Biome`
      :async:


   .. py:method:: getBlockData(self, _0:int, _1:int, _2:int) -> :py:class:`BlockData`
      :async:


   .. py:method:: getData(self, _0:int, _1:int, _2:int) -> :py:class:`byte`
      :async:


   .. py:method:: getMaxHeight(self) -> int
      :async:


   .. py:method:: getMinHeight(self) -> int
      :async:


   .. py:method:: getType(self, _0:int, _1:int, _2:int) -> :py:class:`Material`
      :async:


   .. py:method:: getTypeAndData(self, _0:int, _1:int, _2:int) -> :py:class:`MaterialData`
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: setBlock

       .. py:method:: setBlock(self, _0:int, _1:int, _2:int, _3:MaterialData) -> None
          :async:
          :noindex:

       .. py:method:: setBlock(self, _0:int, _1:int, _2:int, _3:BlockData) -> None
          :async:
          :noindex:

       .. py:method:: setBlock(self, _0:int, _1:int, _2:int, _3:Material) -> None
          :async:
          :noindex:


   .. py:method:: setRegion

       .. py:method:: setRegion(self, _0:int, _1:int, _2:int, _3:int, _4:int, _5:int, _6:MaterialData) -> None
          :async:
          :noindex:

       .. py:method:: setRegion(self, _0:int, _1:int, _2:int, _3:int, _4:int, _5:int, _6:BlockData) -> None
          :async:
          :noindex:

       .. py:method:: setRegion(self, _0:int, _1:int, _2:int, _3:int, _4:int, _5:int, _6:Material) -> None
          :async:
          :noindex:

