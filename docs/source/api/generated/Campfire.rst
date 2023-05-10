.. currentmodule:: pycraft.server.final

Campfire
========

Inheritance
------------
* pycraft.server.final.Campfire
* :py:class:`pycraft.server.world.Campfire`
* :py:class:`pycraft.server.final.Directional`
* :py:class:`pycraft.server.final.Lightable`
* :py:class:`pycraft.server.final.Waterlogged`
* :py:class:`pycraft.server.final.BlockData`
* :py:class:`pycraft.server.world.BlockData`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.block.data.type.Campfire <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/block/data/type/Campfire.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Campfire(self, string_value=None, **named)
   :canonical: pycraft.server.final.Campfire

   Data describing a particular block (or a potential block)

   .. py:method:: __init__(self, string_value=None, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: from_server(named)
      

      Convert server-side structure to local object


   .. py:method:: getAsString(self) -> str
      :async:


   .. py:method:: getFaces(self) -> typing.List[:py:class:`BlockFace`]
      :async:


   .. py:method:: getFacing(self) -> :py:class:`BlockFace`
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
      

   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isFaceSturdy(self, _0:BlockFace, _1:BlockSupport) -> bool
      :async:


   .. py:method:: isLit(self) -> bool
      :async:


   .. py:method:: isOccluding(self) -> bool
      :async:


   .. py:method:: isPreferredTool(self, _0:ItemStack) -> bool
      :async:


   .. py:method:: isRandomlyTicked(self) -> bool
      :async:


   .. py:method:: isSignalFire(self) -> bool
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


   .. py:method:: setFacing(self, _0:BlockFace) -> None
      :async:


   .. py:method:: setLit(self, _0:boolean) -> None
      :async:


   .. py:method:: setSignalFire(self, _0:boolean) -> None
      :async:


   .. py:method:: setWaterlogged(self, _0:boolean) -> None
      :async:

