.. currentmodule:: pycraft.server.final

MapFont
=======

Inheritance
------------
* pycraft.server.final.MapFont
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.map.MapFont <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/map/MapFont.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: MapFont(self, **named)
   :canonical: pycraft.server.final.MapFont

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getChar(self, _0:char) -> :py:class:`CharacterSprite`
      :async:


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getHeight(self) -> int
      :async:


   .. py:method:: getWidth(self, _0:String) -> int
      :async:


   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isValid(self, _0:String) -> bool
      :async:


   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: setChar(self, _0:char, _1:CharacterSprite) -> None
      :async:


   .. py:method:: toString(self) -> str
      :async:

