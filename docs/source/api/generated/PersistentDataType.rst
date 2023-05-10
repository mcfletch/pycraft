.. currentmodule:: pycraft.server.final

PersistentDataType
==================

Inheritance
------------
* pycraft.server.final.PersistentDataType
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.persistence.PersistentDataType <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/persistence/PersistentDataType.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: PersistentDataType(self, **named)
   :canonical: pycraft.server.final.PersistentDataType

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: fromPrimitive(self, _0:Object, _1:PersistentDataAdapterContext) -> :py:class:`Object`
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getComplexType(self) -> :py:class:`Class`
      :async:


   .. py:method:: getPrimitiveType(self) -> :py:class:`Class`
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: toPrimitive(self, _0:Object, _1:PersistentDataAdapterContext) -> :py:class:`Object`
      :async:

