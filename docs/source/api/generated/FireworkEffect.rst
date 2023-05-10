.. currentmodule:: pycraft.server.final

FireworkEffect
==============

Inheritance
------------
* pycraft.server.final.FireworkEffect
* :py:class:`pycraft.server.final.ConfigurationSerializable`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.FireworkEffect <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/FireworkEffect.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: FireworkEffect(self, **named)
   :canonical: pycraft.server.final.FireworkEffect

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: builder(cls) -> :py:class:`Builder`
      :async:
      :classmethod:


   .. py:method:: deserialize(cls, _0:Map) -> :py:class:`ConfigurationSerializable`
      :async:
      :classmethod:


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getColors(self) -> typing.List[:py:class:`Color`]
      :async:


   .. py:method:: getFadeColors(self) -> typing.List[:py:class:`Color`]
      :async:


   .. py:method:: getType(self) -> :py:class:`Type`
      :async:


   .. py:method:: hasFlicker(self) -> bool
      :async:


   .. py:method:: hasTrail(self) -> bool
      :async:


   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: serialize(self) -> :py:class:`Map`
      :async:


   .. py:method:: toString(self) -> str
      :async:

