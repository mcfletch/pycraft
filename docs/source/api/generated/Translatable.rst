.. currentmodule:: pycraft.server.final

Translatable
============

Inheritance
------------
* pycraft.server.final.Translatable
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.Translatable <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Translatable.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Translatable(self, **named)
   :canonical: pycraft.server.final.Translatable

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getTranslationKey(self) -> str
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace

