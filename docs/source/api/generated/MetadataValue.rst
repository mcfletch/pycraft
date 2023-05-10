.. currentmodule:: pycraft.server.final

MetadataValue
=============

Inheritance
------------
* pycraft.server.final.MetadataValue
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.metadata.MetadataValue <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/metadata/MetadataValue.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: MetadataValue(self, **named)
   :canonical: pycraft.server.final.MetadataValue

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: asBoolean(self) -> bool
      :async:


   .. py:method:: asByte(self) -> :py:class:`byte`
      :async:


   .. py:method:: asDouble(self) -> float
      :async:


   .. py:method:: asFloat(self) -> float
      :async:


   .. py:method:: asInt(self) -> int
      :async:


   .. py:method:: asLong(self) -> :py:class:`long`
      :async:


   .. py:method:: asShort(self) -> :py:class:`short`
      :async:


   .. py:method:: asString(self) -> str
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getOwningPlugin(self) -> :py:class:`Plugin`
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: invalidate(self) -> None
      :async:


   .. py:method:: value(self) -> :py:class:`Object`
      :async:

