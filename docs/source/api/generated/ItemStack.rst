.. currentmodule:: pycraft.server.final

ItemStack
=========

Inheritance
------------
* pycraft.server.final.ItemStack
* :py:class:`pycraft.server.world.ItemStack`
* :py:class:`pycraft.server.final.ConfigurationSerializable`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.inventory.ItemStack <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/inventory/ItemStack.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: ItemStack(self, **named)
   :canonical: pycraft.server.final.ItemStack

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: add

       .. py:method:: add(self) -> :py:class:`ItemStack`
          :async:
          :noindex:

       .. py:method:: add(self, _0:int) -> :py:class:`ItemStack`
          :async:
          :noindex:


   .. py:method:: addEnchantment(self, _0:Enchantment, _1:int) -> None
      :async:


   .. py:method:: addEnchantments(self, _0:Map) -> None
      :async:


   .. py:method:: addItemFlags(self, _0:ItemFlag[]) -> None
      :async:


   .. py:method:: addUnsafeEnchantment(self, _0:Enchantment, _1:int) -> None
      :async:


   .. py:method:: addUnsafeEnchantments(self, _0:Map) -> None
      :async:


   .. py:method:: asHoverEvent

       .. py:method:: asHoverEvent(self) -> :py:class:`HoverEvent`
          :async:
          :noindex:

       .. py:method:: asHoverEvent(self, _0:UnaryOperator) -> :py:class:`HoverEvent`
          :async:
          :noindex:


   .. py:method:: asOne(self) -> :py:class:`ItemStack`
      :async:


   .. py:method:: asQuantity(self, _0:int) -> :py:class:`ItemStack`
      :async:


   .. py:method:: canRepair(self, _0:ItemStack) -> bool
      :async:


   .. py:method:: containsEnchantment(self, _0:Enchantment) -> bool
      :async:


   .. py:method:: damage(self, _0:int, _1:LivingEntity) -> :py:class:`ItemStack`
      :async:


   .. py:method:: deserialize(cls, _0:Map) -> :py:class:`ItemStack`
      :async:
      :classmethod:


   .. py:method:: deserializeBytes(cls, _0:byte[]) -> :py:class:`ItemStack`
      :async:
      :classmethod:


   .. py:method:: displayName(self) -> :py:class:`Component`
      :async:


   .. py:method:: editMeta

       .. py:method:: editMeta(self, _0:Consumer) -> bool
          :async:
          :noindex:

       .. py:method:: editMeta(self, _0:Class, _1:Consumer) -> bool
          :async:
          :noindex:


   .. py:method:: enchantWithLevels(self, _0:int, _1:boolean, _2:Random) -> :py:class:`ItemStack`
      :async:


   .. py:method:: ensureServerConversions(self) -> :py:class:`ItemStack`
      :async:


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getAmount(self) -> int
      :async:


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getData(self) -> :py:class:`MaterialData`
      :async:


   .. py:method:: getDurability(self) -> :py:class:`short`
      :async:


   .. py:method:: getEnchantmentLevel(self, _0:Enchantment) -> int
      :async:


   .. py:method:: getEnchantments(self) -> :py:class:`Map`
      :async:


   .. py:method:: getI18NDisplayName(self) -> str
      :async:


   .. py:method:: getItemFlags(self) -> typing.List[:py:class:`ItemFlag`]
      :async:


   .. py:method:: getItemMeta(self) -> :py:class:`ItemMeta`
      :async:


   .. py:method:: getLore(self) -> typing.List[str]
      :async:


   .. py:method:: getMaxItemUseDuration(self) -> int
      :async:


   .. py:method:: getMaxStackSize(self) -> int
      :async:


   .. py:method:: getMeta(self)
      :async:

      Retrieve the ItemMeta and set it's key to our key...


   .. py:method:: getRarity(self) -> :py:class:`ItemRarity`
      :async:


   .. py:method:: getTranslationKey(self) -> str
      :async:


   .. py:method:: getType(self) -> :py:class:`Material`
      :async:


   .. py:method:: get_key(self)
      

   .. py:method:: hasItemFlag(self, _0:ItemFlag) -> bool
      :async:


   .. py:method:: hasItemMeta(self) -> bool
      :async:


   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isRepairableBy(self, _0:ItemStack) -> bool
      :async:


   .. py:method:: isSimilar(self, _0:ItemStack) -> bool
      :async:


   .. py:method:: lore

       .. py:method:: lore(self) -> typing.List[:py:class:`Component`]
          :async:
          :noindex:

       .. py:method:: lore(self, _0:List) -> None
          :async:
          :noindex:


   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: removeEnchantment(self, _0:Enchantment) -> int
      :async:


   .. py:method:: removeItemFlags(self, _0:ItemFlag[]) -> None
      :async:


   .. py:method:: serialize(self) -> :py:class:`Map`
      :async:


   .. py:method:: serializeAsBytes(self) -> typing.List[:py:class:`byte`]
      :async:


   .. py:method:: setAmount(self, _0:int) -> None
      :async:


   .. py:method:: setData(self, _0:MaterialData) -> None
      :async:


   .. py:method:: setDurability(self, _0:short) -> None
      :async:


   .. py:method:: setItemMeta(self, _0:ItemMeta) -> bool
      :async:


   .. py:method:: setLore(self, _0:List) -> None
      :async:


   .. py:method:: setType(self, _0:Material) -> None
      :async:


   .. py:method:: subtract

       .. py:method:: subtract(self) -> :py:class:`ItemStack`
          :async:
          :noindex:

       .. py:method:: subtract(self, _0:int) -> :py:class:`ItemStack`
          :async:
          :noindex:


   .. py:method:: toString(self) -> str
      :async:


   .. py:method:: translationKey(self) -> str
      :async:

