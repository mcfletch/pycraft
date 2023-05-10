.. currentmodule:: pycraft.server.final

BanEntry
========

Inheritance
------------
* pycraft.server.final.BanEntry
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.BanEntry <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/BanEntry.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: BanEntry(self, **named)
   :canonical: pycraft.server.final.BanEntry

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getCreated(self) -> :py:class:`Date`
      :async:


   .. py:method:: getExpiration(self) -> :py:class:`Date`
      :async:


   .. py:method:: getReason(self) -> str
      :async:


   .. py:method:: getSource(self) -> str
      :async:


   .. py:method:: getTarget(self) -> str
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: save(self) -> None
      :async:


   .. py:method:: setCreated(self, _0:Date) -> None
      :async:


   .. py:method:: setExpiration(self, _0:Date) -> None
      :async:


   .. py:method:: setReason(self, _0:String) -> None
      :async:


   .. py:method:: setSource(self, _0:String) -> None
      :async:

