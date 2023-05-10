.. currentmodule:: pycraft.server.final

BukkitRunnable
==============

Inheritance
------------
* pycraft.server.final.BukkitRunnable
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.scheduler.BukkitRunnable <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/scheduler/BukkitRunnable.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: BukkitRunnable(self, **named)
   :canonical: pycraft.server.final.BukkitRunnable

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: cancel(self) -> None
      :async:


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getTaskId(self) -> int
      :async:


   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isCancelled(self) -> bool
      :async:


   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: run(self) -> None
      :async:


   .. py:method:: runTask(self, _0:Plugin) -> :py:class:`BukkitTask`
      :async:


   .. py:method:: runTaskAsynchronously(self, _0:Plugin) -> :py:class:`BukkitTask`
      :async:


   .. py:method:: runTaskLater(self, _0:Plugin, _1:long) -> :py:class:`BukkitTask`
      :async:


   .. py:method:: runTaskLaterAsynchronously(self, _0:Plugin, _1:long) -> :py:class:`BukkitTask`
      :async:


   .. py:method:: runTaskTimer(self, _0:Plugin, _1:long, _2:long) -> :py:class:`BukkitTask`
      :async:


   .. py:method:: runTaskTimerAsynchronously(self, _0:Plugin, _1:long, _2:long) -> :py:class:`BukkitTask`
      :async:


   .. py:method:: toString(self) -> str
      :async:

