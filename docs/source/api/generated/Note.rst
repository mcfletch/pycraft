.. currentmodule:: pycraft.server.final

Note
====

Inheritance
------------
* pycraft.server.final.Note
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.Note <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Note.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Note(self, **named)
   :canonical: pycraft.server.final.Note

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: flat(cls, _0:int, _1:Tone) -> :py:class:`Note`
      :async:
      :classmethod:


   .. py:method:: flattened(self) -> :py:class:`Note`
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getId(self) -> :py:class:`byte`
      :async:


   .. py:method:: getOctave(self) -> int
      :async:


   .. py:method:: getTone(self) -> :py:class:`Tone`
      :async:


   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isSharped(self) -> bool
      :async:


   .. py:method:: natural(cls, _0:int, _1:Tone) -> :py:class:`Note`
      :async:
      :classmethod:


   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: sharp(cls, _0:int, _1:Tone) -> :py:class:`Note`
      :async:
      :classmethod:


   .. py:method:: sharped(self) -> :py:class:`Note`
      :async:


   .. py:method:: toString(self) -> str
      :async:

