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
    public BlockData setBlocks(World world, Vector start, Vector size, BlockData data) {
        /* Set blocks starting at start for (x,y,z) size to given blockdata */
        Location setter = new Location(world, start.getBlockX(), start.getBlockY(), start.getBlockZ());
        int x_start = start.getBlockX();
        int y_start = start.getBlockY();
        int z_start = start.getBlockZ();
        for (int y = 0; y < size.getY(); y++) {
            setter.setY(y_start + y);
            for (int z = 0; z < size.getZ(); z++) {
                setter.setZ(z_start + z);
                for (int x = 0; x < size.getX(); x++) {
                    setter.setX(x_start + x);
                    setter.getBlock().setBlockData(data);
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

}