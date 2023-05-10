.. currentmodule:: pycraft.server.final

Sittable
========

Inheritance
------------
* pycraft.server.final.Sittable
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.entity.Sittable <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/entity/Sittable.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Sittable(self, **named)
   :canonical: pycraft.server.final.Sittable

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isSitting(self) -> bool
      :async:


   .. py:method:: setSitting(self, _0:boolean) -> None
      :async:

