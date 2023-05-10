.. currentmodule:: pycraft.server.final

Conversable
===========

Inheritance
------------
* pycraft.server.final.Conversable
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.conversations.Conversable <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/conversations/Conversable.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Conversable(self, **named)
   :canonical: pycraft.server.final.Conversable

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: abandonConversation

       .. py:method:: abandonConversation(self, _0:Conversation) -> None
          :async:
          :noindex:

       .. py:method:: abandonConversation(self, _0:Conversation, _1:ConversationAbandonedEvent) -> None
          :async:
          :noindex:


   .. py:method:: acceptConversationInput(self, _0:String) -> None
      :async:


   .. py:method:: beginConversation(self, _0:Conversation) -> bool
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isConversing(self) -> bool
      :async:


   .. py:method:: sendRawMessage

       .. py:method:: sendRawMessage(self, _0:String) -> None
          :async:
          :noindex:

       .. py:method:: sendRawMessage(self, _0:UUID, _1:String) -> None
          :async:
          :noindex:

