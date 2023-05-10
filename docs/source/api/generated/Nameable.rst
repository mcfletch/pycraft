.. currentmodule:: pycraft.server.final

Nameable
========

Inheritance
------------
* pycraft.server.final.Nameable
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.Nameable <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Nameable.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Nameable(self, **named)
   :canonical: pycraft.server.final.Nameable

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: customName

       .. py:method:: customName(self) -> :py:class:`Component`
          :async:
          :noindex:

       .. py:method:: customName(self, _0:Component) -> None
          :async:
          :noindex:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getCustomName(self) -> str
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: setCustomName(self, _0:String) -> None
      :async:

