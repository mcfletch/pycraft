.. currentmodule:: pycraft.server.final

BukkitTask
==========

Inheritance
------------
* pycraft.server.final.BukkitTask
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.scheduler.BukkitTask <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/scheduler/BukkitTask.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: BukkitTask(self, **named)
   :canonical: pycraft.server.final.BukkitTask

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: cancel(self) -> None
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getOwner(self) -> :py:class:`Plugin`
      :async:


   .. py:method:: getTaskId(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isCancelled(self) -> bool
      :async:


   .. py:method:: isSync(self) -> bool
      :async:

