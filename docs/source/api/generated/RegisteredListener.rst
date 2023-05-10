.. currentmodule:: pycraft.server.final

RegisteredListener
==================

Inheritance
------------
* pycraft.server.final.RegisteredListener
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.plugin.RegisteredListener <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/plugin/RegisteredListener.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: RegisteredListener(self, **named)
   :canonical: pycraft.server.final.RegisteredListener

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: callEvent(self, _0:Event) -> None
      :async:


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getExecutor(self) -> :py:class:`EventExecutor`
      :async:


   .. py:method:: getListener(self) -> :py:class:`Listener`
      :async:


   .. py:method:: getPlugin(self) -> :py:class:`Plugin`
      :async:


   .. py:method:: getPriority(self) -> :py:class:`EventPriority`
      :async:


   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isIgnoringCancelled(self) -> bool
      :async:


   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: toString(self) -> str
      :async:

