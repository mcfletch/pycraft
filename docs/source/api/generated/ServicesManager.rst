.. currentmodule:: pycraft.server.final

ServicesManager
===============

Inheritance
------------
* pycraft.server.final.ServicesManager
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.plugin.ServicesManager <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/plugin/ServicesManager.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: ServicesManager(self, **named)
   :canonical: pycraft.server.final.ServicesManager

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getKnownServices(self) -> typing.List[:py:class:`java.lang.Class<?>`]
      :async:


   .. py:method:: getRegistration(self, _0:Class) -> :py:class:`RegisteredServiceProvider`
      :async:


   .. py:method:: getRegistrations

       .. py:method:: getRegistrations(self, _0:Class) -> typing.List[:py:class:`org.bukkit.plugin.RegisteredServiceProvider<T>`]
          :async:
          :noindex:

       .. py:method:: getRegistrations(self, _0:Plugin) -> typing.List[:py:class:`org.bukkit.plugin.RegisteredServiceProvider<?>`]
          :async:
          :noindex:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isProvidedFor(self, _0:Class) -> bool
      :async:


   .. py:method:: load(self, _0:Class) -> :py:class:`Object`
      :async:


   .. py:method:: register(self, _0:Class, _1:Object, _2:Plugin, _3:ServicePriority) -> None
      :async:


   .. py:method:: unregister

       .. py:method:: unregister(self, _0:Object) -> None
          :async:
          :noindex:

       .. py:method:: unregister(self, _0:Class, _1:Object) -> None
          :async:
          :noindex:


   .. py:method:: unregisterAll(self, _0:Plugin) -> None
      :async:

