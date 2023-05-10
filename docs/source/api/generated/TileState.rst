.. currentmodule:: pycraft.server.final

TileState
=========

Inheritance
------------
* pycraft.server.final.TileState
* :py:class:`pycraft.server.final.BlockState`
* :py:class:`pycraft.server.final.Metadatable`
* :py:class:`pycraft.server.final.PersistentDataHolder`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.block.TileState <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/block/TileState.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: TileState(self, **named)
   :canonical: pycraft.server.final.TileState

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getBlock(self) -> :py:class:`Block`
      :async:


   .. py:method:: getBlockData(self) -> :py:class:`BlockData`
      :async:


   .. py:method:: getChunk(self) -> :py:class:`Chunk`
      :async:


   .. py:method:: getData(self) -> :py:class:`MaterialData`
      :async:


   .. py:method:: getDrops

       .. py:method:: getDrops(self) -> typing.List[:py:class:`ItemStack`]
          :async:
          :noindex:

       .. py:method:: getDrops(self, _0:ItemStack) -> typing.List[:py:class:`ItemStack`]
          :async:
          :noindex:

       .. py:method:: getDrops(self, _0:ItemStack, _1:Entity) -> typing.List[:py:class:`ItemStack`]
          :async:
          :noindex:


   .. py:method:: getLightLevel(self) -> :py:class:`byte`
      :async:


   .. py:method:: getLocation

       .. py:method:: getLocation(self) -> :py:class:`Location`
          :async:
          :noindex:

       .. py:method:: getLocation(self, _0:Location) -> :py:class:`Location`
          :async:
          :noindex:


   .. py:method:: getMetadata(self, _0:String) -> typing.List[:py:class:`MetadataValue`]
      :async:


   .. py:method:: getPersistentDataContainer(self) -> :py:class:`PersistentDataContainer`
      :async:


   .. py:method:: getRawData(self) -> :py:class:`byte`
      :async:


   .. py:method:: getType(self) -> :py:class:`Material`
      :async:


   .. py:method:: getWorld(self) -> :py:class:`World`
      :async:


   .. py:method:: getX(self) -> int
      :async:


   .. py:method:: getY(self) -> int
      :async:


   .. py:method:: getZ(self) -> int
      :async:


   .. py:method:: hasMetadata(self, _0:String) -> bool
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isCollidable(self) -> bool
      :async:


   .. py:method:: isPlaced(self) -> bool
      :async:


   .. py:method:: isSnapshot(self) -> bool
      :async:


   .. py:method:: removeMetadata(self, _0:String, _1:Plugin) -> None
      :async:


   .. py:method:: setBlockData(self, _0:BlockData) -> None
      :async:


   .. py:method:: setData(self, _0:MaterialData) -> None
      :async:


   .. py:method:: setMetadata(self, _0:String, _1:MetadataValue) -> None
      :async:


   .. py:method:: setRawData(self, _0:byte) -> None
      :async:


   .. py:method:: setType(self, _0:Material) -> None
      :async:


   .. py:method:: update

       .. py:method:: update(self) -> bool
          :async:
          :noindex:

       .. py:method:: update(self, _0:boolean) -> bool
          :async:
          :noindex:

       .. py:method:: update(self, _0:boolean, _1:boolean) -> bool
          :async:
          :noindex:

