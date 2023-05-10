.. currentmodule:: pycraft.server.final

PlayerInventory
===============

Inheritance
------------
* pycraft.server.final.PlayerInventory
* :py:class:`pycraft.server.final.Inventory`
* :py:class:`pycraft.server.world.Inventory`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.inventory.PlayerInventory <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/inventory/PlayerInventory.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: PlayerInventory(self, *args, **named)
   :canonical: pycraft.server.final.PlayerInventory

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


   .. py:method:: getArmorContents(self) -> typing.List[:py:class:`ItemStack`]
      :async:


   .. py:method:: getBoots(self) -> :py:class:`ItemStack`
      :async:


   .. py:method:: getChestplate(self) -> :py:class:`ItemStack`
      :async:


   .. py:method:: getContents(self) -> typing.List[:py:class:`ItemStack`]
      :async:


   .. py:method:: getExtraContents(self) -> typing.List[:py:class:`ItemStack`]
      :async:


   .. py:method:: getHeldItemSlot(self) -> int
      :async:


   .. py:method:: getHelmet(self) -> :py:class:`ItemStack`
      :async:


   .. py:method:: getHolder

       .. py:method:: getHolder(self) -> :py:class:`InventoryHolder`
          :async:
          :noindex:

       .. py:method:: getHolder(self) -> :py:class:`HumanEntity`
          :async:
          :noindex:

       .. py:method:: getHolder(self, _0:boolean) -> :py:class:`InventoryHolder`
          :async:
          :noindex:


   .. py:method:: getItem

       .. py:method:: getItem(self, _0:EquipmentSlot) -> :py:class:`ItemStack`
          :async:
          :noindex:

       .. py:method:: getItem(self, _0:int) -> :py:class:`ItemStack`
          :async:
          :noindex:


   .. py:method:: getItemInHand(self) -> :py:class:`ItemStack`
      :async:


   .. py:method:: getItemInMainHand(self) -> :py:class:`ItemStack`
      :async:


   .. py:method:: getItemInOffHand(self) -> :py:class:`ItemStack`
      :async:


   .. py:method:: getLeggings(self) -> :py:class:`ItemStack`
      :async:


   .. py:method:: getLocation(self) -> :py:class:`Location`
      :async:


   .. py:method:: getMaxStackSize(self) -> int
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


   .. py:method:: setArmorContents(self, _0:ItemStack[]) -> None
      :async:


   .. py:method:: setBoots(self, _0:ItemStack) -> None
      :async:


   .. py:method:: setChestplate(self, _0:ItemStack) -> None
      :async:


   .. py:method:: setContents(self, _0:ItemStack[]) -> None
      :async:


   .. py:method:: setExtraContents(self, _0:ItemStack[]) -> None
      :async:


   .. py:method:: setHeldItemSlot(self, _0:int) -> None
      :async:


   .. py:method:: setHelmet(self, _0:ItemStack) -> None
      :async:


   .. py:method:: setItem

       .. py:method:: setItem(self, _0:int, _1:ItemStack) -> None
          :async:
          :noindex:

       .. py:method:: setItem(self, _0:EquipmentSlot, _1:ItemStack) -> None
          :async:
          :noindex:


   .. py:method:: setItemInHand(self, _0:ItemStack) -> None
      :async:


   .. py:method:: setItemInMainHand(self, _0:ItemStack) -> None
      :async:


   .. py:method:: setItemInOffHand(self, _0:ItemStack) -> None
      :async:


   .. py:method:: setLeggings(self, _0:ItemStack) -> None
      :async:


   .. py:method:: setMaxStackSize(self, _0:int) -> None
      :async:


   .. py:method:: setStorageContents(self, _0:ItemStack[]) -> None
      :async:


   .. py:method:: spliterator(self) -> :py:class:`Spliterator`
      :async:

