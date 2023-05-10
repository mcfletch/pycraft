.. currentmodule:: pycraft.server.final

BookMetaBuilder
===============

Inheritance
------------
* pycraft.server.final.BookMetaBuilder
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.inventory.meta.BookMeta.BookMetaBuilder <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/inventory/meta/BookMeta/BookMetaBuilder.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: BookMetaBuilder(self, **named)
   :canonical: pycraft.server.final.BookMetaBuilder

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: addPage

       .. py:method:: addPage(self, _0:Component) -> :py:class:`BookMetaBuilder`
          :async:
          :noindex:

       .. py:method:: addPage(self, _0:Component) -> :py:class:`Builder`
          :async:
          :noindex:


   .. py:method:: author

       .. py:method:: author(self, _0:Component) -> :py:class:`Builder`
          :async:
          :noindex:

       .. py:method:: author(self, _0:Component) -> :py:class:`BookMetaBuilder`
          :async:
          :noindex:


   .. py:method:: build

       .. py:method:: build(self) -> :py:class:`Object`
          :async:
          :noindex:

       .. py:method:: build(self) -> :py:class:`BookMeta`
          :async:
          :noindex:

       .. py:method:: build(self) -> :py:class:`Book`
          :async:
          :noindex:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: pages

       .. py:method:: pages(self, _0:Collection) -> :py:class:`Builder`
          :async:
          :noindex:

       .. py:method:: pages(self, _0:Collection) -> :py:class:`BookMetaBuilder`
          :async:
          :noindex:

       .. py:method:: pages(self, _0:Component[]) -> :py:class:`BookMetaBuilder`
          :async:
          :noindex:

       .. py:method:: pages(self, _0:Component[]) -> :py:class:`Builder`
          :async:
          :noindex:


   .. py:method:: title

       .. py:method:: title(self, _0:Component) -> :py:class:`BookMetaBuilder`
          :async:
          :noindex:

       .. py:method:: title(self, _0:Component) -> :py:class:`Builder`
          :async:
          :noindex:

