.. currentmodule:: pycraft.server.final

PermissionRemovedExecutor
=========================

Inheritance
------------
* pycraft.server.final.PermissionRemovedExecutor
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.permissions.PermissionRemovedExecutor <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/permissions/PermissionRemovedExecutor.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: PermissionRemovedExecutor(self, **named)
   :canonical: pycraft.server.final.PermissionRemovedExecutor

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: attachmentRemoved(self, _0:PermissionAttachment) -> None
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace

