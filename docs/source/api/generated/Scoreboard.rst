.. currentmodule:: pycraft.server.final

Scoreboard
==========

Inheritance
------------
* pycraft.server.final.Scoreboard
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.scoreboard.Scoreboard <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/scoreboard/Scoreboard.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Scoreboard(self, **named)
   :canonical: pycraft.server.final.Scoreboard

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: clearSlot(self, _0:DisplaySlot) -> None
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getEntityTeam(self, _0:Entity) -> :py:class:`Team`
      :async:


   .. py:method:: getEntries(self) -> typing.List[str]
      :async:


   .. py:method:: getEntryTeam(self, _0:String) -> :py:class:`Team`
      :async:


   .. py:method:: getObjective

       .. py:method:: getObjective(self, _0:String) -> :py:class:`Objective`
          :async:
          :noindex:

       .. py:method:: getObjective(self, _0:DisplaySlot) -> :py:class:`Objective`
          :async:
          :noindex:


   .. py:method:: getObjectives(self) -> typing.List[:py:class:`Objective`]
      :async:


   .. py:method:: getObjectivesByCriteria

       .. py:method:: getObjectivesByCriteria(self, _0:Criteria) -> typing.List[:py:class:`Objective`]
          :async:
          :noindex:

       .. py:method:: getObjectivesByCriteria(self, _0:String) -> typing.List[:py:class:`Objective`]
          :async:
          :noindex:


   .. py:method:: getPlayerTeam(self, _0:OfflinePlayer) -> :py:class:`Team`
      :async:


   .. py:method:: getPlayers(self) -> typing.List[:py:class:`OfflinePlayer`]
      :async:


   .. py:method:: getScores

       .. py:method:: getScores(self, _0:OfflinePlayer) -> typing.List[:py:class:`Score`]
          :async:
          :noindex:

       .. py:method:: getScores(self, _0:String) -> typing.List[:py:class:`Score`]
          :async:
          :noindex:


   .. py:method:: getScoresFor(self, _0:Entity) -> typing.List[:py:class:`Score`]
      :async:


   .. py:method:: getTeam(self, _0:String) -> :py:class:`Team`
      :async:


   .. py:method:: getTeams(self) -> typing.List[:py:class:`Team`]
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: registerNewObjective

       .. py:method:: registerNewObjective(self, _0:String, _1:String) -> :py:class:`Objective`
          :async:
          :noindex:

       .. py:method:: registerNewObjective(self, _0:String, _1:Criteria, _2:Component) -> :py:class:`Objective`
          :async:
          :noindex:

       .. py:method:: registerNewObjective(self, _0:String, _1:String, _2:Component) -> :py:class:`Objective`
          :async:
          :noindex:

       .. py:method:: registerNewObjective(self, _0:String, _1:Criteria, _2:String) -> :py:class:`Objective`
          :async:
          :noindex:

       .. py:method:: registerNewObjective(self, _0:String, _1:String, _2:String) -> :py:class:`Objective`
          :async:
          :noindex:

       .. py:method:: registerNewObjective(self, _0:String, _1:Criteria, _2:Component, _3:RenderType) -> :py:class:`Objective`
          :async:
          :noindex:

       .. py:method:: registerNewObjective(self, _0:String, _1:String, _2:Component, _3:RenderType) -> :py:class:`Objective`
          :async:
          :noindex:

       .. py:method:: registerNewObjective(self, _0:String, _1:Criteria, _2:String, _3:RenderType) -> :py:class:`Objective`
          :async:
          :noindex:

       .. py:method:: registerNewObjective(self, _0:String, _1:String, _2:String, _3:RenderType) -> :py:class:`Objective`
          :async:
          :noindex:


   .. py:method:: registerNewTeam(self, _0:String) -> :py:class:`Team`
      :async:


   .. py:method:: resetScores

       .. py:method:: resetScores(self, _0:String) -> None
          :async:
          :noindex:

       .. py:method:: resetScores(self, _0:OfflinePlayer) -> None
          :async:
          :noindex:


   .. py:method:: resetScoresFor(self, _0:Entity) -> None
      :async:

