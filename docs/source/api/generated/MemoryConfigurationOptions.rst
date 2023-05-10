.. currentmodule:: pycraft.server.final

MemoryConfigurationOptions
==========================

Inheritance
------------
* pycraft.server.final.MemoryConfigurationOptions
* :py:class:`pycraft.server.final.ConfigurationOptions`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.configuration.MemoryConfigurationOptions <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/configuration/MemoryConfigurationOptions.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: MemoryConfigurationOptions(self, **named)
   :canonical: pycraft.server.final.MemoryConfigurationOptions

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: configuration

       .. py:method:: configuration(self) -> :py:class:`Configuration`
          :async:
          :noindex:

       .. py:method:: configuration(self) -> :py:class:`MemoryConfiguration`
          :async:
          :noindex:


   .. py:method:: copyDefaults

       .. py:method:: copyDefaults(self) -> bool
          :async:
          :noindex:

       .. py:method:: copyDefaults(self, _0:boolean) -> :py:class:`MemoryConfigurationOptions`
          :async:
          :noindex:

       .. py:method:: copyDefaults(self, _0:boolean) -> :py:class:`ConfigurationOptions`
          :async:
          :noindex:


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: pathSeparator

       .. py:method:: pathSeparator(self) -> :py:class:`char`
          :async:
          :noindex:

       .. py:method:: pathSeparator(self, _0:char) -> :py:class:`ConfigurationOptions`
          :async:
          :noindex:

       .. py:method:: pathSeparator(self, _0:char) -> :py:class:`MemoryConfigurationOptions`
          :async:
          :noindex:


   .. py:method:: toString(self) -> str
      :async:

