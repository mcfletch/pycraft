.. currentmodule:: pycraft.server.final

MapView
=======

Inheritance
------------
* pycraft.server.final.MapView
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.map.MapView <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/map/MapView.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: MapView(self, **named)
   :canonical: pycraft.server.final.MapView

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: addRenderer(self, _0:MapRenderer) -> None
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getCenterX(self) -> int
      :async:


   .. py:method:: getCenterZ(self) -> int
      :async:


   .. py:method:: getId(self) -> int
      :async:


   .. py:method:: getRenderers(self) -> typing.List[:py:class:`MapRenderer`]
      :async:


   .. py:method:: getScale(self) -> :py:class:`Scale`
      :async:


   .. py:method:: getWorld(self) -> :py:class:`World`
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isLocked(self) -> bool
      :async:


   .. py:method:: isTrackingPosition(self) -> bool
      :async:


   .. py:method:: isUnlimitedTracking(self) -> bool
      :async:


   .. py:method:: isVirtual(self) -> bool
      :async:


   .. py:method:: removeRenderer(self, _0:MapRenderer) -> bool
      :async:


   .. py:method:: setCenterX(self, _0:int) -> None
      :async:


   .. py:method:: setCenterZ(self, _0:int) -> None
      :async:


   .. py:method:: setLocked(self, _0:boolean) -> None
      :async:


   .. py:method:: setScale(self, _0:Scale) -> None
      :async:


   .. py:method:: setTrackingPosition(self, _0:boolean) -> None
      :async:


   .. py:method:: setUnlimitedTracking(self, _0:boolean) -> None
      :async:


   .. py:method:: setWorld(self, _0:World) -> None
      :async:

