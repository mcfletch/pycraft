.. currentmodule:: pycraft.server.final

Objective
=========

Inheritance
------------
* pycraft.server.final.Objective
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.scoreboard.Objective <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/scoreboard/Objective.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Objective(self, **named)
   :canonical: pycraft.server.final.Objective

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: displayName

       .. py:method:: displayName(self) -> :py:class:`Component`
          :async:
          :noindex:

       .. py:method:: displayName(self, _0:Component) -> None
          :async:
          :noindex:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getCriteria(self) -> str
      :async:


   .. py:method:: getDisplayName(self) -> str
      :async:


   .. py:method:: getDisplaySlot(self) -> :py:class:`DisplaySlot`
      :async:


   .. py:method:: getName(self) -> str
      :async:


   .. py:method:: getRenderType(self) -> :py:class:`RenderType`
      :async:


   .. py:method:: getScore

       .. py:method:: getScore(self, _0:OfflinePlayer) -> :py:class:`Score`
          :async:
          :noindex:

       .. py:method:: getScore(self, _0:String) -> :py:class:`Score`
          :async:
          :noindex:


   .. py:method:: getScoreFor(self, _0:Entity) -> :py:class:`Score`
      :async:


   .. py:method:: getScoreboard(self) -> :py:class:`Scoreboard`
      :async:


   .. py:method:: getTrackedCriteria(self) -> :py:class:`Criteria`
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isModifiable(self) -> bool
      :async:


   .. py:method:: setDisplayName(self, _0:String) -> None
      :async:


   .. py:method:: setDisplaySlot(self, _0:DisplaySlot) -> None
      :async:


   .. py:method:: setRenderType(self, _0:RenderType) -> None
      :async:


   .. py:method:: unregister(self) -> None
      :async:

