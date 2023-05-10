.. currentmodule:: pycraft.server.final

BukkitScheduler
===============

Inheritance
------------
* pycraft.server.final.BukkitScheduler
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.scheduler.BukkitScheduler <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/scheduler/BukkitScheduler.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: BukkitScheduler(self, **named)
   :canonical: pycraft.server.final.BukkitScheduler

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: callSyncMethod(self, _0:Plugin, _1:Callable) -> :py:class:`Future`
      :async:


   .. py:method:: cancelTask(self, _0:int) -> None
      :async:


   .. py:method:: cancelTasks(self, _0:Plugin) -> None
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getActiveWorkers(self) -> typing.List[:py:class:`BukkitWorker`]
      :async:


   .. py:method:: getMainThreadExecutor(self, _0:Plugin) -> :py:class:`Executor`
      :async:


   .. py:method:: getPendingTasks(self) -> typing.List[:py:class:`BukkitTask`]
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isCurrentlyRunning(self, _0:int) -> bool
      :async:


   .. py:method:: isQueued(self, _0:int) -> bool
      :async:


   .. py:method:: runTask

       .. py:method:: runTask(self, _0:Plugin, _1:Consumer) -> None
          :async:
          :noindex:

       .. py:method:: runTask(self, _0:Plugin, _1:Runnable) -> :py:class:`BukkitTask`
          :async:
          :noindex:

       .. py:method:: runTask(self, _0:Plugin, _1:BukkitRunnable) -> :py:class:`BukkitTask`
          :async:
          :noindex:


   .. py:method:: runTaskAsynchronously

       .. py:method:: runTaskAsynchronously(self, _0:Plugin, _1:BukkitRunnable) -> :py:class:`BukkitTask`
          :async:
          :noindex:

       .. py:method:: runTaskAsynchronously(self, _0:Plugin, _1:Consumer) -> None
          :async:
          :noindex:

       .. py:method:: runTaskAsynchronously(self, _0:Plugin, _1:Runnable) -> :py:class:`BukkitTask`
          :async:
          :noindex:


   .. py:method:: runTaskLater

       .. py:method:: runTaskLater(self, _0:Plugin, _1:Consumer, _2:long) -> None
          :async:
          :noindex:

       .. py:method:: runTaskLater(self, _0:Plugin, _1:Runnable, _2:long) -> :py:class:`BukkitTask`
          :async:
          :noindex:

       .. py:method:: runTaskLater(self, _0:Plugin, _1:BukkitRunnable, _2:long) -> :py:class:`BukkitTask`
          :async:
          :noindex:


   .. py:method:: runTaskLaterAsynchronously

       .. py:method:: runTaskLaterAsynchronously(self, _0:Plugin, _1:BukkitRunnable, _2:long) -> :py:class:`BukkitTask`
          :async:
          :noindex:

       .. py:method:: runTaskLaterAsynchronously(self, _0:Plugin, _1:Runnable, _2:long) -> :py:class:`BukkitTask`
          :async:
          :noindex:

       .. py:method:: runTaskLaterAsynchronously(self, _0:Plugin, _1:Consumer, _2:long) -> None
          :async:
          :noindex:


   .. py:method:: runTaskTimer

       .. py:method:: runTaskTimer(self, _0:Plugin, _1:Runnable, _2:long, _3:long) -> :py:class:`BukkitTask`
          :async:
          :noindex:

       .. py:method:: runTaskTimer(self, _0:Plugin, _1:Consumer, _2:long, _3:long) -> None
          :async:
          :noindex:

       .. py:method:: runTaskTimer(self, _0:Plugin, _1:BukkitRunnable, _2:long, _3:long) -> :py:class:`BukkitTask`
          :async:
          :noindex:


   .. py:method:: runTaskTimerAsynchronously

       .. py:method:: runTaskTimerAsynchronously(self, _0:Plugin, _1:Runnable, _2:long, _3:long) -> :py:class:`BukkitTask`
          :async:
          :noindex:

       .. py:method:: runTaskTimerAsynchronously(self, _0:Plugin, _1:BukkitRunnable, _2:long, _3:long) -> :py:class:`BukkitTask`
          :async:
          :noindex:

       .. py:method:: runTaskTimerAsynchronously(self, _0:Plugin, _1:Consumer, _2:long, _3:long) -> None
          :async:
          :noindex:


   .. py:method:: scheduleAsyncDelayedTask

       .. py:method:: scheduleAsyncDelayedTask(self, _0:Plugin, _1:Runnable) -> int
          :async:
          :noindex:

       .. py:method:: scheduleAsyncDelayedTask(self, _0:Plugin, _1:Runnable, _2:long) -> int
          :async:
          :noindex:


   .. py:method:: scheduleAsyncRepeatingTask(self, _0:Plugin, _1:Runnable, _2:long, _3:long) -> int
      :async:


   .. py:method:: scheduleSyncDelayedTask

       .. py:method:: scheduleSyncDelayedTask(self, _0:Plugin, _1:BukkitRunnable) -> int
          :async:
          :noindex:

       .. py:method:: scheduleSyncDelayedTask(self, _0:Plugin, _1:Runnable) -> int
          :async:
          :noindex:

       .. py:method:: scheduleSyncDelayedTask(self, _0:Plugin, _1:Runnable, _2:long) -> int
          :async:
          :noindex:

       .. py:method:: scheduleSyncDelayedTask(self, _0:Plugin, _1:BukkitRunnable, _2:long) -> int
          :async:
          :noindex:


   .. py:method:: scheduleSyncRepeatingTask

       .. py:method:: scheduleSyncRepeatingTask(self, _0:Plugin, _1:Runnable, _2:long, _3:long) -> int
          :async:
          :noindex:

       .. py:method:: scheduleSyncRepeatingTask(self, _0:Plugin, _1:BukkitRunnable, _2:long, _3:long) -> int
          :async:
          :noindex:

