.. currentmodule:: pycraft.server.final

PlayerTextures
==============

Inheritance
------------
* pycraft.server.final.PlayerTextures
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.profile.PlayerTextures <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/profile/PlayerTextures.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: PlayerTextures(self, **named)
   :canonical: pycraft.server.final.PlayerTextures

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: clear(self) -> None
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getCape(self) -> :py:class:`URL`
      :async:


   .. py:method:: getSkin(self) -> :py:class:`URL`
      :async:


   .. py:method:: getSkinModel(self) -> :py:class:`SkinModel`
      :async:


   .. py:method:: getTimestamp(self) -> :py:class:`long`
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isEmpty(self) -> bool
      :async:


   .. py:method:: isSigned(self) -> bool
      :async:


   .. py:method:: setCape(self, _0:URL) -> None
      :async:


   .. py:method:: setSkin

       .. py:method:: setSkin(self, _0:URL) -> None
          :async:
          :noindex:

       .. py:method:: setSkin(self, _0:URL, _1:SkinModel) -> None
          :async:
          :noindex:

