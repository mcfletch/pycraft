.. currentmodule:: pycraft.server.final

Material
========

Inheritance
------------
* pycraft.server.final.Material
* :py:class:`pycraft.server.world.Material`
* :py:class:`pycraft.server.proxyobjects.KeyedServerObjectEnum`
* :py:class:`pycraft.server.proxyobjects.ServerObjectEnum`
* :py:class:`pycraft.server.proxyobjects.ServerObjectProxy`

Python Proxy to `org.bukkit.Material <https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Material.html>`_ from :py:mod:`pycraft.server.final`

.. py:class:: Material(self, key)
   :canonical: pycraft.server.final.Material

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


   .. py:method:: createBlockData

       .. py:method:: createBlockData(self) -> :py:class:`BlockData`
          :async:
          :noindex:

       .. py:method:: createBlockData(self, _0:String) -> :py:class:`BlockData`
          :async:
          :noindex:

       .. py:method:: createBlockData(self, _0:Consumer) -> :py:class:`BlockData`
          :async:
          :noindex:


   .. py:method:: describeConstable(self) -> :py:class:`Optional`
      :async:


   .. py:method:: equals(self, _0:Object) -> bool
      :async:


   .. py:method:: from_server(key)
      

      Convert server-side structure to local object


   .. py:method:: getBlastResistance(self) -> float
      :async:


   .. py:method:: getBlockTranslationKey(self) -> str
      :async:


   .. py:method:: getClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getCraftingRemainingItem(self) -> :py:class:`Material`
      :async:


   .. py:method:: getCreativeCategory(self) -> :py:class:`CreativeCategory`
      :async:


   .. py:method:: getData(self) -> :py:class:`Class`
      :async:


   .. py:method:: getDeclaringClass(self) -> :py:class:`Class`
      :async:


   .. py:method:: getDefaultAttributeModifiers(self, _0:EquipmentSlot) -> :py:class:`Multimap`
      :async:


   .. py:method:: getEquipmentSlot(self) -> :py:class:`EquipmentSlot`
      :async:


   .. py:method:: getHardness(self) -> float
      :async:


   .. py:method:: getId(self) -> int
      :async:


   .. py:method:: getItemAttributes(self, _0:EquipmentSlot) -> :py:class:`Multimap`
      :async:


   .. py:method:: getItemRarity(self) -> :py:class:`ItemRarity`
      :async:


   .. py:method:: getItemTranslationKey(self) -> str
      :async:


   .. py:method:: getKey(self) -> :py:class:`NamespacedKey`
      :async:


   .. py:method:: getMaterial

       .. py:method:: getMaterial(cls, _0:String) -> :py:class:`Material`
          :async:
          :classmethod:
          :noindex:

       .. py:method:: getMaterial(cls, _0:String, _1:boolean) -> :py:class:`Material`
          :async:
          :classmethod:
          :noindex:


   .. py:method:: getMaxDurability(self) -> :py:class:`short`
      :async:


   .. py:method:: getMaxStackSize(self) -> int
      :async:


   .. py:method:: getNewData(self, _0:byte) -> :py:class:`MaterialData`
      :async:


   .. py:method:: getSlipperiness(self) -> float
      :async:


   .. py:method:: getTranslationKey(self) -> str
      :async:


   .. py:method:: get_key(self)
      

   .. py:method:: hasGravity(self) -> bool
      :async:


   .. py:method:: hashCode(self) -> int
      :async:


   .. py:method:: inject_methods(channel, method_descriptions)
      

      Inject the methods the server reports are available for this namespace


   .. py:method:: isAir(self) -> bool
      :async:


   .. py:method:: isBlock(self) -> bool
      :async:


   .. py:method:: isBurnable(self) -> bool
      :async:


   .. py:method:: isCollidable(self) -> bool
      :async:


   .. py:method:: isEdible(self) -> bool
      :async:


   .. py:method:: isEmpty(self) -> bool
      :async:


   .. py:method:: isFlammable(self) -> bool
      :async:


   .. py:method:: isFuel(self) -> bool
      :async:


   .. py:method:: isInteractable(self) -> bool
      :async:


   .. py:method:: isItem(self) -> bool
      :async:


   .. py:method:: isLegacy(self) -> bool
      :async:


   .. py:method:: isOccluding(self) -> bool
      :async:


   .. py:method:: isRecord(self) -> bool
      :async:


   .. py:method:: isSolid(self) -> bool
      :async:


   .. py:method:: isTransparent(self) -> bool
      :async:


   .. py:method:: key(self) -> :py:class:`Key`
      :async:


   .. py:method:: loosely_match(name)
      :async:

   .. py:method:: matchMaterial

       .. py:method:: matchMaterial(cls, _0:String) -> :py:class:`Material`
          :async:
          :classmethod:
          :noindex:

       .. py:method:: matchMaterial(cls, _0:String, _1:boolean) -> :py:class:`Material`
          :async:
          :classmethod:
          :noindex:


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

       .. py:method:: valueOf(cls, _0:String) -> :py:class:`Material`
          :async:
          :classmethod:
          :noindex:

       .. py:method:: valueOf(cls, _0:Class, _1:String) -> :py:class:`Enum`
          :async:
          :classmethod:
          :noindex:


   .. py:method:: values(cls) -> typing.List[:py:class:`Material`]
      :async:
      :classmethod:


Values
-------

* minecraft:air
* minecraft:stone
* minecraft:granite
* minecraft:polished_granite
* minecraft:diorite
* minecraft:polished_diorite
* minecraft:andesite
* minecraft:polished_andesite
* minecraft:deepslate
* minecraft:cobbled_deepslate
* minecraft:polished_deepslate
* minecraft:calcite
* minecraft:tuff
* minecraft:dripstone_block
* minecraft:grass_block
* minecraft:dirt
* minecraft:coarse_dirt
* minecraft:podzol
* minecraft:rooted_dirt
* minecraft:mud
* minecraft:crimson_nylium
* minecraft:warped_nylium
* minecraft:cobblestone
* minecraft:oak_planks
* minecraft:spruce_planks
* minecraft:birch_planks
* minecraft:jungle_planks
* minecraft:acacia_planks
* minecraft:cherry_planks
* minecraft:dark_oak_planks
* minecraft:mangrove_planks
* minecraft:bamboo_planks
* minecraft:crimson_planks
* minecraft:warped_planks
* minecraft:bamboo_mosaic
* minecraft:oak_sapling
* minecraft:spruce_sapling
* minecraft:birch_sapling
* minecraft:jungle_sapling
* minecraft:acacia_sapling
* minecraft:cherry_sapling
* minecraft:dark_oak_sapling
* minecraft:mangrove_propagule
* minecraft:bedrock
* minecraft:sand
* minecraft:suspicious_sand
* minecraft:red_sand
* minecraft:gravel
* minecraft:coal_ore
* minecraft:deepslate_coal_ore
* minecraft:iron_ore
* minecraft:deepslate_iron_ore
* minecraft:copper_ore
* minecraft:deepslate_copper_ore
* minecraft:gold_ore
* minecraft:deepslate_gold_ore
* minecraft:redstone_ore
* minecraft:deepslate_redstone_ore
* minecraft:emerald_ore
* minecraft:deepslate_emerald_ore
* minecraft:lapis_ore
* minecraft:deepslate_lapis_ore
* minecraft:diamond_ore
* minecraft:deepslate_diamond_ore
* minecraft:nether_gold_ore
* minecraft:nether_quartz_ore
* minecraft:ancient_debris
* minecraft:coal_block
* minecraft:raw_iron_block
* minecraft:raw_copper_block
* minecraft:raw_gold_block
* minecraft:amethyst_block
* minecraft:budding_amethyst
* minecraft:iron_block
* minecraft:copper_block
* minecraft:gold_block
* minecraft:diamond_block
* minecraft:netherite_block
* minecraft:exposed_copper
* minecraft:weathered_copper
* minecraft:oxidized_copper
* minecraft:cut_copper
* minecraft:exposed_cut_copper
* minecraft:weathered_cut_copper
* minecraft:oxidized_cut_copper
* minecraft:cut_copper_stairs
* minecraft:exposed_cut_copper_stairs
* minecraft:weathered_cut_copper_stairs
* minecraft:oxidized_cut_copper_stairs
* minecraft:cut_copper_slab
* minecraft:exposed_cut_copper_slab
* minecraft:weathered_cut_copper_slab
* minecraft:oxidized_cut_copper_slab
* minecraft:waxed_copper_block
* minecraft:waxed_exposed_copper
* minecraft:waxed_weathered_copper
* minecraft:waxed_oxidized_copper
* minecraft:waxed_cut_copper
* minecraft:waxed_exposed_cut_copper
* minecraft:waxed_weathered_cut_copper
* minecraft:waxed_oxidized_cut_copper
* minecraft:waxed_cut_copper_stairs
* minecraft:waxed_exposed_cut_copper_stairs
* minecraft:waxed_weathered_cut_copper_stairs
* minecraft:waxed_oxidized_cut_copper_stairs
* minecraft:waxed_cut_copper_slab
* minecraft:waxed_exposed_cut_copper_slab
* minecraft:waxed_weathered_cut_copper_slab
* minecraft:waxed_oxidized_cut_copper_slab
* minecraft:oak_log
* minecraft:spruce_log
* minecraft:birch_log
* minecraft:jungle_log
* minecraft:acacia_log
* minecraft:cherry_log
* minecraft:dark_oak_log
* minecraft:mangrove_log
* minecraft:mangrove_roots
* minecraft:muddy_mangrove_roots
* minecraft:crimson_stem
* minecraft:warped_stem
* minecraft:bamboo_block
* minecraft:stripped_oak_log
* minecraft:stripped_spruce_log
* minecraft:stripped_birch_log
* minecraft:stripped_jungle_log
* minecraft:stripped_acacia_log
* minecraft:stripped_cherry_log
* minecraft:stripped_dark_oak_log
* minecraft:stripped_mangrove_log
* minecraft:stripped_crimson_stem
* minecraft:stripped_warped_stem
* minecraft:stripped_oak_wood
* minecraft:stripped_spruce_wood
* minecraft:stripped_birch_wood
* minecraft:stripped_jungle_wood
* minecraft:stripped_acacia_wood
* minecraft:stripped_cherry_wood
* minecraft:stripped_dark_oak_wood
* minecraft:stripped_mangrove_wood
* minecraft:stripped_crimson_hyphae
* minecraft:stripped_warped_hyphae
* minecraft:stripped_bamboo_block
* minecraft:oak_wood
* minecraft:spruce_wood
* minecraft:birch_wood
* minecraft:jungle_wood
* minecraft:acacia_wood
* minecraft:cherry_wood
* minecraft:dark_oak_wood
* minecraft:mangrove_wood
* minecraft:crimson_hyphae
* minecraft:warped_hyphae
* minecraft:oak_leaves
* minecraft:spruce_leaves
* minecraft:birch_leaves
* minecraft:jungle_leaves
* minecraft:acacia_leaves
* minecraft:cherry_leaves
* minecraft:dark_oak_leaves
* minecraft:mangrove_leaves
* minecraft:azalea_leaves
* minecraft:flowering_azalea_leaves
* minecraft:sponge
* minecraft:wet_sponge
* minecraft:glass
* minecraft:tinted_glass
* minecraft:lapis_block
* minecraft:sandstone
* minecraft:chiseled_sandstone
* minecraft:cut_sandstone
* minecraft:cobweb
* minecraft:grass
* minecraft:fern
* minecraft:azalea
* minecraft:flowering_azalea
* minecraft:dead_bush
* minecraft:seagrass
* minecraft:sea_pickle
* minecraft:white_wool
* minecraft:orange_wool
* minecraft:magenta_wool
* minecraft:light_blue_wool
* minecraft:yellow_wool
* minecraft:lime_wool
* minecraft:pink_wool
* minecraft:gray_wool
* minecraft:light_gray_wool
* minecraft:cyan_wool
* minecraft:purple_wool
* minecraft:blue_wool
* minecraft:brown_wool
* minecraft:green_wool
* minecraft:red_wool
* minecraft:black_wool
* minecraft:dandelion
* minecraft:poppy
* minecraft:blue_orchid
* minecraft:allium
* minecraft:azure_bluet
* minecraft:red_tulip
* minecraft:orange_tulip
* minecraft:white_tulip
* minecraft:pink_tulip
* minecraft:oxeye_daisy
* minecraft:cornflower
* minecraft:lily_of_the_valley
* minecraft:wither_rose
* minecraft:torchflower
* minecraft:spore_blossom
* minecraft:brown_mushroom
* minecraft:red_mushroom
* minecraft:crimson_fungus
* minecraft:warped_fungus
* minecraft:crimson_roots
* minecraft:warped_roots
* minecraft:nether_sprouts
* minecraft:weeping_vines
* minecraft:twisting_vines
* minecraft:sugar_cane
* minecraft:kelp
* minecraft:moss_carpet
* minecraft:pink_petals
* minecraft:moss_block
* minecraft:hanging_roots
* minecraft:big_dripleaf
* minecraft:small_dripleaf
* minecraft:bamboo
* minecraft:oak_slab
* minecraft:spruce_slab
* minecraft:birch_slab
* minecraft:jungle_slab
* minecraft:acacia_slab
* minecraft:cherry_slab
* minecraft:dark_oak_slab
* minecraft:mangrove_slab
* minecraft:bamboo_slab
* minecraft:bamboo_mosaic_slab
* minecraft:crimson_slab
* minecraft:warped_slab
* minecraft:stone_slab
* minecraft:smooth_stone_slab
* minecraft:sandstone_slab
* minecraft:cut_sandstone_slab
* minecraft:petrified_oak_slab
* minecraft:cobblestone_slab
* minecraft:brick_slab
* minecraft:stone_brick_slab
* minecraft:mud_brick_slab
* minecraft:nether_brick_slab
* minecraft:quartz_slab
* minecraft:red_sandstone_slab
* minecraft:cut_red_sandstone_slab
* minecraft:purpur_slab
* minecraft:prismarine_slab
* minecraft:prismarine_brick_slab
* minecraft:dark_prismarine_slab
* minecraft:smooth_quartz
* minecraft:smooth_red_sandstone
* minecraft:smooth_sandstone
* minecraft:smooth_stone
* minecraft:bricks
* minecraft:bookshelf
* minecraft:chiseled_bookshelf
* minecraft:decorated_pot
* minecraft:mossy_cobblestone
* minecraft:obsidian
* minecraft:torch
* minecraft:end_rod
* minecraft:chorus_plant
* minecraft:chorus_flower
* minecraft:purpur_block
* minecraft:purpur_pillar
* minecraft:purpur_stairs
* minecraft:spawner
* minecraft:chest
* minecraft:crafting_table
* minecraft:farmland
* minecraft:furnace
* minecraft:ladder
* minecraft:cobblestone_stairs
* minecraft:snow
* minecraft:ice
* minecraft:snow_block
* minecraft:cactus
* minecraft:clay
* minecraft:jukebox
* minecraft:oak_fence
* minecraft:spruce_fence
* minecraft:birch_fence
* minecraft:jungle_fence
* minecraft:acacia_fence
* minecraft:cherry_fence
* minecraft:dark_oak_fence
* minecraft:mangrove_fence
* minecraft:bamboo_fence
* minecraft:crimson_fence
* minecraft:warped_fence
* minecraft:pumpkin
* minecraft:carved_pumpkin
* minecraft:jack_o_lantern
* minecraft:netherrack
* minecraft:soul_sand
* minecraft:soul_soil
* minecraft:basalt
* minecraft:polished_basalt
* minecraft:smooth_basalt
* minecraft:soul_torch
* minecraft:glowstone
* minecraft:infested_stone
* minecraft:infested_cobblestone
* minecraft:infested_stone_bricks
* minecraft:infested_mossy_stone_bricks
* minecraft:infested_cracked_stone_bricks
* minecraft:infested_chiseled_stone_bricks
* minecraft:infested_deepslate
* minecraft:stone_bricks
* minecraft:mossy_stone_bricks
* minecraft:cracked_stone_bricks
* minecraft:chiseled_stone_bricks
* minecraft:packed_mud
* minecraft:mud_bricks
* minecraft:deepslate_bricks
* minecraft:cracked_deepslate_bricks
* minecraft:deepslate_tiles
* minecraft:cracked_deepslate_tiles
* minecraft:chiseled_deepslate
* minecraft:reinforced_deepslate
* minecraft:brown_mushroom_block
* minecraft:red_mushroom_block
* minecraft:mushroom_stem
* minecraft:iron_bars
* minecraft:chain
* minecraft:glass_pane
* minecraft:melon
* minecraft:vine
* minecraft:glow_lichen
* minecraft:brick_stairs
* minecraft:stone_brick_stairs
* minecraft:mud_brick_stairs
* minecraft:mycelium
* minecraft:lily_pad
* minecraft:nether_bricks
* minecraft:cracked_nether_bricks
* minecraft:chiseled_nether_bricks
* minecraft:nether_brick_fence
* minecraft:nether_brick_stairs
* minecraft:sculk
* minecraft:sculk_vein
* minecraft:sculk_catalyst
* minecraft:sculk_shrieker
* minecraft:enchanting_table
* minecraft:end_portal_frame
* minecraft:end_stone
* minecraft:end_stone_bricks
* minecraft:dragon_egg
* minecraft:sandstone_stairs
* minecraft:ender_chest
* minecraft:emerald_block
* minecraft:oak_stairs
* minecraft:spruce_stairs
* minecraft:birch_stairs
* minecraft:jungle_stairs
* minecraft:acacia_stairs
* minecraft:cherry_stairs
* minecraft:dark_oak_stairs
* minecraft:mangrove_stairs
* minecraft:bamboo_stairs
* minecraft:bamboo_mosaic_stairs
* minecraft:crimson_stairs
* minecraft:warped_stairs
* minecraft:command_block
* minecraft:beacon
* minecraft:cobblestone_wall
* minecraft:mossy_cobblestone_wall
* minecraft:brick_wall
* minecraft:prismarine_wall
* minecraft:red_sandstone_wall
* minecraft:mossy_stone_brick_wall
* minecraft:granite_wall
* minecraft:stone_brick_wall
* minecraft:mud_brick_wall
* minecraft:nether_brick_wall
* minecraft:andesite_wall
* minecraft:red_nether_brick_wall
* minecraft:sandstone_wall
* minecraft:end_stone_brick_wall
* minecraft:diorite_wall
* minecraft:blackstone_wall
* minecraft:polished_blackstone_wall
* minecraft:polished_blackstone_brick_wall
* minecraft:cobbled_deepslate_wall
* minecraft:polished_deepslate_wall
* minecraft:deepslate_brick_wall
* minecraft:deepslate_tile_wall
* minecraft:anvil
* minecraft:chipped_anvil
* minecraft:damaged_anvil
* minecraft:chiseled_quartz_block
* minecraft:quartz_block
* minecraft:quartz_bricks
* minecraft:quartz_pillar
* minecraft:quartz_stairs
* minecraft:white_terracotta
* minecraft:orange_terracotta
* minecraft:magenta_terracotta
* minecraft:light_blue_terracotta
* minecraft:yellow_terracotta
* minecraft:lime_terracotta
* minecraft:pink_terracotta
* minecraft:gray_terracotta
* minecraft:light_gray_terracotta
* minecraft:cyan_terracotta
* minecraft:purple_terracotta
* minecraft:blue_terracotta
* minecraft:brown_terracotta
* minecraft:green_terracotta
* minecraft:red_terracotta
* minecraft:black_terracotta
* minecraft:barrier
* minecraft:light
* minecraft:hay_block
* minecraft:white_carpet
* minecraft:orange_carpet
* minecraft:magenta_carpet
* minecraft:light_blue_carpet
* minecraft:yellow_carpet
* minecraft:lime_carpet
* minecraft:pink_carpet
* minecraft:gray_carpet
* minecraft:light_gray_carpet
* minecraft:cyan_carpet
* minecraft:purple_carpet
* minecraft:blue_carpet
* minecraft:brown_carpet
* minecraft:green_carpet
* minecraft:red_carpet
* minecraft:black_carpet
* minecraft:terracotta
* minecraft:packed_ice
* minecraft:dirt_path
* minecraft:sunflower
* minecraft:lilac
* minecraft:rose_bush
* minecraft:peony
* minecraft:tall_grass
* minecraft:large_fern
* minecraft:white_stained_glass
* minecraft:orange_stained_glass
* minecraft:magenta_stained_glass
* minecraft:light_blue_stained_glass
* minecraft:yellow_stained_glass
* minecraft:lime_stained_glass
* minecraft:pink_stained_glass
* minecraft:gray_stained_glass
* minecraft:light_gray_stained_glass
* minecraft:cyan_stained_glass
* minecraft:purple_stained_glass
* minecraft:blue_stained_glass
* minecraft:brown_stained_glass
* minecraft:green_stained_glass
* minecraft:red_stained_glass
* minecraft:black_stained_glass
* minecraft:white_stained_glass_pane
* minecraft:orange_stained_glass_pane
* minecraft:magenta_stained_glass_pane
* minecraft:light_blue_stained_glass_pane
* minecraft:yellow_stained_glass_pane
* minecraft:lime_stained_glass_pane
* minecraft:pink_stained_glass_pane
* minecraft:gray_stained_glass_pane
* minecraft:light_gray_stained_glass_pane
* minecraft:cyan_stained_glass_pane
* minecraft:purple_stained_glass_pane
* minecraft:blue_stained_glass_pane
* minecraft:brown_stained_glass_pane
* minecraft:green_stained_glass_pane
* minecraft:red_stained_glass_pane
* minecraft:black_stained_glass_pane
* minecraft:prismarine
* minecraft:prismarine_bricks
* minecraft:dark_prismarine
* minecraft:prismarine_stairs
* minecraft:prismarine_brick_stairs
* minecraft:dark_prismarine_stairs
* minecraft:sea_lantern
* minecraft:red_sandstone
* minecraft:chiseled_red_sandstone
* minecraft:cut_red_sandstone
* minecraft:red_sandstone_stairs
* minecraft:repeating_command_block
* minecraft:chain_command_block
* minecraft:magma_block
* minecraft:nether_wart_block
* minecraft:warped_wart_block
* minecraft:red_nether_bricks
* minecraft:bone_block
* minecraft:structure_void
* minecraft:shulker_box
* minecraft:white_shulker_box
* minecraft:orange_shulker_box
* minecraft:magenta_shulker_box
* minecraft:light_blue_shulker_box
* minecraft:yellow_shulker_box
* minecraft:lime_shulker_box
* minecraft:pink_shulker_box
* minecraft:gray_shulker_box
* minecraft:light_gray_shulker_box
* minecraft:cyan_shulker_box
* minecraft:purple_shulker_box
* minecraft:blue_shulker_box
* minecraft:brown_shulker_box
* minecraft:green_shulker_box
* minecraft:red_shulker_box
* minecraft:black_shulker_box
* minecraft:white_glazed_terracotta
* minecraft:orange_glazed_terracotta
* minecraft:magenta_glazed_terracotta
* minecraft:light_blue_glazed_terracotta
* minecraft:yellow_glazed_terracotta
* minecraft:lime_glazed_terracotta
* minecraft:pink_glazed_terracotta
* minecraft:gray_glazed_terracotta
* minecraft:light_gray_glazed_terracotta
* minecraft:cyan_glazed_terracotta
* minecraft:purple_glazed_terracotta
* minecraft:blue_glazed_terracotta
* minecraft:brown_glazed_terracotta
* minecraft:green_glazed_terracotta
* minecraft:red_glazed_terracotta
* minecraft:black_glazed_terracotta
* minecraft:white_concrete
* minecraft:orange_concrete
* minecraft:magenta_concrete
* minecraft:light_blue_concrete
* minecraft:yellow_concrete
* minecraft:lime_concrete
* minecraft:pink_concrete
* minecraft:gray_concrete
* minecraft:light_gray_concrete
* minecraft:cyan_concrete
* minecraft:purple_concrete
* minecraft:blue_concrete
* minecraft:brown_concrete
* minecraft:green_concrete
* minecraft:red_concrete
* minecraft:black_concrete
* minecraft:white_concrete_powder
* minecraft:orange_concrete_powder
* minecraft:magenta_concrete_powder
* minecraft:light_blue_concrete_powder
* minecraft:yellow_concrete_powder
* minecraft:lime_concrete_powder
* minecraft:pink_concrete_powder
* minecraft:gray_concrete_powder
* minecraft:light_gray_concrete_powder
* minecraft:cyan_concrete_powder
* minecraft:purple_concrete_powder
* minecraft:blue_concrete_powder
* minecraft:brown_concrete_powder
* minecraft:green_concrete_powder
* minecraft:red_concrete_powder
* minecraft:black_concrete_powder
* minecraft:turtle_egg
* minecraft:dead_tube_coral_block
* minecraft:dead_brain_coral_block
* minecraft:dead_bubble_coral_block
* minecraft:dead_fire_coral_block
* minecraft:dead_horn_coral_block
* minecraft:tube_coral_block
* minecraft:brain_coral_block
* minecraft:bubble_coral_block
* minecraft:fire_coral_block
* minecraft:horn_coral_block
* minecraft:tube_coral
* minecraft:brain_coral
* minecraft:bubble_coral
* minecraft:fire_coral
* minecraft:horn_coral
* minecraft:dead_brain_coral
* minecraft:dead_bubble_coral
* minecraft:dead_fire_coral
* minecraft:dead_horn_coral
* minecraft:dead_tube_coral
* minecraft:tube_coral_fan
* minecraft:brain_coral_fan
* minecraft:bubble_coral_fan
* minecraft:fire_coral_fan
* minecraft:horn_coral_fan
* minecraft:dead_tube_coral_fan
* minecraft:dead_brain_coral_fan
* minecraft:dead_bubble_coral_fan
* minecraft:dead_fire_coral_fan
* minecraft:dead_horn_coral_fan
* minecraft:blue_ice
* minecraft:conduit
* minecraft:polished_granite_stairs
* minecraft:smooth_red_sandstone_stairs
* minecraft:mossy_stone_brick_stairs
* minecraft:polished_diorite_stairs
* minecraft:mossy_cobblestone_stairs
* minecraft:end_stone_brick_stairs
* minecraft:stone_stairs
* minecraft:smooth_sandstone_stairs
* minecraft:smooth_quartz_stairs
* minecraft:granite_stairs
* minecraft:andesite_stairs
* minecraft:red_nether_brick_stairs
* minecraft:polished_andesite_stairs
* minecraft:diorite_stairs
* minecraft:cobbled_deepslate_stairs
* minecraft:polished_deepslate_stairs
* minecraft:deepslate_brick_stairs
* minecraft:deepslate_tile_stairs
* minecraft:polished_granite_slab
* minecraft:smooth_red_sandstone_slab
* minecraft:mossy_stone_brick_slab
* minecraft:polished_diorite_slab
* minecraft:mossy_cobblestone_slab
* minecraft:end_stone_brick_slab
* minecraft:smooth_sandstone_slab
* minecraft:smooth_quartz_slab
* minecraft:granite_slab
* minecraft:andesite_slab
* minecraft:red_nether_brick_slab
* minecraft:polished_andesite_slab
* minecraft:diorite_slab
* minecraft:cobbled_deepslate_slab
* minecraft:polished_deepslate_slab
* minecraft:deepslate_brick_slab
* minecraft:deepslate_tile_slab
* minecraft:scaffolding
* minecraft:redstone
* minecraft:redstone_torch
* minecraft:redstone_block
* minecraft:repeater
* minecraft:comparator
* minecraft:piston
* minecraft:sticky_piston
* minecraft:slime_block
* minecraft:honey_block
* minecraft:observer
* minecraft:hopper
* minecraft:dispenser
* minecraft:dropper
* minecraft:lectern
* minecraft:target
* minecraft:lever
* minecraft:lightning_rod
* minecraft:daylight_detector
* minecraft:sculk_sensor
* minecraft:tripwire_hook
* minecraft:trapped_chest
* minecraft:tnt
* minecraft:redstone_lamp
* minecraft:note_block
* minecraft:stone_button
* minecraft:polished_blackstone_button
* minecraft:oak_button
* minecraft:spruce_button
* minecraft:birch_button
* minecraft:jungle_button
* minecraft:acacia_button
* minecraft:cherry_button
* minecraft:dark_oak_button
* minecraft:mangrove_button
* minecraft:bamboo_button
* minecraft:crimson_button
* minecraft:warped_button
* minecraft:stone_pressure_plate
* minecraft:polished_blackstone_pressure_plate
* minecraft:light_weighted_pressure_plate
* minecraft:heavy_weighted_pressure_plate
* minecraft:oak_pressure_plate
* minecraft:spruce_pressure_plate
* minecraft:birch_pressure_plate
* minecraft:jungle_pressure_plate
* minecraft:acacia_pressure_plate
* minecraft:cherry_pressure_plate
* minecraft:dark_oak_pressure_plate
* minecraft:mangrove_pressure_plate
* minecraft:bamboo_pressure_plate
* minecraft:crimson_pressure_plate
* minecraft:warped_pressure_plate
* minecraft:iron_door
* minecraft:oak_door
* minecraft:spruce_door
* minecraft:birch_door
* minecraft:jungle_door
* minecraft:acacia_door
* minecraft:cherry_door
* minecraft:dark_oak_door
* minecraft:mangrove_door
* minecraft:bamboo_door
* minecraft:crimson_door
* minecraft:warped_door
* minecraft:iron_trapdoor
* minecraft:oak_trapdoor
* minecraft:spruce_trapdoor
* minecraft:birch_trapdoor
* minecraft:jungle_trapdoor
* minecraft:acacia_trapdoor
* minecraft:cherry_trapdoor
* minecraft:dark_oak_trapdoor
* minecraft:mangrove_trapdoor
* minecraft:bamboo_trapdoor
* minecraft:crimson_trapdoor
* minecraft:warped_trapdoor
* minecraft:oak_fence_gate
* minecraft:spruce_fence_gate
* minecraft:birch_fence_gate
* minecraft:jungle_fence_gate
* minecraft:acacia_fence_gate
* minecraft:cherry_fence_gate
* minecraft:dark_oak_fence_gate
* minecraft:mangrove_fence_gate
* minecraft:bamboo_fence_gate
* minecraft:crimson_fence_gate
* minecraft:warped_fence_gate
* minecraft:powered_rail
* minecraft:detector_rail
* minecraft:rail
* minecraft:activator_rail
* minecraft:saddle
* minecraft:minecart
* minecraft:chest_minecart
* minecraft:furnace_minecart
* minecraft:tnt_minecart
* minecraft:hopper_minecart
* minecraft:carrot_on_a_stick
* minecraft:warped_fungus_on_a_stick
* minecraft:elytra
* minecraft:oak_boat
* minecraft:oak_chest_boat
* minecraft:spruce_boat
* minecraft:spruce_chest_boat
* minecraft:birch_boat
* minecraft:birch_chest_boat
* minecraft:jungle_boat
* minecraft:jungle_chest_boat
* minecraft:acacia_boat
* minecraft:acacia_chest_boat
* minecraft:cherry_boat
* minecraft:cherry_chest_boat
* minecraft:dark_oak_boat
* minecraft:dark_oak_chest_boat
* minecraft:mangrove_boat
* minecraft:mangrove_chest_boat
* minecraft:bamboo_raft
* minecraft:bamboo_chest_raft
* minecraft:structure_block
* minecraft:jigsaw
* minecraft:turtle_helmet
* minecraft:scute
* minecraft:flint_and_steel
* minecraft:apple
* minecraft:bow
* minecraft:arrow
* minecraft:coal
* minecraft:charcoal
* minecraft:diamond
* minecraft:emerald
* minecraft:lapis_lazuli
* minecraft:quartz
* minecraft:amethyst_shard
* minecraft:raw_iron
* minecraft:iron_ingot
* minecraft:raw_copper
* minecraft:copper_ingot
* minecraft:raw_gold
* minecraft:gold_ingot
* minecraft:netherite_ingot
* minecraft:netherite_scrap
* minecraft:wooden_sword
* minecraft:wooden_shovel
* minecraft:wooden_pickaxe
* minecraft:wooden_axe
* minecraft:wooden_hoe
* minecraft:stone_sword
* minecraft:stone_shovel
* minecraft:stone_pickaxe
* minecraft:stone_axe
* minecraft:stone_hoe
* minecraft:golden_sword
* minecraft:golden_shovel
* minecraft:golden_pickaxe
* minecraft:golden_axe
* minecraft:golden_hoe
* minecraft:iron_sword
* minecraft:iron_shovel
* minecraft:iron_pickaxe
* minecraft:iron_axe
* minecraft:iron_hoe
* minecraft:diamond_sword
* minecraft:diamond_shovel
* minecraft:diamond_pickaxe
* minecraft:diamond_axe
* minecraft:diamond_hoe
* minecraft:netherite_sword
* minecraft:netherite_shovel
* minecraft:netherite_pickaxe
* minecraft:netherite_axe
* minecraft:netherite_hoe
* minecraft:stick
* minecraft:bowl
* minecraft:mushroom_stew
* minecraft:string
* minecraft:feather
* minecraft:gunpowder
* minecraft:wheat_seeds
* minecraft:wheat
* minecraft:bread
* minecraft:leather_helmet
* minecraft:leather_chestplate
* minecraft:leather_leggings
* minecraft:leather_boots
* minecraft:chainmail_helmet
* minecraft:chainmail_chestplate
* minecraft:chainmail_leggings
* minecraft:chainmail_boots
* minecraft:iron_helmet
* minecraft:iron_chestplate
* minecraft:iron_leggings
* minecraft:iron_boots
* minecraft:diamond_helmet
* minecraft:diamond_chestplate
* minecraft:diamond_leggings
* minecraft:diamond_boots
* minecraft:golden_helmet
* minecraft:golden_chestplate
* minecraft:golden_leggings
* minecraft:golden_boots
* minecraft:netherite_helmet
* minecraft:netherite_chestplate
* minecraft:netherite_leggings
* minecraft:netherite_boots
* minecraft:flint
* minecraft:porkchop
* minecraft:cooked_porkchop
* minecraft:painting
* minecraft:golden_apple
* minecraft:enchanted_golden_apple
* minecraft:oak_sign
* minecraft:spruce_sign
* minecraft:birch_sign
* minecraft:jungle_sign
* minecraft:acacia_sign
* minecraft:cherry_sign
* minecraft:dark_oak_sign
* minecraft:mangrove_sign
* minecraft:bamboo_sign
* minecraft:crimson_sign
* minecraft:warped_sign
* minecraft:oak_hanging_sign
* minecraft:spruce_hanging_sign
* minecraft:birch_hanging_sign
* minecraft:jungle_hanging_sign
* minecraft:acacia_hanging_sign
* minecraft:cherry_hanging_sign
* minecraft:dark_oak_hanging_sign
* minecraft:mangrove_hanging_sign
* minecraft:bamboo_hanging_sign
* minecraft:crimson_hanging_sign
* minecraft:warped_hanging_sign
* minecraft:bucket
* minecraft:water_bucket
* minecraft:lava_bucket
* minecraft:powder_snow_bucket
* minecraft:snowball
* minecraft:leather
* minecraft:milk_bucket
* minecraft:pufferfish_bucket
* minecraft:salmon_bucket
* minecraft:cod_bucket
* minecraft:tropical_fish_bucket
* minecraft:axolotl_bucket
* minecraft:tadpole_bucket
* minecraft:brick
* minecraft:clay_ball
* minecraft:dried_kelp_block
* minecraft:paper
* minecraft:book
* minecraft:slime_ball
* minecraft:egg
* minecraft:compass
* minecraft:recovery_compass
* minecraft:bundle
* minecraft:fishing_rod
* minecraft:clock
* minecraft:spyglass
* minecraft:glowstone_dust
* minecraft:cod
* minecraft:salmon
* minecraft:tropical_fish
* minecraft:pufferfish
* minecraft:cooked_cod
* minecraft:cooked_salmon
* minecraft:ink_sac
* minecraft:glow_ink_sac
* minecraft:cocoa_beans
* minecraft:white_dye
* minecraft:orange_dye
* minecraft:magenta_dye
* minecraft:light_blue_dye
* minecraft:yellow_dye
* minecraft:lime_dye
* minecraft:pink_dye
* minecraft:gray_dye
* minecraft:light_gray_dye
* minecraft:cyan_dye
* minecraft:purple_dye
* minecraft:blue_dye
* minecraft:brown_dye
* minecraft:green_dye
* minecraft:red_dye
* minecraft:black_dye
* minecraft:bone_meal
* minecraft:bone
* minecraft:sugar
* minecraft:cake
* minecraft:white_bed
* minecraft:orange_bed
* minecraft:magenta_bed
* minecraft:light_blue_bed
* minecraft:yellow_bed
* minecraft:lime_bed
* minecraft:pink_bed
* minecraft:gray_bed
* minecraft:light_gray_bed
* minecraft:cyan_bed
* minecraft:purple_bed
* minecraft:blue_bed
* minecraft:brown_bed
* minecraft:green_bed
* minecraft:red_bed
* minecraft:black_bed
* minecraft:cookie
* minecraft:filled_map
* minecraft:shears
* minecraft:melon_slice
* minecraft:dried_kelp
* minecraft:pumpkin_seeds
* minecraft:melon_seeds
* minecraft:beef
* minecraft:cooked_beef
* minecraft:chicken
* minecraft:cooked_chicken
* minecraft:rotten_flesh
* minecraft:ender_pearl
* minecraft:blaze_rod
* minecraft:ghast_tear
* minecraft:gold_nugget
* minecraft:nether_wart
* minecraft:potion
* minecraft:glass_bottle
* minecraft:spider_eye
* minecraft:fermented_spider_eye
* minecraft:blaze_powder
* minecraft:magma_cream
* minecraft:brewing_stand
* minecraft:cauldron
* minecraft:ender_eye
* minecraft:glistering_melon_slice
* minecraft:allay_spawn_egg
* minecraft:axolotl_spawn_egg
* minecraft:bat_spawn_egg
* minecraft:bee_spawn_egg
* minecraft:blaze_spawn_egg
* minecraft:cat_spawn_egg
* minecraft:camel_spawn_egg
* minecraft:cave_spider_spawn_egg
* minecraft:chicken_spawn_egg
* minecraft:cod_spawn_egg
* minecraft:cow_spawn_egg
* minecraft:creeper_spawn_egg
* minecraft:dolphin_spawn_egg
* minecraft:donkey_spawn_egg
* minecraft:drowned_spawn_egg
* minecraft:elder_guardian_spawn_egg
* minecraft:ender_dragon_spawn_egg
* minecraft:enderman_spawn_egg
* minecraft:endermite_spawn_egg
* minecraft:evoker_spawn_egg
* minecraft:fox_spawn_egg
* minecraft:frog_spawn_egg
* minecraft:ghast_spawn_egg
* minecraft:glow_squid_spawn_egg
* minecraft:goat_spawn_egg
* minecraft:guardian_spawn_egg
* minecraft:hoglin_spawn_egg
* minecraft:horse_spawn_egg
* minecraft:husk_spawn_egg
* minecraft:iron_golem_spawn_egg
* minecraft:llama_spawn_egg
* minecraft:magma_cube_spawn_egg
* minecraft:mooshroom_spawn_egg
* minecraft:mule_spawn_egg
* minecraft:ocelot_spawn_egg
* minecraft:panda_spawn_egg
* minecraft:parrot_spawn_egg
* minecraft:phantom_spawn_egg
* minecraft:pig_spawn_egg
* minecraft:piglin_spawn_egg
* minecraft:piglin_brute_spawn_egg
* minecraft:pillager_spawn_egg
* minecraft:polar_bear_spawn_egg
* minecraft:pufferfish_spawn_egg
* minecraft:rabbit_spawn_egg
* minecraft:ravager_spawn_egg
* minecraft:salmon_spawn_egg
* minecraft:sheep_spawn_egg
* minecraft:shulker_spawn_egg
* minecraft:silverfish_spawn_egg
* minecraft:skeleton_spawn_egg
* minecraft:skeleton_horse_spawn_egg
* minecraft:slime_spawn_egg
* minecraft:sniffer_spawn_egg
* minecraft:snow_golem_spawn_egg
* minecraft:spider_spawn_egg
* minecraft:squid_spawn_egg
* minecraft:stray_spawn_egg
* minecraft:strider_spawn_egg
* minecraft:tadpole_spawn_egg
* minecraft:trader_llama_spawn_egg
* minecraft:tropical_fish_spawn_egg
* minecraft:turtle_spawn_egg
* minecraft:vex_spawn_egg
* minecraft:villager_spawn_egg
* minecraft:vindicator_spawn_egg
* minecraft:wandering_trader_spawn_egg
* minecraft:warden_spawn_egg
* minecraft:witch_spawn_egg
* minecraft:wither_spawn_egg
* minecraft:wither_skeleton_spawn_egg
* minecraft:wolf_spawn_egg
* minecraft:zoglin_spawn_egg
* minecraft:zombie_spawn_egg
* minecraft:zombie_horse_spawn_egg
* minecraft:zombie_villager_spawn_egg
* minecraft:zombified_piglin_spawn_egg
* minecraft:experience_bottle
* minecraft:fire_charge
* minecraft:writable_book
* minecraft:written_book
* minecraft:item_frame
* minecraft:glow_item_frame
* minecraft:flower_pot
* minecraft:carrot
* minecraft:potato
* minecraft:baked_potato
* minecraft:poisonous_potato
* minecraft:map
* minecraft:golden_carrot
* minecraft:skeleton_skull
* minecraft:wither_skeleton_skull
* minecraft:player_head
* minecraft:zombie_head
* minecraft:creeper_head
* minecraft:dragon_head
* minecraft:piglin_head
* minecraft:nether_star
* minecraft:pumpkin_pie
* minecraft:firework_rocket
* minecraft:firework_star
* minecraft:enchanted_book
* minecraft:nether_brick
* minecraft:prismarine_shard
* minecraft:prismarine_crystals
* minecraft:rabbit
* minecraft:cooked_rabbit
* minecraft:rabbit_stew
* minecraft:rabbit_foot
* minecraft:rabbit_hide
* minecraft:armor_stand
* minecraft:iron_horse_armor
* minecraft:golden_horse_armor
* minecraft:diamond_horse_armor
* minecraft:leather_horse_armor
* minecraft:lead
* minecraft:name_tag
* minecraft:command_block_minecart
* minecraft:mutton
* minecraft:cooked_mutton
* minecraft:white_banner
* minecraft:orange_banner
* minecraft:magenta_banner
* minecraft:light_blue_banner
* minecraft:yellow_banner
* minecraft:lime_banner
* minecraft:pink_banner
* minecraft:gray_banner
* minecraft:light_gray_banner
* minecraft:cyan_banner
* minecraft:purple_banner
* minecraft:blue_banner
* minecraft:brown_banner
* minecraft:green_banner
* minecraft:red_banner
* minecraft:black_banner
* minecraft:end_crystal
* minecraft:chorus_fruit
* minecraft:popped_chorus_fruit
* minecraft:torchflower_seeds
* minecraft:beetroot
* minecraft:beetroot_seeds
* minecraft:beetroot_soup
* minecraft:dragon_breath
* minecraft:splash_potion
* minecraft:spectral_arrow
* minecraft:tipped_arrow
* minecraft:lingering_potion
* minecraft:shield
* minecraft:totem_of_undying
* minecraft:shulker_shell
* minecraft:iron_nugget
* minecraft:knowledge_book
* minecraft:debug_stick
* minecraft:music_disc_13
* minecraft:music_disc_cat
* minecraft:music_disc_blocks
* minecraft:music_disc_chirp
* minecraft:music_disc_far
* minecraft:music_disc_mall
* minecraft:music_disc_mellohi
* minecraft:music_disc_stal
* minecraft:music_disc_strad
* minecraft:music_disc_ward
* minecraft:music_disc_11
* minecraft:music_disc_wait
* minecraft:music_disc_otherside
* minecraft:music_disc_5
* minecraft:music_disc_pigstep
* minecraft:disc_fragment_5
* minecraft:trident
* minecraft:phantom_membrane
* minecraft:nautilus_shell
* minecraft:heart_of_the_sea
* minecraft:crossbow
* minecraft:suspicious_stew
* minecraft:loom
* minecraft:flower_banner_pattern
* minecraft:creeper_banner_pattern
* minecraft:skull_banner_pattern
* minecraft:mojang_banner_pattern
* minecraft:globe_banner_pattern
* minecraft:piglin_banner_pattern
* minecraft:goat_horn
* minecraft:composter
* minecraft:barrel
* minecraft:smoker
* minecraft:blast_furnace
* minecraft:cartography_table
* minecraft:fletching_table
* minecraft:grindstone
* minecraft:smithing_table
* minecraft:stonecutter
* minecraft:bell
* minecraft:lantern
* minecraft:soul_lantern
* minecraft:sweet_berries
* minecraft:glow_berries
* minecraft:campfire
* minecraft:soul_campfire
* minecraft:shroomlight
* minecraft:honeycomb
* minecraft:bee_nest
* minecraft:beehive
* minecraft:honey_bottle
* minecraft:honeycomb_block
* minecraft:lodestone
* minecraft:crying_obsidian
* minecraft:blackstone
* minecraft:blackstone_slab
* minecraft:blackstone_stairs
* minecraft:gilded_blackstone
* minecraft:polished_blackstone
* minecraft:polished_blackstone_slab
* minecraft:polished_blackstone_stairs
* minecraft:chiseled_polished_blackstone
* minecraft:polished_blackstone_bricks
* minecraft:polished_blackstone_brick_slab
* minecraft:polished_blackstone_brick_stairs
* minecraft:cracked_polished_blackstone_bricks
* minecraft:respawn_anchor
* minecraft:candle
* minecraft:white_candle
* minecraft:orange_candle
* minecraft:magenta_candle
* minecraft:light_blue_candle
* minecraft:yellow_candle
* minecraft:lime_candle
* minecraft:pink_candle
* minecraft:gray_candle
* minecraft:light_gray_candle
* minecraft:cyan_candle
* minecraft:purple_candle
* minecraft:blue_candle
* minecraft:brown_candle
* minecraft:green_candle
* minecraft:red_candle
* minecraft:black_candle
* minecraft:small_amethyst_bud
* minecraft:medium_amethyst_bud
* minecraft:large_amethyst_bud
* minecraft:amethyst_cluster
* minecraft:pointed_dripstone
* minecraft:ochre_froglight
* minecraft:verdant_froglight
* minecraft:pearlescent_froglight
* minecraft:frogspawn
* minecraft:echo_shard
* minecraft:brush
* minecraft:netherite_upgrade_smithing_template
* minecraft:sentry_armor_trim_smithing_template
* minecraft:dune_armor_trim_smithing_template
* minecraft:coast_armor_trim_smithing_template
* minecraft:wild_armor_trim_smithing_template
* minecraft:ward_armor_trim_smithing_template
* minecraft:eye_armor_trim_smithing_template
* minecraft:vex_armor_trim_smithing_template
* minecraft:tide_armor_trim_smithing_template
* minecraft:snout_armor_trim_smithing_template
* minecraft:rib_armor_trim_smithing_template
* minecraft:spire_armor_trim_smithing_template
* minecraft:pottery_shard_archer
* minecraft:pottery_shard_prize
* minecraft:pottery_shard_arms_up
* minecraft:pottery_shard_skull
* minecraft:water
* minecraft:lava
* minecraft:tall_seagrass
* minecraft:piston_head
* minecraft:moving_piston
* minecraft:wall_torch
* minecraft:fire
* minecraft:soul_fire
* minecraft:redstone_wire
* minecraft:oak_wall_sign
* minecraft:spruce_wall_sign
* minecraft:birch_wall_sign
* minecraft:acacia_wall_sign
* minecraft:cherry_wall_sign
* minecraft:jungle_wall_sign
* minecraft:dark_oak_wall_sign
* minecraft:mangrove_wall_sign
* minecraft:bamboo_wall_sign
* minecraft:oak_wall_hanging_sign
* minecraft:spruce_wall_hanging_sign
* minecraft:birch_wall_hanging_sign
* minecraft:acacia_wall_hanging_sign
* minecraft:cherry_wall_hanging_sign
* minecraft:jungle_wall_hanging_sign
* minecraft:dark_oak_wall_hanging_sign
* minecraft:mangrove_wall_hanging_sign
* minecraft:crimson_wall_hanging_sign
* minecraft:warped_wall_hanging_sign
* minecraft:bamboo_wall_hanging_sign
* minecraft:redstone_wall_torch
* minecraft:soul_wall_torch
* minecraft:nether_portal
* minecraft:attached_pumpkin_stem
* minecraft:attached_melon_stem
* minecraft:pumpkin_stem
* minecraft:melon_stem
* minecraft:water_cauldron
* minecraft:lava_cauldron
* minecraft:powder_snow_cauldron
* minecraft:end_portal
* minecraft:cocoa
* minecraft:tripwire
* minecraft:potted_torchflower
* minecraft:potted_oak_sapling
* minecraft:potted_spruce_sapling
* minecraft:potted_birch_sapling
* minecraft:potted_jungle_sapling
* minecraft:potted_acacia_sapling
* minecraft:potted_cherry_sapling
* minecraft:potted_dark_oak_sapling
* minecraft:potted_mangrove_propagule
* minecraft:potted_fern
* minecraft:potted_dandelion
* minecraft:potted_poppy
* minecraft:potted_blue_orchid
* minecraft:potted_allium
* minecraft:potted_azure_bluet
* minecraft:potted_red_tulip
* minecraft:potted_orange_tulip
* minecraft:potted_white_tulip
* minecraft:potted_pink_tulip
* minecraft:potted_oxeye_daisy
* minecraft:potted_cornflower
* minecraft:potted_lily_of_the_valley
* minecraft:potted_wither_rose
* minecraft:potted_red_mushroom
* minecraft:potted_brown_mushroom
* minecraft:potted_dead_bush
* minecraft:potted_cactus
* minecraft:carrots
* minecraft:potatoes
* minecraft:skeleton_wall_skull
* minecraft:wither_skeleton_wall_skull
* minecraft:zombie_wall_head
* minecraft:player_wall_head
* minecraft:creeper_wall_head
* minecraft:dragon_wall_head
* minecraft:piglin_wall_head
* minecraft:white_wall_banner
* minecraft:orange_wall_banner
* minecraft:magenta_wall_banner
* minecraft:light_blue_wall_banner
* minecraft:yellow_wall_banner
* minecraft:lime_wall_banner
* minecraft:pink_wall_banner
* minecraft:gray_wall_banner
* minecraft:light_gray_wall_banner
* minecraft:cyan_wall_banner
* minecraft:purple_wall_banner
* minecraft:blue_wall_banner
* minecraft:brown_wall_banner
* minecraft:green_wall_banner
* minecraft:red_wall_banner
* minecraft:black_wall_banner
* minecraft:torchflower_crop
* minecraft:beetroots
* minecraft:end_gateway
* minecraft:frosted_ice
* minecraft:kelp_plant
* minecraft:dead_tube_coral_wall_fan
* minecraft:dead_brain_coral_wall_fan
* minecraft:dead_bubble_coral_wall_fan
* minecraft:dead_fire_coral_wall_fan
* minecraft:dead_horn_coral_wall_fan
* minecraft:tube_coral_wall_fan
* minecraft:brain_coral_wall_fan
* minecraft:bubble_coral_wall_fan
* minecraft:fire_coral_wall_fan
* minecraft:horn_coral_wall_fan
* minecraft:bamboo_sapling
* minecraft:potted_bamboo
* minecraft:void_air
* minecraft:cave_air
* minecraft:bubble_column
* minecraft:sweet_berry_bush
* minecraft:weeping_vines_plant
* minecraft:twisting_vines_plant
* minecraft:crimson_wall_sign
* minecraft:warped_wall_sign
* minecraft:potted_crimson_fungus
* minecraft:potted_warped_fungus
* minecraft:potted_crimson_roots
* minecraft:potted_warped_roots
* minecraft:candle_cake
* minecraft:white_candle_cake
* minecraft:orange_candle_cake
* minecraft:magenta_candle_cake
* minecraft:light_blue_candle_cake
* minecraft:yellow_candle_cake
* minecraft:lime_candle_cake
* minecraft:pink_candle_cake
* minecraft:gray_candle_cake
* minecraft:light_gray_candle_cake
* minecraft:cyan_candle_cake
* minecraft:purple_candle_cake
* minecraft:blue_candle_cake
* minecraft:brown_candle_cake
* minecraft:green_candle_cake
* minecraft:red_candle_cake
* minecraft:black_candle_cake
* minecraft:powder_snow
* minecraft:cave_vines
* minecraft:cave_vines_plant
* minecraft:big_dripleaf_stem
* minecraft:potted_azalea_bush
* minecraft:potted_flowering_azalea_bush
* minecraft:LEGACY_AIR
* minecraft:LEGACY_STONE
* minecraft:LEGACY_GRASS
* minecraft:LEGACY_DIRT
* minecraft:LEGACY_COBBLESTONE
* minecraft:LEGACY_WOOD
* minecraft:LEGACY_SAPLING
* minecraft:LEGACY_BEDROCK
* minecraft:LEGACY_WATER
* minecraft:LEGACY_STATIONARY_WATER
* minecraft:LEGACY_LAVA
* minecraft:LEGACY_STATIONARY_LAVA
* minecraft:LEGACY_SAND
* minecraft:LEGACY_GRAVEL
* minecraft:LEGACY_GOLD_ORE
* minecraft:LEGACY_IRON_ORE
* minecraft:LEGACY_COAL_ORE
* minecraft:LEGACY_LOG
* minecraft:LEGACY_LEAVES
* minecraft:LEGACY_SPONGE
* minecraft:LEGACY_GLASS
* minecraft:LEGACY_LAPIS_ORE
* minecraft:LEGACY_LAPIS_BLOCK
* minecraft:LEGACY_DISPENSER
* minecraft:LEGACY_SANDSTONE
* minecraft:LEGACY_NOTE_BLOCK
* minecraft:LEGACY_BED_BLOCK
* minecraft:LEGACY_POWERED_RAIL
* minecraft:LEGACY_DETECTOR_RAIL
* minecraft:LEGACY_PISTON_STICKY_BASE
* minecraft:LEGACY_WEB
* minecraft:LEGACY_LONG_GRASS
* minecraft:LEGACY_DEAD_BUSH
* minecraft:LEGACY_PISTON_BASE
* minecraft:LEGACY_PISTON_EXTENSION
* minecraft:LEGACY_WOOL
* minecraft:LEGACY_PISTON_MOVING_PIECE
* minecraft:LEGACY_YELLOW_FLOWER
* minecraft:LEGACY_RED_ROSE
* minecraft:LEGACY_BROWN_MUSHROOM
* minecraft:LEGACY_RED_MUSHROOM
* minecraft:LEGACY_GOLD_BLOCK
* minecraft:LEGACY_IRON_BLOCK
* minecraft:LEGACY_DOUBLE_STEP
* minecraft:LEGACY_STEP
* minecraft:LEGACY_BRICK
* minecraft:LEGACY_TNT
* minecraft:LEGACY_BOOKSHELF
* minecraft:LEGACY_MOSSY_COBBLESTONE
* minecraft:LEGACY_OBSIDIAN
* minecraft:LEGACY_TORCH
* minecraft:LEGACY_FIRE
* minecraft:LEGACY_MOB_SPAWNER
* minecraft:LEGACY_WOOD_STAIRS
* minecraft:LEGACY_CHEST
* minecraft:LEGACY_REDSTONE_WIRE
* minecraft:LEGACY_DIAMOND_ORE
* minecraft:LEGACY_DIAMOND_BLOCK
* minecraft:LEGACY_WORKBENCH
* minecraft:LEGACY_CROPS
* minecraft:LEGACY_SOIL
* minecraft:LEGACY_FURNACE
* minecraft:LEGACY_BURNING_FURNACE
* minecraft:LEGACY_SIGN_POST
* minecraft:LEGACY_WOODEN_DOOR
* minecraft:LEGACY_LADDER
* minecraft:LEGACY_RAILS
* minecraft:LEGACY_COBBLESTONE_STAIRS
* minecraft:LEGACY_WALL_SIGN
* minecraft:LEGACY_LEVER
* minecraft:LEGACY_STONE_PLATE
* minecraft:LEGACY_IRON_DOOR_BLOCK
* minecraft:LEGACY_WOOD_PLATE
* minecraft:LEGACY_REDSTONE_ORE
* minecraft:LEGACY_GLOWING_REDSTONE_ORE
* minecraft:LEGACY_REDSTONE_TORCH_OFF
* minecraft:LEGACY_REDSTONE_TORCH_ON
* minecraft:LEGACY_STONE_BUTTON
* minecraft:LEGACY_SNOW
* minecraft:LEGACY_ICE
* minecraft:LEGACY_SNOW_BLOCK
* minecraft:LEGACY_CACTUS
* minecraft:LEGACY_CLAY
* minecraft:LEGACY_SUGAR_CANE_BLOCK
* minecraft:LEGACY_JUKEBOX
* minecraft:LEGACY_FENCE
* minecraft:LEGACY_PUMPKIN
* minecraft:LEGACY_NETHERRACK
* minecraft:LEGACY_SOUL_SAND
* minecraft:LEGACY_GLOWSTONE
* minecraft:LEGACY_PORTAL
* minecraft:LEGACY_JACK_O_LANTERN
* minecraft:LEGACY_CAKE_BLOCK
* minecraft:LEGACY_DIODE_BLOCK_OFF
* minecraft:LEGACY_DIODE_BLOCK_ON
* minecraft:LEGACY_STAINED_GLASS
* minecraft:LEGACY_TRAP_DOOR
* minecraft:LEGACY_MONSTER_EGGS
* minecraft:LEGACY_SMOOTH_BRICK
* minecraft:LEGACY_HUGE_MUSHROOM_1
* minecraft:LEGACY_HUGE_MUSHROOM_2
* minecraft:LEGACY_IRON_FENCE
* minecraft:LEGACY_THIN_GLASS
* minecraft:LEGACY_MELON_BLOCK
* minecraft:LEGACY_PUMPKIN_STEM
* minecraft:LEGACY_MELON_STEM
* minecraft:LEGACY_VINE
* minecraft:LEGACY_FENCE_GATE
* minecraft:LEGACY_BRICK_STAIRS
* minecraft:LEGACY_SMOOTH_STAIRS
* minecraft:LEGACY_MYCEL
* minecraft:LEGACY_WATER_LILY
* minecraft:LEGACY_NETHER_BRICK
* minecraft:LEGACY_NETHER_FENCE
* minecraft:LEGACY_NETHER_BRICK_STAIRS
* minecraft:LEGACY_NETHER_WARTS
* minecraft:LEGACY_ENCHANTMENT_TABLE
* minecraft:LEGACY_BREWING_STAND
* minecraft:LEGACY_CAULDRON
* minecraft:LEGACY_ENDER_PORTAL
* minecraft:LEGACY_ENDER_PORTAL_FRAME
* minecraft:LEGACY_ENDER_STONE
* minecraft:LEGACY_DRAGON_EGG
* minecraft:LEGACY_REDSTONE_LAMP_OFF
* minecraft:LEGACY_REDSTONE_LAMP_ON
* minecraft:LEGACY_WOOD_DOUBLE_STEP
* minecraft:LEGACY_WOOD_STEP
* minecraft:LEGACY_COCOA
* minecraft:LEGACY_SANDSTONE_STAIRS
* minecraft:LEGACY_EMERALD_ORE
* minecraft:LEGACY_ENDER_CHEST
* minecraft:LEGACY_TRIPWIRE_HOOK
* minecraft:LEGACY_TRIPWIRE
* minecraft:LEGACY_EMERALD_BLOCK
* minecraft:LEGACY_SPRUCE_WOOD_STAIRS
* minecraft:LEGACY_BIRCH_WOOD_STAIRS
* minecraft:LEGACY_JUNGLE_WOOD_STAIRS
* minecraft:LEGACY_COMMAND
* minecraft:LEGACY_BEACON
* minecraft:LEGACY_COBBLE_WALL
* minecraft:LEGACY_FLOWER_POT
* minecraft:LEGACY_CARROT
* minecraft:LEGACY_POTATO
* minecraft:LEGACY_WOOD_BUTTON
* minecraft:LEGACY_SKULL
* minecraft:LEGACY_ANVIL
* minecraft:LEGACY_TRAPPED_CHEST
* minecraft:LEGACY_GOLD_PLATE
* minecraft:LEGACY_IRON_PLATE
* minecraft:LEGACY_REDSTONE_COMPARATOR_OFF
* minecraft:LEGACY_REDSTONE_COMPARATOR_ON
* minecraft:LEGACY_DAYLIGHT_DETECTOR
* minecraft:LEGACY_REDSTONE_BLOCK
* minecraft:LEGACY_QUARTZ_ORE
* minecraft:LEGACY_HOPPER
* minecraft:LEGACY_QUARTZ_BLOCK
* minecraft:LEGACY_QUARTZ_STAIRS
* minecraft:LEGACY_ACTIVATOR_RAIL
* minecraft:LEGACY_DROPPER
* minecraft:LEGACY_STAINED_CLAY
* minecraft:LEGACY_STAINED_GLASS_PANE
* minecraft:LEGACY_LEAVES_2
* minecraft:LEGACY_LOG_2
* minecraft:LEGACY_ACACIA_STAIRS
* minecraft:LEGACY_DARK_OAK_STAIRS
* minecraft:LEGACY_SLIME_BLOCK
* minecraft:LEGACY_BARRIER
* minecraft:LEGACY_IRON_TRAPDOOR
* minecraft:LEGACY_PRISMARINE
* minecraft:LEGACY_SEA_LANTERN
* minecraft:LEGACY_HAY_BLOCK
* minecraft:LEGACY_CARPET
* minecraft:LEGACY_HARD_CLAY
* minecraft:LEGACY_COAL_BLOCK
* minecraft:LEGACY_PACKED_ICE
* minecraft:LEGACY_DOUBLE_PLANT
* minecraft:LEGACY_STANDING_BANNER
* minecraft:LEGACY_WALL_BANNER
* minecraft:LEGACY_DAYLIGHT_DETECTOR_INVERTED
* minecraft:LEGACY_RED_SANDSTONE
* minecraft:LEGACY_RED_SANDSTONE_STAIRS
* minecraft:LEGACY_DOUBLE_STONE_SLAB2
* minecraft:LEGACY_STONE_SLAB2
* minecraft:LEGACY_SPRUCE_FENCE_GATE
* minecraft:LEGACY_BIRCH_FENCE_GATE
* minecraft:LEGACY_JUNGLE_FENCE_GATE
* minecraft:LEGACY_DARK_OAK_FENCE_GATE
* minecraft:LEGACY_ACACIA_FENCE_GATE
* minecraft:LEGACY_SPRUCE_FENCE
* minecraft:LEGACY_BIRCH_FENCE
* minecraft:LEGACY_JUNGLE_FENCE
* minecraft:LEGACY_DARK_OAK_FENCE
* minecraft:LEGACY_ACACIA_FENCE
* minecraft:LEGACY_SPRUCE_DOOR
* minecraft:LEGACY_BIRCH_DOOR
* minecraft:LEGACY_JUNGLE_DOOR
* minecraft:LEGACY_ACACIA_DOOR
* minecraft:LEGACY_DARK_OAK_DOOR
* minecraft:LEGACY_END_ROD
* minecraft:LEGACY_CHORUS_PLANT
* minecraft:LEGACY_CHORUS_FLOWER
* minecraft:LEGACY_PURPUR_BLOCK
* minecraft:LEGACY_PURPUR_PILLAR
* minecraft:LEGACY_PURPUR_STAIRS
* minecraft:LEGACY_PURPUR_DOUBLE_SLAB
* minecraft:LEGACY_PURPUR_SLAB
* minecraft:LEGACY_END_BRICKS
* minecraft:LEGACY_BEETROOT_BLOCK
* minecraft:LEGACY_GRASS_PATH
* minecraft:LEGACY_END_GATEWAY
* minecraft:LEGACY_COMMAND_REPEATING
* minecraft:LEGACY_COMMAND_CHAIN
* minecraft:LEGACY_FROSTED_ICE
* minecraft:LEGACY_MAGMA
* minecraft:LEGACY_NETHER_WART_BLOCK
* minecraft:LEGACY_RED_NETHER_BRICK
* minecraft:LEGACY_BONE_BLOCK
* minecraft:LEGACY_STRUCTURE_VOID
* minecraft:LEGACY_OBSERVER
* minecraft:LEGACY_WHITE_SHULKER_BOX
* minecraft:LEGACY_ORANGE_SHULKER_BOX
* minecraft:LEGACY_MAGENTA_SHULKER_BOX
* minecraft:LEGACY_LIGHT_BLUE_SHULKER_BOX
* minecraft:LEGACY_YELLOW_SHULKER_BOX
* minecraft:LEGACY_LIME_SHULKER_BOX
* minecraft:LEGACY_PINK_SHULKER_BOX
* minecraft:LEGACY_GRAY_SHULKER_BOX
* minecraft:LEGACY_SILVER_SHULKER_BOX
* minecraft:LEGACY_CYAN_SHULKER_BOX
* minecraft:LEGACY_PURPLE_SHULKER_BOX
* minecraft:LEGACY_BLUE_SHULKER_BOX
* minecraft:LEGACY_BROWN_SHULKER_BOX
* minecraft:LEGACY_GREEN_SHULKER_BOX
* minecraft:LEGACY_RED_SHULKER_BOX
* minecraft:LEGACY_BLACK_SHULKER_BOX
* minecraft:LEGACY_WHITE_GLAZED_TERRACOTTA
* minecraft:LEGACY_ORANGE_GLAZED_TERRACOTTA
* minecraft:LEGACY_MAGENTA_GLAZED_TERRACOTTA
* minecraft:LEGACY_LIGHT_BLUE_GLAZED_TERRACOTTA
* minecraft:LEGACY_YELLOW_GLAZED_TERRACOTTA
* minecraft:LEGACY_LIME_GLAZED_TERRACOTTA
* minecraft:LEGACY_PINK_GLAZED_TERRACOTTA
* minecraft:LEGACY_GRAY_GLAZED_TERRACOTTA
* minecraft:LEGACY_SILVER_GLAZED_TERRACOTTA
* minecraft:LEGACY_CYAN_GLAZED_TERRACOTTA
* minecraft:LEGACY_PURPLE_GLAZED_TERRACOTTA
* minecraft:LEGACY_BLUE_GLAZED_TERRACOTTA
* minecraft:LEGACY_BROWN_GLAZED_TERRACOTTA
* minecraft:LEGACY_GREEN_GLAZED_TERRACOTTA
* minecraft:LEGACY_RED_GLAZED_TERRACOTTA
* minecraft:LEGACY_BLACK_GLAZED_TERRACOTTA
* minecraft:LEGACY_CONCRETE
* minecraft:LEGACY_CONCRETE_POWDER
* minecraft:LEGACY_STRUCTURE_BLOCK
* minecraft:LEGACY_IRON_SPADE
* minecraft:LEGACY_IRON_PICKAXE
* minecraft:LEGACY_IRON_AXE
* minecraft:LEGACY_FLINT_AND_STEEL
* minecraft:LEGACY_APPLE
* minecraft:LEGACY_BOW
* minecraft:LEGACY_ARROW
* minecraft:LEGACY_COAL
* minecraft:LEGACY_DIAMOND
* minecraft:LEGACY_IRON_INGOT
* minecraft:LEGACY_GOLD_INGOT
* minecraft:LEGACY_IRON_SWORD
* minecraft:LEGACY_WOOD_SWORD
* minecraft:LEGACY_WOOD_SPADE
* minecraft:LEGACY_WOOD_PICKAXE
* minecraft:LEGACY_WOOD_AXE
* minecraft:LEGACY_STONE_SWORD
* minecraft:LEGACY_STONE_SPADE
* minecraft:LEGACY_STONE_PICKAXE
* minecraft:LEGACY_STONE_AXE
* minecraft:LEGACY_DIAMOND_SWORD
* minecraft:LEGACY_DIAMOND_SPADE
* minecraft:LEGACY_DIAMOND_PICKAXE
* minecraft:LEGACY_DIAMOND_AXE
* minecraft:LEGACY_STICK
* minecraft:LEGACY_BOWL
* minecraft:LEGACY_MUSHROOM_SOUP
* minecraft:LEGACY_GOLD_SWORD
* minecraft:LEGACY_GOLD_SPADE
* minecraft:LEGACY_GOLD_PICKAXE
* minecraft:LEGACY_GOLD_AXE
* minecraft:LEGACY_STRING
* minecraft:LEGACY_FEATHER
* minecraft:LEGACY_SULPHUR
* minecraft:LEGACY_WOOD_HOE
* minecraft:LEGACY_STONE_HOE
* minecraft:LEGACY_IRON_HOE
* minecraft:LEGACY_DIAMOND_HOE
* minecraft:LEGACY_GOLD_HOE
* minecraft:LEGACY_SEEDS
* minecraft:LEGACY_WHEAT
* minecraft:LEGACY_BREAD
* minecraft:LEGACY_LEATHER_HELMET
* minecraft:LEGACY_LEATHER_CHESTPLATE
* minecraft:LEGACY_LEATHER_LEGGINGS
* minecraft:LEGACY_LEATHER_BOOTS
* minecraft:LEGACY_CHAINMAIL_HELMET
* minecraft:LEGACY_CHAINMAIL_CHESTPLATE
* minecraft:LEGACY_CHAINMAIL_LEGGINGS
* minecraft:LEGACY_CHAINMAIL_BOOTS
* minecraft:LEGACY_IRON_HELMET
* minecraft:LEGACY_IRON_CHESTPLATE
* minecraft:LEGACY_IRON_LEGGINGS
* minecraft:LEGACY_IRON_BOOTS
* minecraft:LEGACY_DIAMOND_HELMET
* minecraft:LEGACY_DIAMOND_CHESTPLATE
* minecraft:LEGACY_DIAMOND_LEGGINGS
* minecraft:LEGACY_DIAMOND_BOOTS
* minecraft:LEGACY_GOLD_HELMET
* minecraft:LEGACY_GOLD_CHESTPLATE
* minecraft:LEGACY_GOLD_LEGGINGS
* minecraft:LEGACY_GOLD_BOOTS
* minecraft:LEGACY_FLINT
* minecraft:LEGACY_PORK
* minecraft:LEGACY_GRILLED_PORK
* minecraft:LEGACY_PAINTING
* minecraft:LEGACY_GOLDEN_APPLE
* minecraft:LEGACY_SIGN
* minecraft:LEGACY_WOOD_DOOR
* minecraft:LEGACY_BUCKET
* minecraft:LEGACY_WATER_BUCKET
* minecraft:LEGACY_LAVA_BUCKET
* minecraft:LEGACY_MINECART
* minecraft:LEGACY_SADDLE
* minecraft:LEGACY_IRON_DOOR
* minecraft:LEGACY_REDSTONE
* minecraft:LEGACY_SNOW_BALL
* minecraft:LEGACY_BOAT
* minecraft:LEGACY_LEATHER
* minecraft:LEGACY_MILK_BUCKET
* minecraft:LEGACY_CLAY_BRICK
* minecraft:LEGACY_CLAY_BALL
* minecraft:LEGACY_SUGAR_CANE
* minecraft:LEGACY_PAPER
* minecraft:LEGACY_BOOK
* minecraft:LEGACY_SLIME_BALL
* minecraft:LEGACY_STORAGE_MINECART
* minecraft:LEGACY_POWERED_MINECART
* minecraft:LEGACY_EGG
* minecraft:LEGACY_COMPASS
* minecraft:LEGACY_FISHING_ROD
* minecraft:LEGACY_WATCH
* minecraft:LEGACY_GLOWSTONE_DUST
* minecraft:LEGACY_RAW_FISH
* minecraft:LEGACY_COOKED_FISH
* minecraft:LEGACY_INK_SACK
* minecraft:LEGACY_BONE
* minecraft:LEGACY_SUGAR
* minecraft:LEGACY_CAKE
* minecraft:LEGACY_BED
* minecraft:LEGACY_DIODE
* minecraft:LEGACY_COOKIE
* minecraft:LEGACY_MAP
* minecraft:LEGACY_SHEARS
* minecraft:LEGACY_MELON
* minecraft:LEGACY_PUMPKIN_SEEDS
* minecraft:LEGACY_MELON_SEEDS
* minecraft:LEGACY_RAW_BEEF
* minecraft:LEGACY_COOKED_BEEF
* minecraft:LEGACY_RAW_CHICKEN
* minecraft:LEGACY_COOKED_CHICKEN
* minecraft:LEGACY_ROTTEN_FLESH
* minecraft:LEGACY_ENDER_PEARL
* minecraft:LEGACY_BLAZE_ROD
* minecraft:LEGACY_GHAST_TEAR
* minecraft:LEGACY_GOLD_NUGGET
* minecraft:LEGACY_NETHER_STALK
* minecraft:LEGACY_POTION
* minecraft:LEGACY_GLASS_BOTTLE
* minecraft:LEGACY_SPIDER_EYE
* minecraft:LEGACY_FERMENTED_SPIDER_EYE
* minecraft:LEGACY_BLAZE_POWDER
* minecraft:LEGACY_MAGMA_CREAM
* minecraft:LEGACY_BREWING_STAND_ITEM
* minecraft:LEGACY_CAULDRON_ITEM
* minecraft:LEGACY_EYE_OF_ENDER
* minecraft:LEGACY_SPECKLED_MELON
* minecraft:LEGACY_MONSTER_EGG
* minecraft:LEGACY_EXP_BOTTLE
* minecraft:LEGACY_FIREBALL
* minecraft:LEGACY_BOOK_AND_QUILL
* minecraft:LEGACY_WRITTEN_BOOK
* minecraft:LEGACY_EMERALD
* minecraft:LEGACY_ITEM_FRAME
* minecraft:LEGACY_FLOWER_POT_ITEM
* minecraft:LEGACY_CARROT_ITEM
* minecraft:LEGACY_POTATO_ITEM
* minecraft:LEGACY_BAKED_POTATO
* minecraft:LEGACY_POISONOUS_POTATO
* minecraft:LEGACY_EMPTY_MAP
* minecraft:LEGACY_GOLDEN_CARROT
* minecraft:LEGACY_SKULL_ITEM
* minecraft:LEGACY_CARROT_STICK
* minecraft:LEGACY_NETHER_STAR
* minecraft:LEGACY_PUMPKIN_PIE
* minecraft:LEGACY_FIREWORK
* minecraft:LEGACY_FIREWORK_CHARGE
* minecraft:LEGACY_ENCHANTED_BOOK
* minecraft:LEGACY_REDSTONE_COMPARATOR
* minecraft:LEGACY_NETHER_BRICK_ITEM
* minecraft:LEGACY_QUARTZ
* minecraft:LEGACY_EXPLOSIVE_MINECART
* minecraft:LEGACY_HOPPER_MINECART
* minecraft:LEGACY_PRISMARINE_SHARD
* minecraft:LEGACY_PRISMARINE_CRYSTALS
* minecraft:LEGACY_RABBIT
* minecraft:LEGACY_COOKED_RABBIT
* minecraft:LEGACY_RABBIT_STEW
* minecraft:LEGACY_RABBIT_FOOT
* minecraft:LEGACY_RABBIT_HIDE
* minecraft:LEGACY_ARMOR_STAND
* minecraft:LEGACY_IRON_BARDING
* minecraft:LEGACY_GOLD_BARDING
* minecraft:LEGACY_DIAMOND_BARDING
* minecraft:LEGACY_LEASH
* minecraft:LEGACY_NAME_TAG
* minecraft:LEGACY_COMMAND_MINECART
* minecraft:LEGACY_MUTTON
* minecraft:LEGACY_COOKED_MUTTON
* minecraft:LEGACY_BANNER
* minecraft:LEGACY_END_CRYSTAL
* minecraft:LEGACY_SPRUCE_DOOR_ITEM
* minecraft:LEGACY_BIRCH_DOOR_ITEM
* minecraft:LEGACY_JUNGLE_DOOR_ITEM
* minecraft:LEGACY_ACACIA_DOOR_ITEM
* minecraft:LEGACY_DARK_OAK_DOOR_ITEM
* minecraft:LEGACY_CHORUS_FRUIT
* minecraft:LEGACY_CHORUS_FRUIT_POPPED
* minecraft:LEGACY_BEETROOT
* minecraft:LEGACY_BEETROOT_SEEDS
* minecraft:LEGACY_BEETROOT_SOUP
* minecraft:LEGACY_DRAGONS_BREATH
* minecraft:LEGACY_SPLASH_POTION
* minecraft:LEGACY_SPECTRAL_ARROW
* minecraft:LEGACY_TIPPED_ARROW
* minecraft:LEGACY_LINGERING_POTION
* minecraft:LEGACY_SHIELD
* minecraft:LEGACY_ELYTRA
* minecraft:LEGACY_BOAT_SPRUCE
* minecraft:LEGACY_BOAT_BIRCH
* minecraft:LEGACY_BOAT_JUNGLE
* minecraft:LEGACY_BOAT_ACACIA
* minecraft:LEGACY_BOAT_DARK_OAK
* minecraft:LEGACY_TOTEM
* minecraft:LEGACY_SHULKER_SHELL
* minecraft:LEGACY_IRON_NUGGET
* minecraft:LEGACY_KNOWLEDGE_BOOK
* minecraft:LEGACY_GOLD_RECORD
* minecraft:LEGACY_GREEN_RECORD
* minecraft:LEGACY_RECORD_3
* minecraft:LEGACY_RECORD_4
* minecraft:LEGACY_RECORD_5
* minecraft:LEGACY_RECORD_6
* minecraft:LEGACY_RECORD_7
* minecraft:LEGACY_RECORD_8
* minecraft:LEGACY_RECORD_9
* minecraft:LEGACY_RECORD_10
* minecraft:LEGACY_RECORD_11
* minecraft:LEGACY_RECORD_12
