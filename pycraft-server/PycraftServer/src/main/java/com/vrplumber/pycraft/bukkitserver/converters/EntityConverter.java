package com.vrplumber.pycraft.bukkitserver.converters;

import java.lang.Math;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.lang.reflect.Field;
import java.lang.Enum;
import java.security.InvalidParameterException;
import java.util.List;
import java.util.Map;
import java.util.HashMap;
import java.util.Arrays;
import org.bukkit.block.Block;
import org.bukkit.util.Vector;
import org.bukkit.Location;
import org.bukkit.entity.Entity;

import com.vrplumber.pycraft.bukkitserver.PycraftAPI;
import com.vrplumber.pycraft.bukkitserver.converters.Converter;

public class EntityConverter implements Converter {
    /* Given a message and an index convert the value to an instance of T */
    PycraftConverterRegistry registry;

    EntityConverter(PycraftConverterRegistry registry) {
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

    public Map<String, Object> entityAsMapping(PycraftAPI api, Object value) {
        org.bukkit.entity.Entity asEntity = (Entity) value;
        Location loc = asEntity.getLocation();
        Map<String, Object> asMap = new HashMap<String, Object>();
        asMap.put("world", asEntity.getWorld().getName());
        asMap.put("location", loc);
        // asMap.put("uuid", asEntity.getUniqueId());
        asMap.put("type", asEntity.getType());
        asMap.put("name", asEntity.getName());
        return asMap;
    }

    public String fromJava(PycraftAPI api, Object value) {
        return registry.fromJava(api, entityAsMapping(api, value));
    }
}
