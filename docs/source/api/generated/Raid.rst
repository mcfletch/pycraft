.. currentmodule:: pycraft.server.final

Raid
====

Inheritance
------------
* pycraft.server.final.Raid
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.Raid <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Raid.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Raid(self, **named)
   :canonical: pycraft.server.final.Raid

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getActiveTicks(self) -> :py:class:`long`
      :async:


   .. py:method:: getBadOmenLevel(self) -> int
      :async:


   .. py:method:: getHeroes(self) -> typing.List[uuid.UUID]
      :async:


   .. py:method:: getLocation(self) -> :py:class:`Location`
      :async:


   .. py:method:: getRaiders(self) -> typing.List[:py:class:`Raider`]
      :async:


   .. py:method:: getSpawnedGroups(self) -> int
      :async:


   .. py:method:: getStatus(self) -> :py:class:`RaidStatus`
      :async:


   .. py:method:: getTotalGroups(self) -> int
      :async:


   .. py:method:: getTotalHealth(self) -> float
      :async:


   .. py:method:: getTotalWaves(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isStarted(self) -> bool
      :async:


   .. py:method:: setBadOmenLevel(self, _0:int) -> None
      :async:

