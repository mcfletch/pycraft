.. currentmodule:: pycraft.server.final

BossBar
=======

Inheritance
------------
* pycraft.server.final.BossBar
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.boss.BossBar <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/boss/BossBar.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: BossBar(self, **named)
   :canonical: pycraft.server.final.BossBar

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: addFlag(self, _0:BarFlag) -> None
      :async:


   .. py:method:: addPlayer(self, _0:Player) -> None
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getColor(self) -> :py:class:`BarColor`
      :async:


   .. py:method:: getPlayers(self) -> typing.List[:py:class:`Player`]
      :async:


   .. py:method:: getProgress(self) -> float
      :async:


   .. py:method:: getStyle(self) -> :py:class:`BarStyle`
      :async:


   .. py:method:: getTitle(self) -> str
      :async:


   .. py:method:: hasFlag(self, _0:BarFlag) -> bool
      :async:


   .. py:method:: hide(self) -> None
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isVisible(self) -> bool
      :async:


   .. py:method:: removeAll(self) -> None
      :async:


   .. py:method:: removeFlag(self, _0:BarFlag) -> None
      :async:


   .. py:method:: removePlayer(self, _0:Player) -> None
      :async:


   .. py:method:: setColor(self, _0:BarColor) -> None
      :async:


   .. py:method:: setProgress(self, _0:double) -> None
      :async:


   .. py:method:: setStyle(self, _0:BarStyle) -> None
      :async:


   .. py:method:: setTitle(self, _0:String) -> None
      :async:


   .. py:method:: setVisible(self, _0:boolean) -> None
      :async:


   .. py:method:: show(self) -> None
      :async:

