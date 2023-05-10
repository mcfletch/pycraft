.. currentmodule:: pycraft.server.final

PotionEffect
============

Inheritance
------------
* pycraft.server.final.PotionEffect
* :py:class:`pycraft.server.final.ConfigurationSerializable`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.potion.PotionEffect <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/potion/PotionEffect.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: PotionEffect(self, **named)
   :canonical: pycraft.server.final.PotionEffect

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: apply(self, _0:LivingEntity) -> bool
      :async:


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getAmplifier(self) -> int
      :async:


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getColor(self) -> :py:class:`Color`
      :async:


   .. py:method:: getDuration(self) -> int
      :async:


   .. py:method:: getType(self) -> :py:class:`PotionEffectType`
      :async:


   .. py:method:: hasIcon(self) -> bool
      :async:


   .. py:method:: hasParticles(self) -> bool
      :async:


   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isAmbient(self) -> bool
      :async:


   .. py:method:: isInfinite(self) -> bool
      :async:


   .. py:method:: isShorterThan(self, _0:PotionEffect) -> bool
      :async:


   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: serialize(self) -> :py:class:`Map`
      :async:


   .. py:method:: toString(self) -> str
      :async:


   .. py:method:: withAmbient(self, _0:boolean) -> :py:class:`PotionEffect`
      :async:


   .. py:method:: withAmplifier(self, _0:int) -> :py:class:`PotionEffect`
      :async:


   .. py:method:: withDuration(self, _0:int) -> :py:class:`PotionEffect`
      :async:


   .. py:method:: withIcon(self, _0:boolean) -> :py:class:`PotionEffect`
      :async:


   .. py:method:: withParticles(self, _0:boolean) -> :py:class:`PotionEffect`
      :async:


   .. py:method:: withType(self, _0:PotionEffectType) -> :py:class:`PotionEffect`
      :async:

