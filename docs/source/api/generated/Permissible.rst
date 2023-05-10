.. currentmodule:: pycraft.server.final

Permissible
===========

Inheritance
------------
* pycraft.server.final.Permissible
* :py:class:`pycraft.server.final.ServerOperator`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.permissions.Permissible <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/permissions/Permissible.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Permissible(self, **named)
   :canonical: pycraft.server.final.Permissible

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: addAttachment

       .. py:method:: addAttachment(self, _0:Plugin) -> :py:class:`PermissionAttachment`
          :async:
          :noindex:

       .. py:method:: addAttachment(self, _0:Plugin, _1:int) -> :py:class:`PermissionAttachment`
          :async:
          :noindex:

       .. py:method:: addAttachment(self, _0:Plugin, _1:String, _2:boolean) -> :py:class:`PermissionAttachment`
          :async:
          :noindex:

       .. py:method:: addAttachment(self, _0:Plugin, _1:String, _2:boolean, _3:int) -> :py:class:`PermissionAttachment`
          :async:
          :noindex:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getEffectivePermissions(self) -> typing.List[:py:class:`PermissionAttachmentInfo`]
      :async:


   .. py:method:: hasPermission

       .. py:method:: hasPermission(self, _0:Permission) -> bool
          :async:
          :noindex:

       .. py:method:: hasPermission(self, _0:String) -> bool
          :async:
          :noindex:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isOp(self) -> bool
      :async:


   .. py:method:: isPermissionSet

       .. py:method:: isPermissionSet(self, _0:String) -> bool
          :async:
          :noindex:

       .. py:method:: isPermissionSet(self, _0:Permission) -> bool
          :async:
          :noindex:


   .. py:method:: permissionValue

       .. py:method:: permissionValue(self, _0:Permission) -> :py:class:`TriState`
          :async:
          :noindex:

       .. py:method:: permissionValue(self, _0:String) -> :py:class:`TriState`
          :async:
          :noindex:


   .. py:method:: recalculatePermissions(self) -> None
      :async:


   .. py:method:: removeAttachment(self, _0:PermissionAttachment) -> None
      :async:


   .. py:method:: setOp(self, _0:boolean) -> None
      :async:

