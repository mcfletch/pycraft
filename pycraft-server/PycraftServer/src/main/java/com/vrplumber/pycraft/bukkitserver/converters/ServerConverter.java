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
import org.bukkit.Server;
import org.bukkit.World;
import org.bukkit.entity.Entity;
import org.bukkit.entity.Player;

import com.vrplumber.pycraft.bukkitserver.PycraftAPI;
import com.vrplumber.pycraft.bukkitserver.converters.Converter;

public class ServerConverter implements Converter {
    /* Given a message and an index convert the value to an instance of T */
    PycraftConverterRegistry registry;

    ServerConverter(PycraftConverterRegistry registry) {
        this.registry = registry;
    }

    public Object toJava(PycraftAPI api, Object value, Class finalType) {
        return api.getServer();
    }

    public String fromJava(PycraftAPI api, Object value) {
        Server server = (Server) value;
        Map<String, Object> asMap = new HashMap<String, Object>();
        asMap.put("type", "Server");
        asMap.put("version", api.getServer().getVersion());
        asMap.put("pycraft_version", api.getPlugin().getDescription().getVersion());
        return registry.fromJava(api, asMap);
    }
}
