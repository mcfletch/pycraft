.. currentmodule:: pycraft.server.final

CharacterSprite
===============

Inheritance
------------
* pycraft.server.final.CharacterSprite
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.map.MapFont.CharacterSprite <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/map/MapFont/CharacterSprite.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: CharacterSprite(self, **named)
   :canonical: pycraft.server.final.CharacterSprite

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: get(self, _0:int, _1:int) -> bool
      :async:


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getHeight(self) -> int
      :async:


   .. py:method:: getWidth(self) -> int
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

