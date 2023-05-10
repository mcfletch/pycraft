.. currentmodule:: pycraft.server.final

ConfigurationSerializable
=========================

Inheritance
------------
* pycraft.server.final.ConfigurationSerializable
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.configuration.serialization.ConfigurationSerializable <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/configuration/serialization/ConfigurationSerializable.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: ConfigurationSerializable(self, **named)
   :canonical: pycraft.server.final.ConfigurationSerializable

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: serialize(self) -> :py:class:`Map`
      :async:

