.. currentmodule:: pycraft.server.final

Art
===

Inheritance
------------
* pycraft.server.final.Art
* :py:class:`pycraft.server.world.Art`
* :py:class:`pycraft.server.proxyobjects.KeyedServerObjectEnum`
* :py:class:`pycraft.server.proxyobjects.ServerObjectEnum`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.Art <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Art.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Art(self, key)
   :canonical: pycraft.server.final.Art

   Namespaced/keyed enumerations

   .. py:method:: __init__(self, key)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: cached_values()
      :async:

      Get the cached values for the given enumeration


   .. py:method:: compareTo

       .. py:method:: compareTo(self, _0:Object) -> int
          :async:
          :noindex:

       .. py:method:: compareTo(self, _0:Enum) -> int
          :async:
          :noindex:


   .. py:method:: describeConstable(self) -> :py:class:`Optional`
      :async:


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: from_server(key)
      

      Convert server-side structure to local object


   .. py:method:: getBlockHeight(self) -> int
      :async:


   .. py:method:: getBlockWidth(self) -> int
      :async:


   .. py:method:: getById(cls, _0:int) -> :py:class:`Art`
      :async:
      :classmethod:


   .. py:method:: getByName(cls, _0:String) -> :py:class:`Art`
      :async:
      :classmethod:


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getDeclaringClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getId(self) -> int
      :async:


   .. py:method:: getKey(self) -> :py:class:`NamespacedKey`
      :async:


   .. py:method:: get_key(self)
      

   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: key(self) -> :py:class:`Key`
      :async:


   .. py:method:: loosely_match(name)
      :async:

   .. py:method:: name(self) -> str
      :async:


   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: ordinal(self) -> int
      :async:


   .. py:method:: toString(self) -> str
      :async:


   .. py:method:: valueOf

       .. py:method:: valueOf(cls, _0:String) -> :py:class:`Art`
          :async:
          :classmethod:
          :noindex:

       .. py:method:: valueOf(cls, _0:Class, _1:String) -> :py:class:`Enum`
          :async:
          :classmethod:
          :noindex:


   .. py:method:: values(cls) -> typing.List[:py:class:`Art`]
      :async:
      :classmethod:

