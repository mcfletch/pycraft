.. currentmodule:: pycraft.server.final

BiomeGrid
=========

Inheritance
------------
* pycraft.server.final.BiomeGrid
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.generator.ChunkGenerator.BiomeGrid <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/generator/ChunkGenerator/BiomeGrid.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: BiomeGrid(self, **named)
   :canonical: pycraft.server.final.BiomeGrid

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getBiome

       .. py:method:: getBiome(self, _0:int, _1:int) -> :py:class:`Biome`
          :async:
          :noindex:

       .. py:method:: getBiome(self, _0:int, _1:int, _2:int) -> :py:class:`Biome`
          :async:
          :noindex:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: setBiome

       .. py:method:: setBiome(self, _0:int, _1:int, _2:Biome) -> None
          :async:
          :noindex:

       .. py:method:: setBiome(self, _0:int, _1:int, _2:int, _3:Biome) -> None
          :async:
          :noindex:

