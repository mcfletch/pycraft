package com.vrplumber.pycraft.bukkitserver;

import com.vrplumber.pycraft.bukkitserver.APIServer;
import com.vrplumber.pycraft.bukkitserver.MessageHandler;
import com.vrplumber.pycraft.bukkitserver.EchoHandler;
import com.vrplumber.pycraft.bukkitserver.WorldHandler;
// import com.vrplumber.pycraft.bukkitserver.EntityHandler;
import com.vrplumber.pycraft.bukkitserver.PycraftMessage;
import com.vrplumber.pycraft.bukkitserver.IHandlerRegistry;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import org.bukkit.Location;
import org.bukkit.Material;
import org.bukkit.OfflinePlayer;
import org.bukkit.Server;
import org.bukkit.block.Biome;
import org.bukkit.block.Block;
import org.bukkit.block.BlockFace;
import org.bukkit.block.PistonMoveReaction;
import org.bukkit.block.data.BlockData;
import org.bukkit.enchantments.Enchantment;
import org.bukkit.entity.EntityType;
import org.bukkit.entity.Player;
import org.bukkit.inventory.Inventory;
import org.bukkit.inventory.ItemStack;
import org.bukkit.plugin.java.JavaPlugin;
import org.bukkit.util.Vector;

import java.util.HashMap;
import java.util.logging.Handler;
import org.bukkit.block.data.type.*;

import javax.swing.text.html.parser.Entity;

class HandlerRegistry implements IHandlerRegistry {
    private static List<Class> handlers;

    static {
        handlers = new ArrayList<Class>();
        handlers.add(EchoHandler.class);
        handlers.add(WorldHandler.class);
        handlers.add(SubscriptionHandler.class);
        // handlers.add(EntityHandler.class);
    }

    private static HandlerRegistry instance = null;

    static public HandlerRegistry getInstance() {
        if (instance == null) {
            instance = new HandlerRegistry();
        }
        return instance;
    }

    public HashMap<String, MessageHandler> implementations;

    public HandlerRegistry() {
        implementations = new HashMap<String, MessageHandler>();
    }

    public void registerImplementation(String name, MessageHandler payload) {
        implementations.put(name, payload);
        payload.register(this);
    }

    public List<String> namespaceMethods(Map<String, MessageHandler> subcommands) {
        List<String> response = new ArrayList<String>();
        for (String key : subcommands.keySet()) {
            MessageHandler handler = subcommands.get(key);
            response.add(String.format("%s => %s", key, handler.getDescription()));
        }
        return response;
    }

    public void registerHandlers() {
        for (EntityType entityType : EntityType.values()) {
            GenericHandler handler = new GenericHandler(entityType.getEntityClass());
            if (handler.cls != null) {
                registerImplementation(handler.getMethod(), handler);
            }
        }
        registerImplementation("Player", new GenericHandler(Player.class));
        registerImplementation("OfflinePlayer", new GenericHandler(OfflinePlayer.class));
        registerImplementation("BlockData", new GenericHandler(BlockData.class));
        registerImplementation("Block", new GenericHandler(Block.class));
        registerImplementation("Material", new GenericHandler(Material.class));
        registerImplementation("Location", new GenericHandler(Location.class));
        registerImplementation("Vector", new GenericHandler(Vector.class));
        registerImplementation("ItemStack", new GenericHandler(ItemStack.class));
        registerImplementation("Inventory", new GenericHandler(Inventory.class));
        registerImplementation("Enchantment", new GenericHandler(Enchantment.class));
        registerImplementation("Entity", new GenericHandler(Entity.class));
        registerImplementation("EntityType", new GenericHandler(EntityType.class));
        registerImplementation("Server", new GenericHandler(Server.class));
        registerImplementation("Biome", new GenericHandler(Biome.class));
        registerImplementation("BlockFace", new GenericHandler(BlockFace.class));
        registerImplementation("PistonMoveReaction", new GenericHandler(PistonMoveReaction.class));

        registerImplementation("Bamboo", new GenericHandler(Bamboo.class));
        registerImplementation("Bed", new GenericHandler(Bed.class));
        registerImplementation("Beehive", new GenericHandler(Beehive.class));
        registerImplementation("Bell", new GenericHandler(Bell.class));
        registerImplementation("BrewingStand", new GenericHandler(BrewingStand.class));
        registerImplementation("BubbleColumn", new GenericHandler(BubbleColumn.class));
        registerImplementation("Cake", new GenericHandler(Cake.class));
        registerImplementation("Campfire", new GenericHandler(Campfire.class));
        registerImplementation("Chain", new GenericHandler(Chain.class));
        registerImplementation("Chest", new GenericHandler(Chest.class));
        registerImplementation("Cocoa", new GenericHandler(Cocoa.class));
        registerImplementation("CommandBlock", new GenericHandler(CommandBlock.class));
        registerImplementation("Comparator", new GenericHandler(Comparator.class));
        registerImplementation("CoralWallFan", new GenericHandler(CoralWallFan.class));
        registerImplementation("DaylightDetector", new GenericHandler(DaylightDetector.class));
        registerImplementation("Dispenser", new GenericHandler(Dispenser.class));
        registerImplementation("Door", new GenericHandler(Door.class));
        registerImplementation("EnderChest", new GenericHandler(EnderChest.class));
        registerImplementation("EndPortalFrame", new GenericHandler(EndPortalFrame.class));
        registerImplementation("Farmland", new GenericHandler(Farmland.class));
        registerImplementation("Fence", new GenericHandler(Fence.class));
        registerImplementation("Fire", new GenericHandler(Fire.class));
        registerImplementation("Furnace", new GenericHandler(Furnace.class));
        registerImplementation("Gate", new GenericHandler(Gate.class));
        registerImplementation("GlassPane", new GenericHandler(GlassPane.class));
        registerImplementation("Grindstone", new GenericHandler(Grindstone.class));
        registerImplementation("Hopper", new GenericHandler(Hopper.class));
        registerImplementation("Jigsaw", new GenericHandler(Jigsaw.class));
        registerImplementation("Jukebox", new GenericHandler(Jukebox.class));
        registerImplementation("Ladder", new GenericHandler(Ladder.class));
        registerImplementation("Lantern", new GenericHandler(Lantern.class));
        registerImplementation("Leaves", new GenericHandler(Leaves.class));
        registerImplementation("Lectern", new GenericHandler(Lectern.class));
        registerImplementation("NoteBlock", new GenericHandler(NoteBlock.class));
        registerImplementation("Observer", new GenericHandler(Observer.class));
        registerImplementation("Piston", new GenericHandler(Piston.class));
        registerImplementation("PistonHead", new GenericHandler(PistonHead.class));
        registerImplementation("RedstoneRail", new GenericHandler(RedstoneRail.class));
        registerImplementation("RedstoneWallTorch", new GenericHandler(RedstoneWallTorch.class));
        registerImplementation("RedstoneWire", new GenericHandler(RedstoneWire.class));
        registerImplementation("Repeater", new GenericHandler(Repeater.class));
        registerImplementation("RespawnAnchor", new GenericHandler(RespawnAnchor.class));
        registerImplementation("Sapling", new GenericHandler(Sapling.class));
        registerImplementation("Scaffolding", new GenericHandler(Scaffolding.class));
        registerImplementation("SeaPickle", new GenericHandler(SeaPickle.class));
        registerImplementation("Sign", new GenericHandler(Sign.class));
        registerImplementation("Slab", new GenericHandler(Slab.class));
        registerImplementation("Snow", new GenericHandler(Snow.class));
        registerImplementation("Stairs", new GenericHandler(Stairs.class));
        registerImplementation("StructureBlock", new GenericHandler(StructureBlock.class));
        registerImplementation("Switch", new GenericHandler(Switch.class));
        registerImplementation("TechnicalPiston", new GenericHandler(TechnicalPiston.class));
        registerImplementation("TNT", new GenericHandler(TNT.class));
        registerImplementation("TrapDoor", new GenericHandler(TrapDoor.class));
        registerImplementation("Tripwire", new GenericHandler(Tripwire.class));
        registerImplementation("TripwireHook", new GenericHandler(TripwireHook.class));
        registerImplementation("TurtleEgg", new GenericHandler(TurtleEgg.class));
        registerImplementation("Wall", new GenericHandler(Wall.class));
        registerImplementation("WallSign", new GenericHandler(WallSign.class));

        for (Class handlerCls : handlers) {
            try {
                MessageHandler handler = (MessageHandler) (handlerCls.getDeclaredConstructor().newInstance());
                if (handler == null) {
                    // getLogger().warning(String.format("Unable to create %s instance",
                    // handlerCls.getName()));
                    continue;
                }
                // getLogger().info(
                // String.format("Registering command %s", handler.getMethod()));
                registerImplementation(handler.getMethod(), handler);

            } catch (Exception err) {
                err.printStackTrace();
            }
        }
    }

    public MessageHandler getHandler(String name) {
        return implementations.get(name);
    }

    public List<String> getMethodDescriptions() {
        return namespaceMethods(implementations);
    }
}