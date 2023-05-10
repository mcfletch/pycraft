.. currentmodule:: pycraft.server.final

AdvancementProgress
===================

Inheritance
------------
* pycraft.server.final.AdvancementProgress
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.advancement.AdvancementProgress <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/advancement/AdvancementProgress.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: AdvancementProgress(self, **named)
   :canonical: pycraft.server.final.AdvancementProgress

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: awardCriteria(self, _0:String) -> bool
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getAdvancement(self) -> :py:class:`Advancement`
      :async:


   .. py:method:: getAwardedCriteria(self) -> typing.List[str]
      :async:


   .. py:method:: getDateAwarded(self, _0:String) -> :py:class:`Date`
      :async:


   .. py:method:: getRemainingCriteria(self) -> typing.List[str]
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isDone(self) -> bool
      :async:


   .. py:method:: revokeCriteria(self, _0:String) -> bool
      :async:

