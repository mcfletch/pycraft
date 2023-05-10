.. currentmodule:: pycraft.server.final

RegisteredServiceProvider
=========================

Inheritance
------------
* pycraft.server.final.RegisteredServiceProvider
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.plugin.RegisteredServiceProvider <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/plugin/RegisteredServiceProvider.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: RegisteredServiceProvider(self, **named)
   :canonical: pycraft.server.final.RegisteredServiceProvider

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: compareTo

       .. py:method:: compareTo(self, _0:RegisteredServiceProvider) -> int
          :async:
          :noindex:

       .. py:method:: compareTo(self, _0:Object) -> int
          :async:
          :noindex:


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getPlugin(self) -> :py:class:`Plugin`
      :async:


   .. py:method:: getPriority(self) -> :py:class:`ServicePriority`
      :async:


   .. py:method:: getProvider(self) -> :py:class:`Object`
      :async:


   .. py:method:: getService(self) -> :py:class:`Class`
      :async:


   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: toString(self) -> str
      :async:

