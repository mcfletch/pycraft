.. currentmodule:: pycraft.server.final

MapRenderer
===========

Inheritance
------------
* pycraft.server.final.MapRenderer
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.map.MapRenderer <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/map/MapRenderer.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: MapRenderer(self, **named)
   :canonical: pycraft.server.final.MapRenderer

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: initialize(self, _0:MapView) -> None
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isContextual(self) -> bool
      :async:


   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: render(self, _0:MapView, _1:MapCanvas, _2:Player) -> None
      :async:


   .. py:method:: toString(self) -> str
      :async:

