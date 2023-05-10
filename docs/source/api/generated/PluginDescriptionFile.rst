.. currentmodule:: pycraft.server.final

PluginDescriptionFile
=====================

Inheritance
------------
* pycraft.server.final.PluginDescriptionFile
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.plugin.PluginDescriptionFile <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/plugin/PluginDescriptionFile.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: PluginDescriptionFile(self, **named)
   :canonical: pycraft.server.final.PluginDescriptionFile

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getAPIVersion(self) -> str
      :async:


   .. py:method:: getAuthors(self) -> typing.List[str]
      :async:


   .. py:method:: getAwareness(self) -> typing.List[:py:class:`PluginAwareness`]
      :async:


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getClassLoaderOf(self) -> str
      :async:


   .. py:method:: getCommands(self) -> :py:class:`Map`
      :async:


   .. py:method:: getContributors(self) -> typing.List[str]
      :async:


   .. py:method:: getDepend(self) -> typing.List[str]
      :async:


   .. py:method:: getDescription(self) -> str
      :async:


   .. py:method:: getDisplayName(self) -> str
      :async:


   .. py:method:: getFullName(self) -> str
      :async:


   .. py:method:: getLibraries(self) -> typing.List[str]
      :async:


   .. py:method:: getLoad(self) -> :py:class:`PluginLoadOrder`
      :async:


   .. py:method:: getLoadBefore(self) -> typing.List[str]
      :async:


   .. py:method:: getLoadBeforePlugins(self) -> typing.List[str]
      :async:


   .. py:method:: getLoadOrder(self) -> :py:class:`PluginLoadOrder`
      :async:


   .. py:method:: getLoggerPrefix(self) -> str
      :async:


   .. py:method:: getMain(self) -> str
      :async:


   .. py:method:: getMainClass(self) -> str
      :async:


   .. py:method:: getName(self) -> str
      :async:


   .. py:method:: getPermissionDefault(self) -> :py:class:`PermissionDefault`
      :async:


   .. py:method:: getPermissions(self) -> typing.List[:py:class:`Permission`]
      :async:


   .. py:method:: getPluginDependencies(self) -> typing.List[str]
      :async:


   .. py:method:: getPluginSoftDependencies(self) -> typing.List[str]
      :async:


   .. py:method:: getPrefix(self) -> str
      :async:


   .. py:method:: getProvidedPlugins(self) -> typing.List[str]
      :async:


   .. py:method:: getProvides(self) -> typing.List[str]
      :async:


   .. py:method:: getRawName(self) -> str
      :async:


   .. py:method:: getSoftDepend(self) -> typing.List[str]
      :async:


   .. py:method:: getVersion(self) -> str
      :async:


   .. py:method:: getWebsite(self) -> str
      :async:


   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: save(self, _0:Writer) -> None
      :async:


   .. py:method:: toString(self) -> str
      :async:

