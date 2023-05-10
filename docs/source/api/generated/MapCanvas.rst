.. currentmodule:: pycraft.server.final

MapCanvas
=========

Inheritance
------------
* pycraft.server.final.MapCanvas
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.map.MapCanvas <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/map/MapCanvas.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: MapCanvas(self, **named)
   :canonical: pycraft.server.final.MapCanvas

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: drawImage(self, _0:int, _1:int, _2:Image) -> None
      :async:


   .. py:method:: drawText(self, _0:int, _1:int, _2:MapFont, _3:String) -> None
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getBasePixel(self, _0:int, _1:int) -> :py:class:`byte`
      :async:


   .. py:method:: getBasePixelColor(self, _0:int, _1:int) -> :py:class:`Color`
      :async:


   .. py:method:: getCursors(self) -> :py:class:`MapCursorCollection`
      :async:


   .. py:method:: getMapView(self) -> :py:class:`MapView`
      :async:


   .. py:method:: getPixel(self, _0:int, _1:int) -> :py:class:`byte`
      :async:


   .. py:method:: getPixelColor(self, _0:int, _1:int) -> :py:class:`Color`
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: setCursors(self, _0:MapCursorCollection) -> None
      :async:


   .. py:method:: setPixel(self, _0:int, _1:int, _2:byte) -> None
      :async:


   .. py:method:: setPixelColor(self, _0:int, _1:int, _2:Color) -> None
      :async:

