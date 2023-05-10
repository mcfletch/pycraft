.. currentmodule:: pycraft.server.final

EntityEvent
===========

Inheritance
------------
* pycraft.server.final.EntityEvent
* :py:class:`pycraft.server.world.EntityEvent`
* :py:class:`pycraft.server.final.Event`
* :py:class:`pycraft.server.world.Event`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.event.entity.EntityEvent <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/event/entity/EntityEvent.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: EntityEvent(self, **named)
   :canonical: pycraft.server.final.EntityEvent

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


   .. py:method:: getEntity(self) -> :py:class:`Entity`
      :async:


   .. py:method:: getEntityType(self) -> :py:class:`EntityType`
      :async:


   .. py:method:: getEventName(self) -> str
      :async:


   .. py:method:: getHandlers(self) -> :py:class:`HandlerList`
      :async:


   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isAsynchronous(self) -> bool
      :async:


   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: toString(self) -> str
      :async:

