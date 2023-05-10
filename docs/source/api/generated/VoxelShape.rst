.. currentmodule:: pycraft.server.final

VoxelShape
==========

Inheritance
------------
* pycraft.server.final.VoxelShape
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.util.VoxelShape <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/util/VoxelShape.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: VoxelShape(self, **named)
   :canonical: pycraft.server.final.VoxelShape

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getBoundingBoxes(self) -> typing.List[:py:class:`BoundingBox`]
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: overlaps(self, _0:BoundingBox) -> bool
      :async:

