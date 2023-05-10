.. currentmodule:: pycraft.server.final

ConversationPrefix
==================

Inheritance
------------
* pycraft.server.final.ConversationPrefix
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.conversations.ConversationPrefix <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/conversations/ConversationPrefix.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: ConversationPrefix(self, **named)
   :canonical: pycraft.server.final.ConversationPrefix

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getPrefix(self, _0:ConversationContext) -> str
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace

