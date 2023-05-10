.. currentmodule:: pycraft.server.final

PersistentDataContainer
=======================

Inheritance
------------
* pycraft.server.final.PersistentDataContainer
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.persistence.PersistentDataContainer <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/persistence/PersistentDataContainer.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: PersistentDataContainer(self, **named)
   :canonical: pycraft.server.final.PersistentDataContainer

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: get(self, _0:NamespacedKey, _1:PersistentDataType) -> :py:class:`Object`
      :async:


   .. py:method:: getAdapterContext(self) -> :py:class:`PersistentDataAdapterContext`
      :async:


   .. py:method:: getKeys(self) -> typing.List[:py:class:`NamespacedKey`]
      :async:


   .. py:method:: getOrDefault(self, _0:NamespacedKey, _1:PersistentDataType, _2:Object) -> :py:class:`Object`
      :async:


   .. py:method:: has

       .. py:method:: has(self, _0:NamespacedKey) -> bool
          :async:
          :noindex:

       .. py:method:: has(self, _0:NamespacedKey, _1:PersistentDataType) -> bool
          :async:
          :noindex:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isEmpty(self) -> bool
      :async:


   .. py:method:: readFromBytes

       .. py:method:: readFromBytes(self, _0:byte[]) -> None
          :async:
          :noindex:

       .. py:method:: readFromBytes(self, _0:byte[], _1:boolean) -> None
          :async:
          :noindex:


   .. py:method:: remove(self, _0:NamespacedKey) -> None
      :async:


   .. py:method:: serializeToBytes(self) -> typing.List[:py:class:`byte`]
      :async:


   .. py:method:: set(self, _0:NamespacedKey, _1:PersistentDataType, _2:Object) -> None
      :async:

