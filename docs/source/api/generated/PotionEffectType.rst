.. currentmodule:: pycraft.server.final

PotionEffectType
================

Inheritance
------------
* pycraft.server.final.PotionEffectType
* :py:class:`pycraft.server.proxyobjects.KeyedServerObjectEnum`
* :py:class:`pycraft.server.proxyobjects.ServerObjectEnum`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.potion.PotionEffectType <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/potion/PotionEffectType.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: PotionEffectType(self, key)
   :canonical: pycraft.server.final.PotionEffectType

   Namespaced/keyed enumerations

   .. py:method:: __init__(self, key)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: cached_values()
      :async:

      Get the cached values for the given enumeration


   .. py:method:: createEffect(self, _0:int, _1:int) -> :py:class:`PotionEffect`
      :async:


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: from_server(key)
      

      Convert server-side structure to local object


   .. py:method:: getAttributeModifierAmount(self, _0:Attribute, _1:int) -> float
      :async:


   .. py:method:: getById(cls, _0:int) -> :py:class:`PotionEffectType`
      :async:
      :classmethod:


   .. py:method:: getByKey(cls, _0:NamespacedKey) -> :py:class:`PotionEffectType`
      :async:
      :classmethod:


   .. py:method:: getByName(cls, _0:String) -> :py:class:`PotionEffectType`
      :async:
      :classmethod:


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getColor(self) -> :py:class:`Color`
      :async:


   .. py:method:: getDurationModifier(self) -> float
      :async:


   .. py:method:: getEffectAttributes(self) -> :py:class:`Map`
      :async:


   .. py:method:: getEffectCategory(self) -> :py:class:`Category`
      :async:


   .. py:method:: getId(self) -> int
      :async:


   .. py:method:: getKey(self) -> :py:class:`NamespacedKey`
      :async:


   .. py:method:: getName(self) -> str
      :async:


   .. py:method:: get_key(self)
      

   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isInstant(self) -> bool
      :async:


   .. py:method:: key(self) -> :py:class:`Key`
      :async:


   .. py:method:: loosely_match(name)
      :async:

   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: registerPotionEffectType(cls, _0:PotionEffectType) -> None
      :async:
      :classmethod:


   .. py:method:: stopAcceptingRegistrations(cls) -> None
      :async:
      :classmethod:


   .. py:method:: toString(self) -> str
      :async:


   .. py:method:: translationKey(self) -> str
      :async:


   .. py:method:: values(cls) -> typing.List[:py:class:`PotionEffectType`]
      :async:
      :classmethod:


Values
-------

