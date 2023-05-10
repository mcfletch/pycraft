.. currentmodule:: pycraft.server.final

CommandExecutor
===============

Inheritance
------------
* pycraft.server.final.CommandExecutor
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.command.CommandExecutor <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/command/CommandExecutor.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: CommandExecutor(self, **named)
   :canonical: pycraft.server.final.CommandExecutor

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

