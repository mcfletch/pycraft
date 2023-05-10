.. currentmodule:: pycraft.server.final

BiomeProvider
=============

Inheritance
------------
* pycraft.server.final.BiomeProvider
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.generator.BiomeProvider <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/generator/BiomeProvider.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: BiomeProvider(self, **named)
   :canonical: pycraft.server.final.BiomeProvider

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getBiome

       .. py:method:: getBiome(self, _0:WorldInfo, _1:int, _2:int, _3:int) -> :py:class:`Biome`
          :async:
          :noindex:

       .. py:method:: getBiome(self, _0:WorldInfo, _1:int, _2:int, _3:int, _4:BiomeParameterPoint) -> :py:class:`Biome`
          :async:
          :noindex:


   .. py:method:: getBiomes(self, _0:WorldInfo) -> typing.List[:py:class:`Biome`]
      :async:


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: toString(self) -> str
      :async:

