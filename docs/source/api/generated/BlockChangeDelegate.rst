.. currentmodule:: pycraft.server.final

BlockChangeDelegate
===================

Inheritance
------------
* pycraft.server.final.BlockChangeDelegate
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.BlockChangeDelegate <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/BlockChangeDelegate.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: BlockChangeDelegate(self, **named)
   :canonical: pycraft.server.final.BlockChangeDelegate

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getBlockData(self, _0:int, _1:int, _2:int) -> :py:class:`BlockData`
      :async:


   .. py:method:: getHeight(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isEmpty(self, _0:int, _1:int, _2:int) -> bool
      :async:


   .. py:method:: setBlockData(self, _0:int, _1:int, _2:int, _3:BlockData) -> bool
      :async:

