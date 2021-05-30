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

import com.vrplumber.pycraft.bukkitserver.NamespaceHandler;
import com.vrplumber.pycraft.bukkitserver.PycraftAPI;
import com.vrplumber.pycraft.bukkitserver.converters.Converter;

public class EntityConverter implements Converter {
    /* Given a message and an index convert the value to an instance of T */
    PycraftConverterRegistry registry;

    EntityConverter(PycraftConverterRegistry registry) {
        this.registry = registry;
    }

    public Object toJava(PycraftAPI api, Object value, Class finalType) {
        if (value instanceof String) {
            UUID identifier = null;
            try {
                identifier = UUID.fromString((String) value);
            } catch (Exception e) {

            }
            if (identifier != null) {
                Entity byUUID = api.getServer().getEntity(identifier);
                if (byUUID == null) {
                    throw new InvalidParameterException(
                            String.format("Entity with UUID %s does not appear on the server", identifier.toString()));
                }
                return byUUID;
            }
            Player player = api.getServer().getPlayer((String) value);
            if (player != null) {
                return player;
            }
            for (World world : api.getServer().getWorlds()) {
                for (Entity entity : world.getEntities()) {
                    if (entity.getName() == (String) value) {
                        return entity;
                    }
                }

            }
            throw new InvalidParameterException(
                    String.format("Could not find entity by uuid or name: %s", value.toString()));
        }
        throw new InvalidParameterException(
                String.format("Need a UUID or name for entity lookup in String format, got %s", value.toString()));
    }

    public Map<String, Object> entityAsMapping(PycraftAPI api, Object value) {
        org.bukkit.entity.Entity asEntity = (Entity) value;
        Location loc = asEntity.getLocation();
        Map<String, Object> asMap = new HashMap<String, Object>();
        asMap.put("__type__", asEntity.getClass().getSimpleName());
        asMap.put("__namespace__", "Entity");
        asMap.put("location", loc);
        try {
            asMap.put("uuid", asEntity.getUniqueId());
        } catch (Exception e) {
            // Mock bukkit exception...
        }
        List<String> interfaces = new ArrayList<String>();
        for (Class provided : NamespaceHandler.removeInterfaceSuperclasses(asEntity.getClass().getInterfaces())) {
            interfaces.add(provided.getSimpleName());
        }
        asMap.put("interfaces", interfaces);

        asMap.put("type", asEntity.getType());
        asMap.put("name", asEntity.getName());
        return asMap;
    }

    public String fromJava(PycraftAPI api, Object value) {
        return registry.fromJava(api, entityAsMapping(api, value));
    }
}
