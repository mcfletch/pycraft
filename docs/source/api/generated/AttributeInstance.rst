.. currentmodule:: pycraft.server.final

AttributeInstance
=================

Inheritance
------------
* pycraft.server.final.AttributeInstance
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.attribute.AttributeInstance <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/attribute/AttributeInstance.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: AttributeInstance(self, **named)
   :canonical: pycraft.server.final.AttributeInstance

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: addModifier(self, _0:AttributeModifier) -> None
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getAttribute(self) -> :py:class:`Attribute`
      :async:


   .. py:method:: getBaseValue(self) -> float
      :async:


   .. py:method:: getDefaultValue(self) -> float
      :async:


   .. py:method:: getModifiers(self) -> typing.List[:py:class:`AttributeModifier`]
      :async:


   .. py:method:: getValue(self) -> float
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: removeModifier(self, _0:AttributeModifier) -> None
      :async:


   .. py:method:: setBaseValue(self, _0:double) -> None
      :async:

