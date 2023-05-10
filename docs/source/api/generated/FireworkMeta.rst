.. currentmodule:: pycraft.server.final

FireworkMeta
============

Inheritance
------------
* pycraft.server.final.FireworkMeta
* :py:class:`pycraft.server.final.ItemMeta`
* :py:class:`pycraft.server.world.ItemMeta`
* :py:class:`pycraft.server.final.ConfigurationSerializable`
* :py:class:`pycraft.server.final.PersistentDataHolder`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.inventory.meta.FireworkMeta <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/inventory/meta/FireworkMeta.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: FireworkMeta(self, **named)
   :canonical: pycraft.server.final.FireworkMeta

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: addAttributeModifier(self, _0:Attribute, _1:AttributeModifier) -> bool
      :async:


   .. py:method:: addEffect(self, _0:FireworkEffect) -> None
      :async:


   .. py:method:: addEffects

       .. py:method:: addEffects(self, _0:Iterable) -> None
          :async:
          :noindex:

       .. py:method:: addEffects(self, _0:FireworkEffect[]) -> None
          :async:
          :noindex:


   .. py:method:: addEnchant(self, _0:Enchantment, _1:int, _2:boolean) -> bool
      :async:


   .. py:method:: addItemFlags(self, _0:ItemFlag[]) -> None
      :async:


   .. py:method:: clearEffects(self) -> None
      :async:


   .. py:method:: displayName

       .. py:method:: displayName(self) -> :py:class:`Component`
          :async:
          :noindex:

       .. py:method:: displayName(self, _0:Component) -> None
          :async:
          :noindex:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getAsString(self) -> str
      :async:


   .. py:method:: getAttributeModifiers

       .. py:method:: getAttributeModifiers(self) -> :py:class:`Multimap`
          :async:
          :noindex:

       .. py:method:: getAttributeModifiers(self, _0:Attribute) -> typing.List[:py:class:`AttributeModifier`]
          :async:
          :noindex:

       .. py:method:: getAttributeModifiers(self, _0:EquipmentSlot) -> :py:class:`Multimap`
          :async:
          :noindex:


   .. py:method:: getCanDestroy(self) -> typing.List[:py:class:`Material`]
      :async:


   .. py:method:: getCanPlaceOn(self) -> typing.List[:py:class:`Material`]
      :async:


   .. py:method:: getCustomModelData(self) -> int
      :async:


   .. py:method:: getCustomTagContainer(self) -> :py:class:`CustomItemTagContainer`
      :async:


   .. py:method:: getDestroyableKeys(self) -> typing.List[:py:class:`Namespaced`]
      :async:


   .. py:method:: getDisplayName(self) -> str
      :async:


   .. py:method:: getDisplayNameComponent(self) -> typing.List[:py:class:`BaseComponent`]
      :async:


   .. py:method:: getEffects(self) -> typing.List[:py:class:`FireworkEffect`]
      :async:


   .. py:method:: getEffectsSize(self) -> int
      :async:


   .. py:method:: getEnchantLevel(self, _0:Enchantment) -> int
      :async:


   .. py:method:: getEnchants(self) -> :py:class:`Map`
      :async:


   .. py:method:: getItemFlags(self) -> typing.List[:py:class:`ItemFlag`]
      :async:


   .. py:method:: getLocalizedName(self) -> str
      :async:


   .. py:method:: getLore(self) -> typing.List[str]
      :async:


   .. py:method:: getLoreComponents(self) -> typing.List[typing.List[:py:class:`BaseComponent`]]
      :async:


   .. py:method:: getPersistentDataContainer(self) -> :py:class:`PersistentDataContainer`
      :async:


   .. py:method:: getPlaceableKeys(self) -> typing.List[:py:class:`Namespaced`]
      :async:


   .. py:method:: getPower(self) -> int
      :async:


   .. py:method:: get_key(self)
      

   .. py:method:: hasAttributeModifiers(self) -> bool
      :async:


   .. py:method:: hasConflictingEnchant(self, _0:Enchantment) -> bool
      :async:


   .. py:method:: hasCustomModelData(self) -> bool
      :async:


   .. py:method:: hasDestroyableKeys(self) -> bool
      :async:


   .. py:method:: hasDisplayName(self) -> bool
      :async:


   .. py:method:: hasEffects(self) -> bool
      :async:


   .. py:method:: hasEnchant(self, _0:Enchantment) -> bool
      :async:


   .. py:method:: hasEnchants(self) -> bool
      :async:


   .. py:method:: hasItemFlag(self, _0:ItemFlag) -> bool
      :async:


   .. py:method:: hasLocalizedName(self) -> bool
      :async:


   .. py:method:: hasLore(self) -> bool
      :async:


   .. py:method:: hasPlaceableKeys(self) -> bool
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isUnbreakable(self) -> bool
      :async:


   .. py:method:: lore

       .. py:method:: lore(self) -> typing.List[:py:class:`Component`]
          :async:
          :noindex:

       .. py:method:: lore(self, _0:List) -> None
          :async:
          :noindex:


   .. py:method:: removeAttributeModifier

       .. py:method:: removeAttributeModifier(self, _0:Attribute) -> bool
          :async:
          :noindex:

       .. py:method:: removeAttributeModifier(self, _0:EquipmentSlot) -> bool
          :async:
          :noindex:

       .. py:method:: removeAttributeModifier(self, _0:Attribute, _1:AttributeModifier) -> bool
          :async:
          :noindex:


   .. py:method:: removeEffect(self, _0:int) -> None
      :async:


   .. py:method:: removeEnchant(self, _0:Enchantment) -> bool
      :async:


   .. py:method:: removeItemFlags(self, _0:ItemFlag[]) -> None
      :async:


   .. py:method:: serialize(self) -> :py:class:`Map`
      :async:


   .. py:method:: setAttributeModifiers(self, _0:Multimap) -> None
      :async:


   .. py:method:: setCanDestroy(self, _0:Set) -> None
      :async:


   .. py:method:: setCanPlaceOn(self, _0:Set) -> None
      :async:


   .. py:method:: setCustomModelData(self, _0:Integer) -> None
      :async:


   .. py:method:: setDestroyableKeys(self, _0:Collection) -> None
      :async:


   .. py:method:: setDisplayName(self, _0:String) -> None
      :async:


   .. py:method:: setDisplayNameComponent(self, _0:BaseComponent[]) -> None
      :async:


   .. py:method:: setLocalizedName(self, _0:String) -> None
      :async:


   .. py:method:: setLore(self, _0:List) -> None
      :async:


   .. py:method:: setLoreComponents(self, _0:List) -> None
      :async:


   .. py:method:: setPlaceableKeys(self, _0:Collection) -> None
      :async:


   .. py:method:: setPower(self, _0:int) -> None
      :async:


   .. py:method:: setUnbreakable(self, _0:boolean) -> None
      :async:


   .. py:method:: setVersion(self, _0:int) -> None
      :async:

