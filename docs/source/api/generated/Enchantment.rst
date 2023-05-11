.. currentmodule:: pycraft.server.final

Enchantment
===========

Inheritance
------------
* pycraft.server.final.Enchantment
* :py:class:`pycraft.server.world.Enchantment`
* :py:class:`pycraft.server.proxyobjects.KeyedServerObjectEnum`
* :py:class:`pycraft.server.proxyobjects.ServerObjectEnum`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.enchantments.Enchantment <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/enchantments/Enchantment.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Enchantment(self, key)
   :canonical: pycraft.server.final.Enchantment

   Namespaced/keyed enumerations

   .. py:method:: __init__(self, key)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: cached_values()
      :async:

      Get the cached values for the given enumeration


   .. py:method:: canEnchantItem(self, _0:ItemStack) -> bool
      :async:


   .. py:method:: conflictsWith(self, _0:Enchantment) -> bool
      :async:


   .. py:method:: displayName(self, _0:int) -> :py:class:`Component`
      :async:


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: from_server(key)
      

      Convert server-side structure to local object


   .. py:method:: getActiveSlots(self) -> typing.List[:py:class:`EquipmentSlot`]
      :async:


   .. py:method:: getByKey(cls, _0:NamespacedKey) -> :py:class:`Enchantment`
      :async:
      :classmethod:


   .. py:method:: getByName(cls, _0:String) -> :py:class:`Enchantment`
      :async:
      :classmethod:


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getDamageIncrease(self, _0:int, _1:EntityCategory) -> float
      :async:


   .. py:method:: getItemTarget(self) -> :py:class:`EnchantmentTarget`
      :async:


   .. py:method:: getKey(self) -> :py:class:`NamespacedKey`
      :async:


   .. py:method:: getMaxLevel(self) -> int
      :async:


   .. py:method:: getName(self) -> str
      :async:


   .. py:method:: getRarity(self) -> :py:class:`EnchantmentRarity`
      :async:


   .. py:method:: getStartLevel(self) -> int
      :async:


   .. py:method:: get_key(self)
      

   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isAcceptingRegistrations(cls) -> bool
      :async:
      :classmethod:


   .. py:method:: isCursed(self) -> bool
      :async:


   .. py:method:: isDiscoverable(self) -> bool
      :async:


   .. py:method:: isTradeable(self) -> bool
      :async:


   .. py:method:: isTreasure(self) -> bool
      :async:


   .. py:method:: key(self) -> :py:class:`Key`
      :async:


   .. py:method:: loosely_match(name)
      :async:

   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: registerEnchantment(cls, _0:Enchantment) -> None
      :async:
      :classmethod:


   .. py:method:: stopAcceptingRegistrations(cls) -> None
      :async:
      :classmethod:


   .. py:method:: toString(self) -> str
      :async:


   .. py:method:: translationKey(self) -> str
      :async:


   .. py:method:: values(cls) -> typing.List[:py:class:`Enchantment`]
      :async:
      :classmethod:


Values
-------

* minecraft:fire_protection
* minecraft:sharpness
* minecraft:flame
* minecraft:soul_speed
* minecraft:aqua_affinity
* minecraft:punch
* minecraft:loyalty
* minecraft:depth_strider
* minecraft:vanishing_curse
* minecraft:unbreaking
* minecraft:knockback
* minecraft:luck_of_the_sea
* minecraft:binding_curse
* minecraft:fortune
* minecraft:protection
* minecraft:efficiency
* minecraft:mending
* minecraft:frost_walker
* minecraft:lure
* minecraft:looting
* minecraft:piercing
* minecraft:blast_protection
* minecraft:smite
* minecraft:multishot
* minecraft:swift_sneak
* minecraft:fire_aspect
* minecraft:channeling
* minecraft:sweeping
* minecraft:thorns
* minecraft:bane_of_arthropods
* minecraft:respiration
* minecraft:riptide
* minecraft:silk_touch
* minecraft:quick_charge
* minecraft:projectile_protection
* minecraft:impaling
* minecraft:feather_falling
* minecraft:power
* minecraft:infinity
