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
import java.util.UUID;
import org.bukkit.block.Block;
import org.bukkit.util.Vector;
import org.bukkit.Location;
import org.bukkit.World;
import org.bukkit.entity.Entity;
import org.bukkit.entity.Player;

import com.vrplumber.pycraft.bukkitserver.PycraftAPI;
import com.vrplumber.pycraft.bukkitserver.converters.Converter;

public class PlayerConverter implements Converter {
    /* Given a message and an index convert the value to an instance of T */
    PycraftConverterRegistry registry;

    PlayerConverter(PycraftConverterRegistry registry) {
        this.registry = registry;
    }

    public Object toJava(PycraftAPI api, Object value, Class finalType) {
        if (value instanceof String) {
            try {
                UUID identifier = UUID.fromString((String) value);
                if (identifier != null) {
                    return api.getServer().getEntity(identifier);
                }
            } catch (Exception e) {

            }
            Player player = api.getServer().getPlayer((String) value);
            if (player != null) {
                return player;
            }
            throw new InvalidParameterException(
                    String.format("Could not find player by uuid or name: %s", value.toString()));
        }
        throw new InvalidParameterException(
                String.format("Need a UUID or name for player lookup in String format, got %s", value.toString()));
    }

    public Map<String, Object> entityAsMapping(PycraftAPI api, Object value) {
        Player asPlayer = (Player) value;
        Location loc = asPlayer.getLocation();
        Map<String, Object> asMap = new HashMap<String, Object>();
        asMap.put("__type__", asPlayer.getClass().getSimpleName());
        asMap.put("__namespace__", "Player");
        asMap.put("location", loc);
        try {
            asMap.put("uuid", asPlayer.getUniqueId());
        } catch (Exception e) {
            // Mock bukkit exception...
        }
        asMap.put("type", asPlayer.getType());
        asMap.put("name", asPlayer.getName());
        asMap.put("display_name", asPlayer.getDisplayName());
        asMap.put("last_played", (Double) ((double) asPlayer.getLastPlayed()));
        return asMap;
    }

    public String fromJava(PycraftAPI api, Object value) {
        return registry.fromJava(api, entityAsMapping(api, value));
    }
}
