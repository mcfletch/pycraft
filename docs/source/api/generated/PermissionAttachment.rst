.. currentmodule:: pycraft.server.final

PermissionAttachment
====================

Inheritance
------------
* pycraft.server.final.PermissionAttachment
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.permissions.PermissionAttachment <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/permissions/PermissionAttachment.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: PermissionAttachment(self, **named)
   :canonical: pycraft.server.final.PermissionAttachment

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


   .. py:method:: getPermissible(self) -> :py:class:`Permissible`
      :async:


   .. py:method:: getPermissions(self) -> :py:class:`Map`
      :async:


   .. py:method:: getPlugin(self) -> :py:class:`Plugin`
      :async:


   .. py:method:: getRemovalCallback(self) -> :py:class:`PermissionRemovedExecutor`
      :async:


   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: remove(self) -> bool
      :async:


   .. py:method:: setPermission

       .. py:method:: setPermission(self, _0:Permission, _1:boolean) -> None
          :async:
          :noindex:

       .. py:method:: setPermission(self, _0:String, _1:boolean) -> None
          :async:
          :noindex:


   .. py:method:: setRemovalCallback(self, _0:PermissionRemovedExecutor) -> None
      :async:


   .. py:method:: toString(self) -> str
      :async:


   .. py:method:: unsetPermission

       .. py:method:: unsetPermission(self, _0:Permission) -> None
          :async:
          :noindex:

       .. py:method:: unsetPermission(self, _0:String) -> None
          :async:
          :noindex:

