package com.vrplumber.pycraft.bukkitserver;

import com.vrplumber.pycraft.bukkitserver.NamespaceHandler;
import com.vrplumber.pycraft.bukkitserver.MessageHandler;
import com.vrplumber.pycraft.bukkitserver.PycraftAPI;
import com.vrplumber.pycraft.bukkitserver.PycraftMessage;
import com.vrplumber.pycraft.bukkitserver.HelperMethod;
import com.vrplumber.pycraft.bukkitserver.InjectedMethod;
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

    @InjectedMethod
    @HelperMethod
    static public List<List<List<String>>> getBlocks(World world, Vector start, Vector end) {
        Location getter = new Location(world, start.getBlockX(), start.getBlockY(), start.getBlockZ());
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
        List<List<List<String>>> result = new ArrayList<List<List<String>>>();
        for (int y = 0; y < dy; y += ystep) {
            List<List<String>> slab = new ArrayList<List<String>>();
            for (int z = 0; z < dz; z += zstep) {
                List<String> row = new ArrayList<String>();
                for (int x = 0; x < dx; x += xstep) {
                    Location tmp = getter.add(x, y, z);
                    BlockData data = tmp.getBlock().getBlockData();
                    try {
                        row.add(data.getAsString());
                    } catch (Exception err) {
                        row.add(data.getMaterial().getKey().toString());
                    }
                }
                slab.add(row);
            }
            result.add(slab);
        }
        return result;
    }

    @HelperMethod
    @InjectedMethod
    public BlockData setBlocks(World world, Vector start, Vector end, BlockData data) {
        /* Set Blocks to the given BlockData value */
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

        for (int y = 0; y < dy; y += ystep) {
            for (int z = 0; z < dz; z += zstep) {
                for (int x = 0; x < dx; x += xstep) {
                    Location tmp = setter.add(x, y, z);
                    tmp.getBlock().setBlockData(data);
                }
            }
        }
        return data;
    }

    public void register(HandlerRegistry registry) {
        /* Called when we are registered with the registry (api likely not up yet) */
        for (MessageHandler handler : MethodHandler.forClass(World.class)) {
            this.addHandler(handler.getMethod(), handler);
        }
        MethodHandler.forHandler(World.class, this);

    }

    @HelperMethod
    @InjectedMethod
    public List<Material> getMaterialTypes() {
        /* Get all *non-legacy* material types */
        List<Material> result = new ArrayList<Material>();
        for (Material material : Material.values()) {
            // So *how* do you go about supporting all materials without
            // relying on deprecated legacy prefix???
            if (!material.name().startsWith(Material.LEGACY_PREFIX)) {
                result.add(material);
            }
        }
        return result;
    }

    @HelperMethod
    @InjectedMethod
    public List<EntityType> getEntityTypes() {
        /*
         * Get set of all materials for reference by the client-side software (filtering
         * unknown)
         */
        List<EntityType> result = new ArrayList<EntityType>();
        for (EntityType entityType : EntityType.values()) {
            if (entityType != EntityType.UNKNOWN) {
                result.add(entityType);
            }
        }
        return result;
    }

}