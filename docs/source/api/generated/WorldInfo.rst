.. currentmodule:: pycraft.server.final

WorldInfo
=========

Inheritance
------------
* pycraft.server.final.WorldInfo
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.generator.WorldInfo <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/generator/WorldInfo.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: WorldInfo(self, **named)
   :canonical: pycraft.server.final.WorldInfo

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getEnvironment(self) -> :py:class:`Environment`
      :async:


   .. py:method:: getMaxHeight(self) -> int
      :async:


   .. py:method:: getMinHeight(self) -> int
      :async:


   .. py:method:: getName(self) -> str
      :async:


   .. py:method:: getSeed(self) -> :py:class:`long`
      :async:


   .. py:method:: getUID(self) -> uuid.UUID
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: vanillaBiomeProvider(self) -> :py:class:`BiomeProvider`
      :async:

