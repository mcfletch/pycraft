.. currentmodule:: pycraft.server.final

EventExecutor
=============

Inheritance
------------
* pycraft.server.final.EventExecutor
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.plugin.EventExecutor <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/plugin/EventExecutor.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: EventExecutor(self, **named)
   :canonical: pycraft.server.final.EventExecutor

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: create(cls, _0:Method, _1:Class) -> :py:class:`EventExecutor`
      :async:
      :classmethod:


   .. py:method:: execute(self, _0:Listener, _1:Event) -> None
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace

