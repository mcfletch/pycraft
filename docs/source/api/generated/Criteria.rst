.. currentmodule:: pycraft.server.final

Criteria
========

Inheritance
------------
* pycraft.server.final.Criteria
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.scoreboard.Criteria <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/scoreboard/Criteria.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Criteria(self, **named)
   :canonical: pycraft.server.final.Criteria

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: create(cls, _0:String) -> :py:class:`Criteria`
      :async:
      :classmethod:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getDefaultRenderType(self) -> :py:class:`RenderType`
      :async:


   .. py:method:: getName(self) -> str
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isReadOnly(self) -> bool
      :async:


   .. py:method:: statistic

       .. py:method:: statistic(cls, _0:Statistic) -> :py:class:`Criteria`
          :async:
          :classmethod:
          :noindex:

       .. py:method:: statistic(cls, _0:Statistic, _1:EntityType) -> :py:class:`Criteria`
          :async:
          :classmethod:
          :noindex:

       .. py:method:: statistic(cls, _0:Statistic, _1:Material) -> :py:class:`Criteria`
          :async:
          :classmethod:
          :noindex:

