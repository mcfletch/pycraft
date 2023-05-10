.. currentmodule:: pycraft.server.final

WorldCreator
============

Inheritance
------------
* pycraft.server.final.WorldCreator
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.WorldCreator <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/WorldCreator.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: WorldCreator(self, **named)
   :canonical: pycraft.server.final.WorldCreator

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: biomeProvider

       .. py:method:: biomeProvider(self) -> :py:class:`BiomeProvider`
          :async:
          :noindex:

       .. py:method:: biomeProvider(self, _0:String) -> :py:class:`WorldCreator`
          :async:
          :noindex:

       .. py:method:: biomeProvider(self, _0:BiomeProvider) -> :py:class:`WorldCreator`
          :async:
          :noindex:

       .. py:method:: biomeProvider(self, _0:String, _1:CommandSender) -> :py:class:`WorldCreator`
          :async:
          :noindex:


   .. py:method:: copy

       .. py:method:: copy(self, _0:WorldCreator) -> :py:class:`WorldCreator`
          :async:
          :noindex:

       .. py:method:: copy(self, _0:World) -> :py:class:`WorldCreator`
          :async:
          :noindex:


   .. py:method:: createWorld(self) -> :py:class:`World`
      :async:


   .. py:method:: environment

       .. py:method:: environment(self) -> :py:class:`Environment`
          :async:
          :noindex:

       .. py:method:: environment(self, _0:Environment) -> :py:class:`WorldCreator`
          :async:
          :noindex:


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: generateStructures

       .. py:method:: generateStructures(self) -> bool
          :async:
          :noindex:

       .. py:method:: generateStructures(self, _0:boolean) -> :py:class:`WorldCreator`
          :async:
          :noindex:


   .. py:method:: generator

       .. py:method:: generator(self) -> :py:class:`ChunkGenerator`
          :async:
          :noindex:

       .. py:method:: generator(self, _0:String) -> :py:class:`WorldCreator`
          :async:
          :noindex:

       .. py:method:: generator(self, _0:ChunkGenerator) -> :py:class:`WorldCreator`
          :async:
          :noindex:

       .. py:method:: generator(self, _0:String, _1:CommandSender) -> :py:class:`WorldCreator`
          :async:
          :noindex:


   .. py:method:: generatorSettings

       .. py:method:: generatorSettings(self) -> str
          :async:
          :noindex:

       .. py:method:: generatorSettings(self, _0:String) -> :py:class:`WorldCreator`
          :async:
          :noindex:


   .. py:method:: getBiomeProviderForName(cls, _0:String, _1:String, _2:CommandSender) -> :py:class:`BiomeProvider`
      :async:
      :classmethod:


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getGeneratorForName(cls, _0:String, _1:String, _2:CommandSender) -> :py:class:`ChunkGenerator`
      :async:
      :classmethod:


   .. py:method:: hardcore

       .. py:method:: hardcore(self) -> bool
          :async:
          :noindex:

       .. py:method:: hardcore(self, _0:boolean) -> :py:class:`WorldCreator`
          :async:
          :noindex:


   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: keepSpawnLoaded

       .. py:method:: keepSpawnLoaded(self) -> :py:class:`TriState`
          :async:
          :noindex:

       .. py:method:: keepSpawnLoaded(self, _0:TriState) -> :py:class:`WorldCreator`
          :async:
          :noindex:


   .. py:method:: key(self) -> :py:class:`NamespacedKey`
      :async:


   .. py:method:: name

       .. py:method:: name(self) -> str
          :async:
          :noindex:

       .. py:method:: name(cls, _0:String) -> :py:class:`WorldCreator`
          :async:
          :classmethod:
          :noindex:


   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: ofKey(cls, _0:NamespacedKey) -> :py:class:`WorldCreator`
      :async:
      :classmethod:


   .. py:method:: ofNameAndKey(cls, _0:String, _1:NamespacedKey) -> :py:class:`WorldCreator`
      :async:
      :classmethod:


   .. py:method:: seed

       .. py:method:: seed(self) -> :py:class:`long`
          :async:
          :noindex:

       .. py:method:: seed(self, _0:long) -> :py:class:`WorldCreator`
          :async:
          :noindex:


   .. py:method:: toString(self) -> str
      :async:


   .. py:method:: type

       .. py:method:: type(self) -> :py:class:`WorldType`
          :async:
          :noindex:

       .. py:method:: type(self, _0:WorldType) -> :py:class:`WorldCreator`
          :async:
          :noindex:

