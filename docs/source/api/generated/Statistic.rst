.. currentmodule:: pycraft.server.final

Statistic
=========

Inheritance
------------
* pycraft.server.final.Statistic
* :py:class:`pycraft.server.world.Statistic`
* :py:class:`pycraft.server.proxyobjects.KeyedServerObjectEnum`
* :py:class:`pycraft.server.proxyobjects.ServerObjectEnum`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.Statistic <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Statistic.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Statistic(self, key)
   :canonical: pycraft.server.final.Statistic

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


   .. py:method:: from_server(key)
      

      Convert server-side structure to local object


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getDeclaringClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getKey(self) -> :py:class:`NamespacedKey`
      :async:


   .. py:method:: getType(self) -> :py:class:`Type`
      :async:


   .. py:method:: get_key(self)
      

   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isBlock(self) -> bool
      :async:


   .. py:method:: isSubstatistic(self) -> bool
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


   .. py:method:: valueOf

       .. py:method:: valueOf(cls, _0:String) -> :py:class:`Statistic`
          :async:
          :classmethod:
          :noindex:

       .. py:method:: valueOf(cls, _0:Class, _1:String) -> :py:class:`Enum`
          :async:
          :classmethod:
          :noindex:


   .. py:method:: values(cls) -> typing.List[:py:class:`Statistic`]
      :async:
      :classmethod:


Values
-------

* minecraft:damage_dealt
* minecraft:damage_taken
* minecraft:deaths
* minecraft:mob_kills
* minecraft:player_kills
* minecraft:fish_caught
* minecraft:animals_bred
* minecraft:leave_game
* minecraft:jump
* minecraft:drop_count
* minecraft:drop
* minecraft:pickup
* minecraft:play_one_minute
* minecraft:total_world_time
* minecraft:walk_one_cm
* minecraft:walk_on_water_one_cm
* minecraft:fall_one_cm
* minecraft:sneak_time
* minecraft:climb_one_cm
* minecraft:fly_one_cm
* minecraft:walk_under_water_one_cm
* minecraft:minecart_one_cm
* minecraft:boat_one_cm
* minecraft:pig_one_cm
* minecraft:horse_one_cm
* minecraft:sprint_one_cm
* minecraft:crouch_one_cm
* minecraft:aviate_one_cm
* minecraft:mine_block
* minecraft:use_item
* minecraft:break_item
* minecraft:craft_item
* minecraft:kill_entity
* minecraft:entity_killed_by
* minecraft:time_since_death
* minecraft:talked_to_villager
* minecraft:traded_with_villager
* minecraft:cake_slices_eaten
* minecraft:cauldron_filled
* minecraft:cauldron_used
* minecraft:armor_cleaned
* minecraft:banner_cleaned
* minecraft:brewingstand_interaction
* minecraft:beacon_interaction
* minecraft:dropper_inspected
* minecraft:hopper_inspected
* minecraft:dispenser_inspected
* minecraft:noteblock_played
* minecraft:noteblock_tuned
* minecraft:flower_potted
* minecraft:trapped_chest_triggered
* minecraft:enderchest_opened
* minecraft:item_enchanted
* minecraft:record_played
* minecraft:furnace_interaction
* minecraft:crafting_table_interaction
* minecraft:chest_opened
* minecraft:sleep_in_bed
* minecraft:shulker_box_opened
* minecraft:time_since_rest
* minecraft:swim_one_cm
* minecraft:damage_dealt_absorbed
* minecraft:damage_dealt_resisted
* minecraft:damage_blocked_by_shield
* minecraft:damage_absorbed
* minecraft:damage_resisted
* minecraft:clean_shulker_box
* minecraft:open_barrel
* minecraft:interact_with_blast_furnace
* minecraft:interact_with_smoker
* minecraft:interact_with_lectern
* minecraft:interact_with_campfire
* minecraft:interact_with_cartography_table
* minecraft:interact_with_loom
* minecraft:interact_with_stonecutter
* minecraft:bell_ring
* minecraft:raid_trigger
* minecraft:raid_win
* minecraft:interact_with_anvil
* minecraft:interact_with_grindstone
* minecraft:target_hit
* minecraft:interact_with_smithing_table
* minecraft:strider_one_cm
