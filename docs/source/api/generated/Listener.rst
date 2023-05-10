.. currentmodule:: pycraft.server.final

Listener
========

Inheritance
------------
* pycraft.server.final.Listener
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.event.Listener <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/event/Listener.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Listener(self, **named)
   :canonical: pycraft.server.final.Listener

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace

