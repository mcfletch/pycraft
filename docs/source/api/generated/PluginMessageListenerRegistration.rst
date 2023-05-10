.. currentmodule:: pycraft.server.final

PluginMessageListenerRegistration
=================================

Inheritance
------------
* pycraft.server.final.PluginMessageListenerRegistration
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.plugin.messaging.PluginMessageListenerRegistration <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/plugin/messaging/PluginMessageListenerRegistration.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: PluginMessageListenerRegistration(self, **named)
   :canonical: pycraft.server.final.PluginMessageListenerRegistration

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getChannel(self) -> str
      :async:


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getListener(self) -> :py:class:`PluginMessageListener`
      :async:


   .. py:method:: getPlugin(self) -> :py:class:`Plugin`
      :async:


   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isValid(self) -> bool
      :async:


   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: toString(self) -> str
      :async:

