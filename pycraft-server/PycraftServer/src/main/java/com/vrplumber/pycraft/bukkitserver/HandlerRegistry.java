package com.vrplumber.pycraft.bukkitserver;

import com.vrplumber.pycraft.bukkitserver.APIServer;
import com.vrplumber.pycraft.bukkitserver.EchoHandler;
import com.vrplumber.pycraft.bukkitserver.WorldHandler;
import com.vrplumber.pycraft.bukkitserver.EntityHandler;
import com.vrplumber.pycraft.bukkitserver.MessageHandler;
import com.vrplumber.pycraft.bukkitserver.PycraftMessage;
import com.vrplumber.pycraft.bukkitserver.IHandlerRegistry;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import org.bukkit.Material;
import org.bukkit.block.Block;
import org.bukkit.block.data.BlockData;
import org.bukkit.entity.EntityType;
import org.bukkit.entity.Player;
import org.bukkit.inventory.Inventory;
import org.bukkit.inventory.ItemStack;
import org.bukkit.plugin.java.JavaPlugin;
import java.util.HashMap;
import java.util.logging.Handler;

class HandlerRegistry implements IHandlerRegistry {
    private static List<Class> handlers;

    static {
        handlers = new ArrayList<Class>();
        handlers.add(EchoHandler.class);
        handlers.add(WorldHandler.class);
        handlers.add(SubscriptionHandler.class);
        handlers.add(EntityHandler.class);
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
        registerImplementation("BlockData", new GenericHandler(BlockData.class));
        registerImplementation("Block", new GenericHandler(Block.class));
        registerImplementation("ItemStack", new GenericHandler(ItemStack.class));
        registerImplementation("Inventory", new GenericHandler(Inventory.class));
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