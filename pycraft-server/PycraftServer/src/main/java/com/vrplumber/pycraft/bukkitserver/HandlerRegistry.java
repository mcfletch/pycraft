package com.vrplumber.pycraft.bukkitserver;

import java.lang.reflect.Method;
import java.lang.reflect.Type;
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

import org.bukkit.Art;
import org.bukkit.Fluid;
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
import org.bukkit.entity.Entity;
import org.bukkit.entity.EntityType;
import org.bukkit.entity.Player;
import org.bukkit.inventory.Inventory;
import org.bukkit.inventory.InventoryHolder;
import org.bukkit.inventory.ItemStack;
import org.bukkit.plugin.java.JavaPlugin;
import org.bukkit.util.Vector;

import java.util.HashMap;
import java.util.logging.Handler;
import org.bukkit.block.data.type.*;

class HandlerRegistry implements IHandlerRegistry {
    private static List<Class> handlers;

    static {
        handlers = new ArrayList<Class>();
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

    public Map<String, Object> getDescription() {
        Map<String, Object> result = new HashMap<String, Object>();
        result.put("type", "namespace");
        result.put("name", "");
        List<Map<String, Object>> commands = new ArrayList<Map<String, Object>>();
        for (String key : implementations.keySet()) {
            MessageHandler handler = implementations.get(key);
            commands.add(handler.getDescription());
        }
        result.put("commands", commands);
        return result;
    }

    public void exposeClass(Class cls) {
        /* Expose the class, its interfaces and any return types it needs */
        if (cls == null) {
            return;
        }
        String name = cls.getSimpleName();
        if (implementations.get(name) == null) {
            registerImplementation(cls.getSimpleName(), new GenericHandler(cls));
            for (Class interfaceClass : cls.getInterfaces()) {
                if (interfaceClass.getPackage() != null
                        && interfaceClass.getPackage().getName().startsWith("org.bukkit")) {
                    exposeClass(interfaceClass);
                }
            }
            for (java.lang.reflect.Method method : cls.getMethods()) {
                Class returnType = method.getReturnType();
                if (!returnType.isPrimitive()) {
                    if (returnType.getPackage() != null && returnType.getPackage().getName().startsWith("org.bukkit")) {
                        exposeClass(returnType);
                    }
                }
                for (Class paramType : method.getParameterTypes()) {
                    if (!paramType.isPrimitive()) {
                        if (paramType.getPackage() != null
                                && paramType.getPackage().getName().startsWith("org.bukkit")) {
                            exposeClass(paramType);
                        }
                    }
                }
            }
        }

    }

    public void registerHandlers() {

        for (EntityType entityType : EntityType.values()) {
            exposeClass(entityType.getEntityClass());
        }
        exposeClass(Player.class);
        exposeClass(OfflinePlayer.class);
        exposeClass(BlockData.class);
        exposeClass(Block.class);
        exposeClass(Material.class);
        exposeClass(Location.class);
        exposeClass(Vector.class);
        exposeClass(ItemStack.class);
        exposeClass(Inventory.class);
        exposeClass(InventoryHolder.class);
        exposeClass(Enchantment.class);
        exposeClass(Entity.class);
        exposeClass(EntityType.class);
        exposeClass(Server.class);
        exposeClass(Biome.class);
        exposeClass(BlockFace.class);
        exposeClass(PistonMoveReaction.class);
        exposeClass(Art.class);
        exposeClass(Fluid.class);
        exposeClass(Bamboo.class);
        exposeClass(Bed.class);
        exposeClass(Beehive.class);
        exposeClass(Bell.class);
        exposeClass(BrewingStand.class);
        exposeClass(BubbleColumn.class);
        exposeClass(Cake.class);
        exposeClass(Campfire.class);
        exposeClass(Chain.class);
        exposeClass(Chest.class);
        exposeClass(Cocoa.class);
        exposeClass(CommandBlock.class);
        exposeClass(Comparator.class);
        exposeClass(CoralWallFan.class);
        exposeClass(DaylightDetector.class);
        exposeClass(Dispenser.class);
        exposeClass(Door.class);
        exposeClass(EnderChest.class);
        exposeClass(EndPortalFrame.class);
        exposeClass(Farmland.class);
        exposeClass(Fence.class);
        exposeClass(Fire.class);
        exposeClass(Furnace.class);
        exposeClass(Gate.class);
        exposeClass(GlassPane.class);
        exposeClass(Grindstone.class);
        exposeClass(Hopper.class);
        exposeClass(Jigsaw.class);
        exposeClass(Jukebox.class);
        exposeClass(Ladder.class);
        exposeClass(Lantern.class);
        exposeClass(Leaves.class);
        exposeClass(Lectern.class);
        exposeClass(NoteBlock.class);
        exposeClass(Observer.class);
        exposeClass(Piston.class);
        exposeClass(PistonHead.class);
        exposeClass(RedstoneRail.class);
        exposeClass(RedstoneWallTorch.class);
        exposeClass(RedstoneWire.class);
        exposeClass(Repeater.class);
        exposeClass(RespawnAnchor.class);
        exposeClass(Sapling.class);
        exposeClass(Scaffolding.class);
        exposeClass(SeaPickle.class);
        exposeClass(Sign.class);
        exposeClass(Slab.class);
        exposeClass(Snow.class);
        exposeClass(Stairs.class);
        exposeClass(StructureBlock.class);
        exposeClass(Switch.class);
        exposeClass(TechnicalPiston.class);
        exposeClass(TNT.class);
        exposeClass(TrapDoor.class);
        exposeClass(Tripwire.class);
        exposeClass(TripwireHook.class);
        exposeClass(TurtleEgg.class);
        exposeClass(Wall.class);
        exposeClass(WallSign.class);

        registerImplementation("World", new WorldHandler());
        registerImplementation("echo", new EchoHandler());
        registerImplementation("subscribe", new SubscriptionHandler());
    }

    public MessageHandler getHandler(String name) {
        return implementations.get(name);
    }
}