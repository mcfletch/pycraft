.. currentmodule:: pycraft.server.final

HandlerList
===========

Inheritance
------------
* pycraft.server.final.HandlerList
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.event.HandlerList <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/event/HandlerList.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: HandlerList(self, **named)
   :canonical: pycraft.server.final.HandlerList

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: bake(self) -> None
      :async:


   .. py:method:: bakeAll(cls) -> None
      :async:
      :classmethod:


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getHandlerLists(cls) -> :py:class:`ArrayList`
      :async:
      :classmethod:


   .. py:method:: getRegisteredListeners

       .. py:method:: getRegisteredListeners(self) -> typing.List[:py:class:`RegisteredListener`]
          :async:
          :noindex:

       .. py:method:: getRegisteredListeners(cls, _0:Plugin) -> :py:class:`ArrayList`
          :async:
          :classmethod:
          :noindex:


   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: register(self, _0:RegisteredListener) -> None
      :async:


   .. py:method:: registerAll(self, _0:Collection) -> None
      :async:


   .. py:method:: toString(self) -> str
      :async:


   .. py:method:: unregister

       .. py:method:: unregister(self, _0:RegisteredListener) -> None
          :async:
          :noindex:

       .. py:method:: unregister(self, _0:Plugin) -> None
          :async:
          :noindex:

       .. py:method:: unregister(self, _0:Listener) -> None
          :async:
          :noindex:


   .. py:method:: unregisterAll

       .. py:method:: unregisterAll(cls) -> None
          :async:
          :classmethod:
          :noindex:

       .. py:method:: unregisterAll(cls, _0:Plugin) -> None
          :async:
          :classmethod:
          :noindex:

       .. py:method:: unregisterAll(cls, _0:Listener) -> None
          :async:
          :classmethod:
          :noindex:

