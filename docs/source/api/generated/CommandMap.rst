.. currentmodule:: pycraft.server.final

CommandMap
==========

Inheritance
------------
* pycraft.server.final.CommandMap
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.command.CommandMap <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/command/CommandMap.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: CommandMap(self, **named)
   :canonical: pycraft.server.final.CommandMap

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: clearCommands(self) -> None
      :async:


   .. py:method:: dispatch(self, _0:CommandSender, _1:String) -> bool
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getCommand(self, _0:String) -> :py:class:`Command`
      :async:


   .. py:method:: getKnownCommands(self) -> :py:class:`Map`
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: register

       .. py:method:: register(self, _0:String, _1:Command) -> bool
          :async:
          :noindex:

       .. py:method:: register(self, _0:String, _1:String, _2:Command) -> bool
          :async:
          :noindex:


   .. py:method:: registerAll(self, _0:String, _1:List) -> None
      :async:


   .. py:method:: tabComplete

       .. py:method:: tabComplete(self, _0:CommandSender, _1:String) -> typing.List[str]
          :async:
          :noindex:

       .. py:method:: tabComplete(self, _0:CommandSender, _1:String, _2:Location) -> typing.List[str]
          :async:
          :noindex:

