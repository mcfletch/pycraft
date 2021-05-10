package com.vrplumber.pycraft.bukkitserver.converters;

import java.lang.Math;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.lang.Enum;
import java.security.InvalidParameterException;
import java.util.List;
import java.util.Map;
import java.util.HashMap;
import java.util.Arrays;
import org.bukkit.block.Block;
import org.bukkit.util.Vector;
import org.bukkit.Location;

import com.vrplumber.pycraft.bukkitserver.PycraftAPI;
import com.vrplumber.pycraft.bukkitserver.converters.Converter;

public class BlockConverter implements Converter {
    /* Given a message and an index convert the value to an instance of T */
    PycraftConverterRegistry registry;

    BlockConverter(PycraftConverterRegistry registry) {
        this.registry = registry;
    }

    public Object toJava(PycraftAPI api, Object value, Class finalType) {
        if (value instanceof List<?>) {
            Vector vector = (Vector) registry.toJava(Vector.class, api, value);
            Block block = api.getWorld().getBlockAt(vector.getBlockX(), vector.getBlockY(), vector.getBlockZ());
            return block;
        }
        throw new InvalidParameterException(
                String.format("Need a 3-element list of coordinates, got %s", value.toString()));
    }

    public Map<String, Object> blockAsMapping(PycraftAPI api, Object value) {
        org.bukkit.block.Block asBlock = (Block) value;
        Location loc = asBlock.getLocation();
        Map<String, Object> asMap = new HashMap<String, Object>();
        asMap.put("world", asBlock.getWorld().getName());
        asMap.put("location", loc);
        asMap.put("material", asBlock.getBlockData());
        return asMap;
    }

    public String fromJava(PycraftAPI api, Object value) {
        return registry.fromJava(api, blockAsMapping(api, value));
    }
}
