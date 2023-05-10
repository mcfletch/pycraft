.. currentmodule:: pycraft.server.final

CachedServerIcon
================

Inheritance
------------
* pycraft.server.final.CachedServerIcon
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.util.CachedServerIcon <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/util/CachedServerIcon.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: CachedServerIcon(self, **named)
   :canonical: pycraft.server.final.CachedServerIcon

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getData(self) -> str
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isEmpty(self) -> bool
      :async:

