.. currentmodule:: pycraft.server.final

LootContext
===========

Inheritance
------------
* pycraft.server.final.LootContext
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.loot.LootContext <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/loot/LootContext.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: LootContext(self, **named)
   :canonical: pycraft.server.final.LootContext

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getKiller(self) -> :py:class:`HumanEntity`
      :async:


   .. py:method:: getLocation(self) -> :py:class:`Location`
      :async:


   .. py:method:: getLootedEntity(self) -> :py:class:`Entity`
      :async:


   .. py:method:: getLootingModifier(self) -> int
      :async:


   .. py:method:: getLuck(self) -> float
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

