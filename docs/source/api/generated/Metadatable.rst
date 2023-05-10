.. currentmodule:: pycraft.server.final

Metadatable
===========

Inheritance
------------
* pycraft.server.final.Metadatable
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.metadata.Metadatable <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/metadata/Metadatable.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Metadatable(self, **named)
   :canonical: pycraft.server.final.Metadatable

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getMetadata(self, _0:String) -> typing.List[:py:class:`MetadataValue`]
      :async:


   .. py:method:: hasMetadata(self, _0:String) -> bool
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: removeMetadata(self, _0:String, _1:Plugin) -> None
      :async:


   .. py:method:: setMetadata(self, _0:String, _1:MetadataValue) -> None
      :async:

