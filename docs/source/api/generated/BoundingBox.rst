.. currentmodule:: pycraft.server.final

BoundingBox
===========

Inheritance
------------
* pycraft.server.final.BoundingBox
* :py:class:`pycraft.server.final.ConfigurationSerializable`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.util.BoundingBox <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/util/BoundingBox.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: BoundingBox(self, **named)
   :canonical: pycraft.server.final.BoundingBox

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: contains

       .. py:method:: contains(self, _0:Vector) -> bool
          :async:
          :noindex:

       .. py:method:: contains(self, _0:BoundingBox) -> bool
          :async:
          :noindex:

       .. py:method:: contains(self, _0:Vector, _1:Vector) -> bool
          :async:
          :noindex:

       .. py:method:: contains(self, _0:double, _1:double, _2:double) -> bool
          :async:
          :noindex:


   .. py:method:: copy(self, _0:BoundingBox) -> :py:class:`BoundingBox`
      :async:


   .. py:method:: deserialize(cls, _0:Map) -> :py:class:`BoundingBox`
      :async:
      :classmethod:


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: expand

       .. py:method:: expand(self, _0:double) -> :py:class:`BoundingBox`
          :async:
          :noindex:

       .. py:method:: expand(self, _0:Vector) -> :py:class:`BoundingBox`
          :async:
          :noindex:

       .. py:method:: expand(self, _0:Vector, _1:double) -> :py:class:`BoundingBox`
          :async:
          :noindex:

       .. py:method:: expand(self, _0:BlockFace, _1:double) -> :py:class:`BoundingBox`
          :async:
          :noindex:

       .. py:method:: expand(self, _0:double, _1:double, _2:double) -> :py:class:`BoundingBox`
          :async:
          :noindex:

       .. py:method:: expand(self, _0:double, _1:double, _2:double, _3:double) -> :py:class:`BoundingBox`
          :async:
          :noindex:

       .. py:method:: expand(self, _0:double, _1:double, _2:double, _3:double, _4:double, _5:double) -> :py:class:`BoundingBox`
          :async:
          :noindex:


   .. py:method:: expandDirectional

       .. py:method:: expandDirectional(self, _0:Vector) -> :py:class:`BoundingBox`
          :async:
          :noindex:

       .. py:method:: expandDirectional(self, _0:double, _1:double, _2:double) -> :py:class:`BoundingBox`
          :async:
          :noindex:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getCenter(self) -> :py:class:`Vector`
      :async:


   .. py:method:: getCenterX(self) -> float
      :async:


   .. py:method:: getCenterY(self) -> float
      :async:


   .. py:method:: getCenterZ(self) -> float
      :async:


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getHeight(self) -> float
      :async:


   .. py:method:: getMax(self) -> :py:class:`Vector`
      :async:


   .. py:method:: getMaxX(self) -> float
      :async:


   .. py:method:: getMaxY(self) -> float
      :async:


   .. py:method:: getMaxZ(self) -> float
      :async:


   .. py:method:: getMin(self) -> :py:class:`Vector`
      :async:


   .. py:method:: getMinX(self) -> float
      :async:


   .. py:method:: getMinY(self) -> float
      :async:


   .. py:method:: getMinZ(self) -> float
      :async:


   .. py:method:: getVolume(self) -> float
      :async:


   .. py:method:: getWidthX(self) -> float
      :async:


   .. py:method:: getWidthZ(self) -> float
      :async:


   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: intersection(self, _0:BoundingBox) -> :py:class:`BoundingBox`
      :async:


   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: of

       .. py:method:: of(cls, _0:Block) -> :py:class:`BoundingBox`
          :async:
          :classmethod:
          :noindex:

       .. py:method:: of(cls, _0:Vector, _1:Vector) -> :py:class:`BoundingBox`
          :async:
          :classmethod:
          :noindex:

       .. py:method:: of(cls, _0:Location, _1:Location) -> :py:class:`BoundingBox`
          :async:
          :classmethod:
          :noindex:

       .. py:method:: of(cls, _0:Block, _1:Block) -> :py:class:`BoundingBox`
          :async:
          :classmethod:
          :noindex:

       .. py:method:: of(cls, _0:Location, _1:double, _2:double, _3:double) -> :py:class:`BoundingBox`
          :async:
          :classmethod:
          :noindex:

       .. py:method:: of(cls, _0:Vector, _1:double, _2:double, _3:double) -> :py:class:`BoundingBox`
          :async:
          :classmethod:
          :noindex:


   .. py:method:: overlaps

       .. py:method:: overlaps(self, _0:BoundingBox) -> bool
          :async:
          :noindex:

       .. py:method:: overlaps(self, _0:Vector, _1:Vector) -> bool
          :async:
          :noindex:


   .. py:method:: rayTrace(self, _0:Vector, _1:Vector, _2:double) -> :py:class:`RayTraceResult`
      :async:


   .. py:method:: resize(self, _0:double, _1:double, _2:double, _3:double, _4:double, _5:double) -> :py:class:`BoundingBox`
      :async:


   .. py:method:: serialize(self) -> :py:class:`Map`
      :async:


   .. py:method:: shift

       .. py:method:: shift(self, _0:Location) -> :py:class:`BoundingBox`
          :async:
          :noindex:

       .. py:method:: shift(self, _0:Vector) -> :py:class:`BoundingBox`
          :async:
          :noindex:

       .. py:method:: shift(self, _0:double, _1:double, _2:double) -> :py:class:`BoundingBox`
          :async:
          :noindex:


   .. py:method:: toString(self) -> str
      :async:


   .. py:method:: union

       .. py:method:: union(self, _0:Vector) -> :py:class:`BoundingBox`
          :async:
          :noindex:

       .. py:method:: union(self, _0:Location) -> :py:class:`BoundingBox`
          :async:
          :noindex:

       .. py:method:: union(self, _0:BoundingBox) -> :py:class:`BoundingBox`
          :async:
          :noindex:

       .. py:method:: union(self, _0:double, _1:double, _2:double) -> :py:class:`BoundingBox`
          :async:
          :noindex:

