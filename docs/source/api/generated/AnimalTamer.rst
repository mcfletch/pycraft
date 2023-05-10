.. currentmodule:: pycraft.server.final

AnimalTamer
===========

Inheritance
------------
* pycraft.server.final.AnimalTamer
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.entity.AnimalTamer <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/entity/AnimalTamer.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: AnimalTamer(self, **named)
   :canonical: pycraft.server.final.AnimalTamer

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getName(self) -> str
      :async:


   .. py:method:: getUniqueId(self) -> uuid.UUID
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace

