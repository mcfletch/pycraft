.. currentmodule:: pycraft.server.final

PotionBrewer
============

Inheritance
------------
* pycraft.server.final.PotionBrewer
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.potion.PotionBrewer <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/potion/PotionBrewer.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: PotionBrewer(self, **named)
   :canonical: pycraft.server.final.PotionBrewer

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: addPotionMix(self, _0:PotionMix) -> None
      :async:


   .. py:method:: createEffect(self, _0:PotionEffectType, _1:int, _2:int) -> :py:class:`PotionEffect`
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getEffects(self, _0:PotionType, _1:boolean, _2:boolean) -> typing.List[:py:class:`PotionEffect`]
      :async:


   .. py:method:: getEffectsFromDamage(self, _0:int) -> typing.List[:py:class:`PotionEffect`]
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: removePotionMix(self, _0:NamespacedKey) -> None
      :async:


   .. py:method:: resetPotionMixes(self) -> None
      :async:

