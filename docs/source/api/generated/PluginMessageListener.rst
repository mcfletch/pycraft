.. currentmodule:: pycraft.server.final

PluginMessageListener
=====================

Inheritance
------------
* pycraft.server.final.PluginMessageListener
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.plugin.messaging.PluginMessageListener <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/plugin/messaging/PluginMessageListener.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: PluginMessageListener(self, **named)
   :canonical: pycraft.server.final.PluginMessageListener

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: onPluginMessageReceived(self, _0:String, _1:Player, _2:byte[]) -> None
      :async:

