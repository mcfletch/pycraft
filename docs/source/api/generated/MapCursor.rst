.. currentmodule:: pycraft.server.final

MapCursor
=========

Inheritance
------------
* pycraft.server.final.MapCursor
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.map.MapCursor <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/map/MapCursor.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: MapCursor(self, **named)
   :canonical: pycraft.server.final.MapCursor

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: caption

       .. py:method:: caption(self) -> :py:class:`Component`
          :async:
          :noindex:

       .. py:method:: caption(self, _0:Component) -> None
          :async:
          :noindex:


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getCaption(self) -> str
      :async:


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getDirection(self) -> :py:class:`byte`
      :async:


   .. py:method:: getRawType(self) -> :py:class:`byte`
      :async:


   .. py:method:: getType(self) -> :py:class:`Type`
      :async:


   .. py:method:: getX(self) -> :py:class:`byte`
      :async:


   .. py:method:: getY(self) -> :py:class:`byte`
      :async:


   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isVisible(self) -> bool
      :async:


   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: setCaption(self, _0:String) -> None
      :async:


   .. py:method:: setDirection(self, _0:byte) -> None
      :async:


   .. py:method:: setRawType(self, _0:byte) -> None
      :async:


   .. py:method:: setType(self, _0:Type) -> None
      :async:


   .. py:method:: setVisible(self, _0:boolean) -> None
      :async:


   .. py:method:: setX(self, _0:byte) -> None
      :async:


   .. py:method:: setY(self, _0:byte) -> None
      :async:


   .. py:method:: toString(self) -> str
      :async:

