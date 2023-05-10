.. currentmodule:: pycraft.server.final

PluginLoader
============

Inheritance
------------
* pycraft.server.final.PluginLoader
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.plugin.PluginLoader <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/plugin/PluginLoader.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: PluginLoader(self, **named)
   :canonical: pycraft.server.final.PluginLoader

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: createRegisteredListeners(self, _0:Listener, _1:Plugin) -> :py:class:`Map`
      :async:


   .. py:method:: disablePlugin(self, _0:Plugin) -> None
      :async:


   .. py:method:: enablePlugin(self, _0:Plugin) -> None
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getPluginDescription(self, _0:File) -> :py:class:`PluginDescriptionFile`
      :async:


   .. py:method:: getPluginFileFilters(self) -> typing.List[:py:class:`Pattern`]
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: loadPlugin(self, _0:File) -> :py:class:`Plugin`
      :async:

