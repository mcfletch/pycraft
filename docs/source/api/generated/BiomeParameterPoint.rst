.. currentmodule:: pycraft.server.final

BiomeParameterPoint
===================

Inheritance
------------
* pycraft.server.final.BiomeParameterPoint
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.generator.BiomeParameterPoint <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/generator/BiomeParameterPoint.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: BiomeParameterPoint(self, **named)
   :canonical: pycraft.server.final.BiomeParameterPoint

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getContinentalness(self) -> float
      :async:


   .. py:method:: getDepth(self) -> float
      :async:


   .. py:method:: getErosion(self) -> float
      :async:


   .. py:method:: getHumidity(self) -> float
      :async:


   .. py:method:: getMaxContinentalness(self) -> float
      :async:


   .. py:method:: getMaxDepth(self) -> float
      :async:


   .. py:method:: getMaxErosion(self) -> float
      :async:


   .. py:method:: getMaxHumidity(self) -> float
      :async:


   .. py:method:: getMaxTemperature(self) -> float
      :async:


   .. py:method:: getMaxWeirdness(self) -> float
      :async:


   .. py:method:: getMinContinentalness(self) -> float
      :async:


   .. py:method:: getMinDepth(self) -> float
      :async:


   .. py:method:: getMinErosion(self) -> float
      :async:


   .. py:method:: getMinHumidity(self) -> float
      :async:


   .. py:method:: getMinTemperature(self) -> float
      :async:


   .. py:method:: getMinWeirdness(self) -> float
      :async:


   .. py:method:: getTemperature(self) -> float
      :async:


   .. py:method:: getWeirdness(self) -> float
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace

