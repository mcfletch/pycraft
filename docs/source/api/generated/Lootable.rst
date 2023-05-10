.. currentmodule:: pycraft.server.final

Lootable
========

Inheritance
------------
* pycraft.server.final.Lootable
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.loot.Lootable <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/loot/Lootable.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Lootable(self, **named)
   :canonical: pycraft.server.final.Lootable

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: clearLootTable(self) -> None
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getLootTable(self) -> :py:class:`LootTable`
      :async:


   .. py:method:: getSeed(self) -> :py:class:`long`
      :async:


   .. py:method:: hasLootTable(self) -> bool
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: setLootTable

       .. py:method:: setLootTable(self, _0:LootTable) -> None
          :async:
          :noindex:

       .. py:method:: setLootTable(self, _0:LootTable, _1:long) -> None
          :async:
          :noindex:


   .. py:method:: setSeed(self, _0:long) -> None
      :async:

