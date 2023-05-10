.. currentmodule:: pycraft.server.final

Messenger
=========

Inheritance
------------
* pycraft.server.final.Messenger
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.plugin.messaging.Messenger <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/plugin/messaging/Messenger.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Messenger(self, **named)
   :canonical: pycraft.server.final.Messenger

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: dispatchIncomingMessage(self, _0:Player, _1:String, _2:byte[]) -> None
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getIncomingChannelRegistrations

       .. py:method:: getIncomingChannelRegistrations(self, _0:Plugin) -> typing.List[:py:class:`PluginMessageListenerRegistration`]
          :async:
          :noindex:

       .. py:method:: getIncomingChannelRegistrations(self, _0:String) -> typing.List[:py:class:`PluginMessageListenerRegistration`]
          :async:
          :noindex:

       .. py:method:: getIncomingChannelRegistrations(self, _0:Plugin, _1:String) -> typing.List[:py:class:`PluginMessageListenerRegistration`]
          :async:
          :noindex:


   .. py:method:: getIncomingChannels

       .. py:method:: getIncomingChannels(self) -> typing.List[str]
          :async:
          :noindex:

       .. py:method:: getIncomingChannels(self, _0:Plugin) -> typing.List[str]
          :async:
          :noindex:


   .. py:method:: getOutgoingChannels

       .. py:method:: getOutgoingChannels(self) -> typing.List[str]
          :async:
          :noindex:

       .. py:method:: getOutgoingChannels(self, _0:Plugin) -> typing.List[str]
          :async:
          :noindex:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isIncomingChannelRegistered(self, _0:Plugin, _1:String) -> bool
      :async:


   .. py:method:: isOutgoingChannelRegistered(self, _0:Plugin, _1:String) -> bool
      :async:


   .. py:method:: isRegistrationValid(self, _0:PluginMessageListenerRegistration) -> bool
      :async:


   .. py:method:: isReservedChannel(self, _0:String) -> bool
      :async:


   .. py:method:: registerIncomingPluginChannel(self, _0:Plugin, _1:String, _2:PluginMessageListener) -> :py:class:`PluginMessageListenerRegistration`
      :async:


   .. py:method:: registerOutgoingPluginChannel(self, _0:Plugin, _1:String) -> None
      :async:


   .. py:method:: unregisterIncomingPluginChannel

       .. py:method:: unregisterIncomingPluginChannel(self, _0:Plugin) -> None
          :async:
          :noindex:

       .. py:method:: unregisterIncomingPluginChannel(self, _0:Plugin, _1:String) -> None
          :async:
          :noindex:

       .. py:method:: unregisterIncomingPluginChannel(self, _0:Plugin, _1:String, _2:PluginMessageListener) -> None
          :async:
          :noindex:


   .. py:method:: unregisterOutgoingPluginChannel

       .. py:method:: unregisterOutgoingPluginChannel(self, _0:Plugin) -> None
          :async:
          :noindex:

       .. py:method:: unregisterOutgoingPluginChannel(self, _0:Plugin, _1:String) -> None
          :async:
          :noindex:

