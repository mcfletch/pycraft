.. currentmodule:: pycraft.server.final

Registry
========

Inheritance
------------
* pycraft.server.final.Registry
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.Registry <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Registry.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Registry(self, **named)
   :canonical: pycraft.server.final.Registry

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: forEach(self, _0:Consumer) -> None
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: get(self, _0:NamespacedKey) -> :py:class:`Keyed`
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: iterator(self) -> :py:class:`Iterator`
      :async:


   .. py:method:: match(self, _0:String) -> :py:class:`Keyed`
      :async:


   .. py:method:: spliterator(self) -> :py:class:`Spliterator`
      :async:

