.. currentmodule:: pycraft.server.final

ChunkLoadCallback
=================

Inheritance
------------
* pycraft.server.final.ChunkLoadCallback
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.World.ChunkLoadCallback <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/World/ChunkLoadCallback.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: ChunkLoadCallback(self, **named)
   :canonical: pycraft.server.final.ChunkLoadCallback

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: accept

       .. py:method:: accept(self, _0:Chunk) -> None
          :async:
          :noindex:

       .. py:method:: accept(self, _0:Object) -> None
          :async:
          :noindex:


   .. py:method:: andThen(self, _0:Consumer) -> :py:class:`Consumer`
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: onLoad(self, _0:Chunk) -> None
      :async:

