.. currentmodule:: pycraft.server.final

OfflinePlayer
=============

Inheritance
------------
* pycraft.server.final.OfflinePlayer
* :py:class:`pycraft.server.world.OfflinePlayer`
* :py:class:`pycraft.server.world.Player`
* :py:class:`pycraft.server.world.Entity`
* :py:class:`pycraft.server.final.ServerOperator`
* :py:class:`pycraft.server.final.AnimalTamer`
* :py:class:`pycraft.server.final.ConfigurationSerializable`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.OfflinePlayer <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/OfflinePlayer.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: OfflinePlayer(self, **named)
   :canonical: pycraft.server.final.OfflinePlayer

   A particular player (potentially not currently logged in) on the server

   .. py:property:: back

   .. py:property:: backward

   .. py:property:: direction
      Retrieve the direction reported when this record was retrieved (not necessarily the *current* direction)

   .. py:property:: forward

   .. py:property:: forward_and_cross

   .. py:property:: id
      Get our local unique key for referencing (uuid)

   .. py:property:: left

   .. py:property:: position
      Retrieve the location reported when this record was retrieved (not necessarily the *current* location)

   .. py:property:: right

   .. py:property:: tile_position

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: banPlayer

       .. py:method:: banPlayer(self, _0:String) -> :py:class:`BanEntry`
          :async:
          :noindex:

       .. py:method:: banPlayer(self, _0:String, _1:String) -> :py:class:`BanEntry`
          :async:
          :noindex:

       .. py:method:: banPlayer(self, _0:String, _1:Date) -> :py:class:`BanEntry`
          :async:
          :noindex:

       .. py:method:: banPlayer(self, _0:String, _1:Date, _2:String) -> :py:class:`BanEntry`
          :async:
          :noindex:

       .. py:method:: banPlayer(self, _0:String, _1:Date, _2:String, _3:boolean) -> :py:class:`BanEntry`
          :async:
          :noindex:


   .. py:method:: decrementStatistic

       .. py:method:: decrementStatistic(self, _0:Statistic) -> None
          :async:
          :noindex:

       .. py:method:: decrementStatistic(self, _0:Statistic, _1:EntityType) -> None
          :async:
          :noindex:

       .. py:method:: decrementStatistic(self, _0:Statistic, _1:int) -> None
          :async:
          :noindex:

       .. py:method:: decrementStatistic(self, _0:Statistic, _1:Material) -> None
          :async:
          :noindex:

       .. py:method:: decrementStatistic(self, _0:Statistic, _1:Material, _2:int) -> None
          :async:
          :noindex:

       .. py:method:: decrementStatistic(self, _0:Statistic, _1:EntityType, _2:int) -> None
          :async:
          :noindex:


   .. py:method:: from_server(named)
      

      Convert server-side structure to local object


   .. py:method:: getBedSpawnLocation(self) -> :py:class:`Location`
      :async:


   .. py:method:: getFirstPlayed(self) -> :py:class:`long`
      :async:


   .. py:method:: getLastDeathLocation(self) -> :py:class:`Location`
      :async:


   .. py:method:: getLastLogin(self) -> :py:class:`long`
      :async:


   .. py:method:: getLastPlayed(self) -> :py:class:`long`
      :async:


   .. py:method:: getLastSeen(self) -> :py:class:`long`
      :async:


   .. py:method:: getName(self) -> str
      :async:


   .. py:method:: getPlayer(self) -> :py:class:`Player`
      :async:


   .. py:method:: getPlayerProfile(self) -> :py:class:`PlayerProfile`
      :async:


   .. py:method:: getStatistic

       .. py:method:: getStatistic(self, _0:Statistic) -> int
          :async:
          :noindex:

       .. py:method:: getStatistic(self, _0:Statistic, _1:Material) -> int
          :async:
          :noindex:

       .. py:method:: getStatistic(self, _0:Statistic, _1:EntityType) -> int
          :async:
          :noindex:


   .. py:method:: getUniqueId(self) -> uuid.UUID
      :async:


   .. py:method:: get_key(self)
      

      Return our unique key for lookup on the server (uuid)


   .. py:method:: hasPlayedBefore(self) -> bool
      :async:


   .. py:method:: incrementStatistic

       .. py:method:: incrementStatistic(self, _0:Statistic) -> None
          :async:
          :noindex:

       .. py:method:: incrementStatistic(self, _0:Statistic, _1:Material) -> None
          :async:
          :noindex:

       .. py:method:: incrementStatistic(self, _0:Statistic, _1:EntityType) -> None
          :async:
          :noindex:

       .. py:method:: incrementStatistic(self, _0:Statistic, _1:int) -> None
          :async:
          :noindex:

       .. py:method:: incrementStatistic(self, _0:Statistic, _1:Material, _2:int) -> None
          :async:
          :noindex:

       .. py:method:: incrementStatistic(self, _0:Statistic, _1:EntityType, _2:int) -> None
          :async:
          :noindex:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isBanned(self) -> bool
      :async:


   .. py:method:: isOnline(self) -> bool
      :async:


   .. py:method:: isOp(self) -> bool
      :async:


   .. py:method:: isWhitelisted(self) -> bool
      :async:


   .. py:method:: serialize(self) -> :py:class:`Map`
      :async:


   .. py:method:: setOp(self, _0:boolean) -> None
      :async:


   .. py:method:: setStatistic

       .. py:method:: setStatistic(self, _0:Statistic, _1:int) -> None
          :async:
          :noindex:

       .. py:method:: setStatistic(self, _0:Statistic, _1:EntityType, _2:int) -> None
          :async:
          :noindex:

       .. py:method:: setStatistic(self, _0:Statistic, _1:Material, _2:int) -> None
          :async:
          :noindex:


   .. py:method:: setWhitelisted(self, _0:boolean) -> None
      :async:


   .. py:method:: set_location(self, location)
      :async:

      Set the user's position to the given location or vector


   .. py:method:: tilt(self)
      

      Get the rise/run 1 value float telling how far the entity's gaze rises/falls per unit of run

