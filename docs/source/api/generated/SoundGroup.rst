.. currentmodule:: pycraft.server.final

SoundGroup
==========

Inheritance
------------
* pycraft.server.final.SoundGroup
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.SoundGroup <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/SoundGroup.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: SoundGroup(self, **named)
   :canonical: pycraft.server.final.SoundGroup

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getBreakSound(self) -> :py:class:`Sound`
      :async:


   .. py:method:: getFallSound(self) -> :py:class:`Sound`
      :async:


   .. py:method:: getHitSound(self) -> :py:class:`Sound`
      :async:


   .. py:method:: getPitch(self) -> float
      :async:


   .. py:method:: getPlaceSound(self) -> :py:class:`Sound`
      :async:


   .. py:method:: getStepSound(self) -> :py:class:`Sound`
      :async:


   .. py:method:: getVolume(self) -> float
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace

