.. currentmodule:: pycraft.server.final

PluginManager
=============

Inheritance
------------
* pycraft.server.final.PluginManager
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.plugin.PluginManager <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/plugin/PluginManager.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: PluginManager(self, **named)
   :canonical: pycraft.server.final.PluginManager

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: addPermission(self, _0:Permission) -> None
      :async:


   .. py:method:: addPermissions(self, _0:List) -> None
      :async:


   .. py:method:: callEvent(self, _0:Event) -> None
      :async:


   .. py:method:: clearPermissions(self) -> None
      :async:


   .. py:method:: clearPlugins(self) -> None
      :async:


   .. py:method:: disablePlugin(self, _0:Plugin) -> None
      :async:


   .. py:method:: disablePlugins(self) -> None
      :async:


   .. py:method:: enablePlugin(self, _0:Plugin) -> None
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getDefaultPermSubscriptions(self, _0:boolean) -> typing.List[:py:class:`Permissible`]
      :async:


   .. py:method:: getDefaultPermissions(self, _0:boolean) -> typing.List[:py:class:`Permission`]
      :async:


   .. py:method:: getPermission(self, _0:String) -> :py:class:`Permission`
      :async:


   .. py:method:: getPermissionSubscriptions(self, _0:String) -> typing.List[:py:class:`Permissible`]
      :async:


   .. py:method:: getPermissions(self) -> typing.List[:py:class:`Permission`]
      :async:


   .. py:method:: getPlugin(self, _0:String) -> :py:class:`Plugin`
      :async:


   .. py:method:: getPlugins(self) -> typing.List[:py:class:`Plugin`]
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isPluginEnabled

       .. py:method:: isPluginEnabled(self, _0:String) -> bool
          :async:
          :noindex:

       .. py:method:: isPluginEnabled(self, _0:Plugin) -> bool
          :async:
          :noindex:


   .. py:method:: isTransitiveDependency(self, _0:PluginMeta, _1:PluginMeta) -> bool
      :async:


   .. py:method:: loadPlugin(self, _0:File) -> :py:class:`Plugin`
      :async:


   .. py:method:: loadPlugins(self, _0:File) -> typing.List[:py:class:`Plugin`]
      :async:


   .. py:method:: overridePermissionManager(self, _0:Plugin, _1:PermissionManager) -> None
      :async:


   .. py:method:: recalculatePermissionDefaults(self, _0:Permission) -> None
      :async:


   .. py:method:: registerEvent

       .. py:method:: registerEvent(self, _0:Class, _1:Listener, _2:EventPriority, _3:EventExecutor, _4:Plugin) -> None
          :async:
          :noindex:

       .. py:method:: registerEvent(self, _0:Class, _1:Listener, _2:EventPriority, _3:EventExecutor, _4:Plugin, _5:boolean) -> None
          :async:
          :noindex:


   .. py:method:: registerEvents(self, _0:Listener, _1:Plugin) -> None
      :async:


   .. py:method:: registerInterface(self, _0:Class) -> None
      :async:


   .. py:method:: removePermission

       .. py:method:: removePermission(self, _0:Permission) -> None
          :async:
          :noindex:

       .. py:method:: removePermission(self, _0:String) -> None
          :async:
          :noindex:


   .. py:method:: subscribeToDefaultPerms(self, _0:boolean, _1:Permissible) -> None
      :async:


   .. py:method:: subscribeToPermission(self, _0:String, _1:Permissible) -> None
      :async:


   .. py:method:: unsubscribeFromDefaultPerms(self, _0:boolean, _1:Permissible) -> None
      :async:


   .. py:method:: unsubscribeFromPermission(self, _0:String, _1:Permissible) -> None
      :async:


   .. py:method:: useTimings(self) -> bool
      :async:

