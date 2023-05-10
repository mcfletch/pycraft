.. currentmodule:: pycraft.server.final

PlayerInteractEvent
===================

Inheritance
------------
* pycraft.server.final.PlayerInteractEvent
* :py:class:`pycraft.server.final.Cancellable`
* :py:class:`pycraft.server.final.PlayerEvent`
* :py:class:`pycraft.server.final.Event`
* :py:class:`pycraft.server.world.Event`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.event.player.PlayerInteractEvent <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/event/player/PlayerInteractEvent.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: PlayerInteractEvent(self, **named)
   :canonical: pycraft.server.final.PlayerInteractEvent

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: callEvent(self) -> bool
      :async:


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getAction(self) -> :py:class:`Action`
      :async:


   .. py:method:: getBlockFace(self) -> :py:class:`BlockFace`
      :async:


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getClickedBlock(self) -> :py:class:`Block`
      :async:


   .. py:method:: getEventName(self) -> str
      :async:


   .. py:method:: getHand(self) -> :py:class:`EquipmentSlot`
      :async:


   .. py:method:: getHandlerList(cls) -> :py:class:`HandlerList`
      :async:
      :classmethod:


   .. py:method:: getHandlers(self) -> :py:class:`HandlerList`
      :async:


   .. py:method:: getInteractionPoint(self) -> :py:class:`Location`
      :async:


   .. py:method:: getItem(self) -> :py:class:`ItemStack`
      :async:


   .. py:method:: getMaterial(self) -> :py:class:`Material`
      :async:


   .. py:method:: getPlayer(self) -> :py:class:`Player`
      :async:


   .. py:method:: hasBlock(self) -> bool
      :async:


   .. py:method:: hasItem(self) -> bool
      :async:


   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isAsynchronous(self) -> bool
      :async:


   .. py:method:: isBlockInHand(self) -> bool
      :async:


   .. py:method:: isCancelled(self) -> bool
      :async:


   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: setCancelled(self, _0:boolean) -> None
      :async:


   .. py:method:: setUseInteractedBlock(self, _0:Result) -> None
      :async:


   .. py:method:: setUseItemInHand(self, _0:Result) -> None
      :async:


   .. py:method:: toString(self) -> str
      :async:


   .. py:method:: useInteractedBlock(self) -> :py:class:`Result`
      :async:


   .. py:method:: useItemInHand(self) -> :py:class:`Result`
      :async:

