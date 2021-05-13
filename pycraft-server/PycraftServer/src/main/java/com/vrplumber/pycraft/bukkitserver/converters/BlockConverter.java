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
            Location location = (Location) registry.toJava(Location.class, api, value);
            if (location == null) {
                throw new InvalidParameterException(String.format("Location was null for %s", value.toString()));
            }
            Block block = location.getBlock();
            if (block == null) {
                throw new InvalidParameterException(String.format("Block was null for %s", location.toString()));
            }
            return block;
        }
        throw new InvalidParameterException(String.format("Need a location ['world',x,y,z], got %s", value.toString()));
    }

    public Map<String, Object> blockAsMapping(PycraftAPI api, Object value) {
        org.bukkit.block.Block asBlock = (Block) value;
        Location loc = asBlock.getLocation();
        Map<String, Object> asMap = new HashMap<String, Object>();
        asMap.put("__type__", asBlock.getClass().getSimpleName());
        asMap.put("__namespace__", "Block");
        asMap.put("location", loc);
        asMap.put("data", asBlock.getBlockData());
        return asMap;
    }

    public String fromJava(PycraftAPI api, Object value) {
        return registry.fromJava(api, blockAsMapping(api, value));
    }
}
