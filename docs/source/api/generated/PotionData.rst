.. currentmodule:: pycraft.server.final

PotionData
==========

Inheritance
------------
* pycraft.server.final.PotionData
* :py:class:`pycraft.server.world.PotionData`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.potion.PotionData <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/potion/PotionData.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: PotionData(self, **named)
   :canonical: pycraft.server.final.PotionData

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getType(self) -> :py:class:`PotionType`
      :async:


   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isExtended(self) -> bool
      :async:


   .. py:method:: isUpgraded(self) -> bool
      :async:


   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: toString(self) -> str
      :async:

