.. currentmodule:: pycraft.server.final

CustomItemTagContainer
======================

Inheritance
------------
* pycraft.server.final.CustomItemTagContainer
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.inventory.meta.tags.CustomItemTagContainer <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/inventory/meta/tags/CustomItemTagContainer.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: CustomItemTagContainer(self, **named)
   :canonical: pycraft.server.final.CustomItemTagContainer

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getAdapterContext(self) -> :py:class:`ItemTagAdapterContext`
      :async:


   .. py:method:: getCustomTag(self, _0:NamespacedKey, _1:ItemTagType) -> :py:class:`Object`
      :async:


   .. py:method:: hasCustomTag(self, _0:NamespacedKey, _1:ItemTagType) -> bool
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isEmpty(self) -> bool
      :async:


   .. py:method:: removeCustomTag(self, _0:NamespacedKey) -> None
      :async:


   .. py:method:: setCustomTag(self, _0:NamespacedKey, _1:ItemTagType, _2:Object) -> None
      :async:

