.. currentmodule:: pycraft.server.final

ItemFactory
===========

Inheritance
------------
* pycraft.server.final.ItemFactory
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.inventory.ItemFactory <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/inventory/ItemFactory.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: ItemFactory(self, **named)
   :canonical: pycraft.server.final.ItemFactory

   Object reference on the server which we are proxying

   .. py:method:: __init__(self, **named)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: asHoverEvent(self, _0:ItemStack, _1:UnaryOperator) -> :py:class:`HoverEvent`
      :async:


   .. py:method:: asMetaFor

       .. py:method:: asMetaFor(self, _0:ItemMeta, _1:Material) -> :py:class:`ItemMeta`
          :async:
          :noindex:

       .. py:method:: asMetaFor(self, _0:ItemMeta, _1:ItemStack) -> :py:class:`ItemMeta`
          :async:
          :noindex:


   .. py:method:: createItemStack(self, _0:String) -> :py:class:`ItemStack`
      :async:


   .. py:method:: displayName(self, _0:ItemStack) -> :py:class:`Component`
      :async:


   .. py:method:: enchantWithLevels(self, _0:ItemStack, _1:int, _2:boolean, _3:Random) -> :py:class:`ItemStack`
      :async:


   .. py:method:: ensureServerConversions(self, _0:ItemStack) -> :py:class:`ItemStack`
      :async:


   .. py:method:: equals(self, _0:ItemMeta, _1:ItemMeta) -> bool
      :async:


   .. py:method:: from_server(struct)
      

      Convert server-side structure to local object


   .. py:method:: getDefaultLeatherColor(self) -> :py:class:`Color`
      :async:


   .. py:method:: getI18NDisplayName(self, _0:ItemStack) -> str
      :async:


   .. py:method:: getItemMeta(self, _0:Material) -> :py:class:`ItemMeta`
      :async:


   .. py:method:: getSpawnEgg(self, _0:EntityType) -> :py:class:`ItemStack`
      :async:


   .. py:method:: hoverContentOf

       .. py:method:: hoverContentOf(self, _0:ItemStack) -> :py:class:`Content`
          :async:
          :noindex:

       .. py:method:: hoverContentOf(self, _0:Entity) -> :py:class:`Content`
          :async:
          :noindex:

       .. py:method:: hoverContentOf(self, _0:Entity, _1:BaseComponent[]) -> :py:class:`Content`
          :async:
          :noindex:

       .. py:method:: hoverContentOf(self, _0:Entity, _1:BaseComponent) -> :py:class:`Content`
          :async:
          :noindex:

       .. py:method:: hoverContentOf(self, _0:Entity, _1:String) -> :py:class:`Content`
          :async:
          :noindex:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isApplicable

       .. py:method:: isApplicable(self, _0:ItemMeta, _1:ItemStack) -> bool
          :async:
          :noindex:

       .. py:method:: isApplicable(self, _0:ItemMeta, _1:Material) -> bool
          :async:
          :noindex:


   .. py:method:: updateMaterial(self, _0:ItemMeta, _1:Material) -> :py:class:`Material`
      :async:

