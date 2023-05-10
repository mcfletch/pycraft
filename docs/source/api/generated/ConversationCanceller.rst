.. currentmodule:: pycraft.server.final

ConversationCanceller
=====================

Inheritance
------------
* pycraft.server.final.ConversationCanceller
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.conversations.ConversationCanceller <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/conversations/ConversationCanceller.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: ConversationCanceller(self, **named)
   :canonical: pycraft.server.final.ConversationCanceller

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: cancelBasedOnInput(self, _0:ConversationContext, _1:String) -> bool
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: setConversation(self, _0:Conversation) -> None
      :async:

