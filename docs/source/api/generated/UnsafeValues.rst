.. currentmodule:: pycraft.server.final

UnsafeValues
============

Inheritance
------------
* pycraft.server.final.UnsafeValues
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.UnsafeValues <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/UnsafeValues.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: UnsafeValues(self, **named)
   :canonical: pycraft.server.final.UnsafeValues

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: checkSupported(self, _0:PluginDescriptionFile) -> None
      :async:


   .. py:method:: colorDownsamplingGsonComponentSerializer(self) -> :py:class:`GsonComponentSerializer`
      :async:


   .. py:method:: componentFlattener(self) -> :py:class:`ComponentFlattener`
      :async:


   .. py:method:: deserializeEntity

       .. py:method:: deserializeEntity(self, _0:byte[], _1:World) -> :py:class:`Entity`
          :async:
          :noindex:

       .. py:method:: deserializeEntity(self, _0:byte[], _1:World, _2:boolean) -> :py:class:`Entity`
          :async:
          :noindex:


   .. py:method:: deserializeItem(self, _0:byte[]) -> :py:class:`ItemStack`
      :async:


   .. py:method:: fromLegacy

       .. py:method:: fromLegacy(self, _0:Material) -> :py:class:`Material`
          :async:
          :noindex:

       .. py:method:: fromLegacy(self, _0:MaterialData) -> :py:class:`Material`
          :async:
          :noindex:

       .. py:method:: fromLegacy(self, _0:MaterialData, _1:boolean) -> :py:class:`Material`
          :async:
          :noindex:

       .. py:method:: fromLegacy(self, _0:Material, _1:byte) -> :py:class:`BlockData`
          :async:
          :noindex:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getBiomeKey(self, _0:RegionAccessor, _1:int, _2:int, _3:int) -> :py:class:`NamespacedKey`
      :async:


   .. py:method:: getBlockTranslationKey(self, _0:Material) -> str
      :async:


   .. py:method:: getCreativeCategory(self, _0:Material) -> :py:class:`CreativeCategory`
      :async:


   .. py:method:: getDataVersion(self) -> int
      :async:


   .. py:method:: getDefaultAttributeModifiers(self, _0:Material, _1:EquipmentSlot) -> :py:class:`Multimap`
      :async:


   .. py:method:: getDefaultEntityAttributes(self, _0:NamespacedKey) -> :py:class:`Attributable`
      :async:


   .. py:method:: getItemAttributes(self, _0:Material, _1:EquipmentSlot) -> :py:class:`Multimap`
      :async:


   .. py:method:: getItemRarity(self, _0:Material) -> :py:class:`ItemRarity`
      :async:


   .. py:method:: getItemStackRarity(self, _0:ItemStack) -> :py:class:`ItemRarity`
      :async:


   .. py:method:: getItemTranslationKey(self, _0:Material) -> str
      :async:


   .. py:method:: getMainLevelName(self) -> str
      :async:


   .. py:method:: getMaterial(self, _0:String, _1:int) -> :py:class:`Material`
      :async:


   .. py:method:: getProtocolVersion(self) -> int
      :async:


   .. py:method:: getTimingsServerName(self) -> str
      :async:


   .. py:method:: getTranslationKey

       .. py:method:: getTranslationKey(self, _0:EntityType) -> str
          :async:
          :noindex:

       .. py:method:: getTranslationKey(self, _0:ItemStack) -> str
          :async:
          :noindex:


   .. py:method:: getVersionFetcher(self) -> :py:class:`VersionFetcher`
      :async:


   .. py:method:: gsonComponentSerializer(self) -> :py:class:`GsonComponentSerializer`
      :async:


   .. py:method:: hasDefaultEntityAttributes(self, _0:NamespacedKey) -> bool
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isCollidable(self, _0:Material) -> bool
      :async:


   .. py:method:: isLegacyPlugin(cls, _0:Plugin) -> bool
      :async:
      :classmethod:


   .. py:method:: isSupportedApiVersion(self, _0:String) -> bool
      :async:


   .. py:method:: isValidRepairItemStack(self, _0:ItemStack, _1:ItemStack) -> bool
      :async:


   .. py:method:: legacyComponentSerializer(self) -> :py:class:`LegacyComponentSerializer`
      :async:


   .. py:method:: loadAdvancement(self, _0:NamespacedKey, _1:String) -> :py:class:`Advancement`
      :async:


   .. py:method:: modifyItemStack(self, _0:ItemStack, _1:String) -> :py:class:`ItemStack`
      :async:


   .. py:method:: nextEntityId(self) -> int
      :async:


   .. py:method:: plainComponentSerializer(self) -> :py:class:`PlainComponentSerializer`
      :async:


   .. py:method:: plainTextSerializer(self) -> :py:class:`PlainTextComponentSerializer`
      :async:


   .. py:method:: processClass(self, _0:PluginDescriptionFile, _1:String, _2:byte[]) -> typing.List[:py:class:`byte`]
      :async:


   .. py:method:: removeAdvancement(self, _0:NamespacedKey) -> bool
      :async:


   .. py:method:: reportTimings(self) -> None
      :async:


   .. py:method:: resolveWithContext(self, _0:Component, _1:CommandSender, _2:Entity, _3:boolean) -> :py:class:`Component`
      :async:


   .. py:method:: serializeEntity(self, _0:Entity) -> typing.List[:py:class:`byte`]
      :async:


   .. py:method:: serializeItem(self, _0:ItemStack) -> typing.List[:py:class:`byte`]
      :async:


   .. py:method:: setBiomeKey(self, _0:RegionAccessor, _1:int, _2:int, _3:int, _4:NamespacedKey) -> None
      :async:


   .. py:method:: toLegacy(self, _0:Material) -> :py:class:`Material`
      :async:

