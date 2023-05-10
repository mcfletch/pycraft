.. currentmodule:: pycraft.server.final

WorldBorder
===========

Inheritance
------------
* pycraft.server.final.WorldBorder
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.WorldBorder <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/WorldBorder.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: WorldBorder(self, **named)
   :canonical: pycraft.server.final.WorldBorder

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getCenter(self) -> :py:class:`Location`
      :async:


   .. py:method:: getDamageAmount(self) -> float
      :async:


   .. py:method:: getDamageBuffer(self) -> float
      :async:


   .. py:method:: getMaxCenterCoordinate(self) -> float
      :async:


   .. py:method:: getMaxSize(self) -> float
      :async:


   .. py:method:: getSize(self) -> float
      :async:


   .. py:method:: getWarningDistance(self) -> int
      :async:


   .. py:method:: getWarningTime(self) -> int
      :async:


   .. py:method:: getWorld(self) -> :py:class:`World`
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isInBounds(self, _0:Location) -> bool
      :async:


   .. py:method:: isInside(self, _0:Location) -> bool
      :async:


   .. py:method:: reset(self) -> None
      :async:


   .. py:method:: setCenter

       .. py:method:: setCenter(self, _0:Location) -> None
          :async:
          :noindex:

       .. py:method:: setCenter(self, _0:double, _1:double) -> None
          :async:
          :noindex:


   .. py:method:: setDamageAmount(self, _0:double) -> None
      :async:


   .. py:method:: setDamageBuffer(self, _0:double) -> None
      :async:


   .. py:method:: setSize

       .. py:method:: setSize(self, _0:double) -> None
          :async:
          :noindex:

       .. py:method:: setSize(self, _0:double, _1:long) -> None
          :async:
          :noindex:

       .. py:method:: setSize(self, _0:double, _1:TimeUnit, _2:long) -> None
          :async:
          :noindex:


   .. py:method:: setWarningDistance(self, _0:int) -> None
      :async:


   .. py:method:: setWarningTime(self, _0:int) -> None
      :async:

