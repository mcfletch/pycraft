.. currentmodule:: pycraft.server.final

BlockVector
===========

Inheritance
------------
* pycraft.server.final.BlockVector
* :py:class:`pycraft.server.final.Vector`
* :py:class:`pycraft.server.world.Vector`
* :py:class:`pycraft.server.final.ConfigurationSerializable`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.util.BlockVector <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/util/BlockVector.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: BlockVector(self, record, *args)
   :canonical: pycraft.server.final.BlockVector

   Object reference on the server which we are proxying

   .. py:property:: x

   .. py:property:: y

   .. py:property:: z

   .. py:method:: __add__(self, other) -> 'Vector'
      

   .. py:method:: __div__(self, other) -> 'Vector'
      

   .. py:method:: __eq__(self, other) -> bool
      

      Return self==value.


   .. py:method:: __floordiv__(self, other) -> 'Vector'
      

   .. py:method:: __getitem__(self, slice)
      

   .. py:method:: __init__(self, record, *args)
      

      Set each named key/value as an attribute on object


   .. py:method:: __iter__(self) -> (<class 'int'>, <class 'float'>, <class 'complex'>, <class 'int'>, <class 'bool'>, <class 'bytes'>, <class 'str'>, <class 'memoryview'>, <class 'numpy.bool_'>, <class 'numpy.complex64'>, <class 'numpy.complex128'>, <class 'numpy.complex256'>, <class 'numpy.float16'>, <class 'numpy.float32'>, <class 'numpy.float64'>, <class 'numpy.float128'>, <class 'numpy.int8'>, <class 'numpy.int16'>, <class 'numpy.int32'>, <class 'numpy.int64'>, <class 'numpy.longlong'>, <class 'numpy.timedelta64'>, <class 'numpy.datetime64'>, <class 'numpy.object_'>, <class 'numpy.bytes_'>, <class 'numpy.str_'>, <class 'numpy.uint8'>, <class 'numpy.uint16'>, <class 'numpy.uint32'>, <class 'numpy.uint64'>, <class 'numpy.ulonglong'>, <class 'numpy.void'>)
      

   .. py:method:: __len__(self) -> int
      

   .. py:method:: __mul__(self, other) -> 'Vector'
      

   .. py:method:: __neg__(self) -> 'Vector'
      

   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: __sub__(self, other) -> 'Vector'
      

   .. py:method:: add(self, _0:Vector) -> :py:class:`Vector`
      :async:


   .. py:method:: angle(self, _0:Vector) -> float
      :async:


   .. py:method:: checkFinite(self) -> None
      :async:


   .. py:method:: copy(self, _0:Vector) -> :py:class:`Vector`
      :async:


   .. py:method:: crossProduct(self, _0:Vector) -> :py:class:`Vector`
      :async:


   .. py:method:: deserialize

       .. py:method:: deserialize(cls, _0:Map) -> :py:class:`BlockVector`
          :async:
          :classmethod:
          :noindex:

       .. py:method:: deserialize(cls, _0:Map) -> :py:class:`Vector`
          :async:
          :classmethod:
          :noindex:


   .. py:method:: distance(self, _0:Vector) -> float
      :async:


   .. py:method:: distanceSquared(self, _0:Vector) -> float
      :async:


   .. py:method:: divide(self, _0:Vector) -> :py:class:`Vector`
      :async:


   .. py:method:: dot(self, _0:Vector) -> float
      :async:


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: from_server(record)
      

      Convert server-side structure to local object


   .. py:method:: getBlockX(self) -> int
      :async:


   .. py:method:: getBlockY(self) -> int
      :async:


   .. py:method:: getBlockZ(self) -> int
      :async:


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getCrossProduct(self, _0:Vector) -> :py:class:`Vector`
      :async:


   .. py:method:: getEpsilon(cls) -> float
      :async:
      :classmethod:


   .. py:method:: getMaximum(cls, _0:Vector, _1:Vector) -> :py:class:`Vector`
      :async:
      :classmethod:


   .. py:method:: getMidpoint(self, _0:Vector) -> :py:class:`Vector`
      :async:


   .. py:method:: getMinimum(cls, _0:Vector, _1:Vector) -> :py:class:`Vector`
      :async:
      :classmethod:


   .. py:method:: getRandom(cls) -> :py:class:`Vector`
      :async:
      :classmethod:


   .. py:method:: getX(self) -> float
      :async:


   .. py:method:: getY(self) -> float
      :async:


   .. py:method:: getZ(self) -> float
      :async:


   .. py:method:: get_key(self)
      

   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isInAABB(self, _0:Vector, _1:Vector) -> bool
      :async:


   .. py:method:: isInSphere(self, _0:Vector, _1:double) -> bool
      :async:


   .. py:method:: isNormalized(self) -> bool
      :async:


   .. py:method:: isZero(self) -> bool
      :async:


   .. py:method:: length(self) -> float
      :async:


   .. py:method:: lengthSquared(self) -> float
      :async:


   .. py:method:: midpoint(self, _0:Vector) -> :py:class:`Vector`
      :async:


   .. py:method:: multiply

       .. py:method:: multiply(self, _0:float) -> :py:class:`Vector`
          :async:
          :noindex:

       .. py:method:: multiply(self, _0:int) -> :py:class:`Vector`
          :async:
          :noindex:

       .. py:method:: multiply(self, _0:Vector) -> :py:class:`Vector`
          :async:
          :noindex:

       .. py:method:: multiply(self, _0:double) -> :py:class:`Vector`
          :async:
          :noindex:


   .. py:method:: normalize(self) -> :py:class:`Vector`
      :async:


   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: rotateAroundAxis(self, _0:Vector, _1:double) -> :py:class:`Vector`
      :async:


   .. py:method:: rotateAroundNonUnitAxis(self, _0:Vector, _1:double) -> :py:class:`Vector`
      :async:


   .. py:method:: rotateAroundX(self, _0:double) -> :py:class:`Vector`
      :async:


   .. py:method:: rotateAroundY(self, _0:double) -> :py:class:`Vector`
      :async:


   .. py:method:: rotateAroundZ(self, _0:double) -> :py:class:`Vector`
      :async:


   .. py:method:: serialize(self) -> :py:class:`Map`
      :async:


   .. py:method:: setX

       .. py:method:: setX(self, _0:float) -> :py:class:`Vector`
          :async:
          :noindex:

       .. py:method:: setX(self, _0:int) -> :py:class:`Vector`
          :async:
          :noindex:

       .. py:method:: setX(self, _0:double) -> :py:class:`Vector`
          :async:
          :noindex:


   .. py:method:: setY

       .. py:method:: setY(self, _0:float) -> :py:class:`Vector`
          :async:
          :noindex:

       .. py:method:: setY(self, _0:double) -> :py:class:`Vector`
          :async:
          :noindex:

       .. py:method:: setY(self, _0:int) -> :py:class:`Vector`
          :async:
          :noindex:


   .. py:method:: setZ

       .. py:method:: setZ(self, _0:double) -> :py:class:`Vector`
          :async:
          :noindex:

       .. py:method:: setZ(self, _0:float) -> :py:class:`Vector`
          :async:
          :noindex:

       .. py:method:: setZ(self, _0:int) -> :py:class:`Vector`
          :async:
          :noindex:


   .. py:method:: subtract(self, _0:Vector) -> :py:class:`Vector`
      :async:


   .. py:method:: toBlockVector(self) -> :py:class:`BlockVector`
      :async:


   .. py:method:: toLocation

       .. py:method:: toLocation(self, _0:World) -> :py:class:`Location`
          :async:
          :noindex:

       .. py:method:: toLocation(self, _0:World, _1:float, _2:float) -> :py:class:`Location`
          :async:
          :noindex:


   .. py:method:: toString(self) -> str
      :async:


   .. py:method:: zero(self) -> :py:class:`Vector`
      :async:

