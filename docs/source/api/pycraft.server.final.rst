pycraft.server.final
=====================

The pycraft.server.final module contains the final classes representing the server-side
        proxy objects which follow the Java Bukkit API. The classes described here are Python classes,
        but with special proxy methods for calling into the related Java objects. The documentation
        here is mostly a reference as to what is exposed, while the Bukkit API documentation linked
        from each Proxy class's page provides details and semantics of what the methods do.
        

.. :py:module: pycraft.server.final
.. toctree::
   :maxdepth: 1
   :caption: Contents:

   class AbstractArrow(Projectile) <./generated/AbstractArrow>
   class PickupRule() <./generated/PickupRule>
   class PickupStatus() <./generated/PickupStatus>
   class AbstractHorse(Vehicle, InventoryHolder, Tameable) <./generated/AbstractHorse>
   class AbstractHorseInventory(Inventory) <./generated/AbstractHorseInventory>
   class AbstractSkeleton(Monster) <./generated/AbstractSkeleton>
   class AbstractVillager(Breedable, NPC, InventoryHolder, Merchant) <./generated/AbstractVillager>
   class Action() <./generated/Action>
   class Advancement() <./generated/Advancement>
   class AdvancementProgress() <./generated/AdvancementProgress>
   class Ageable(Creature) <./generated/Ageable>
   class Allay(Creature, InventoryHolder) <./generated/Allay>
   class Ambient(Mob) <./generated/Ambient>
   class AnaloguePowerable(BlockData) <./generated/AnaloguePowerable>
   class AnimalTamer() <./generated/AnimalTamer>
   class Animals(Breedable) <./generated/Animals>
   class AreaEffectCloud(Entity) <./generated/AreaEffectCloud>
   class ArmorStand(LivingEntity) <./generated/ArmorStand>
   class LockType() <./generated/LockType>
   class ArmoredHorseInventory(AbstractHorseInventory) <./generated/ArmoredHorseInventory>
   class Arrow(AbstractArrow) <./generated/Arrow>
   class Art() <./generated/Art>
   class Attachable(BlockData) <./generated/Attachable>
   class Attributable() <./generated/Attributable>
   class Attribute() <./generated/Attribute>
   class AttributeInstance() <./generated/AttributeInstance>
   class AttributeModifier(ConfigurationSerializable) <./generated/AttributeModifier>
   class Operation() <./generated/Operation>
   class Axis() <./generated/Axis>
   class Axolotl(Animals) <./generated/Axolotl>
   class Bamboo(Ageable, Sapling) <./generated/Bamboo>
   class Leaves() <./generated/Leaves>
   class BanEntry() <./generated/BanEntry>
   class BanList() <./generated/BanList>
   class BannerMeta(ItemMeta) <./generated/BannerMeta>
   class BarColor() <./generated/BarColor>
   class BarFlag() <./generated/BarFlag>
   class BarStyle() <./generated/BarStyle>
   class Bat(Ambient) <./generated/Bat>
   class Bed(Directional) <./generated/Bed>
   class Part() <./generated/Part>
   class Bee(Animals) <./generated/Bee>
   class Beehive(Directional) <./generated/Beehive>
   class Bell(Directional, Powerable) <./generated/Bell>
   class Attachment() <./generated/Attachment>
   class Biome() <./generated/Biome>
   class BiomeParameterPoint() <./generated/BiomeParameterPoint>
   class BiomeProvider() <./generated/BiomeProvider>
   class Bisected(BlockData) <./generated/Bisected>
   class Half() <./generated/Half>
   class Blaze(Monster) <./generated/Blaze>
   class Block(Metadatable) <./generated/Block>
   class BlockChangeDelegate() <./generated/BlockChangeDelegate>
   class BlockData() <./generated/BlockData>
   class BlockDataMeta(ItemMeta) <./generated/BlockDataMeta>
   class BlockDisplay(Display) <./generated/BlockDisplay>
   class BlockFace() <./generated/BlockFace>
   class BlockState(Metadatable) <./generated/BlockState>
   class BlockStateMeta(ItemMeta) <./generated/BlockStateMeta>
   class BlockSupport() <./generated/BlockSupport>
   class BlockVector(Vector) <./generated/BlockVector>
   class Boat(Vehicle) <./generated/Boat>
   class BookMeta(ItemMeta) <./generated/BookMeta>
   class BookMetaBuilder() <./generated/BookMetaBuilder>
   class Generation() <./generated/Generation>
   class Boss(Entity) <./generated/Boss>
   class BossBar() <./generated/BossBar>
   class BoundingBox(ConfigurationSerializable) <./generated/BoundingBox>
   class Breedable(Ageable) <./generated/Breedable>
   class BrewingStand(BlockData) <./generated/BrewingStand>
   class BubbleColumn(BlockData) <./generated/BubbleColumn>
   class Bukkit() <./generated/Bukkit>
   class BukkitRunnable() <./generated/BukkitRunnable>
   class BukkitScheduler() <./generated/BukkitScheduler>
   class BukkitTask() <./generated/BukkitTask>
   class CachedServerIcon() <./generated/CachedServerIcon>
   class Cake(BlockData) <./generated/Cake>
   class Camel(AbstractHorse, Sittable) <./generated/Camel>
   class Campfire(Directional, Lightable, Waterlogged) <./generated/Campfire>
   class Cancellable() <./generated/Cancellable>
   class Cat(Tameable, Sittable) <./generated/Cat>
   class CaveSpider(Spider) <./generated/CaveSpider>
   class Chain(Orientable, Waterlogged) <./generated/Chain>
   class ChatColor() <./generated/ChatColor>
   class Chest(Directional, Waterlogged) <./generated/Chest>
   class ChestBoat(Boat, InventoryHolder) <./generated/ChestBoat>
   class ChestedHorse(AbstractHorse) <./generated/ChestedHorse>
   class Chicken(Animals) <./generated/Chicken>
   class Chunk(PersistentDataHolder) <./generated/Chunk>
   class LoadLevel() <./generated/LoadLevel>
   class ChunkGenerator() <./generated/ChunkGenerator>
   class BiomeGrid() <./generated/BiomeGrid>
   class ChunkData() <./generated/ChunkData>
   class ChunkSnapshot() <./generated/ChunkSnapshot>
   class Cocoa(Ageable, Directional) <./generated/Cocoa>
   class Cod() <./generated/Cod>
   class Color(ConfigurationSerializable) <./generated/Color>
   class Colorable() <./generated/Colorable>
   class Command() <./generated/Command>
   class CommandBlock(Directional) <./generated/CommandBlock>
   class CommandExecutor() <./generated/CommandExecutor>
   class CommandMap() <./generated/CommandMap>
   class CommandMinecart(Minecart) <./generated/CommandMinecart>
   class CommandSender(Permissible) <./generated/CommandSender>
   class Spigot() <./generated/Spigot>
   class Comparator(Directional, Powerable) <./generated/Comparator>
   class Mode() <./generated/Mode>
   class CompassMeta(ItemMeta) <./generated/CompassMeta>
   class ComplexEntityPart(Entity) <./generated/ComplexEntityPart>
   class ComplexLivingEntity(LivingEntity) <./generated/ComplexLivingEntity>
   class Configuration(ConfigurationSection) <./generated/Configuration>
   class ConfigurationOptions() <./generated/ConfigurationOptions>
   class ConfigurationSection() <./generated/ConfigurationSection>
   class ConfigurationSerializable() <./generated/ConfigurationSerializable>
   class ConsoleCommandSender(CommandSender, Conversable) <./generated/ConsoleCommandSender>
   class Consumer() <./generated/Consumer>
   class Conversable() <./generated/Conversable>
   class Conversation() <./generated/Conversation>
   class ConversationState() <./generated/ConversationState>
   class ConversationAbandonedEvent() <./generated/ConversationAbandonedEvent>
   class ConversationAbandonedListener() <./generated/ConversationAbandonedListener>
   class ConversationCanceller() <./generated/ConversationCanceller>
   class ConversationContext() <./generated/ConversationContext>
   class ConversationPrefix() <./generated/ConversationPrefix>
   class CoralWallFan(Directional, Waterlogged) <./generated/CoralWallFan>
   class Cow(Animals) <./generated/Cow>
   class CreativeCategory() <./generated/CreativeCategory>
   class Creature(Mob) <./generated/Creature>
   class SpawnReason() <./generated/SpawnReason>
   class Creeper(Monster) <./generated/Creeper>
   class Criteria() <./generated/Criteria>
   class CrossbowMeta(ItemMeta) <./generated/CrossbowMeta>
   class CustomItemTagContainer() <./generated/CustomItemTagContainer>
   class Damageable(Entity) <./generated/Damageable>
   class DaylightDetector(AnaloguePowerable) <./generated/DaylightDetector>
   class Difficulty() <./generated/Difficulty>
   class Directional(BlockData) <./generated/Directional>
   class Dispenser(Directional) <./generated/Dispenser>
   class Display(Entity) <./generated/Display>
   class Billboard() <./generated/Billboard>
   class Brightness() <./generated/Brightness>
   class DisplaySlot() <./generated/DisplaySlot>
   class Dolphin(WaterMob) <./generated/Dolphin>
   class Donkey(ChestedHorse) <./generated/Donkey>
   class Door(Bisected, Directional, Openable, Powerable) <./generated/Door>
   class Hinge() <./generated/Hinge>
   class DragonBattle() <./generated/DragonBattle>
   class RespawnPhase() <./generated/RespawnPhase>
   class DragonFireball(Fireball) <./generated/DragonFireball>
   class Drowned(Zombie) <./generated/Drowned>
   class DyeColor() <./generated/DyeColor>
   class Effect() <./generated/Effect>
   class Egg(ThrowableProjectile) <./generated/Egg>
   class ElderGuardian(Guardian) <./generated/ElderGuardian>
   class Enchantment() <./generated/Enchantment>
   class EnchantmentStorageMeta(ItemMeta) <./generated/EnchantmentStorageMeta>
   class EnchantmentTarget() <./generated/EnchantmentTarget>
   class EndPortalFrame(Directional) <./generated/EndPortalFrame>
   class EnderChest(Directional, Waterlogged) <./generated/EnderChest>
   class EnderCrystal(Entity) <./generated/EnderCrystal>
   class EnderDragon(ComplexLivingEntity, Boss, Mob, Enemy) <./generated/EnderDragon>
   class Phase() <./generated/Phase>
   class EnderDragonPart(ComplexEntityPart, Damageable) <./generated/EnderDragonPart>
   class EnderPearl(ThrowableProjectile) <./generated/EnderPearl>
   class EnderSignal(Entity) <./generated/EnderSignal>
   class Enderman(Monster) <./generated/Enderman>
   class Endermite(Monster) <./generated/Endermite>
   class Enemy(LivingEntity) <./generated/Enemy>
   class Entity(Metadatable, CommandSender, PersistentDataHolder) <./generated/Entity>
   class EntityCategory() <./generated/EntityCategory>
   class EntityDamageEvent(Cancellable, EntityEvent) <./generated/EntityDamageEvent>
   class DamageCause() <./generated/DamageCause>
   class DamageModifier() <./generated/DamageModifier>
   class EntityEffect() <./generated/EntityEffect>
   class EntityEquipment() <./generated/EntityEquipment>
   class EntityEvent(Event) <./generated/EntityEvent>
   class EntityType() <./generated/EntityType>
   class EquipmentSlot() <./generated/EquipmentSlot>
   class EulerAngle() <./generated/EulerAngle>
   class Event() <./generated/Event>
   class Result() <./generated/Result>
   class EventExecutor() <./generated/EventExecutor>
   class EventPriority() <./generated/EventPriority>
   class Evoker(Spellcaster) <./generated/Evoker>
   class EvokerFangs(Entity) <./generated/EvokerFangs>
   class ExperienceOrb(Entity) <./generated/ExperienceOrb>
   class Explosive(Entity) <./generated/Explosive>
   class ExplosiveMinecart(Minecart) <./generated/ExplosiveMinecart>
   class FaceAttachable(BlockData) <./generated/FaceAttachable>
   class AttachedFace() <./generated/AttachedFace>
   class FallingBlock(Entity) <./generated/FallingBlock>
   class Farmland(BlockData) <./generated/Farmland>
   class Fence(MultipleFacing, Waterlogged) <./generated/Fence>
   class FileConfiguration(MemoryConfiguration) <./generated/FileConfiguration>
   class FileConfigurationOptions(MemoryConfigurationOptions) <./generated/FileConfigurationOptions>
   class Fire(Ageable, MultipleFacing) <./generated/Fire>
   class Fireball(Projectile, Explosive) <./generated/Fireball>
   class Firework(Projectile) <./generated/Firework>
   class FireworkEffect(ConfigurationSerializable) <./generated/FireworkEffect>
   class Builder() <./generated/Builder>
   class FireworkEffectMeta(ItemMeta) <./generated/FireworkEffectMeta>
   class FireworkMeta(ItemMeta) <./generated/FireworkMeta>
   class Fish(WaterMob) <./generated/Fish>
   class FishHook(Projectile) <./generated/FishHook>
   class HookState() <./generated/HookState>
   class Fluid() <./generated/Fluid>
   class FluidCollisionMode() <./generated/FluidCollisionMode>
   class Flying(Mob) <./generated/Flying>
   class Fox(Animals, Sittable) <./generated/Fox>
   class Frog(Animals) <./generated/Frog>
   class Furnace(Directional, Lightable) <./generated/Furnace>
   class GameEvent() <./generated/GameEvent>
   class GameMode() <./generated/GameMode>
   class GameRule() <./generated/GameRule>
   class Gate(Directional, Openable, Powerable) <./generated/Gate>
   class Ghast(Flying, Enemy) <./generated/Ghast>
   class Giant(Monster) <./generated/Giant>
   class GlassPane(MultipleFacing, Waterlogged) <./generated/GlassPane>
   class GlowItemFrame(ItemFrame) <./generated/GlowItemFrame>
   class GlowSquid(Squid) <./generated/GlowSquid>
   class Goat(Animals) <./generated/Goat>
   class Golem(Creature) <./generated/Golem>
   class Grindstone(Directional, FaceAttachable) <./generated/Grindstone>
   class Guardian(Monster) <./generated/Guardian>
   class HandlerList() <./generated/HandlerList>
   class Hangable(BlockData) <./generated/Hangable>
   class Hanging(Entity, Attachable) <./generated/Hanging>
   class HeightMap() <./generated/HeightMap>
   class HelpMap() <./generated/HelpMap>
   class HelpTopic() <./generated/HelpTopic>
   class HelpTopicFactory() <./generated/HelpTopicFactory>
   class Hoglin(Animals, Enemy) <./generated/Hoglin>
   class Hopper(Directional) <./generated/Hopper>
   class HopperMinecart(Minecart, InventoryHolder) <./generated/HopperMinecart>
   class Horse(AbstractHorse) <./generated/Horse>
   class Style() <./generated/Style>
   class Variant() <./generated/Variant>
   class HorseInventory(ArmoredHorseInventory) <./generated/HorseInventory>
   class HumanEntity(LivingEntity, AnimalTamer, InventoryHolder) <./generated/HumanEntity>
   class Husk(Zombie) <./generated/Husk>
   class Illager(Raider) <./generated/Illager>
   class Illusioner(Spellcaster) <./generated/Illusioner>
   class Instrument() <./generated/Instrument>
   class Interaction(Entity) <./generated/Interaction>
   class PreviousInteraction() <./generated/PreviousInteraction>
   class Inventory() <./generated/Inventory>
   class Reason() <./generated/Reason>
   class InventoryHolder() <./generated/InventoryHolder>
   class InventoryType() <./generated/InventoryType>
   class SlotType() <./generated/SlotType>
   class InventoryView() <./generated/InventoryView>
   class Property() <./generated/Property>
   class IronGolem(Golem) <./generated/IronGolem>
   class Item(Entity) <./generated/Item>
   class ItemDisplay(Display) <./generated/ItemDisplay>
   class ItemDisplayTransform() <./generated/ItemDisplayTransform>
   class ItemFactory() <./generated/ItemFactory>
   class ItemFlag() <./generated/ItemFlag>
   class ItemFrame(Hanging) <./generated/ItemFrame>
   class ItemMeta(ConfigurationSerializable, PersistentDataHolder) <./generated/ItemMeta>
   class ItemStack(ConfigurationSerializable) <./generated/ItemStack>
   class ItemTagAdapterContext() <./generated/ItemTagAdapterContext>
   class ItemTagType() <./generated/ItemTagType>
   class Jigsaw(BlockData) <./generated/Jigsaw>
   class Orientation() <./generated/Orientation>
   class Jukebox(BlockData) <./generated/Jukebox>
   class Keyed() <./generated/Keyed>
   class KeyedBossBar(BossBar) <./generated/KeyedBossBar>
   class KnowledgeBookMeta(ItemMeta) <./generated/KnowledgeBookMeta>
   class Ladder(Directional, Waterlogged) <./generated/Ladder>
   class Lantern(Hangable, Waterlogged) <./generated/Lantern>
   class LargeFireball(SizedFireball) <./generated/LargeFireball>
   class LeashHitch(Hanging) <./generated/LeashHitch>
   class LeatherArmorMeta(ItemMeta) <./generated/LeatherArmorMeta>
   class Lectern(Directional, Powerable) <./generated/Lectern>
   class Lightable(BlockData) <./generated/Lightable>
   class LightningStrike(Entity) <./generated/LightningStrike>
   class Listener() <./generated/Listener>
   class LivingEntity(Attributable, Damageable, ProjectileSource) <./generated/LivingEntity>
   class Llama(ChestedHorse) <./generated/Llama>
   class LlamaInventory(SaddledHorseInventory) <./generated/LlamaInventory>
   class LlamaSpit(Projectile) <./generated/LlamaSpit>
   class Location(ConfigurationSerializable) <./generated/Location>
   class LootContext() <./generated/LootContext>
   class LootTable() <./generated/LootTable>
   class Lootable() <./generated/Lootable>
   class MagmaCube(Slime) <./generated/MagmaCube>
   class MainHand() <./generated/MainHand>
   class MapCanvas() <./generated/MapCanvas>
   class MapCursor() <./generated/MapCursor>
   class MapCursorCollection() <./generated/MapCursorCollection>
   class MapFont() <./generated/MapFont>
   class CharacterSprite() <./generated/CharacterSprite>
   class MapMeta(ItemMeta) <./generated/MapMeta>
   class MapRenderer() <./generated/MapRenderer>
   class MapView() <./generated/MapView>
   class Scale() <./generated/Scale>
   class Marker(Entity) <./generated/Marker>
   class Material() <./generated/Material>
   class MemoryConfiguration(Configuration, MemorySection) <./generated/MemoryConfiguration>
   class MemoryConfigurationOptions(ConfigurationOptions) <./generated/MemoryConfigurationOptions>
   class MemoryKey() <./generated/MemoryKey>
   class MemorySection(ConfigurationSection) <./generated/MemorySection>
   class Merchant() <./generated/Merchant>
   class MerchantRecipe(Recipe) <./generated/MerchantRecipe>
   class Messenger() <./generated/Messenger>
   class MetadataValue() <./generated/MetadataValue>
   class Metadatable() <./generated/Metadatable>
   class Minecart(Vehicle) <./generated/Minecart>
   class Mirror() <./generated/Mirror>
   class Mob(LivingEntity, Lootable) <./generated/Mob>
   class Monster(Creature, Enemy) <./generated/Monster>
   class Mule(ChestedHorse) <./generated/Mule>
   class MultipleFacing(BlockData) <./generated/MultipleFacing>
   class MushroomCow(Cow) <./generated/MushroomCow>
   class NPC(Creature) <./generated/NPC>
   class NameTagVisibility() <./generated/NameTagVisibility>
   class Nameable() <./generated/Nameable>
   class NamespacedKey() <./generated/NamespacedKey>
   class Note() <./generated/Note>
   class Tone() <./generated/Tone>
   class NoteBlock(Powerable) <./generated/NoteBlock>
   class Objective() <./generated/Objective>
   class Observer(Directional, Powerable) <./generated/Observer>
   class Ocelot(Animals) <./generated/Ocelot>
   class OfflinePlayer(ServerOperator, AnimalTamer, ConfigurationSerializable) <./generated/OfflinePlayer>
   class Openable(BlockData) <./generated/Openable>
   class Orientable(BlockData) <./generated/Orientable>
   class Painting(Hanging) <./generated/Painting>
   class Panda(Animals, Sittable) <./generated/Panda>
   class Gene() <./generated/Gene>
   class Parrot(Tameable, Sittable) <./generated/Parrot>
   class Particle() <./generated/Particle>
   class Permissible(ServerOperator) <./generated/Permissible>
   class Permission() <./generated/Permission>
   class PermissionAttachment() <./generated/PermissionAttachment>
   class PermissionDefault() <./generated/PermissionDefault>
   class PermissionRemovedExecutor() <./generated/PermissionRemovedExecutor>
   class PersistentDataAdapterContext() <./generated/PersistentDataAdapterContext>
   class PersistentDataContainer() <./generated/PersistentDataContainer>
   class PersistentDataHolder() <./generated/PersistentDataHolder>
   class PersistentDataType() <./generated/PersistentDataType>
   class Phantom(Flying, Enemy) <./generated/Phantom>
   class Pig(Steerable, Vehicle) <./generated/Pig>
   class PigZombie(Zombie) <./generated/PigZombie>
   class Piglin(PiglinAbstract, InventoryHolder) <./generated/Piglin>
   class PiglinAbstract(Monster, Ageable) <./generated/PiglinAbstract>
   class PiglinBrute(PiglinAbstract) <./generated/PiglinBrute>
   class Pillager(Illager, InventoryHolder) <./generated/Pillager>
   class Piston(Directional) <./generated/Piston>
   class PistonHead(TechnicalPiston) <./generated/PistonHead>
   class PistonMoveReaction() <./generated/PistonMoveReaction>
   class Player(HumanEntity, Conversable, PluginMessageRecipient) <./generated/Player>
   class PlayerEvent(Event) <./generated/PlayerEvent>
   class PlayerInteractAtEntityEvent(PlayerInteractEntityEvent) <./generated/PlayerInteractAtEntityEvent>
   class PlayerInteractEvent(Cancellable, PlayerEvent) <./generated/PlayerInteractEvent>
   class PlayerInventory(Inventory) <./generated/PlayerInventory>
   class Cause() <./generated/Cause>
   class PlayerProfile(ConfigurationSerializable) <./generated/PlayerProfile>
   class Status() <./generated/Status>
   class TeleportCause() <./generated/TeleportCause>
   class PlayerTextures() <./generated/PlayerTextures>
   class SkinModel() <./generated/SkinModel>
   class Plugin(TabExecutor) <./generated/Plugin>
   class PluginCommand(PluginIdentifiableCommand, Command) <./generated/PluginCommand>
   class PluginDescriptionFile() <./generated/PluginDescriptionFile>
   class PluginIdentifiableCommand() <./generated/PluginIdentifiableCommand>
   class PluginLoadOrder() <./generated/PluginLoadOrder>
   class PluginLoader() <./generated/PluginLoader>
   class PluginManager() <./generated/PluginManager>
   class PluginMessageListener() <./generated/PluginMessageListener>
   class PluginMessageListenerRegistration() <./generated/PluginMessageListenerRegistration>
   class PluginMessageRecipient() <./generated/PluginMessageRecipient>
   class PolarBear(Animals) <./generated/PolarBear>
   class Pose() <./generated/Pose>
   class PotionBrewer() <./generated/PotionBrewer>
   class PotionData() <./generated/PotionData>
   class PotionEffect(ConfigurationSerializable) <./generated/PotionEffect>
   class PotionEffectType() <./generated/PotionEffectType>
   class Category() <./generated/Category>
   class PotionMeta(ItemMeta) <./generated/PotionMeta>
   class PotionType() <./generated/PotionType>
   class Powerable(BlockData) <./generated/Powerable>
   class PoweredMinecart(Minecart) <./generated/PoweredMinecart>
   class Projectile(Entity) <./generated/Projectile>
   class ProjectileSource() <./generated/ProjectileSource>
   class PufferFish(Fish) <./generated/PufferFish>
   class Rabbit(Animals) <./generated/Rabbit>
   class Raid() <./generated/Raid>
   class RaidStatus() <./generated/RaidStatus>
   class Raider(Monster) <./generated/Raider>
   class Rail(Waterlogged) <./generated/Rail>
   class Shape() <./generated/Shape>
   class Ravager(Raider) <./generated/Ravager>
   class RayTraceResult() <./generated/RayTraceResult>
   class Recipe() <./generated/Recipe>
   class RedstoneRail(Powerable, Rail) <./generated/RedstoneRail>
   class RedstoneWallTorch(Directional, Lightable) <./generated/RedstoneWallTorch>
   class RedstoneWire(AnaloguePowerable) <./generated/RedstoneWire>
   class Connection() <./generated/Connection>
   class RegionAccessor() <./generated/RegionAccessor>
   class RegisteredListener() <./generated/RegisteredListener>
   class RegisteredServiceProvider() <./generated/RegisteredServiceProvider>
   class Registry() <./generated/Registry>
   class RenderType() <./generated/RenderType>
   class Repeater(Directional, Powerable) <./generated/Repeater>
   class RespawnAnchor(BlockData) <./generated/RespawnAnchor>
   class RideableMinecart(Minecart) <./generated/RideableMinecart>
   class Rotation() <./generated/Rotation>
   class SaddledHorseInventory(AbstractHorseInventory) <./generated/SaddledHorseInventory>
   class Salmon() <./generated/Salmon>
   class Sapling(BlockData) <./generated/Sapling>
   class Scaffolding(Waterlogged) <./generated/Scaffolding>
   class Score() <./generated/Score>
   class Scoreboard() <./generated/Scoreboard>
   class ScoreboardManager() <./generated/ScoreboardManager>
   class SeaPickle(Waterlogged) <./generated/SeaPickle>
   class Server(PluginMessageRecipient) <./generated/Server>
   class ServerOperator() <./generated/ServerOperator>
   class ServicePriority() <./generated/ServicePriority>
   class ServicesManager() <./generated/ServicesManager>
   class Sheep(Animals, Colorable) <./generated/Sheep>
   class Shulker(Golem, Colorable, Enemy) <./generated/Shulker>
   class ShulkerBullet(Projectile) <./generated/ShulkerBullet>
   class Sign(TileState, Colorable) <./generated/Sign>
   class Silverfish(Monster) <./generated/Silverfish>
   class Sittable() <./generated/Sittable>
   class SizedFireball(Fireball) <./generated/SizedFireball>
   class Skeleton(AbstractSkeleton) <./generated/Skeleton>
   class SkeletonType() <./generated/SkeletonType>
   class SkeletonHorse(AbstractHorse) <./generated/SkeletonHorse>
   class SkullMeta(ItemMeta) <./generated/SkullMeta>
   class Slab(Waterlogged) <./generated/Slab>
   class Slime(Mob, Enemy) <./generated/Slime>
   class SmallFireball(SizedFireball) <./generated/SmallFireball>
   class Sniffer(Animals) <./generated/Sniffer>
   class State() <./generated/State>
   class Snow(BlockData) <./generated/Snow>
   class Snowball(ThrowableProjectile) <./generated/Snowball>
   class Snowman(Golem) <./generated/Snowman>
   class Sound() <./generated/Sound>
   class SoundCategory() <./generated/SoundCategory>
   class SoundGroup() <./generated/SoundGroup>
   class SpawnCategory() <./generated/SpawnCategory>
   class SpawnEggMeta(ItemMeta) <./generated/SpawnEggMeta>
   class SpawnerMinecart(Minecart) <./generated/SpawnerMinecart>
   class SpectralArrow(AbstractArrow) <./generated/SpectralArrow>
   class Spellcaster(Illager) <./generated/Spellcaster>
   class Spell() <./generated/Spell>
   class Spider(Monster) <./generated/Spider>
   class Squid(WaterMob) <./generated/Squid>
   class Stairs(Bisected, Directional, Waterlogged) <./generated/Stairs>
   class Statistic() <./generated/Statistic>
   class Steerable(Animals) <./generated/Steerable>
   class StorageMinecart(Minecart, InventoryHolder) <./generated/StorageMinecart>
   class Stray(AbstractSkeleton) <./generated/Stray>
   class Strider(Steerable, Vehicle) <./generated/Strider>
   class Structure() <./generated/Structure>
   class StructureBlock(BlockData) <./generated/StructureBlock>
   class StructureManager() <./generated/StructureManager>
   class StructureRotation() <./generated/StructureRotation>
   class StructureSearchResult() <./generated/StructureSearchResult>
   class StructureType() <./generated/StructureType>
   class SuspiciousStewMeta(ItemMeta) <./generated/SuspiciousStewMeta>
   class Switch(Directional, FaceAttachable, Powerable) <./generated/Switch>
   class Face() <./generated/Face>
   class TNT(BlockData) <./generated/TNT>
   class TNTPrimed(Explosive) <./generated/TNTPrimed>
   class TabCompleter() <./generated/TabCompleter>
   class TabExecutor(TabCompleter, CommandExecutor) <./generated/TabExecutor>
   class Tadpole(Fish) <./generated/Tadpole>
   class Tag() <./generated/Tag>
   class Tameable(Animals) <./generated/Tameable>
   class Team() <./generated/Team>
   class Option() <./generated/Option>
   class OptionStatus() <./generated/OptionStatus>
   class TechnicalPiston(Directional) <./generated/TechnicalPiston>
   class TextDisplay(Display) <./generated/TextDisplay>
   class TextAlignment() <./generated/TextAlignment>
   class ThrowableProjectile(Projectile) <./generated/ThrowableProjectile>
   class ThrownExpBottle(ThrowableProjectile) <./generated/ThrownExpBottle>
   class ThrownPotion(ThrowableProjectile) <./generated/ThrownPotion>
   class TileState(BlockState, PersistentDataHolder) <./generated/TileState>
   class TraderLlama(Llama) <./generated/TraderLlama>
   class Transformation() <./generated/Transformation>
   class Translatable() <./generated/Translatable>
   class TrapDoor(Bisected, Directional, Openable, Powerable, Waterlogged) <./generated/TrapDoor>
   class TreeSpecies() <./generated/TreeSpecies>
   class TreeType() <./generated/TreeType>
   class Trident(AbstractArrow, ThrowableProjectile) <./generated/Trident>
   class Tripwire(Attachable, MultipleFacing, Powerable) <./generated/Tripwire>
   class TripwireHook(Attachable, Directional, Powerable) <./generated/TripwireHook>
   class TropicalFish() <./generated/TropicalFish>
   class Pattern() <./generated/Pattern>
   class TropicalFishBucketMeta(ItemMeta) <./generated/TropicalFishBucketMeta>
   class Turtle(Animals) <./generated/Turtle>
   class TurtleEgg(BlockData) <./generated/TurtleEgg>
   class UnsafeValues() <./generated/UnsafeValues>
   class Vector(ConfigurationSerializable) <./generated/Vector>
   class Vehicle(Entity) <./generated/Vehicle>
   class Vex(Monster) <./generated/Vex>
   class Villager(AbstractVillager) <./generated/Villager>
   class Profession() <./generated/Profession>
   class Type() <./generated/Type>
   class Vindicator(Illager) <./generated/Vindicator>
   class VoxelShape() <./generated/VoxelShape>
   class Wall(Waterlogged) <./generated/Wall>
   class Height() <./generated/Height>
   class WallSign(Directional, Waterlogged) <./generated/WallSign>
   class WanderingTrader(AbstractVillager) <./generated/WanderingTrader>
   class Warden(Monster) <./generated/Warden>
   class AngerLevel() <./generated/AngerLevel>
   class Warning() <./generated/Warning>
   class WarningState() <./generated/WarningState>
   class WaterMob(Creature) <./generated/WaterMob>
   class Waterlogged(BlockData) <./generated/Waterlogged>
   class WeatherType() <./generated/WeatherType>
   class Witch(Raider) <./generated/Witch>
   class Wither(Monster, Boss) <./generated/Wither>
   class Head() <./generated/Head>
   class WitherSkeleton(AbstractSkeleton) <./generated/WitherSkeleton>
   class WitherSkull(Fireball) <./generated/WitherSkull>
   class Wolf(Tameable, Sittable) <./generated/Wolf>
   class World(WorldInfo, PluginMessageRecipient, Metadatable, PersistentDataHolder) <./generated/World>
   class ChunkLoadCallback() <./generated/ChunkLoadCallback>
   class Environment() <./generated/Environment>
   class WorldBorder() <./generated/WorldBorder>
   class WorldCreator() <./generated/WorldCreator>
   class WorldInfo() <./generated/WorldInfo>
   class WorldType() <./generated/WorldType>
   class Zoglin(Monster, Ageable) <./generated/Zoglin>
   class Zombie(Monster, Ageable) <./generated/Zombie>
   class ZombieHorse(AbstractHorse) <./generated/ZombieHorse>
   class ZombieVillager(Zombie) <./generated/ZombieVillager>

Generated 2023-05-27