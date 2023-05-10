.. currentmodule:: pycraft.server.final

NamespacedKey
=============

Inheritance
------------
* pycraft.server.final.NamespacedKey
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.NamespacedKey <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/NamespacedKey.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: NamespacedKey(self, **named)
   :canonical: pycraft.server.final.NamespacedKey

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: asString(self) -> str
      :async:


   .. py:method:: compareTo

       .. py:method:: compareTo(self, _0:Key) -> int
          :async:
          :noindex:

       .. py:method:: compareTo(self, _0:Object) -> int
          :async:
          :noindex:


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: examinableName(self) -> str
      :async:


   .. py:method:: examinableProperties(self) -> :py:class:`Stream`
      :async:


   .. py:method:: examine(self, _0:Examiner) -> :py:class:`Object`
      :async:


   .. py:method:: fromString

       .. py:method:: fromString(cls, _0:String) -> :py:class:`NamespacedKey`
          :async:
          :classmethod:
          :noindex:

       .. py:method:: fromString(cls, _0:String, _1:Plugin) -> :py:class:`NamespacedKey`
          :async:
          :classmethod:
          :noindex:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getKey(self) -> str
      :async:


   .. py:method:: getNamespace(self) -> str
      :async:


   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: key(self) -> :py:class:`Key`
      :async:


   .. py:method:: minecraft(cls, _0:String) -> :py:class:`NamespacedKey`
      :async:
      :classmethod:


   .. py:method:: namespace(self) -> str
      :async:


   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: randomKey(cls) -> :py:class:`NamespacedKey`
      :async:
      :classmethod:


   .. py:method:: toString(self) -> str
      :async:


   .. py:method:: value(self) -> str
      :async:

