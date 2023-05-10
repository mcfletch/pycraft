.. currentmodule:: pycraft.server.final

PluginMessageRecipient
======================

Inheritance
------------
* pycraft.server.final.PluginMessageRecipient
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.plugin.messaging.PluginMessageRecipient <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/plugin/messaging/PluginMessageRecipient.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: PluginMessageRecipient(self, **named)
   :canonical: pycraft.server.final.PluginMessageRecipient

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getListeningPluginChannels(self) -> typing.List[str]
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: sendPluginMessage(self, _0:Plugin, _1:String, _2:byte[]) -> None
      :async:

