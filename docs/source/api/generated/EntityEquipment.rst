.. currentmodule:: pycraft.server.final

EntityEquipment
===============

Inheritance
------------
* pycraft.server.final.EntityEquipment
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.inventory.EntityEquipment <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/inventory/EntityEquipment.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: EntityEquipment(self, **named)
   :canonical: pycraft.server.final.EntityEquipment

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: clear(self) -> None
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getArmorContents(self) -> typing.List[:py:class:`ItemStack`]
      :async:


   .. py:method:: getBoots(self) -> :py:class:`ItemStack`
      :async:


   .. py:method:: getBootsDropChance(self) -> float
      :async:


   .. py:method:: getChestplate(self) -> :py:class:`ItemStack`
      :async:


   .. py:method:: getChestplateDropChance(self) -> float
      :async:


   .. py:method:: getDropChance(self, _0:EquipmentSlot) -> float
      :async:


   .. py:method:: getHelmet(self) -> :py:class:`ItemStack`
      :async:


   .. py:method:: getHelmetDropChance(self) -> float
      :async:


   .. py:method:: getHolder(self) -> :py:class:`Entity`
      :async:


   .. py:method:: getItem(self, _0:EquipmentSlot) -> :py:class:`ItemStack`
      :async:


   .. py:method:: getItemInHand(self) -> :py:class:`ItemStack`
      :async:


   .. py:method:: getItemInHandDropChance(self) -> float
      :async:


   .. py:method:: getItemInMainHand(self) -> :py:class:`ItemStack`
      :async:


   .. py:method:: getItemInMainHandDropChance(self) -> float
      :async:


   .. py:method:: getItemInOffHand(self) -> :py:class:`ItemStack`
      :async:


   .. py:method:: getItemInOffHandDropChance(self) -> float
      :async:


   .. py:method:: getLeggings(self) -> :py:class:`ItemStack`
      :async:


   .. py:method:: getLeggingsDropChance(self) -> float
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: setArmorContents(self, _0:ItemStack[]) -> None
      :async:


   .. py:method:: setBoots

       .. py:method:: setBoots(self, _0:ItemStack) -> None
          :async:
          :noindex:

       .. py:method:: setBoots(self, _0:ItemStack, _1:boolean) -> None
          :async:
          :noindex:


   .. py:method:: setBootsDropChance(self, _0:float) -> None
      :async:


   .. py:method:: setChestplate

       .. py:method:: setChestplate(self, _0:ItemStack) -> None
          :async:
          :noindex:

       .. py:method:: setChestplate(self, _0:ItemStack, _1:boolean) -> None
          :async:
          :noindex:


   .. py:method:: setChestplateDropChance(self, _0:float) -> None
      :async:


   .. py:method:: setDropChance(self, _0:EquipmentSlot, _1:float) -> None
      :async:


   .. py:method:: setHelmet

       .. py:method:: setHelmet(self, _0:ItemStack) -> None
          :async:
          :noindex:

       .. py:method:: setHelmet(self, _0:ItemStack, _1:boolean) -> None
          :async:
          :noindex:


   .. py:method:: setHelmetDropChance(self, _0:float) -> None
      :async:


   .. py:method:: setItem

       .. py:method:: setItem(self, _0:EquipmentSlot, _1:ItemStack) -> None
          :async:
          :noindex:

       .. py:method:: setItem(self, _0:EquipmentSlot, _1:ItemStack, _2:boolean) -> None
          :async:
          :noindex:


   .. py:method:: setItemInHand(self, _0:ItemStack) -> None
      :async:


   .. py:method:: setItemInHandDropChance(self, _0:float) -> None
      :async:


   .. py:method:: setItemInMainHand

       .. py:method:: setItemInMainHand(self, _0:ItemStack) -> None
          :async:
          :noindex:

       .. py:method:: setItemInMainHand(self, _0:ItemStack, _1:boolean) -> None
          :async:
          :noindex:


   .. py:method:: setItemInMainHandDropChance(self, _0:float) -> None
      :async:


   .. py:method:: setItemInOffHand

       .. py:method:: setItemInOffHand(self, _0:ItemStack) -> None
          :async:
          :noindex:

       .. py:method:: setItemInOffHand(self, _0:ItemStack, _1:boolean) -> None
          :async:
          :noindex:


   .. py:method:: setItemInOffHandDropChance(self, _0:float) -> None
      :async:


   .. py:method:: setLeggings

       .. py:method:: setLeggings(self, _0:ItemStack) -> None
          :async:
          :noindex:

       .. py:method:: setLeggings(self, _0:ItemStack, _1:boolean) -> None
          :async:
          :noindex:


   .. py:method:: setLeggingsDropChance(self, _0:float) -> None
      :async:

