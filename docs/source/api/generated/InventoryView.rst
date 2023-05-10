.. currentmodule:: pycraft.server.final

InventoryView
=============

Inheritance
------------
* pycraft.server.final.InventoryView
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.inventory.InventoryView <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/inventory/InventoryView.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: InventoryView(self, **named)
   :canonical: pycraft.server.final.InventoryView

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: close(self) -> None
      :async:


   .. py:method:: convertSlot(self, _0:int) -> int
      :async:


   .. py:method:: countSlots(self) -> int
      :async:


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getBottomInventory(self) -> :py:class:`Inventory`
      :async:


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getCursor(self) -> :py:class:`ItemStack`
      :async:


   .. py:method:: getInventory(self, _0:int) -> :py:class:`Inventory`
      :async:


   .. py:method:: getItem(self, _0:int) -> :py:class:`ItemStack`
      :async:


   .. py:method:: getPlayer(self) -> :py:class:`HumanEntity`
      :async:


   .. py:method:: getSlotType(self, _0:int) -> :py:class:`SlotType`
      :async:


   .. py:method:: getTitle(self) -> str
      :async:


   .. py:method:: getTopInventory(self) -> :py:class:`Inventory`
      :async:


   .. py:method:: getType(self) -> :py:class:`InventoryType`
      :async:


   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: setCursor(self, _0:ItemStack) -> None
      :async:


   .. py:method:: setItem(self, _0:int, _1:ItemStack) -> None
      :async:


   .. py:method:: setProperty(self, _0:Property, _1:int) -> bool
      :async:


   .. py:method:: title(self) -> :py:class:`Component`
      :async:


   .. py:method:: toString(self) -> str
      :async:

