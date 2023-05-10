.. currentmodule:: pycraft.server.final

ScoreboardManager
=================

Inheritance
------------
* pycraft.server.final.ScoreboardManager
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.scoreboard.ScoreboardManager <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/scoreboard/ScoreboardManager.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: ScoreboardManager(self, **named)
   :canonical: pycraft.server.final.ScoreboardManager

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getMainScoreboard(self) -> :py:class:`Scoreboard`
      :async:


   .. py:method:: getNewScoreboard(self) -> :py:class:`Scoreboard`
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace

