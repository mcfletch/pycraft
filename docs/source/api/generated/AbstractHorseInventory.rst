.. currentmodule:: pycraft.server.final

AbstractHorseInventory
======================

Inheritance
------------
* pycraft.server.final.AbstractHorseInventory
* :py:class:`pycraft.server.final.Inventory`
* :py:class:`pycraft.server.world.Inventory`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.inventory.AbstractHorseInventory <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/inventory/AbstractHorseInventory.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: AbstractHorseInventory(self, *args, **named)
   :canonical: pycraft.server.final.AbstractHorseInventory

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, *args, **named)
      

      Initialize self.  See help(type(self)) for accurate signature.


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: addItem(self, _0:ItemStack[]) -> :py:class:`HashMap`
      :async:


   .. py:method:: all

       .. py:method:: all(self, _0:ItemStack) -> :py:class:`HashMap`
          :async:
          :noindex:

       .. py:method:: all(self, _0:Material) -> :py:class:`HashMap`
          :async:
          :noindex:


   .. py:method:: clear

       .. py:method:: clear(self) -> None
          :async:
          :noindex:

       .. py:method:: clear(self, _0:int) -> None
          :async:
          :noindex:


   .. py:method:: close(self) -> int
      :async:


   .. py:method:: contains

       .. py:method:: contains(self, _0:ItemStack) -> bool
          :async:
          :noindex:

       .. py:method:: contains(self, _0:Material) -> bool
          :async:
          :noindex:

       .. py:method:: contains(self, _0:ItemStack, _1:int) -> bool
          :async:
          :noindex:

       .. py:method:: contains(self, _0:Material, _1:int) -> bool
          :async:
          :noindex:


   .. py:method:: containsAtLeast(self, _0:ItemStack, _1:int) -> bool
      :async:


   .. py:method:: empty_slots(self)
      

      Local introspection to find empty content slots


   .. py:method:: first

       .. py:method:: first(self, _0:Material) -> int
          :async:
          :noindex:

       .. py:method:: first(self, _0:ItemStack) -> int
          :async:
          :noindex:


   .. py:method:: firstEmpty(self) -> int
      :async:


   .. py:method:: forEach(self, _0:Consumer) -> None
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getContents(self) -> typing.List[:py:class:`ItemStack`]
      :async:


   .. py:method:: getHolder

       .. py:method:: getHolder(self) -> :py:class:`InventoryHolder`
          :async:
          :noindex:

       .. py:method:: getHolder(self, _0:boolean) -> :py:class:`InventoryHolder`
          :async:
          :noindex:


   .. py:method:: getItem(self, _0:int) -> :py:class:`ItemStack`
      :async:


   .. py:method:: getLocation(self) -> :py:class:`Location`
      :async:


   .. py:method:: getMaxStackSize(self) -> int
      :async:


   .. py:method:: getSaddle(self) -> :py:class:`ItemStack`
      :async:


   .. py:method:: getSize(self) -> int
      :async:


   .. py:method:: getStorageContents(self) -> typing.List[:py:class:`ItemStack`]
      :async:


   .. py:method:: getType(self) -> :py:class:`InventoryType`
      :async:


   .. py:method:: getViewers(self) -> typing.List[:py:class:`HumanEntity`]
      :async:


   .. py:method:: get_key(self)
      

   .. py:method:: get_stack(self, index)
      

   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isEmpty(self) -> bool
      :async:


   .. py:method:: iterator

       .. py:method:: iterator(self) -> :py:class:`Iterator`
          :async:
          :noindex:

       .. py:method:: iterator(self) -> :py:class:`ListIterator`
          :async:
          :noindex:

       .. py:method:: iterator(self, _0:int) -> :py:class:`ListIterator`
          :async:
          :noindex:


   .. py:method:: remove

       .. py:method:: remove(self, _0:ItemStack) -> None
          :async:
          :noindex:

       .. py:method:: remove(self, _0:Material) -> None
          :async:
          :noindex:


   .. py:method:: removeItem(self, _0:ItemStack[]) -> :py:class:`HashMap`
      :async:


   .. py:method:: removeItemAnySlot(self, _0:ItemStack[]) -> :py:class:`HashMap`
      :async:


   .. py:method:: setContents(self, _0:ItemStack[]) -> None
      :async:


   .. py:method:: setItem(self, _0:int, _1:ItemStack) -> None
      :async:


   .. py:method:: setMaxStackSize(self, _0:int) -> None
      :async:


   .. py:method:: setSaddle(self, _0:ItemStack) -> None
      :async:


   .. py:method:: setStorageContents(self, _0:ItemStack[]) -> None
      :async:


   .. py:method:: spliterator(self) -> :py:class:`Spliterator`
      :async:

