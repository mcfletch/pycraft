.. currentmodule:: pycraft.server.final

Spigot
======

Inheritance
------------
* pycraft.server.final.Spigot
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.command.CommandSender.Spigot <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/command/CommandSender/Spigot.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Spigot(self, **named)
   :canonical: pycraft.server.final.Spigot

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: sendMessage

       .. py:method:: sendMessage(self, _0:BaseComponent[]) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:BaseComponent) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:UUID, _1:BaseComponent[]) -> None
          :async:
          :noindex:

       .. py:method:: sendMessage(self, _0:UUID, _1:BaseComponent) -> None
          :async:
          :noindex:


   .. py:method:: toString(self) -> str
      :async:

