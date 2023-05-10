.. currentmodule:: pycraft.server.final

HelpMap
=======

Inheritance
------------
* pycraft.server.final.HelpMap
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.help.HelpMap <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/help/HelpMap.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: HelpMap(self, **named)
   :canonical: pycraft.server.final.HelpMap

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: addTopic(self, _0:HelpTopic) -> None
      :async:


   .. py:method:: clear(self) -> None
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getHelpTopic(self, _0:String) -> :py:class:`HelpTopic`
      :async:


   .. py:method:: getHelpTopics(self) -> typing.List[:py:class:`HelpTopic`]
      :async:


   .. py:method:: getIgnoredPlugins(self) -> typing.List[str]
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: registerHelpTopicFactory(self, _0:Class, _1:HelpTopicFactory) -> None
      :async:

