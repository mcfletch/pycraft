.. currentmodule:: pycraft.server.final

TabExecutor
===========

Inheritance
------------
* pycraft.server.final.TabExecutor
* :py:class:`pycraft.server.final.TabCompleter`
* :py:class:`pycraft.server.final.CommandExecutor`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.command.TabExecutor <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/command/TabExecutor.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: TabExecutor(self, **named)
   :canonical: pycraft.server.final.TabExecutor

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: onCommand(self, _0:CommandSender, _1:Command, _2:String, _3:String[]) -> bool
      :async:


   .. py:method:: onTabComplete(self, _0:CommandSender, _1:Command, _2:String, _3:String[]) -> typing.List[str]
      :async:

