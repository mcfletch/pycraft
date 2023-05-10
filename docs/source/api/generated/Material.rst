.. currentmodule:: pycraft.server.final

Material
========

Inheritance
------------
* pycraft.server.final.Material
* :py:class:`pycraft.server.world.Material`
* :py:class:`pycraft.server.proxyobjects.KeyedServerObjectEnum`
* :py:class:`pycraft.server.proxyobjects.ServerObjectEnum`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.Material <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Material.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Material(self, key)
   :canonical: pycraft.server.final.Material

   Namespaced/keyed enumerations

   .. py:method:: __init__(self, key)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: cached_values()
      :async:

      Get the cached values for the given enumeration


   .. py:method:: compareTo

       .. py:method:: compareTo(self, _0:Object) -> int
          :async:
          :noindex:

       .. py:method:: compareTo(self, _0:Enum) -> int
          :async:
          :noindex:


   .. py:method:: createBlockData

       .. py:method:: createBlockData(self) -> :py:class:`BlockData`
          :async:
          :noindex:

       .. py:method:: createBlockData(self, _0:String) -> :py:class:`BlockData`
          :async:
          :noindex:

       .. py:method:: createBlockData(self, _0:Consumer) -> :py:class:`BlockData`
          :async:
          :noindex:


   .. py:method:: describeConstable(self) -> :py:class:`Optional`
      :async:


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: from_server(key)
      

      Convert server-side structure to local object


   .. py:method:: getBlastResistance(self) -> float
      :async:


   .. py:method:: getBlockTranslationKey(self) -> str
      :async:


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getCraftingRemainingItem(self) -> :py:class:`Material`
      :async:


   .. py:method:: getCreativeCategory(self) -> :py:class:`CreativeCategory`
      :async:


   .. py:method:: getData(self) -> :py:class:`Class`
      :async:


   .. py:method:: getDeclaringClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getDefaultAttributeModifiers(self, _0:EquipmentSlot) -> :py:class:`Multimap`
      :async:


   .. py:method:: getEquipmentSlot(self) -> :py:class:`EquipmentSlot`
      :async:


   .. py:method:: getHardness(self) -> float
      :async:


   .. py:method:: getId(self) -> int
      :async:


   .. py:method:: getItemAttributes(self, _0:EquipmentSlot) -> :py:class:`Multimap`
      :async:


   .. py:method:: getItemRarity(self) -> :py:class:`ItemRarity`
      :async:


   .. py:method:: getItemTranslationKey(self) -> str
      :async:


   .. py:method:: getKey(self) -> :py:class:`NamespacedKey`
      :async:


   .. py:method:: getMaterial

       .. py:method:: getMaterial(cls, _0:String) -> :py:class:`Material`
          :async:
          :classmethod:
          :noindex:

       .. py:method:: getMaterial(cls, _0:String, _1:boolean) -> :py:class:`Material`
          :async:
          :classmethod:
          :noindex:


   .. py:method:: getMaxDurability(self) -> :py:class:`short`
      :async:


   .. py:method:: getMaxStackSize(self) -> int
      :async:


   .. py:method:: getNewData(self, _0:byte) -> :py:class:`MaterialData`
      :async:


   .. py:method:: getSlipperiness(self) -> float
      :async:


   .. py:method:: getTranslationKey(self) -> str
      :async:


   .. py:method:: get_key(self)
      

   .. py:method:: hasGravity(self) -> bool
      :async:


   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isAir(self) -> bool
      :async:


   .. py:method:: isBlock(self) -> bool
      :async:


   .. py:method:: isBurnable(self) -> bool
      :async:


   .. py:method:: isCollidable(self) -> bool
      :async:


   .. py:method:: isEdible(self) -> bool
      :async:


   .. py:method:: isEmpty(self) -> bool
      :async:


   .. py:method:: isFlammable(self) -> bool
      :async:


   .. py:method:: isFuel(self) -> bool
      :async:


   .. py:method:: isInteractable(self) -> bool
      :async:


   .. py:method:: isItem(self) -> bool
      :async:


   .. py:method:: isLegacy(self) -> bool
      :async:


   .. py:method:: isOccluding(self) -> bool
      :async:


   .. py:method:: isRecord(self) -> bool
      :async:


   .. py:method:: isSolid(self) -> bool
      :async:


   .. py:method:: isTransparent(self) -> bool
      :async:


   .. py:method:: key(self) -> :py:class:`Key`
      :async:


   .. py:method:: loosely_match(name)
      :async:

   .. py:method:: matchMaterial

       .. py:method:: matchMaterial(cls, _0:String) -> :py:class:`Material`
          :async:
          :classmethod:
          :noindex:

       .. py:method:: matchMaterial(cls, _0:String, _1:boolean) -> :py:class:`Material`
          :async:
          :classmethod:
          :noindex:


   .. py:method:: name(self) -> str
      :async:


   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: ordinal(self) -> int
      :async:


   .. py:method:: toString(self) -> str
      :async:


   .. py:method:: translationKey(self) -> str
      :async:


   .. py:method:: valueOf

       .. py:method:: valueOf(cls, _0:String) -> :py:class:`Material`
          :async:
          :classmethod:
          :noindex:

       .. py:method:: valueOf(cls, _0:Class, _1:String) -> :py:class:`Enum`
          :async:
          :classmethod:
          :noindex:


   .. py:method:: values(cls) -> typing.List[:py:class:`Material`]
      :async:
      :classmethod:

