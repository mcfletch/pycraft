.. currentmodule:: pycraft.server.final

ItemTagAdapterContext
=====================

Inheritance
------------
* pycraft.server.final.ItemTagAdapterContext
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.inventory.meta.tags.ItemTagAdapterContext <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/inventory/meta/tags/ItemTagAdapterContext.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: ItemTagAdapterContext(self, **named)
   :canonical: pycraft.server.final.ItemTagAdapterContext

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: newTagContainer(self) -> :py:class:`CustomItemTagContainer`
      :async:

