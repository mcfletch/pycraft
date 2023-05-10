.. currentmodule:: pycraft.server.final

MapCursorCollection
===================

Inheritance
------------
* pycraft.server.final.MapCursorCollection
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.map.MapCursorCollection <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/map/MapCursorCollection.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: MapCursorCollection(self, **named)
   :canonical: pycraft.server.final.MapCursorCollection

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: addCursor

       .. py:method:: addCursor(self, _0:MapCursor) -> :py:class:`MapCursor`
          :async:
          :noindex:

       .. py:method:: addCursor(self, _0:int, _1:int, _2:byte) -> :py:class:`MapCursor`
          :async:
          :noindex:

       .. py:method:: addCursor(self, _0:int, _1:int, _2:byte, _3:byte) -> :py:class:`MapCursor`
          :async:
          :noindex:

       .. py:method:: addCursor(self, _0:int, _1:int, _2:byte, _3:byte, _4:boolean) -> :py:class:`MapCursor`
          :async:
          :noindex:

       .. py:method:: addCursor(self, _0:int, _1:int, _2:byte, _3:byte, _4:boolean, _5:String) -> :py:class:`MapCursor`
          :async:
          :noindex:

       .. py:method:: addCursor(self, _0:int, _1:int, _2:byte, _3:byte, _4:boolean, _5:Component) -> :py:class:`MapCursor`
          :async:
          :noindex:


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getCursor(self, _0:int) -> :py:class:`MapCursor`
      :async:


   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: removeCursor(self, _0:MapCursor) -> bool
      :async:


   .. py:method:: size(self) -> int
      :async:


   .. py:method:: toString(self) -> str
      :async:

