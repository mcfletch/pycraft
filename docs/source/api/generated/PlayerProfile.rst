.. currentmodule:: pycraft.server.final

PlayerProfile
=============

Inheritance
------------
* pycraft.server.final.PlayerProfile
* :py:class:`pycraft.server.final.ConfigurationSerializable`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.profile.PlayerProfile <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/profile/PlayerProfile.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: PlayerProfile(self, **named)
   :canonical: pycraft.server.final.PlayerProfile

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getName(self) -> str
      :async:


   .. py:method:: getTextures(self) -> :py:class:`PlayerTextures`
      :async:


   .. py:method:: getUniqueId(self) -> uuid.UUID
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isComplete(self) -> bool
      :async:


   .. py:method:: serialize(self) -> :py:class:`Map`
      :async:


   .. py:method:: setTextures(self, _0:PlayerTextures) -> None
      :async:


   .. py:method:: update(self) -> :py:class:`CompletableFuture`
      :async:

