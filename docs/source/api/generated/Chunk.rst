.. currentmodule:: pycraft.server.final

Chunk
=====

Inheritance
------------
* pycraft.server.final.Chunk
* :py:class:`pycraft.server.final.PersistentDataHolder`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.Chunk <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Chunk.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Chunk(self, **named)
   :canonical: pycraft.server.final.Chunk

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: addPluginChunkTicket(self, _0:Plugin) -> bool
      :async:


   .. py:method:: contains

       .. py:method:: contains(self, _0:Biome) -> bool
          :async:
          :noindex:

       .. py:method:: contains(self, _0:BlockData) -> bool
          :async:
          :noindex:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getBlock(self, _0:int, _1:int, _2:int) -> :py:class:`Block`
      :async:


   .. py:method:: getChunkKey

       .. py:method:: getChunkKey(self) -> :py:class:`long`
          :async:
          :noindex:

       .. py:method:: getChunkKey(cls, _0:Location) -> :py:class:`long`
          :async:
          :classmethod:
          :noindex:

       .. py:method:: getChunkKey(cls, _0:int, _1:int) -> :py:class:`long`
          :async:
          :classmethod:
          :noindex:


   .. py:method:: getChunkSnapshot

       .. py:method:: getChunkSnapshot(self) -> :py:class:`ChunkSnapshot`
          :async:
          :noindex:

       .. py:method:: getChunkSnapshot(self, _0:boolean, _1:boolean, _2:boolean) -> :py:class:`ChunkSnapshot`
          :async:
          :noindex:


   .. py:method:: getEntities(self) -> typing.List[:py:class:`Entity`]
      :async:


   .. py:method:: getInhabitedTime(self) -> :py:class:`long`
      :async:


   .. py:method:: getPersistentDataContainer(self) -> :py:class:`PersistentDataContainer`
      :async:


   .. py:method:: getPluginChunkTickets(self) -> typing.List[:py:class:`Plugin`]
      :async:


   .. py:method:: getTileEntities

       .. py:method:: getTileEntities(self) -> typing.List[:py:class:`BlockState`]
          :async:
          :noindex:

       .. py:method:: getTileEntities(self, _0:boolean) -> typing.List[:py:class:`BlockState`]
          :async:
          :noindex:

       .. py:method:: getTileEntities(self, _0:Predicate, _1:boolean) -> typing.List[:py:class:`BlockState`]
          :async:
          :noindex:


   .. py:method:: getWorld(self) -> :py:class:`World`
      :async:


   .. py:method:: getX(self) -> int
      :async:


   .. py:method:: getZ(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isEntitiesLoaded(self) -> bool
      :async:


   .. py:method:: isForceLoaded(self) -> bool
      :async:


   .. py:method:: isLoaded(self) -> bool
      :async:


   .. py:method:: isSlimeChunk(self) -> bool
      :async:


   .. py:method:: load

       .. py:method:: load(self) -> bool
          :async:
          :noindex:

       .. py:method:: load(self, _0:boolean) -> bool
          :async:
          :noindex:


   .. py:method:: removePluginChunkTicket(self, _0:Plugin) -> bool
      :async:


   .. py:method:: setForceLoaded(self, _0:boolean) -> None
      :async:


   .. py:method:: setInhabitedTime(self, _0:long) -> None
      :async:


   .. py:method:: unload

       .. py:method:: unload(self) -> bool
          :async:
          :noindex:

       .. py:method:: unload(self, _0:boolean) -> bool
          :async:
          :noindex:

