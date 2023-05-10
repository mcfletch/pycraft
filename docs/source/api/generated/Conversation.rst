.. currentmodule:: pycraft.server.final

Conversation
============

Inheritance
------------
* pycraft.server.final.Conversation
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.conversations.Conversation <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/conversations/Conversation.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Conversation(self, **named)
   :canonical: pycraft.server.final.Conversation

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: abandon

       .. py:method:: abandon(self) -> None
          :async:
          :noindex:

       .. py:method:: abandon(self, _0:ConversationAbandonedEvent) -> None
          :async:
          :noindex:


   .. py:method:: acceptInput(self, _0:String) -> None
      :async:


   .. py:method:: addConversationAbandonedListener(self, _0:ConversationAbandonedListener) -> None
      :async:


   .. py:method:: begin(self) -> None
      :async:


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getCancellers(self) -> typing.List[:py:class:`ConversationCanceller`]
      :async:


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getContext(self) -> :py:class:`ConversationContext`
      :async:


   .. py:method:: getForWhom(self) -> :py:class:`Conversable`
      :async:


   .. py:method:: getPrefix(self) -> :py:class:`ConversationPrefix`
      :async:


   .. py:method:: getState(self) -> :py:class:`ConversationState`
      :async:


   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isLocalEchoEnabled(self) -> bool
      :async:


   .. py:method:: isModal(self) -> bool
      :async:


   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: outputNextPrompt(self) -> None
      :async:


   .. py:method:: removeConversationAbandonedListener(self, _0:ConversationAbandonedListener) -> None
      :async:


   .. py:method:: setLocalEchoEnabled(self, _0:boolean) -> None
      :async:


   .. py:method:: toString(self) -> str
      :async:

