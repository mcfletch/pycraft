.. currentmodule:: pycraft.server.final

Merchant
========

Inheritance
------------
* pycraft.server.final.Merchant
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.inventory.Merchant <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/inventory/Merchant.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Merchant(self, **named)
   :canonical: pycraft.server.final.Merchant

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getRecipe(self, _0:int) -> :py:class:`MerchantRecipe`
      :async:


   .. py:method:: getRecipeCount(self) -> int
      :async:


   .. py:method:: getRecipes(self) -> typing.List[:py:class:`MerchantRecipe`]
      :async:


   .. py:method:: getTrader(self) -> :py:class:`HumanEntity`
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isTrading(self) -> bool
      :async:


   .. py:method:: setRecipe(self, _0:int, _1:MerchantRecipe) -> None
      :async:


   .. py:method:: setRecipes(self, _0:List) -> None
      :async:

