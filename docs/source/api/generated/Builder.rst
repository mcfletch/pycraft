.. currentmodule:: pycraft.server.final

Builder
=======

Inheritance
------------
* pycraft.server.final.Builder
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.FireworkEffect.Builder <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/FireworkEffect/Builder.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Builder(self, **named)
   :canonical: pycraft.server.final.Builder

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: build(self) -> :py:class:`FireworkEffect`
      :async:


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: flicker(self, _0:boolean) -> :py:class:`Builder`
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: toString(self) -> str
      :async:


   .. py:method:: trail(self, _0:boolean) -> :py:class:`Builder`
      :async:


   .. py:method:: with(self, _0:Type) -> :py:class:`Builder`
      :async:


   .. py:method:: withColor

       .. py:method:: withColor(self, _0:Iterable) -> :py:class:`Builder`
          :async:
          :noindex:

       .. py:method:: withColor(self, _0:Color) -> :py:class:`Builder`
          :async:
          :noindex:

       .. py:method:: withColor(self, _0:Color[]) -> :py:class:`Builder`
          :async:
          :noindex:


   .. py:method:: withFade

       .. py:method:: withFade(self, _0:Iterable) -> :py:class:`Builder`
          :async:
          :noindex:

       .. py:method:: withFade(self, _0:Color) -> :py:class:`Builder`
          :async:
          :noindex:

       .. py:method:: withFade(self, _0:Color[]) -> :py:class:`Builder`
          :async:
          :noindex:


   .. py:method:: withFlicker(self) -> :py:class:`Builder`
      :async:


   .. py:method:: withTrail(self) -> :py:class:`Builder`
      :async:

