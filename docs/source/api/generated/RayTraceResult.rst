.. currentmodule:: pycraft.server.final

RayTraceResult
==============

Inheritance
------------
* pycraft.server.final.RayTraceResult
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.util.RayTraceResult <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/util/RayTraceResult.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: RayTraceResult(self, **named)
   :canonical: pycraft.server.final.RayTraceResult

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


   .. py:method:: getHitBlock(self) -> :py:class:`Block`
      :async:


   .. py:method:: getHitBlockFace(self) -> :py:class:`BlockFace`
      :async:


   .. py:method:: getHitEntity(self) -> :py:class:`Entity`
      :async:


   .. py:method:: getHitPosition(self) -> :py:class:`Vector`
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

