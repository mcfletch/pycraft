.. currentmodule:: pycraft.server.final

ChatColor
=========

Inheritance
------------
* pycraft.server.final.ChatColor
* :py:class:`pycraft.server.proxyobjects.ServerObjectEnum`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.ChatColor <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/ChatColor.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: ChatColor(self, key)
   :canonical: pycraft.server.final.ChatColor

   Holder for an enumeration where the enumeration's key is used to lookup the value

   .. py:method:: __init__(self, key)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: asBungee(self) -> :py:class:`ChatColor`
      :async:


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


   .. py:method:: getByChar

       .. py:method:: getByChar(cls, _0:char) -> :py:class:`ChatColor`
          :async:
          :classmethod:
          :noindex:

       .. py:method:: getByChar(cls, _0:String) -> :py:class:`ChatColor`
          :async:
          :classmethod:
          :noindex:


   .. py:method:: getChar(self) -> :py:class:`char`
      :async:


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getDeclaringClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getLastColors(cls, _0:String) -> str
      :async:
      :classmethod:


   .. py:method:: get_key(self)
      

   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isColor(self) -> bool
      :async:


   .. py:method:: isFormat(self) -> bool
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


   .. py:method:: stripColor(cls, _0:String) -> str
      :async:
      :classmethod:


   .. py:method:: toString(self) -> str
      :async:


   .. py:method:: translateAlternateColorCodes(cls, _0:char, _1:String) -> str
      :async:
      :classmethod:


   .. py:method:: valueOf

       .. py:method:: valueOf(cls, _0:String) -> :py:class:`ChatColor`
          :async:
          :classmethod:
          :noindex:

       .. py:method:: valueOf(cls, _0:Class, _1:String) -> :py:class:`Enum`
          :async:
          :classmethod:
          :noindex:


   .. py:method:: values(cls) -> typing.List[:py:class:`ChatColor`]
      :async:
      :classmethod:

