.. currentmodule:: pycraft.server.final

Attributable
============

Inheritance
------------
* pycraft.server.final.Attributable
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.attribute.Attributable <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/attribute/Attributable.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Attributable(self, **named)
   :canonical: pycraft.server.final.Attributable

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getAttribute(self, _0:Attribute) -> :py:class:`AttributeInstance`
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: registerAttribute(self, _0:Attribute) -> None
      :async:

