.. currentmodule:: pycraft.server.final

MerchantRecipe
==============

Inheritance
------------
* pycraft.server.final.MerchantRecipe
* :py:class:`pycraft.server.final.Recipe`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.inventory.MerchantRecipe <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/inventory/MerchantRecipe.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: MerchantRecipe(self, **named)
   :canonical: pycraft.server.final.MerchantRecipe

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: addIngredient(self, _0:ItemStack) -> None
      :async:


   .. py:method:: adjust(self, _0:ItemStack) -> None
      :async:


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getAdjustedIngredient1(self) -> :py:class:`ItemStack`
      :async:


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getDemand(self) -> int
      :async:


   .. py:method:: getIngredients(self) -> typing.List[:py:class:`ItemStack`]
      :async:


   .. py:method:: getMaxUses(self) -> int
      :async:


   .. py:method:: getPriceMultiplier(self) -> float
      :async:


   .. py:method:: getResult(self) -> :py:class:`ItemStack`
      :async:


   .. py:method:: getSpecialPrice(self) -> int
      :async:


   .. py:method:: getUses(self) -> int
      :async:


   .. py:method:: getVillagerExperience(self) -> int
      :async:


   .. py:method:: hasExperienceReward(self) -> bool
      :async:


   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: removeIngredient(self, _0:int) -> None
      :async:


   .. py:method:: setDemand(self, _0:int) -> None
      :async:


   .. py:method:: setExperienceReward(self, _0:boolean) -> None
      :async:


   .. py:method:: setIgnoreDiscounts(self, _0:boolean) -> None
      :async:


   .. py:method:: setIngredients(self, _0:List) -> None
      :async:


   .. py:method:: setMaxUses(self, _0:int) -> None
      :async:


   .. py:method:: setPriceMultiplier(self, _0:float) -> None
      :async:


   .. py:method:: setSpecialPrice(self, _0:int) -> None
      :async:


   .. py:method:: setUses(self, _0:int) -> None
      :async:


   .. py:method:: setVillagerExperience(self, _0:int) -> None
      :async:


   .. py:method:: shouldIgnoreDiscounts(self) -> bool
      :async:


   .. py:method:: toString(self) -> str
      :async:

