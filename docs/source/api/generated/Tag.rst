.. currentmodule:: pycraft.server.final

Tag
===

Inheritance
------------
* pycraft.server.final.Tag
* :py:class:`pycraft.server.proxyobjects.KeyedServerObjectEnum`
* :py:class:`pycraft.server.proxyobjects.ServerObjectEnum`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.Tag <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Tag.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Tag(self, key)
   :canonical: pycraft.server.final.Tag

   Namespaced/keyed enumerations

   .. py:method:: __init__(self, key)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: cached_values()
      :async:

      Get the cached values for the given enumeration


   .. py:method:: from_server(key)
      

      Convert server-side structure to local object


   .. py:method:: getKey(self) -> :py:class:`NamespacedKey`
      :async:


   .. py:method:: getValues(self) -> typing.List[:py:class:`T`]
      :async:


   .. py:method:: get_key(self)
      

   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isTagged(self, _0:Keyed) -> bool
      :async:


   .. py:method:: key(self) -> :py:class:`Key`
      :async:


   .. py:method:: loosely_match(name)
      :async:
