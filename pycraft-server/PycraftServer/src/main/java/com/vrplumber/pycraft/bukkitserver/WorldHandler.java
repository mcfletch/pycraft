package com.vrplumber.pycraft.bukkitserver;

import com.vrplumber.pycraft.bukkitserver.NamespaceHandler;
import com.vrplumber.pycraft.bukkitserver.MessageHandler;
import com.vrplumber.pycraft.bukkitserver.PycraftAPI;
import com.vrplumber.pycraft.bukkitserver.PycraftMessage;
import java.lang.Math;
import java.util.List;
import java.util.Arrays;
import java.security.InvalidParameterException;
import java.util.ArrayList;
import org.bukkit.Server;
import org.bukkit.World;
import org.bukkit.util.Vector;
import org.bukkit.Location;
import org.bukkit.block.data.BlockData;
import org.bukkit.block.Block;
import org.bukkit.entity.Entity;
import org.bukkit.entity.EntityType;
import org.bukkit.entity.Player;

public class WorldHandler extends NamespaceHandler {
    /* Interface for things which need to handle messages */
    public String getMethod() {
        return "World";
    }

    private List<String> error(PycraftMessage message, String category, String description) {
        List<String> response = Arrays.asList(category, description);
        return response;
    }

    public Object getWorlds(PycraftAPI api, PycraftMessage message) {
        List<String> names = new ArrayList<String>();
        for (World world : api.getPlugin().getServer().getWorlds()) {
            names.add(world.getName());
        }
        return (Object) names;
    }

    public Object setWorld(PycraftAPI api, PycraftMessage message) {
        /* Set the world on which we will operate */
        String name = api.expectString(message, 0);
        if (name != null) {
            api.setWorld(name);
        }
        return (Object) name;
    }

    public Object getWorld(PycraftAPI api, PycraftMessage message) {
        /* Get the current world, it not yet set, set to the first world */
        World world = api.getWorld();
        if (world != null) {
            return (Object) world.getName();
        } else {
            return null;
        }
    }

    public Object getBlock(PycraftAPI api, PycraftMessage message) {
        World world = api.getWorld();
        Vector vec = api.expectVector(message, 0);
        Location loc = new Location(world, vec.getX(), vec.getY(), vec.getZ());
        return loc.getBlock();
    }

    public Object setBlock(PycraftAPI api, PycraftMessage message) {
        World world = api.getWorld();
        Vector vec = api.expectVector(message, 0);
        Location loc = new Location(world, vec.getX(), vec.getY(), vec.getZ());
        BlockData data = api.expectBlockData(message, 1);
        return loc.getBlock();
    }

    public Object setBlocks(PycraftAPI api, PycraftMessage message) {
        World world = api.getWorld();
        Vector start = api.expectVector(message, 0);
        Vector end = api.expectVector(message, 1);
        BlockData data = api.expectBlockData(message, 2);
        Location setter = new Location(world, start.getBlockX(), start.getBlockY(), start.getBlockZ());
        int dx = end.getBlockX() - start.getBlockX(), dy = end.getBlockY() - start.getBlockY(),
                dz = end.getBlockZ() - start.getBlockZ();
        int xstep = 0, ystep = 0, zstep = 0;
        if (dx != 0) {
            xstep = dx / Math.abs(dx);
        }
        if (dy != 0) {
            ystep = dy / Math.abs(dy);
        }
        if (dz != 0) {
            zstep = dz / Math.abs(dz);
        }

        for (int x = 0; x < dx; x += xstep) {
            for (int y = 0; y < dy; y += ystep) {
                for (int z = 0; z < dz; z += zstep) {
                    Location tmp = setter.add(x, y, z);
                    tmp.getBlock().setBlockData(data);
                }
            }
        }
        return Arrays.asList(start, end, data);
    }

    public Object spawnEntity(PycraftAPI api, PycraftMessage message) {
        World world = api.getWorld();
        Vector vec = api.expectVector(message, 0);
        Location loc = new Location(world, vec.getX(), vec.getY(), vec.getZ());
        EntityType eType = api.expectEntityType(message, 1);
        return api.getWorld().spawnEntity(loc, eType);
    }

    public void register(HandlerRegistry registry) {
        /* Called when we are registered with the registry (api likely not up yet) */
        for (MessageHandler handler : MethodHandler.forClass(World.class)) {
            this.addHandler(handler.getMethod(), handler);
        }

    }

    public String postToChat(PycraftAPI api, PycraftMessage message) {
        World world = api.getWorld();
        String chat = api.expectString(message, 0);
        for (Player p : world.getPlayers()) {
            p.sendMessage(chat);
        }
        return chat;
    }

    public Object handle(PycraftAPI api, PycraftMessage message) {
        String name = message.nextName();
        Object result = null;
        boolean handled = false;
        if (name.equals("getWorlds")) {
            result = getWorlds(api, message);
            handled = true;
        } else if (name.equals("setWorld")) {
            result = setWorld(api, message);
            handled = true;
        } else if (name.equals("getWorld")) {
            result = getWorld(api, message);
            handled = true;
        } else if (name.equals("getBlock")) {
            result = getBlock(api, message);
            handled = true;
        } else if (name.equals("setBlock")) {
            result = setBlock(api, message);
            handled = true;
        } else if (name.equals("setBlocks")) {
            result = setBlocks(api, message);
            handled = true;
        } else if (name.equals("spawnEntity")) {
            result = spawnEntity(api, message);
            handled = true;
        } else if (name.equals("postToChat")) {
            result = postToChat(api, message);
            handled = true;
        } else {
            /* Registered method on the current World */
            MessageHandler subHandler = getHandler(name);
            if (subHandler != null) {
                if (subHandler instanceof MethodHandler) {
                    MethodHandler subMethod = (MethodHandler) subHandler;
                    if (subMethod.cls == World.class) {
                        message.instance = api.getWorld();
                    }
                }
                result = subHandler.handle(api, message);
                handled = true;
            }
        }
        if (handled) {
            // api.sendResponse(message.messageId, result);
            return result;
        } else {
            throw new InvalidParameterException(String.format("unknown-method %s", name));
        }
    };
}