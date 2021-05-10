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
import org.bukkit.World;
import org.bukkit.block.Block;
import org.bukkit.util.Vector;
import org.bukkit.Location;

import com.vrplumber.pycraft.bukkitserver.PycraftAPI;
import com.vrplumber.pycraft.bukkitserver.converters.Converter;

public class WorldConverter implements Converter {
    /* Given a message and an index convert the value to an instance of T */
    PycraftConverterRegistry registry;

    WorldConverter(PycraftConverterRegistry registry) {
        this.registry = registry;
    }

    public Object toJava(PycraftAPI api, Object value, Class finalType) {
        if (value == null) {
            return api.getWorld();
        } else if (value instanceof String) {
            return api.getWorld((String) value);
        }
        throw new InvalidParameterException(
                String.format("Need a null (default world) or a String name for a world", value.toString()));
    }

    public Map<String, Object> worldAsMapping(PycraftAPI api, Object value) {
        World asWorld = (World) value;
        Map<String, Object> asMap = new HashMap<String, Object>();
        asMap.put("name", asWorld.getName());
        asMap.put("players", asWorld.getPlayers());
        asMap.put("type", asWorld.getClass().getSimpleName());
        // asMap.put("allow_animals", asWorld.getAllowAnimals());
        // asMap.put("allow_monsters", asWorld.getAllowMonsters());
        // asMap.put("allow_monsters", asWorld.getAllowMonsters());
        // asMap.put("difficulty", asWorld.getDifficulty());
        asMap.put("players", asWorld.getPlayers());
        return asMap;
    }

    public String fromJava(PycraftAPI api, Object value) {
        return registry.fromJava(api, worldAsMapping(api, value));
    }
}
