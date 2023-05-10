.. currentmodule:: pycraft.server.final

PluginCommand
=============

Inheritance
------------
* pycraft.server.final.PluginCommand
* :py:class:`pycraft.server.final.PluginIdentifiableCommand`
* :py:class:`pycraft.server.final.Command`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.command.PluginCommand <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/command/PluginCommand.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: PluginCommand(self, **named)
   :canonical: pycraft.server.final.PluginCommand

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: broadcastCommandMessage

       .. py:method:: broadcastCommandMessage(cls, _0:CommandSender, _1:String) -> None
          :async:
          :classmethod:
          :noindex:

       .. py:method:: broadcastCommandMessage(cls, _0:CommandSender, _1:Component) -> None
          :async:
          :classmethod:
          :noindex:

       .. py:method:: broadcastCommandMessage(cls, _0:CommandSender, _1:String, _2:boolean) -> None
          :async:
          :classmethod:
          :noindex:

       .. py:method:: broadcastCommandMessage(cls, _0:CommandSender, _1:Component, _2:boolean) -> None
          :async:
          :classmethod:
          :noindex:


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: execute(self, _0:CommandSender, _1:String, _2:String[]) -> bool
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getAliases(self) -> typing.List[str]
      :async:


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getDescription(self) -> str
      :async:


   .. py:method:: getExecutor(self) -> :py:class:`CommandExecutor`
      :async:


   .. py:method:: getLabel(self) -> str
      :async:


   .. py:method:: getName(self) -> str
      :async:


   .. py:method:: getPermission(self) -> str
      :async:


   .. py:method:: getPermissionMessage(self) -> str
      :async:


   .. py:method:: getPlugin(self) -> :py:class:`Plugin`
      :async:


   .. py:method:: getTabCompleter(self) -> :py:class:`TabCompleter`
      :async:


   .. py:method:: getTimingName(self) -> str
      :async:


   .. py:method:: getUsage(self) -> str
      :async:


   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isRegistered(self) -> bool
      :async:


   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: permissionMessage

       .. py:method:: permissionMessage(self) -> :py:class:`Component`
          :async:
          :noindex:

       .. py:method:: permissionMessage(self, _0:Component) -> None
          :async:
          :noindex:


   .. py:method:: register(self, _0:CommandMap) -> bool
      :async:


   .. py:method:: setAliases(self, _0:List) -> :py:class:`Command`
      :async:


   .. py:method:: setDescription(self, _0:String) -> :py:class:`Command`
      :async:


   .. py:method:: setExecutor(self, _0:CommandExecutor) -> None
      :async:


   .. py:method:: setLabel(self, _0:String) -> bool
      :async:


   .. py:method:: setName(self, _0:String) -> bool
      :async:


   .. py:method:: setPermission(self, _0:String) -> None
      :async:


   .. py:method:: setPermissionMessage(self, _0:String) -> :py:class:`Command`
      :async:


   .. py:method:: setTabCompleter(self, _0:TabCompleter) -> None
      :async:


   .. py:method:: setUsage(self, _0:String) -> :py:class:`Command`
      :async:


   .. py:method:: tabComplete

       .. py:method:: tabComplete(self, _0:CommandSender, _1:String, _2:String[]) -> typing.List[str]
          :async:
          :noindex:

       .. py:method:: tabComplete(self, _0:CommandSender, _1:String, _2:String[], _3:Location) -> typing.List[str]
          :async:
          :noindex:


   .. py:method:: testPermission(self, _0:CommandSender) -> bool
      :async:


   .. py:method:: testPermissionSilent(self, _0:CommandSender) -> bool
      :async:


   .. py:method:: toString(self) -> str
      :async:


   .. py:method:: unregister(self, _0:CommandMap) -> bool
      :async:

