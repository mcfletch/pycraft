.. currentmodule:: pycraft.server.final

StructureSearchResult
=====================

Inheritance
------------
* pycraft.server.final.StructureSearchResult
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.util.StructureSearchResult <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/util/StructureSearchResult.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: StructureSearchResult(self, **named)
   :canonical: pycraft.server.final.StructureSearchResult

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getLocation(self) -> :py:class:`Location`
      :async:


   .. py:method:: getStructure(self) -> :py:class:`Structure`
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace

