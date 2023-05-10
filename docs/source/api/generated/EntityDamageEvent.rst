.. currentmodule:: pycraft.server.final

EntityDamageEvent
=================

Inheritance
------------
* pycraft.server.final.EntityDamageEvent
* :py:class:`pycraft.server.final.Cancellable`
* :py:class:`pycraft.server.final.EntityEvent`
* :py:class:`pycraft.server.world.EntityEvent`
* :py:class:`pycraft.server.final.Event`
* :py:class:`pycraft.server.world.Event`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.event.entity.EntityDamageEvent <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/event/entity/EntityDamageEvent.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: EntityDamageEvent(self, **named)
   :canonical: pycraft.server.final.EntityDamageEvent

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


   .. py:method:: getCause(self) -> :py:class:`DamageCause`
      :async:


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getDamage

       .. py:method:: getDamage(self) -> float
          :async:
          :noindex:

       .. py:method:: getDamage(self, _0:DamageModifier) -> float
          :async:
          :noindex:


   .. py:method:: getEntity(self) -> :py:class:`Entity`
      :async:


   .. py:method:: getEntityType(self) -> :py:class:`EntityType`
      :async:


   .. py:method:: getEventName(self) -> str
      :async:


   .. py:method:: getFinalDamage(self) -> float
      :async:


   .. py:method:: getHandlerList(cls) -> :py:class:`HandlerList`
      :async:
      :classmethod:


   .. py:method:: getHandlers(self) -> :py:class:`HandlerList`
      :async:


   .. py:method:: getOriginalDamage(self, _0:DamageModifier) -> float
      :async:


   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isApplicable(self, _0:DamageModifier) -> bool
      :async:


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


   .. py:method:: setDamage

       .. py:method:: setDamage(self, _0:double) -> None
          :async:
          :noindex:

       .. py:method:: setDamage(self, _0:DamageModifier, _1:double) -> None
          :async:
          :noindex:


   .. py:method:: toString(self) -> str
      :async:

