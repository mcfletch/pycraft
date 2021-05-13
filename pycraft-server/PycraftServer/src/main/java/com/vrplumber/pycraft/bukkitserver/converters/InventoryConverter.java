package com.vrplumber.pycraft.bukkitserver.converters;

import java.lang.Math;
import java.lang.reflect.Constructor;
import java.security.InvalidParameterException;
import com.vrplumber.pycraft.bukkitserver.PycraftAPI;
import com.vrplumber.pycraft.bukkitserver.converters.Converter;
import com.vrplumber.pycraft.bukkitserver.converters.VectorConverter;
import java.util.List;
import java.util.Map;
import java.util.HashMap;
import java.util.UUID;
import java.util.stream.Collectors;
import java.util.stream.Stream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.stream.IntStream;
import java.util.stream.DoubleStream;

import org.bukkit.Location;
import org.bukkit.Material;
import org.bukkit.inventory.Inventory;
import org.bukkit.inventory.InventoryHolder;
import org.bukkit.World;
import org.bukkit.block.Block;
import org.bukkit.entity.Entity;

public class InventoryConverter implements Converter {
    /* Given a message and an index convert the value to an instance of T */
    PycraftConverterRegistry registry = null;

    InventoryConverter(PycraftConverterRegistry registry) {
        this.registry = registry;
    }

    public Object toJava(PycraftAPI api, Object value, Class finalType) {
        InventoryHolder holder = null;
        if (value instanceof List<?>) {
            Location loc = (Location) registry.toJava(Location.class, api, value);
            Block block = loc.getBlock();
            if (block == null) {
                throw new InvalidParameterException(String.format("Could not find block", loc.toString()));
            }

            if (!(block instanceof InventoryHolder)) {
                throw new InvalidParameterException(
                        String.format("Block %s does not have inventory", block.toString()));
            }
            holder = (InventoryHolder) block;
        } else if (value instanceof String) {
            Entity entity = (Entity) registry.toJava(Entity.class, api, value);
            if (entity == null) {
                throw new InvalidParameterException(
                        String.format("Could not find Entity with name/uuid %s", value.toString()));
            }
            if (!(entity instanceof InventoryHolder)) {
                throw new InvalidParameterException(
                        String.format("Entity %s does not have inventory", entity.toString()));
            }
            holder = (InventoryHolder) entity;
        } else {
            throw new InvalidParameterException(
                    String.format("Need entity UUID or Block [world,x,y,z] location", value.toString()));

        }
        return holder.getInventory();
    }

    public String fromJava(PycraftAPI api, Object value) {
        Inventory inventory = (Inventory) value;
        Map<String, Object> asMap = new HashMap<String, Object>();
        asMap.put("__type__", inventory.getClass().getSimpleName());
        asMap.put("__namespace__", "Inventory");
        asMap.put("type", inventory.getType().name());
        asMap.put("holder", inventory.getHolder());
        asMap.put("contents", Arrays.asList(inventory.getContents()));
        asMap.put("size", inventory.getSize());
        asMap.put("firstEmpty", inventory.firstEmpty());
        return registry.fromJava(api, asMap);
    }
}
