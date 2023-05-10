.. currentmodule:: pycraft.server.final

Statistic
=========

Inheritance
------------
* pycraft.server.final.Statistic
* :py:class:`pycraft.server.world.Statistic`
* :py:class:`pycraft.server.proxyobjects.KeyedServerObjectEnum`
* :py:class:`pycraft.server.proxyobjects.ServerObjectEnum`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.Statistic <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Statistic.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Statistic(self, key)
   :canonical: pycraft.server.final.Statistic

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


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getDeclaringClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getKey(self) -> :py:class:`NamespacedKey`
      :async:


   .. py:method:: getType(self) -> :py:class:`Type`
      :async:


   .. py:method:: get_key(self)
      

   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isBlock(self) -> bool
      :async:


   .. py:method:: isSubstatistic(self) -> bool
      :async:


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

       .. py:method:: valueOf(cls, _0:String) -> :py:class:`Statistic`
          :async:
          :classmethod:
          :noindex:

       .. py:method:: valueOf(cls, _0:Class, _1:String) -> :py:class:`Enum`
          :async:
          :classmethod:
          :noindex:


   .. py:method:: values(cls) -> typing.List[:py:class:`Statistic`]
      :async:
      :classmethod:

