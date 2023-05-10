.. currentmodule:: pycraft.server.final

FileConfigurationOptions
========================

Inheritance
------------
* pycraft.server.final.FileConfigurationOptions
* :py:class:`pycraft.server.final.MemoryConfigurationOptions`
* :py:class:`pycraft.server.final.ConfigurationOptions`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.configuration.file.FileConfigurationOptions <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/configuration/file/FileConfigurationOptions.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: FileConfigurationOptions(self, **named)
   :canonical: pycraft.server.final.FileConfigurationOptions

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: configuration

       .. py:method:: configuration(self) -> :py:class:`FileConfiguration`
          :async:
          :noindex:

       .. py:method:: configuration(self) -> :py:class:`MemoryConfiguration`
          :async:
          :noindex:

       .. py:method:: configuration(self) -> :py:class:`Configuration`
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

       .. py:method:: copyDefaults(self, _0:boolean) -> :py:class:`FileConfigurationOptions`
          :async:
          :noindex:


   .. py:method:: copyHeader

       .. py:method:: copyHeader(self) -> bool
          :async:
          :noindex:

       .. py:method:: copyHeader(self, _0:boolean) -> :py:class:`FileConfigurationOptions`
          :async:
          :noindex:


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getFooter(self) -> typing.List[str]
      :async:


   .. py:method:: getHeader(self) -> typing.List[str]
      :async:


   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: header

       .. py:method:: header(self) -> str
          :async:
          :noindex:

       .. py:method:: header(self, _0:String) -> :py:class:`FileConfigurationOptions`
          :async:
          :noindex:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: parseComments

       .. py:method:: parseComments(self) -> bool
          :async:
          :noindex:

       .. py:method:: parseComments(self, _0:boolean) -> :py:class:`MemoryConfigurationOptions`
          :async:
          :noindex:


   .. py:method:: pathSeparator

       .. py:method:: pathSeparator(self) -> :py:class:`char`
          :async:
          :noindex:

       .. py:method:: pathSeparator(self, _0:char) -> :py:class:`MemoryConfigurationOptions`
          :async:
          :noindex:

       .. py:method:: pathSeparator(self, _0:char) -> :py:class:`ConfigurationOptions`
          :async:
          :noindex:

       .. py:method:: pathSeparator(self, _0:char) -> :py:class:`FileConfigurationOptions`
          :async:
          :noindex:


   .. py:method:: setFooter(self, _0:List) -> :py:class:`FileConfigurationOptions`
      :async:


   .. py:method:: setHeader(self, _0:List) -> :py:class:`FileConfigurationOptions`
      :async:


   .. py:method:: toString(self) -> str
      :async:

