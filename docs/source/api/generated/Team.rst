.. currentmodule:: pycraft.server.final

Team
====

Inheritance
------------
* pycraft.server.final.Team
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.scoreboard.Team <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/scoreboard/Team.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Team(self, **named)
   :canonical: pycraft.server.final.Team

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: addEntities

       .. py:method:: addEntities(self, _0:Entity[]) -> None
          :async:
          :noindex:

       .. py:method:: addEntities(self, _0:Collection) -> None
          :async:
          :noindex:


   .. py:method:: addEntity(self, _0:Entity) -> None
      :async:


   .. py:method:: addEntries

       .. py:method:: addEntries(self, _0:Collection) -> None
          :async:
          :noindex:

       .. py:method:: addEntries(self, _0:String[]) -> None
          :async:
          :noindex:


   .. py:method:: addEntry(self, _0:String) -> None
      :async:


   .. py:method:: addPlayer(self, _0:OfflinePlayer) -> None
      :async:


   .. py:method:: allowFriendlyFire(self) -> bool
      :async:


   .. py:method:: canSeeFriendlyInvisibles(self) -> bool
      :async:


   .. py:method:: color

       .. py:method:: color(self) -> :py:class:`TextColor`
          :async:
          :noindex:

       .. py:method:: color(self, _0:NamedTextColor) -> None
          :async:
          :noindex:


   .. py:method:: displayName

       .. py:method:: displayName(self) -> :py:class:`Component`
          :async:
          :noindex:

       .. py:method:: displayName(self, _0:Component) -> None
          :async:
          :noindex:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getColor(self) -> :py:class:`ChatColor`
      :async:


   .. py:method:: getDisplayName(self) -> str
      :async:


   .. py:method:: getEntries(self) -> typing.List[str]
      :async:


   .. py:method:: getName(self) -> str
      :async:


   .. py:method:: getNameTagVisibility(self) -> :py:class:`NameTagVisibility`
      :async:


   .. py:method:: getOption(self, _0:Option) -> :py:class:`OptionStatus`
      :async:


   .. py:method:: getPlayers(self) -> typing.List[:py:class:`OfflinePlayer`]
      :async:


   .. py:method:: getPrefix(self) -> str
      :async:


   .. py:method:: getScoreboard(self) -> :py:class:`Scoreboard`
      :async:


   .. py:method:: getSize(self) -> int
      :async:


   .. py:method:: getSuffix(self) -> str
      :async:


   .. py:method:: hasColor(self) -> bool
      :async:


   .. py:method:: hasEntity(self, _0:Entity) -> bool
      :async:


   .. py:method:: hasEntry(self, _0:String) -> bool
      :async:


   .. py:method:: hasPlayer(self, _0:OfflinePlayer) -> bool
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: prefix

       .. py:method:: prefix(self) -> :py:class:`Component`
          :async:
          :noindex:

       .. py:method:: prefix(self, _0:Component) -> None
          :async:
          :noindex:


   .. py:method:: removeEntities

       .. py:method:: removeEntities(self, _0:Entity[]) -> bool
          :async:
          :noindex:

       .. py:method:: removeEntities(self, _0:Collection) -> bool
          :async:
          :noindex:


   .. py:method:: removeEntity(self, _0:Entity) -> bool
      :async:


   .. py:method:: removeEntries

       .. py:method:: removeEntries(self, _0:Collection) -> bool
          :async:
          :noindex:

       .. py:method:: removeEntries(self, _0:String[]) -> bool
          :async:
          :noindex:


   .. py:method:: removeEntry(self, _0:String) -> bool
      :async:


   .. py:method:: removePlayer(self, _0:OfflinePlayer) -> bool
      :async:


   .. py:method:: setAllowFriendlyFire(self, _0:boolean) -> None
      :async:


   .. py:method:: setCanSeeFriendlyInvisibles(self, _0:boolean) -> None
      :async:


   .. py:method:: setColor(self, _0:ChatColor) -> None
      :async:


   .. py:method:: setDisplayName(self, _0:String) -> None
      :async:


   .. py:method:: setNameTagVisibility(self, _0:NameTagVisibility) -> None
      :async:


   .. py:method:: setOption(self, _0:Option, _1:OptionStatus) -> None
      :async:


   .. py:method:: setPrefix(self, _0:String) -> None
      :async:


   .. py:method:: setSuffix(self, _0:String) -> None
      :async:


   .. py:method:: suffix

       .. py:method:: suffix(self) -> :py:class:`Component`
          :async:
          :noindex:

       .. py:method:: suffix(self, _0:Component) -> None
          :async:
          :noindex:


   .. py:method:: unregister(self) -> None
      :async:

