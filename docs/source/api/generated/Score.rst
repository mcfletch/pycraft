.. currentmodule:: pycraft.server.final

Score
=====

Inheritance
------------
* pycraft.server.final.Score
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.scoreboard.Score <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/scoreboard/Score.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Score(self, **named)
   :canonical: pycraft.server.final.Score

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getEntry(self) -> str
      :async:


   .. py:method:: getObjective(self) -> :py:class:`Objective`
      :async:


   .. py:method:: getPlayer(self) -> :py:class:`OfflinePlayer`
      :async:


   .. py:method:: getScore(self) -> int
      :async:


   .. py:method:: getScoreboard(self) -> :py:class:`Scoreboard`
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isScoreSet(self) -> bool
      :async:


   .. py:method:: resetScore(self) -> None
      :async:


   .. py:method:: setScore(self, _0:int) -> None
      :async:

