.. currentmodule:: pycraft.server.final

PreviousInteraction
===================

Inheritance
------------
* pycraft.server.final.PreviousInteraction
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.entity.Interaction.PreviousInteraction <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/entity/Interaction/PreviousInteraction.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: PreviousInteraction(self, **named)
   :canonical: pycraft.server.final.PreviousInteraction

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getPlayer(self) -> :py:class:`OfflinePlayer`
      :async:


   .. py:method:: getTimestamp(self) -> :py:class:`long`
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace

