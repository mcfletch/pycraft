.. currentmodule:: pycraft.server.final

Color
=====

Inheritance
------------
* pycraft.server.final.Color
* :py:class:`pycraft.server.final.ConfigurationSerializable`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.Color <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Color.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Color(self, **named)
   :canonical: pycraft.server.final.Color

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: asARGB(self) -> int
      :async:


   .. py:method:: asBGR(self) -> int
      :async:


   .. py:method:: asRGB(self) -> int
      :async:


   .. py:method:: deserialize(cls, _0:Map) -> :py:class:`Color`
      :async:
      :classmethod:


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: fromARGB

       .. py:method:: fromARGB(cls, _0:int) -> :py:class:`Color`
          :async:
          :classmethod:
          :noindex:

       .. py:method:: fromARGB(cls, _0:int, _1:int, _2:int, _3:int) -> :py:class:`Color`
          :async:
          :classmethod:
          :noindex:


   .. py:method:: fromBGR

       .. py:method:: fromBGR(cls, _0:int) -> :py:class:`Color`
          :async:
          :classmethod:
          :noindex:

       .. py:method:: fromBGR(cls, _0:int, _1:int, _2:int) -> :py:class:`Color`
          :async:
          :classmethod:
          :noindex:


   .. py:method:: fromRGB

       .. py:method:: fromRGB(cls, _0:int) -> :py:class:`Color`
          :async:
          :classmethod:
          :noindex:

       .. py:method:: fromRGB(cls, _0:int, _1:int, _2:int) -> :py:class:`Color`
          :async:
          :classmethod:
          :noindex:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getAlpha(self) -> int
      :async:


   .. py:method:: getBlue(self) -> int
      :async:


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getGreen(self) -> int
      :async:


   .. py:method:: getRed(self) -> int
      :async:


   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: mixColors(self, _0:Color[]) -> :py:class:`Color`
      :async:


   .. py:method:: mixDyes(self, _0:DyeColor[]) -> :py:class:`Color`
      :async:


   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: serialize(self) -> :py:class:`Map`
      :async:


   .. py:method:: setAlpha(self, _0:int) -> :py:class:`Color`
      :async:


   .. py:method:: setBlue(self, _0:int) -> :py:class:`Color`
      :async:


   .. py:method:: setGreen(self, _0:int) -> :py:class:`Color`
      :async:


   .. py:method:: setRed(self, _0:int) -> :py:class:`Color`
      :async:


   .. py:method:: toString(self) -> str
      :async:

