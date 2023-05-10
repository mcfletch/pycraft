.. currentmodule:: pycraft.server.final

Colorable
=========

Inheritance
------------
* pycraft.server.final.Colorable
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.material.Colorable <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/material/Colorable.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Colorable(self, **named)
   :canonical: pycraft.server.final.Colorable

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getColor(self) -> :py:class:`DyeColor`
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: setColor(self, _0:DyeColor) -> None
      :async:

