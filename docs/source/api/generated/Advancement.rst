.. currentmodule:: pycraft.server.final

Advancement
===========

Inheritance
------------
* pycraft.server.final.Advancement
* :py:class:`pycraft.server.proxyobjects.KeyedServerObjectEnum`
* :py:class:`pycraft.server.proxyobjects.ServerObjectEnum`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.advancement.Advancement <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/advancement/Advancement.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Advancement(self, key)
   :canonical: pycraft.server.final.Advancement

   Namespaced/keyed enumerations

   .. py:method:: __init__(self, key)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: cached_values()
      :async:

      Get the cached values for the given enumeration


   .. py:method:: displayName(self) -> :py:class:`Component`
      :async:


   .. py:method:: from_server(key)
      

      Convert server-side structure to local object


   .. py:method:: getChildren(self) -> typing.List[:py:class:`Advancement`]
      :async:


   .. py:method:: getCriteria(self) -> typing.List[str]
      :async:


   .. py:method:: getDisplay(self) -> :py:class:`AdvancementDisplay`
      :async:


   .. py:method:: getKey(self) -> :py:class:`NamespacedKey`
      :async:


   .. py:method:: getParent(self) -> :py:class:`Advancement`
      :async:


   .. py:method:: getRoot(self) -> :py:class:`Advancement`
      :async:


   .. py:method:: get_key(self)
      

   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: key(self) -> :py:class:`Key`
      :async:


   .. py:method:: loosely_match(name)
      :async:
