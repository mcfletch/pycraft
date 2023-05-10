.. currentmodule:: pycraft.server.final

PluginIdentifiableCommand
=========================

Inheritance
------------
* pycraft.server.final.PluginIdentifiableCommand
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.command.PluginIdentifiableCommand <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/command/PluginIdentifiableCommand.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: PluginIdentifiableCommand(self, **named)
   :canonical: pycraft.server.final.PluginIdentifiableCommand

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getPlugin(self) -> :py:class:`Plugin`
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace

