.. currentmodule:: pycraft.server.final

HelpTopicFactory
================

Inheritance
------------
* pycraft.server.final.HelpTopicFactory
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.help.HelpTopicFactory <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/help/HelpTopicFactory.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: HelpTopicFactory(self, **named)
   :canonical: pycraft.server.final.HelpTopicFactory

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: createTopic(self, _0:Command) -> :py:class:`HelpTopic`
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace

