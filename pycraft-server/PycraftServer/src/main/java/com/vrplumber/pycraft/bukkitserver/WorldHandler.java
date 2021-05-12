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
import org.bukkit.Material;
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
        return api.getPlugin().getServer().getWorlds();
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
        World world = (World) api.expectType(message, 0, World.class, true);
        if (world == null) {
            return api.getWorld();
        }
        return world;
    }

    public Object getBlock(PycraftAPI api, PycraftMessage message) {
        Location loc = (Location) api.expectType(message, 0, Location.class);
        return loc.getBlock();
    }

    public Object setBlock(PycraftAPI api, PycraftMessage message) {
        Location loc = (Location) api.expectType(message, 0, Location.class);
        BlockData data = (BlockData) api.expectType(message, 1, BlockData.class);
        if (data == null) {
            throw new InvalidParameterException(
                    String.format("Unable to resolve the blockdata value %s", message.payload.get(1)));
        }
        loc.getBlock().setBlockData(data);
        return data;
    }

    public Object setBlocks(PycraftAPI api, PycraftMessage message) {
        World world = (World) api.expectType(message, 0, World.class, true);
        Vector start = (Vector) api.expectType(message, 1, Vector.class);
        Vector end = (Vector) api.expectType(message, 2, Vector.class);
        BlockData data = (BlockData) api.expectType(message, 3, BlockData.class);

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
        Location loc = (Location) api.expectType(message, 0, Location.class);
        EntityType eType = (EntityType) api.expectType(message, 1, EntityType.class);
        return api.getWorld().spawnEntity(loc, eType);
    }

    public void register(HandlerRegistry registry) {
        /* Called when we are registered with the registry (api likely not up yet) */
        for (MessageHandler handler : MethodHandler.forClass(World.class)) {
            this.addHandler(handler.getMethod(), handler);
        }
        // for (MessageHandler handler :
        // MethodHandler.forClass(WorldHandler.class,Arrays.asList({
        // "getWorlds"
        // }))) {
        // this.addHandler(handler.getMethod(), handler);
        // }

    }

    public String postToChat(PycraftAPI api, PycraftMessage message) {
        World world = api.getWorld();
        String chat = api.expectString(message, 0);
        for (Player p : world.getPlayers()) {
            p.sendMessage(chat);
        }
        return chat;
    }

    public Object getMaterialTypes(PycraftAPI api, PycraftMessage message) {
        // Get set of all materials for reference by the client-side software
        List<String> result = new ArrayList<String>();
        for (Material material : Material.values()) {
            // So *how* do you go about supporting all materials without
            // relying on deprecated legacy prefix???
            if (!material.name().startsWith(Material.LEGACY_PREFIX)) {
                result.add(material.getKey().toString());
            }
        }
        return result;
    }

    public Object getEntityTypes(PycraftAPI api, PycraftMessage message) {
        // Get set of all materials for reference by the client-side software
        List<String> result = new ArrayList<String>();
        for (EntityType entityType : EntityType.values()) {
            if (entityType != EntityType.UNKNOWN) {
                result.add(entityType.getKey().toString());
            }
        }
        return result;
    }

    @Override
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
        } else if (name.equals("getMaterialTypes")) {
            result = getMaterialTypes(api, message);
            handled = true;
        } else if (name.equals("getEntityTypes")) {
            result = getEntityTypes(api, message);
            handled = true;
        } else {
            return super.handle(api, message);
        }
        if (handled) {
            // api.sendResponse(message.messageId, result);
            return result;
        } else {
            throw new InvalidParameterException(String.format("unknown-method %s", name));
        }
    };
}