.. currentmodule:: pycraft.server.final

Keyed
=====

Inheritance
------------
* pycraft.server.final.Keyed
* :py:class:`pycraft.server.proxyobjects.KeyedServerObjectEnum`
* :py:class:`pycraft.server.proxyobjects.ServerObjectEnum`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.Keyed <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Keyed.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Keyed(self, key)
   :canonical: pycraft.server.final.Keyed

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


   .. py:method:: get_key(self)
      

   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: key(self) -> :py:class:`Key`
      :async:


   .. py:method:: loosely_match(name)
      :async:

   .. py:method:: values()
      :async:

      Get the enumerated values in this class

