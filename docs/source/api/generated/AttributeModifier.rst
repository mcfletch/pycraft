.. currentmodule:: pycraft.server.final

AttributeModifier
=================

Inheritance
------------
* pycraft.server.final.AttributeModifier
* :py:class:`pycraft.server.final.ConfigurationSerializable`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.attribute.AttributeModifier <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/attribute/AttributeModifier.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: AttributeModifier(self, **named)
   :canonical: pycraft.server.final.AttributeModifier

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: deserialize(cls, _0:Map) -> :py:class:`AttributeModifier`
      :async:
      :classmethod:


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getAmount(self) -> float
      :async:


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getName(self) -> str
      :async:


   .. py:method:: getOperation(self) -> :py:class:`Operation`
      :async:


   .. py:method:: getSlot(self) -> :py:class:`EquipmentSlot`
      :async:


   .. py:method:: getUniqueId(self) -> uuid.UUID
      :async:


   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: serialize(self) -> :py:class:`Map`
      :async:


   .. py:method:: toString(self) -> str
      :async:

