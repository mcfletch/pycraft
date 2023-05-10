.. currentmodule:: pycraft.server.final

BanList
=======

Inheritance
------------
* pycraft.server.final.BanList
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.BanList <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/BanList.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: BanList(self, **named)
   :canonical: pycraft.server.final.BanList

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: addBan(self, _0:String, _1:String, _2:Date, _3:String) -> :py:class:`BanEntry`
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getBanEntries(self) -> typing.List[:py:class:`BanEntry`]
      :async:


   .. py:method:: getBanEntry(self, _0:String) -> :py:class:`BanEntry`
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isBanned(self, _0:String) -> bool
      :async:


   .. py:method:: pardon(self, _0:String) -> None
      :async:

