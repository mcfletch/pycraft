.. currentmodule:: pycraft.server.final

Consumer
========

Inheritance
------------
* pycraft.server.final.Consumer
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.util.Consumer <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/util/Consumer.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Consumer(self, **named)
   :canonical: pycraft.server.final.Consumer

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: accept(self, _0:Object) -> None
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace

