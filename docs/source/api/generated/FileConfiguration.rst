.. currentmodule:: pycraft.server.final

FileConfiguration
=================

Inheritance
------------
* pycraft.server.final.FileConfiguration
* :py:class:`pycraft.server.final.MemoryConfiguration`
* :py:class:`pycraft.server.final.Configuration`
* :py:class:`pycraft.server.final.MemorySection`
* :py:class:`pycraft.server.final.ConfigurationSection`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.configuration.file.FileConfiguration <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/configuration/file/FileConfiguration.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: FileConfiguration(self, **named)
   :canonical: pycraft.server.final.FileConfiguration

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: addDefault(self, _0:String, _1:Object) -> None
      :async:


   .. py:method:: addDefaults

       .. py:method:: addDefaults(self, _0:Map) -> None
          :async:
          :noindex:

       .. py:method:: addDefaults(self, _0:Configuration) -> None
          :async:
          :noindex:


   .. py:method:: contains

       .. py:method:: contains(self, _0:String) -> bool
          :async:
          :noindex:

       .. py:method:: contains(self, _0:String, _1:boolean) -> bool
          :async:
          :noindex:


   .. py:method:: createPath

       .. py:method:: createPath(cls, _0:ConfigurationSection, _1:String) -> str
          :async:
          :classmethod:
          :noindex:

       .. py:method:: createPath(cls, _0:ConfigurationSection, _1:String, _2:ConfigurationSection) -> str
          :async:
          :classmethod:
          :noindex:


   .. py:method:: createSection

       .. py:method:: createSection(self, _0:String) -> :py:class:`ConfigurationSection`
          :async:
          :noindex:

       .. py:method:: createSection(self, _0:String, _1:Map) -> :py:class:`ConfigurationSection`
          :async:
          :noindex:


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: get

       .. py:method:: get(self, _0:String) -> :py:class:`Object`
          :async:
          :noindex:

       .. py:method:: get(self, _0:String, _1:Object) -> :py:class:`Object`
          :async:
          :noindex:


   .. py:method:: getBoolean

       .. py:method:: getBoolean(self, _0:String) -> bool
          :async:
          :noindex:

       .. py:method:: getBoolean(self, _0:String, _1:boolean) -> bool
          :async:
          :noindex:


   .. py:method:: getBooleanList(self, _0:String) -> typing.List[bool]
      :async:


   .. py:method:: getByteList(self, _0:String) -> typing.List[:py:class:`Byte`]
      :async:


   .. py:method:: getCharacterList(self, _0:String) -> typing.List[:py:class:`Character`]
      :async:


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getColor

       .. py:method:: getColor(self, _0:String) -> :py:class:`Color`
          :async:
          :noindex:

       .. py:method:: getColor(self, _0:String, _1:Color) -> :py:class:`Color`
          :async:
          :noindex:


   .. py:method:: getComments(self, _0:String) -> typing.List[str]
      :async:


   .. py:method:: getConfigurationSection(self, _0:String) -> :py:class:`ConfigurationSection`
      :async:


   .. py:method:: getCurrentPath(self) -> str
      :async:


   .. py:method:: getDefaultSection(self) -> :py:class:`ConfigurationSection`
      :async:


   .. py:method:: getDefaults(self) -> :py:class:`Configuration`
      :async:


   .. py:method:: getDouble

       .. py:method:: getDouble(self, _0:String) -> float
          :async:
          :noindex:

       .. py:method:: getDouble(self, _0:String, _1:double) -> float
          :async:
          :noindex:


   .. py:method:: getDoubleList(self, _0:String) -> typing.List[float]
      :async:


   .. py:method:: getFloatList(self, _0:String) -> typing.List[float]
      :async:


   .. py:method:: getInlineComments(self, _0:String) -> typing.List[str]
      :async:


   .. py:method:: getInt

       .. py:method:: getInt(self, _0:String) -> int
          :async:
          :noindex:

       .. py:method:: getInt(self, _0:String, _1:int) -> int
          :async:
          :noindex:


   .. py:method:: getIntegerList(self, _0:String) -> typing.List[int]
      :async:


   .. py:method:: getItemStack

       .. py:method:: getItemStack(self, _0:String) -> :py:class:`ItemStack`
          :async:
          :noindex:

       .. py:method:: getItemStack(self, _0:String, _1:ItemStack) -> :py:class:`ItemStack`
          :async:
          :noindex:


   .. py:method:: getKeys(self, _0:boolean) -> typing.List[str]
      :async:


   .. py:method:: getList

       .. py:method:: getList(self, _0:String) -> typing.List[:py:class:`?`]
          :async:
          :noindex:

       .. py:method:: getList(self, _0:String, _1:List) -> typing.List[:py:class:`?`]
          :async:
          :noindex:


   .. py:method:: getLocation

       .. py:method:: getLocation(self, _0:String) -> :py:class:`Location`
          :async:
          :noindex:

       .. py:method:: getLocation(self, _0:String, _1:Location) -> :py:class:`Location`
          :async:
          :noindex:


   .. py:method:: getLong

       .. py:method:: getLong(self, _0:String) -> :py:class:`long`
          :async:
          :noindex:

       .. py:method:: getLong(self, _0:String, _1:long) -> :py:class:`long`
          :async:
          :noindex:


   .. py:method:: getLongList(self, _0:String) -> typing.List[:py:class:`Long`]
      :async:


   .. py:method:: getMapList(self, _0:String) -> typing.List[:py:class:`java.util.Map<?, ?>`]
      :async:


   .. py:method:: getName(self) -> str
      :async:


   .. py:method:: getObject

       .. py:method:: getObject(self, _0:String, _1:Class) -> :py:class:`Object`
          :async:
          :noindex:

       .. py:method:: getObject(self, _0:String, _1:Class, _2:Object) -> :py:class:`Object`
          :async:
          :noindex:


   .. py:method:: getOfflinePlayer

       .. py:method:: getOfflinePlayer(self, _0:String) -> :py:class:`OfflinePlayer`
          :async:
          :noindex:

       .. py:method:: getOfflinePlayer(self, _0:String, _1:OfflinePlayer) -> :py:class:`OfflinePlayer`
          :async:
          :noindex:


   .. py:method:: getParent(self) -> :py:class:`ConfigurationSection`
      :async:


   .. py:method:: getRoot(self) -> :py:class:`Configuration`
      :async:


   .. py:method:: getSerializable

       .. py:method:: getSerializable(self, _0:String, _1:Class) -> :py:class:`ConfigurationSerializable`
          :async:
          :noindex:

       .. py:method:: getSerializable(self, _0:String, _1:Class, _2:ConfigurationSerializable) -> :py:class:`ConfigurationSerializable`
          :async:
          :noindex:


   .. py:method:: getShortList(self, _0:String) -> typing.List[:py:class:`Short`]
      :async:


   .. py:method:: getString

       .. py:method:: getString(self, _0:String) -> str
          :async:
          :noindex:

       .. py:method:: getString(self, _0:String, _1:String) -> str
          :async:
          :noindex:


   .. py:method:: getStringList(self, _0:String) -> typing.List[str]
      :async:


   .. py:method:: getValues(self, _0:boolean) -> :py:class:`Map`
      :async:


   .. py:method:: getVector

       .. py:method:: getVector(self, _0:String) -> :py:class:`Vector`
          :async:
          :noindex:

       .. py:method:: getVector(self, _0:String, _1:Vector) -> :py:class:`Vector`
          :async:
          :noindex:


   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isBoolean(self, _0:String) -> bool
      :async:


   .. py:method:: isColor(self, _0:String) -> bool
      :async:


   .. py:method:: isConfigurationSection(self, _0:String) -> bool
      :async:


   .. py:method:: isDouble(self, _0:String) -> bool
      :async:


   .. py:method:: isInt(self, _0:String) -> bool
      :async:


   .. py:method:: isItemStack(self, _0:String) -> bool
      :async:


   .. py:method:: isList(self, _0:String) -> bool
      :async:


   .. py:method:: isLocation(self, _0:String) -> bool
      :async:


   .. py:method:: isLong(self, _0:String) -> bool
      :async:


   .. py:method:: isOfflinePlayer(self, _0:String) -> bool
      :async:


   .. py:method:: isSet(self, _0:String) -> bool
      :async:


   .. py:method:: isString(self, _0:String) -> bool
      :async:


   .. py:method:: isVector(self, _0:String) -> bool
      :async:


   .. py:method:: load

       .. py:method:: load(self, _0:Reader) -> None
          :async:
          :noindex:

       .. py:method:: load(self, _0:File) -> None
          :async:
          :noindex:

       .. py:method:: load(self, _0:String) -> None
          :async:
          :noindex:


   .. py:method:: loadFromString(self, _0:String) -> None
      :async:


   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: options

       .. py:method:: options(self) -> :py:class:`MemoryConfigurationOptions`
          :async:
          :noindex:

       .. py:method:: options(self) -> :py:class:`FileConfigurationOptions`
          :async:
          :noindex:

       .. py:method:: options(self) -> :py:class:`ConfigurationOptions`
          :async:
          :noindex:


   .. py:method:: save

       .. py:method:: save(self, _0:File) -> None
          :async:
          :noindex:

       .. py:method:: save(self, _0:String) -> None
          :async:
          :noindex:


   .. py:method:: saveToString(self) -> str
      :async:


   .. py:method:: set(self, _0:String, _1:Object) -> None
      :async:


   .. py:method:: setComments(self, _0:String, _1:List) -> None
      :async:


   .. py:method:: setDefaults(self, _0:Configuration) -> None
      :async:


   .. py:method:: setInlineComments(self, _0:String, _1:List) -> None
      :async:


   .. py:method:: toString(self) -> str
      :async:

