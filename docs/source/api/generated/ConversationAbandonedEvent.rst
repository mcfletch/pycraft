.. currentmodule:: pycraft.server.final

ConversationAbandonedEvent
==========================

Inheritance
------------
* pycraft.server.final.ConversationAbandonedEvent
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.conversations.ConversationAbandonedEvent <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/conversations/ConversationAbandonedEvent.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: ConversationAbandonedEvent(self, **named)
   :canonical: pycraft.server.final.ConversationAbandonedEvent

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getCanceller(self) -> :py:class:`ConversationCanceller`
      :async:


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getContext(self) -> :py:class:`ConversationContext`
      :async:


   .. py:method:: getSource(self) -> :py:class:`Object`
      :async:


   .. py:method:: gracefulExit(self) -> bool
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

