.. currentmodule:: pycraft.server.final

Location
========

Inheritance
------------
* pycraft.server.final.Location
* :py:class:`pycraft.server.world.Location`
* :py:class:`pycraft.server.final.ConfigurationSerializable`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.Location <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Location.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Location(self, record)
   :canonical: pycraft.server.final.Location

   Object reference on the server which we are proxying

   .. py:property:: direction
      Get the direction faced by this location

   .. py:property:: pitch

   .. py:property:: yaw

   .. py:method:: __add__(self, other)
      

   .. py:method:: __floor__(self)
      

   .. py:method:: __getitem__(self, slice)
      

   .. py:method:: __hash__(self)
      

      Return hash(self).


   .. py:method:: __init__(self, record)
      

      Set each named key/value as an attribute on object


   .. py:method:: __len__(self)
      

   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: __sub__(self, other)
      

   .. py:method:: add

       .. py:method:: add(self, _0:Location) -> :py:class:`Location`
          :async:
          :noindex:

       .. py:method:: add(self, _0:Vector) -> :py:class:`Location`
          :async:
          :noindex:

       .. py:method:: add(self, _0:double, _1:double, _2:double) -> :py:class:`Location`
          :async:
          :noindex:

       .. py:method:: add(self, _0:Location, _1:double, _2:double, _3:double) -> :py:class:`Location`
          :async:
          :noindex:


   .. py:method:: blockX(self) -> int
      :async:


   .. py:method:: blockY(self) -> int
      :async:


   .. py:method:: blockZ(self) -> int
      :async:


   .. py:method:: block_location(self)
      

      Get the block location (block address) for this location


   .. py:method:: checkFinite(self) -> None
      :async:


   .. py:method:: createExplosion

       .. py:method:: createExplosion(self, _0:float) -> bool
          :async:
          :noindex:

       .. py:method:: createExplosion(self, _0:Entity, _1:float) -> bool
          :async:
          :noindex:

       .. py:method:: createExplosion(self, _0:float, _1:boolean) -> bool
          :async:
          :noindex:

       .. py:method:: createExplosion(self, _0:float, _1:boolean, _2:boolean) -> bool
          :async:
          :noindex:

       .. py:method:: createExplosion(self, _0:Entity, _1:float, _2:boolean) -> bool
          :async:
          :noindex:

       .. py:method:: createExplosion(self, _0:Entity, _1:float, _2:boolean, _3:boolean) -> bool
          :async:
          :noindex:


   .. py:method:: deserialize(cls, _0:Map) -> :py:class:`Location`
      :async:
      :classmethod:


   .. py:method:: distance(self, _0:Location) -> float
      :async:


   .. py:method:: distanceSquared(self, _0:Location) -> float
      :async:


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: from_server(record)
      

      Convert server-side structure to local object


   .. py:method:: getBlock(self) -> :py:class:`Block`
      :async:


   .. py:method:: getBlockX(self) -> int
      :async:


   .. py:method:: getBlockY(self) -> int
      :async:


   .. py:method:: getBlockZ(self) -> int
      :async:


   .. py:method:: getChunk(self) -> :py:class:`Chunk`
      :async:


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getDirection(self) -> :py:class:`Vector`
      :async:


   .. py:method:: getNearbyEntities(self, _0:double, _1:double, _2:double) -> typing.List[:py:class:`Entity`]
      :async:


   .. py:method:: getNearbyEntitiesByType

       .. py:method:: getNearbyEntitiesByType(self, _0:Class, _1:double) -> typing.List[:py:class:`T`]
          :async:
          :noindex:

       .. py:method:: getNearbyEntitiesByType(self, _0:Class, _1:double, _2:Predicate) -> typing.List[:py:class:`T`]
          :async:
          :noindex:

       .. py:method:: getNearbyEntitiesByType(self, _0:Class, _1:double, _2:double) -> typing.List[:py:class:`T`]
          :async:
          :noindex:

       .. py:method:: getNearbyEntitiesByType(self, _0:Class, _1:double, _2:double, _3:double) -> typing.List[:py:class:`T`]
          :async:
          :noindex:

       .. py:method:: getNearbyEntitiesByType(self, _0:Class, _1:double, _2:double, _3:Predicate) -> typing.List[:py:class:`T`]
          :async:
          :noindex:

       .. py:method:: getNearbyEntitiesByType(self, _0:Class, _1:double, _2:double, _3:double, _4:Predicate) -> typing.List[:py:class:`T`]
          :async:
          :noindex:


   .. py:method:: getNearbyLivingEntities

       .. py:method:: getNearbyLivingEntities(self, _0:double) -> typing.List[:py:class:`LivingEntity`]
          :async:
          :noindex:

       .. py:method:: getNearbyLivingEntities(self, _0:double, _1:Predicate) -> typing.List[:py:class:`LivingEntity`]
          :async:
          :noindex:

       .. py:method:: getNearbyLivingEntities(self, _0:double, _1:double) -> typing.List[:py:class:`LivingEntity`]
          :async:
          :noindex:

       .. py:method:: getNearbyLivingEntities(self, _0:double, _1:double, _2:double) -> typing.List[:py:class:`LivingEntity`]
          :async:
          :noindex:

       .. py:method:: getNearbyLivingEntities(self, _0:double, _1:double, _2:Predicate) -> typing.List[:py:class:`LivingEntity`]
          :async:
          :noindex:

       .. py:method:: getNearbyLivingEntities(self, _0:double, _1:double, _2:double, _3:Predicate) -> typing.List[:py:class:`LivingEntity`]
          :async:
          :noindex:


   .. py:method:: getNearbyPlayers

       .. py:method:: getNearbyPlayers(self, _0:double) -> typing.List[:py:class:`Player`]
          :async:
          :noindex:

       .. py:method:: getNearbyPlayers(self, _0:double, _1:double) -> typing.List[:py:class:`Player`]
          :async:
          :noindex:

       .. py:method:: getNearbyPlayers(self, _0:double, _1:Predicate) -> typing.List[:py:class:`Player`]
          :async:
          :noindex:

       .. py:method:: getNearbyPlayers(self, _0:double, _1:double, _2:Predicate) -> typing.List[:py:class:`Player`]
          :async:
          :noindex:

       .. py:method:: getNearbyPlayers(self, _0:double, _1:double, _2:double) -> typing.List[:py:class:`Player`]
          :async:
          :noindex:

       .. py:method:: getNearbyPlayers(self, _0:double, _1:double, _2:double, _3:Predicate) -> typing.List[:py:class:`Player`]
          :async:
          :noindex:


   .. py:method:: getPitch(self) -> float
      :async:


   .. py:method:: getWorld(self) -> :py:class:`World`
      :async:


   .. py:method:: getX(self) -> float
      :async:


   .. py:method:: getY(self) -> float
      :async:


   .. py:method:: getYaw(self) -> float
      :async:


   .. py:method:: getZ(self) -> float
      :async:


   .. py:method:: get_key(self)
      

   .. py:method:: get_world(self)
      

   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isBlock(self) -> bool
      :async:


   .. py:method:: isChunkLoaded(self) -> bool
      :async:


   .. py:method:: isFine(self) -> bool
      :async:


   .. py:method:: isGenerated(self) -> bool
      :async:


   .. py:method:: isWorldLoaded(self) -> bool
      :async:


   .. py:method:: length(self) -> float
      :async:


   .. py:method:: lengthSquared(self) -> float
      :async:


   .. py:method:: locToBlock(cls, _0:double) -> int
      :async:
      :classmethod:


   .. py:method:: multiply(self, _0:double) -> :py:class:`Location`
      :async:


   .. py:method:: normalizePitch(cls, _0:float) -> float
      :async:
      :classmethod:


   .. py:method:: normalizeYaw(cls, _0:float) -> float
      :async:
      :classmethod:


   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: offset

       .. py:method:: offset(self, _0:int, _1:int, _2:int) -> :py:class:`FinePosition`
          :async:
          :noindex:

       .. py:method:: offset(self, _0:int, _1:int, _2:int) -> :py:class:`Position`
          :async:
          :noindex:

       .. py:method:: offset(self, _0:double, _1:double, _2:double) -> :py:class:`FinePosition`
          :async:
          :noindex:


   .. py:method:: serialize(self) -> :py:class:`Map`
      :async:


   .. py:method:: set(self, _0:double, _1:double, _2:double) -> :py:class:`Location`
      :async:


   .. py:method:: setDirection(self, _0:Vector) -> :py:class:`Location`
      :async:


   .. py:method:: setPitch(self, _0:float) -> None
      :async:


   .. py:method:: setWorld(self, _0:World) -> None
      :async:


   .. py:method:: setX(self, _0:double) -> None
      :async:


   .. py:method:: setY(self, _0:double) -> None
      :async:


   .. py:method:: setYaw(self, _0:float) -> None
      :async:


   .. py:method:: setZ(self, _0:double) -> None
      :async:


   .. py:method:: subtract

       .. py:method:: subtract(self, _0:Location) -> :py:class:`Location`
          :async:
          :noindex:

       .. py:method:: subtract(self, _0:Vector) -> :py:class:`Location`
          :async:
          :noindex:

       .. py:method:: subtract(self, _0:double, _1:double, _2:double) -> :py:class:`Location`
          :async:
          :noindex:

       .. py:method:: subtract(self, _0:Location, _1:double, _2:double, _3:double) -> :py:class:`Location`
          :async:
          :noindex:


   .. py:method:: tilt(self)
      

      Get the rise/run for the angle of the user's gaze

      This is basically "if you move forward 1 block, you should rise
      N blocks (or fall)


   .. py:method:: toBlock(self) -> :py:class:`BlockPosition`
      :async:


   .. py:method:: toBlockKey(self) -> :py:class:`long`
      :async:


   .. py:method:: toBlockLocation(self) -> :py:class:`Location`
      :async:


   .. py:method:: toCenter(self) -> :py:class:`FinePosition`
      :async:


   .. py:method:: toCenterLocation(self) -> :py:class:`Location`
      :async:


   .. py:method:: toHighestLocation

       .. py:method:: toHighestLocation(self) -> :py:class:`Location`
          :async:
          :noindex:

       .. py:method:: toHighestLocation(self, _0:HeightmapType) -> :py:class:`Location`
          :async:
          :noindex:

       .. py:method:: toHighestLocation(self, _0:HeightMap) -> :py:class:`Location`
          :async:
          :noindex:


   .. py:method:: toLocation(self, _0:World) -> :py:class:`Location`
      :async:


   .. py:method:: toString(self) -> str
      :async:


   .. py:method:: toVector(self) -> :py:class:`Vector`
      :async:


   .. py:method:: x(self) -> float
      :async:


   .. py:method:: y(self) -> float
      :async:


   .. py:method:: z(self) -> float
      :async:


   .. py:method:: zero(self) -> :py:class:`Location`
      :async:

