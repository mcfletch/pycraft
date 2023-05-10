.. currentmodule:: pycraft.server.final

ConversationContext
===================

Inheritance
------------
* pycraft.server.final.ConversationContext
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.conversations.ConversationContext <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/conversations/ConversationContext.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: ConversationContext(self, **named)
   :canonical: pycraft.server.final.ConversationContext

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getAllSessionData(self) -> :py:class:`Map`
      :async:


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getForWhom(self) -> :py:class:`Conversable`
      :async:


   .. py:method:: getPlugin(self) -> :py:class:`Plugin`
      :async:


   .. py:method:: getSessionData(self, _0:Object) -> :py:class:`Object`
      :async:


   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: setSessionData(self, _0:Object, _1:Object) -> None
      :async:


   .. py:method:: toString(self) -> str
      :async:

