.. currentmodule:: pycraft.server.final

Transformation
==============

Inheritance
------------
* pycraft.server.final.Transformation
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.util.Transformation <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/util/Transformation.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Transformation(self, **named)
   :canonical: pycraft.server.final.Transformation

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getLeftRotation(self) -> :py:class:`Quaternionf`
      :async:


   .. py:method:: getRightRotation(self) -> :py:class:`Quaternionf`
      :async:


   .. py:method:: getScale(self) -> :py:class:`Vector3f`
      :async:


   .. py:method:: getTranslation(self) -> :py:class:`Vector3f`
      :async:


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

