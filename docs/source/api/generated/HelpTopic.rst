.. currentmodule:: pycraft.server.final

HelpTopic
=========

Inheritance
------------
* pycraft.server.final.HelpTopic
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.help.HelpTopic <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/help/HelpTopic.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: HelpTopic(self, **named)
   :canonical: pycraft.server.final.HelpTopic

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: amendCanSee(self, _0:String) -> None
      :async:


   .. py:method:: amendTopic(self, _0:String, _1:String) -> None
      :async:


   .. py:method:: canSee(self, _0:CommandSender) -> bool
      :async:


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getFullText(self, _0:CommandSender) -> str
      :async:


   .. py:method:: getName(self) -> str
      :async:


   .. py:method:: getShortText(self) -> str
      :async:


   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: toString(self) -> str
      :async:

