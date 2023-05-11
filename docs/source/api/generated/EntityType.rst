.. currentmodule:: pycraft.server.final

EntityType
==========

Inheritance
------------
* pycraft.server.final.EntityType
* :py:class:`pycraft.server.world.EntityType`
* :py:class:`pycraft.server.proxyobjects.KeyedServerObjectEnum`
* :py:class:`pycraft.server.proxyobjects.ServerObjectEnum`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.entity.EntityType <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/entity/EntityType.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: EntityType(self, key)
   :canonical: pycraft.server.final.EntityType

   Namespaced/keyed enumerations

   .. py:method:: __init__(self, key)
      

      Set each named key/value as an attribute on object


   .. py:method:: __str__(self)
      

      Return str(self).


   .. py:method:: cached_values()
      :async:

      Get the cached values for the given enumeration


   .. py:method:: compareTo

       .. py:method:: compareTo(self, _0:Object) -> int
          :async:
          :noindex:

       .. py:method:: compareTo(self, _0:Enum) -> int
          :async:
          :noindex:


   .. py:method:: describeConstable(self) -> :py:class:`Optional`
      :async:


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: fromId(cls, _0:int) -> :py:class:`EntityType`
      :async:
      :classmethod:


   .. py:method:: fromName(cls, _0:String) -> :py:class:`EntityType`
      :async:
      :classmethod:


   .. py:method:: from_server(key)
      

      Convert server-side structure to local object


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getDeclaringClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getDefaultAttributes(self) -> :py:class:`Attributable`
      :async:


   .. py:method:: getEntityClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getKey(self) -> :py:class:`NamespacedKey`
      :async:


   .. py:method:: getName(self) -> str
      :async:


   .. py:method:: getTranslationKey(self) -> str
      :async:


   .. py:method:: getTypeId(self) -> :py:class:`short`
      :async:


   .. py:method:: get_key(self)
      

   .. py:method:: hasDefaultAttributes(self) -> bool
      :async:


   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isAlive(self) -> bool
      :async:


   .. py:method:: isSpawnable(self) -> bool
      :async:


   .. py:method:: key(self) -> :py:class:`Key`
      :async:


   .. py:method:: loosely_match(name)
      :async:

   .. py:method:: name(self) -> str
      :async:


   .. py:method:: notify(self) -> None
      :async:


   .. py:method:: notifyAll(self) -> None
      :async:


   .. py:method:: ordinal(self) -> int
      :async:


   .. py:method:: toString(self) -> str
      :async:


   .. py:method:: translationKey(self) -> str
      :async:


   .. py:method:: valueOf

       .. py:method:: valueOf(cls, _0:String) -> :py:class:`EntityType`
          :async:
          :classmethod:
          :noindex:

       .. py:method:: valueOf(cls, _0:Class, _1:String) -> :py:class:`Enum`
          :async:
          :classmethod:
          :noindex:


   .. py:method:: values(cls) -> typing.List[:py:class:`EntityType`]
      :async:
      :classmethod:


Values
-------

* minecraft:item
* minecraft:experience_orb
* minecraft:area_effect_cloud
* minecraft:elder_guardian
* minecraft:wither_skeleton
* minecraft:stray
* minecraft:egg
* minecraft:leash_knot
* minecraft:painting
* minecraft:arrow
* minecraft:snowball
* minecraft:fireball
* minecraft:small_fireball
* minecraft:ender_pearl
* minecraft:eye_of_ender
* minecraft:potion
* minecraft:experience_bottle
* minecraft:item_frame
* minecraft:wither_skull
* minecraft:tnt
* minecraft:falling_block
* minecraft:firework_rocket
* minecraft:husk
* minecraft:spectral_arrow
* minecraft:shulker_bullet
* minecraft:dragon_fireball
* minecraft:zombie_villager
* minecraft:skeleton_horse
* minecraft:zombie_horse
* minecraft:armor_stand
* minecraft:donkey
* minecraft:mule
* minecraft:evoker_fangs
* minecraft:evoker
* minecraft:vex
* minecraft:vindicator
* minecraft:illusioner
* minecraft:command_block_minecart
* minecraft:boat
* minecraft:minecart
* minecraft:chest_minecart
* minecraft:furnace_minecart
* minecraft:tnt_minecart
* minecraft:hopper_minecart
* minecraft:spawner_minecart
* minecraft:creeper
* minecraft:skeleton
* minecraft:spider
* minecraft:giant
* minecraft:zombie
* minecraft:slime
* minecraft:ghast
* minecraft:zombified_piglin
* minecraft:enderman
* minecraft:cave_spider
* minecraft:silverfish
* minecraft:blaze
* minecraft:magma_cube
* minecraft:ender_dragon
* minecraft:wither
* minecraft:bat
* minecraft:witch
* minecraft:endermite
* minecraft:guardian
* minecraft:shulker
* minecraft:pig
* minecraft:sheep
* minecraft:cow
* minecraft:chicken
* minecraft:squid
* minecraft:wolf
* minecraft:mooshroom
* minecraft:snow_golem
* minecraft:ocelot
* minecraft:iron_golem
* minecraft:horse
* minecraft:rabbit
* minecraft:polar_bear
* minecraft:llama
* minecraft:llama_spit
* minecraft:parrot
* minecraft:villager
* minecraft:end_crystal
* minecraft:turtle
* minecraft:phantom
* minecraft:trident
* minecraft:cod
* minecraft:salmon
* minecraft:pufferfish
* minecraft:tropical_fish
* minecraft:drowned
* minecraft:dolphin
* minecraft:cat
* minecraft:panda
* minecraft:pillager
* minecraft:ravager
* minecraft:trader_llama
* minecraft:wandering_trader
* minecraft:fox
* minecraft:bee
* minecraft:hoglin
* minecraft:piglin
* minecraft:strider
* minecraft:zoglin
* minecraft:piglin_brute
* minecraft:axolotl
* minecraft:glow_item_frame
* minecraft:glow_squid
* minecraft:goat
* minecraft:marker
* minecraft:allay
* minecraft:chest_boat
* minecraft:frog
* minecraft:tadpole
* minecraft:warden
* minecraft:camel
* minecraft:block_display
* minecraft:interaction
* minecraft:item_display
* minecraft:sniffer
* minecraft:text_display
* minecraft:fishing_bobber
* minecraft:lightning_bolt
* minecraft:player
* minecraft:UNKNOWN
