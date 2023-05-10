.. currentmodule:: pycraft.server.final

TabCompleter
============

Inheritance
------------
* pycraft.server.final.TabCompleter
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.command.TabCompleter <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/command/TabCompleter.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: TabCompleter(self, **named)
   :canonical: pycraft.server.final.TabCompleter

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: onTabComplete(self, _0:CommandSender, _1:Command, _2:String, _3:String[]) -> typing.List[str]
      :async:

