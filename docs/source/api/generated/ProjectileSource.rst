.. currentmodule:: pycraft.server.final

ProjectileSource
================

Inheritance
------------
* pycraft.server.final.ProjectileSource
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.projectiles.ProjectileSource <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/projectiles/ProjectileSource.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: ProjectileSource(self, **named)
   :canonical: pycraft.server.final.ProjectileSource

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: launchProjectile

       .. py:method:: launchProjectile(self, _0:Class) -> :py:class:`Projectile`
          :async:
          :noindex:

       .. py:method:: launchProjectile(self, _0:Class, _1:Vector) -> :py:class:`Projectile`
          :async:
          :noindex:

       .. py:method:: launchProjectile(self, _0:Class, _1:Vector, _2:Consumer) -> :py:class:`Projectile`
          :async:
          :noindex:

