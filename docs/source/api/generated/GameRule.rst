.. currentmodule:: pycraft.server.final

GameRule
========

Inheritance
------------
* pycraft.server.final.GameRule
* :py:class:`pycraft.server.world.GameRule`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.GameRule <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/GameRule.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: GameRule(self, name)
   :canonical: pycraft.server.final.GameRule

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, name)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getByName(cls, _0:String) -> :py:class:`GameRule`
      :async:
      :classmethod:


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getName(self) -> str
      :async:


   .. py:method:: getType(self) -> :py:class:`Class`
      :async:


   .. py:method:: get_key(self)
      

   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: toString(self) -> str
      :async:


   .. py:method:: translationKey(self) -> str
      :async:


   .. py:method:: values(cls) -> typing.List[:py:class:`GameRule`]
      :async:
      :classmethod:

