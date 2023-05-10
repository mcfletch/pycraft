.. currentmodule:: pycraft.server.final

DragonBattle
============

Inheritance
------------
* pycraft.server.final.DragonBattle
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.boss.DragonBattle <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/boss/DragonBattle.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: DragonBattle(self, **named)
   :canonical: pycraft.server.final.DragonBattle

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: generateEndPortal(self, _0:boolean) -> bool
      :async:


   .. py:method:: getBossBar(self) -> :py:class:`BossBar`
      :async:


   .. py:method:: getEndPortalLocation(self) -> :py:class:`Location`
      :async:


   .. py:method:: getEnderDragon(self) -> :py:class:`EnderDragon`
      :async:


   .. py:method:: getRespawnPhase(self) -> :py:class:`RespawnPhase`
      :async:


   .. py:method:: hasBeenPreviouslyKilled(self) -> bool
      :async:


   .. py:method:: initiateRespawn(self) -> None
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: resetCrystals(self) -> None
      :async:


   .. py:method:: setRespawnPhase(self, _0:RespawnPhase) -> bool
      :async:

