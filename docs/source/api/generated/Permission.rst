.. currentmodule:: pycraft.server.final

Permission
==========

Inheritance
------------
* pycraft.server.final.Permission
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.permissions.Permission <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/permissions/Permission.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Permission(self, **named)
   :canonical: pycraft.server.final.Permission

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: addParent

       .. py:method:: addParent(self, _0:String, _1:boolean) -> :py:class:`Permission`
          :async:
          :noindex:

       .. py:method:: addParent(self, _0:Permission, _1:boolean) -> None
          :async:
          :noindex:


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getChildren(self) -> :py:class:`Map`
      :async:


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getDefault(self) -> :py:class:`PermissionDefault`
      :async:


   .. py:method:: getDescription(self) -> str
      :async:


   .. py:method:: getName(self) -> str
      :async:


   .. py:method:: getPermissibles(self) -> typing.List[:py:class:`Permissible`]
      :async:


   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: loadPermission

       .. py:method:: loadPermission(cls, _0:String, _1:Map) -> :py:class:`Permission`
          :async:
          :classmethod:
          :noindex:

       .. py:method:: loadPermission(cls, _0:String, _1:Map, _2:PermissionDefault, _3:List) -> :py:class:`Permission`
          :async:
          :classmethod:
          :noindex:


   .. py:method:: loadPermissions(cls, _0:Map, _1:String, _2:PermissionDefault) -> typing.List[:py:class:`Permission`]
      :async:
      :classmethod:


   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: recalculatePermissibles(self) -> None
      :async:


   .. py:method:: setDefault(self, _0:PermissionDefault) -> None
      :async:


   .. py:method:: setDescription(self, _0:String) -> None
      :async:


   .. py:method:: toString(self) -> str
      :async:

