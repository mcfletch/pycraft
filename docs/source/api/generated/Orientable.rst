.. currentmodule:: pycraft.server.final

Orientable
==========

Inheritance
------------
* pycraft.server.final.Orientable
* :py:class:`pycraft.server.final.BlockData`
* :py:class:`pycraft.server.world.BlockData`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.block.data.Orientable <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/block/data/Orientable.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Orientable(self, string_value=None, **named)
   :canonical: pycraft.server.final.Orientable

   Data describing a particular block (or a potential block)

   .. py:method:: __init__(self, string_value=None, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: from_server(named)
      

      Convert server-side structure to local object


   .. py:method:: getAsString(self) -> str
      :async:


   .. py:method:: getAxes(self) -> typing.List[:py:class:`Axis`]
      :async:


   .. py:method:: getAxis(self) -> :py:class:`Axis`
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


   .. py:method:: matches(self, _0:BlockData) -> bool
      :async:


   .. py:method:: merge(self, _0:BlockData) -> :py:class:`BlockData`
      :async:


   .. py:method:: requiresCorrectToolForDrops(self) -> bool
      :async:


   .. py:method:: setAxis(self, _0:Axis) -> None
      :async:

