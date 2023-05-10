.. currentmodule:: pycraft.server.final

Warning
=======

Inheritance
------------
* pycraft.server.final.Warning
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.Warning <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Warning.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Warning(self, **named)
   :canonical: pycraft.server.final.Warning

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: annotationType(self) -> :py:class:`Class`
      :async:


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: reason(self) -> str
      :async:


   .. py:method:: toString(self) -> str
      :async:


   .. py:method:: value(self) -> bool
      :async:

