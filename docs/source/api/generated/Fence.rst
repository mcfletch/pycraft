.. currentmodule:: pycraft.server.final

Fence
=====

Inheritance
------------
* pycraft.server.final.Fence
* :py:class:`pycraft.server.world.Fence`
* :py:class:`pycraft.server.final.MultipleFacing`
* :py:class:`pycraft.server.final.Waterlogged`
* :py:class:`pycraft.server.final.BlockData`
* :py:class:`pycraft.server.world.BlockData`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.block.data.type.Fence <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/block/data/type/Fence.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Fence(self, string_value=None, **named)
   :canonical: pycraft.server.final.Fence

   Data describing a particular block (or a potential block)

   .. py:method:: __init__(self, string_value=None, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: from_server(named)
      

      Convert server-side structure to local object


   .. py:method:: getAllowedFaces(self) -> typing.List[:py:class:`BlockFace`]
      :async:


   .. py:method:: getAsString(self) -> str
      :async:


   .. py:method:: getFaces(self) -> typing.List[:py:class:`BlockFace`]
      :async:


   .. py:method:: getLightEmission(self) -> int
      :async:


   .. py:method:: getMaterial(self) -> :py:class:`Material`
      :async:


   .. py:method:: getPistonMoveReaction(self) -> :py:class:`PistonMoveReaction`
      :async:


   .. py:method:: getPlacementMaterial(self) -> :py:class:`Material`
      :async:


   .. py:method:: getSoundGroup(self) -> :py:class:`SoundGroup`
      :async:


   .. py:method:: get_key(self)
      

   .. py:method:: hasFace(self, _0:BlockFace) -> bool
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isFaceSturdy(self, _0:BlockFace, _1:BlockSupport) -> bool
      :async:


   .. py:method:: isOccluding(self) -> bool
      :async:


   .. py:method:: isPreferredTool(self, _0:ItemStack) -> bool
      :async:


   .. py:method:: isRandomlyTicked(self) -> bool
      :async:


   .. py:method:: isSupported

       .. py:method:: isSupported(self, _0:Block) -> bool
          :async:
          :noindex:

       .. py:method:: isSupported(self, _0:Location) -> bool
          :async:
          :noindex:


   .. py:method:: isWaterlogged(self) -> bool
      :async:


   .. py:method:: matches(self, _0:BlockData) -> bool
      :async:


   .. py:method:: merge(self, _0:BlockData) -> :py:class:`BlockData`
      :async:


   .. py:method:: requiresCorrectToolForDrops(self) -> bool
      :async:


   .. py:method:: setFace(self, _0:BlockFace, _1:boolean) -> None
      :async:


   .. py:method:: setWaterlogged(self, _0:boolean) -> None
      :async:

