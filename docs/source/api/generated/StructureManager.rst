.. currentmodule:: pycraft.server.final

StructureManager
================

Inheritance
------------
* pycraft.server.final.StructureManager
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.structure.StructureManager <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/structure/StructureManager.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: StructureManager(self, **named)
   :canonical: pycraft.server.final.StructureManager

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: copy(self, _0:Structure) -> :py:class:`Structure`
      :async:


   .. py:method:: createStructure(self) -> :py:class:`Structure`
      :async:


   .. py:method:: deleteStructure

       .. py:method:: deleteStructure(self, _0:NamespacedKey) -> None
          :async:
          :noindex:

       .. py:method:: deleteStructure(self, _0:NamespacedKey, _1:boolean) -> None
          :async:
          :noindex:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getStructure(self, _0:NamespacedKey) -> :py:class:`Structure`
      :async:


   .. py:method:: getStructureFile(self, _0:NamespacedKey) -> :py:class:`File`
      :async:


   .. py:method:: getStructures(self) -> :py:class:`Map`
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: loadStructure

       .. py:method:: loadStructure(self, _0:File) -> :py:class:`Structure`
          :async:
          :noindex:

       .. py:method:: loadStructure(self, _0:InputStream) -> :py:class:`Structure`
          :async:
          :noindex:

       .. py:method:: loadStructure(self, _0:NamespacedKey) -> :py:class:`Structure`
          :async:
          :noindex:

       .. py:method:: loadStructure(self, _0:NamespacedKey, _1:boolean) -> :py:class:`Structure`
          :async:
          :noindex:


   .. py:method:: registerStructure(self, _0:NamespacedKey, _1:Structure) -> :py:class:`Structure`
      :async:


   .. py:method:: saveStructure

       .. py:method:: saveStructure(self, _0:NamespacedKey) -> None
          :async:
          :noindex:

       .. py:method:: saveStructure(self, _0:OutputStream, _1:Structure) -> None
          :async:
          :noindex:

       .. py:method:: saveStructure(self, _0:File, _1:Structure) -> None
          :async:
          :noindex:

       .. py:method:: saveStructure(self, _0:NamespacedKey, _1:Structure) -> None
          :async:
          :noindex:


   .. py:method:: unregisterStructure(self, _0:NamespacedKey) -> :py:class:`Structure`
      :async:

