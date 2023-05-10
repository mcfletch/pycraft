.. currentmodule:: pycraft.server.final

Plugin
======

Inheritance
------------
* pycraft.server.final.Plugin
* :py:class:`pycraft.server.final.TabExecutor`
* :py:class:`pycraft.server.final.TabCompleter`
* :py:class:`pycraft.server.final.CommandExecutor`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.plugin.Plugin <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/plugin/Plugin.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Plugin(self, **named)
   :canonical: pycraft.server.final.Plugin

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getComponentLogger(self) -> :py:class:`ComponentLogger`
      :async:


   .. py:method:: getConfig(self) -> :py:class:`FileConfiguration`
      :async:


   .. py:method:: getDataFolder(self) -> :py:class:`File`
      :async:


   .. py:method:: getDefaultBiomeProvider(self, _0:String, _1:String) -> :py:class:`BiomeProvider`
      :async:


   .. py:method:: getDefaultWorldGenerator(self, _0:String, _1:String) -> :py:class:`ChunkGenerator`
      :async:


   .. py:method:: getDescription(self) -> :py:class:`PluginDescriptionFile`
      :async:


   .. py:method:: getLog4JLogger(self) -> :py:class:`Logger`
      :async:


   .. py:method:: getLogger(self) -> :py:class:`Logger`
      :async:


   .. py:method:: getName(self) -> str
      :async:


   .. py:method:: getPluginLoader(self) -> :py:class:`PluginLoader`
      :async:


   .. py:method:: getPluginMeta(self) -> :py:class:`PluginMeta`
      :async:


   .. py:method:: getResource(self, _0:String) -> :py:class:`InputStream`
      :async:


   .. py:method:: getSLF4JLogger(self) -> :py:class:`Logger`
      :async:


   .. py:method:: getServer(self) -> :py:class:`Server`
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isEnabled(self) -> bool
      :async:


   .. py:method:: isNaggable(self) -> bool
      :async:


   .. py:method:: onCommand(self, _0:CommandSender, _1:Command, _2:String, _3:String[]) -> bool
      :async:


   .. py:method:: onDisable(self) -> None
      :async:


   .. py:method:: onEnable(self) -> None
      :async:


   .. py:method:: onLoad(self) -> None
      :async:


   .. py:method:: onTabComplete(self, _0:CommandSender, _1:Command, _2:String, _3:String[]) -> typing.List[str]
      :async:


   .. py:method:: reloadConfig(self) -> None
      :async:


   .. py:method:: saveConfig(self) -> None
      :async:


   .. py:method:: saveDefaultConfig(self) -> None
      :async:


   .. py:method:: saveResource(self, _0:String, _1:boolean) -> None
      :async:


   .. py:method:: setNaggable(self, _0:boolean) -> None
      :async:

