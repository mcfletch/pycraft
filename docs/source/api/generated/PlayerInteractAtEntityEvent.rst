.. currentmodule:: pycraft.server.final

PlayerInteractAtEntityEvent
===========================

Inheritance
------------
* pycraft.server.final.PlayerInteractAtEntityEvent
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.event.player.PlayerInteractAtEntityEvent <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/event/player/PlayerInteractAtEntityEvent.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: PlayerInteractAtEntityEvent(self, **named)
   :canonical: pycraft.server.final.PlayerInteractAtEntityEvent

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


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getClickedPosition(self) -> :py:class:`Vector`
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


   .. py:method:: getPlayer(self) -> :py:class:`Player`
      :async:


   .. py:method:: getRightClicked(self) -> :py:class:`Entity`
      :async:


   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isAsynchronous(self) -> bool
      :async:


   .. py:method:: isCancelled(self) -> bool
      :async:


   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: setCancelled(self, _0:boolean) -> None
      :async:


   .. py:method:: toString(self) -> str
      :async:

