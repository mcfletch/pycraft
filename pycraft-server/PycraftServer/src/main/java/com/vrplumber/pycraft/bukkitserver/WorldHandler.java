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

    public WorldHandler() {
        super(World.class);
    }

    private List<String> error(PycraftMessage message, String category, String description) {
        List<String> response = Arrays.asList(category, description);
        return response;
    }

    @InjectedMethod
    @HelperMethod
    static public List<List<List<String>>> getBlocks(World world, Vector start, Vector size) {
        Location getter = new Location(world, start.getBlockX(), start.getBlockY(), start.getBlockZ());
        int x_start = start.getBlockX();
        int y_start = start.getBlockY();
        int z_start = start.getBlockZ();
        List<List<List<String>>> result = new ArrayList<List<List<String>>>();
        for (int y = 0; y < size.getY(); y++) {
            List<List<String>> slab = new ArrayList<List<String>>();
            getter.setY(y_start + y);
            for (int z = 0; z < size.getZ(); z++) {
                List<String> row = new ArrayList<String>();
                getter.setZ(z_start + z);
                for (int x = 0; x < size.getX(); x++) {
                    getter.setX(x_start + x);
                    BlockData data = getter.getBlock().getBlockData();
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

    @HelperMethod
    @InjectedMethod
    public void breakBlocks(World world, Vector start, Vector size) {
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
                    setter.getBlock().breakNaturally();
                }
            }
        }
    }

    @HelperMethod
    @InjectedMethod
    public int setBlockList(World world, Location[] locations, BlockData[] datas) {
        int count = 0;
        for (Location location : locations) {
            Block block = location.getBlock();
            if (block != null) {
                BlockData blockData = datas[count];
                if (blockData != null) {
                    block.setBlockData(blockData);
                } else {
                    throw new InvalidParameterException(String.format("Missing blockData at index %d", count));
                }
            } else {
                throw new InvalidParameterException(String.format("Unable to resolve location at index %d", count));
            }
            count += 1;
        }
        return count;
    }

    public void register(HandlerRegistry registry) {
        /* Called when we are registered with the registry (api likely not up yet) */
        for (MessageHandler handler : MethodHandler.forClass(World.class)) {
            this.addHandler(handler.getMethod(), handler);
        }
        MethodHandler.forHandler(World.class, this);

    }

}