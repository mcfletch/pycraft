package com.vrplumber.pycraft.bukkitserver.converters;

import java.lang.Math;
import java.lang.reflect.Constructor;
import java.security.InvalidParameterException;
import com.vrplumber.pycraft.bukkitserver.PycraftAPI;
import com.vrplumber.pycraft.bukkitserver.converters.Converter;
import com.vrplumber.pycraft.bukkitserver.converters.VectorConverter;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Map;
import java.util.HashMap;
import java.util.stream.Stream;
import java.util.stream.IntStream;
import java.util.stream.DoubleStream;
import org.bukkit.Location;
import org.bukkit.World;
import org.bukkit.event.player.AsyncPlayerChatEvent;

public class AsyncPlayerChatEventConverter implements Converter {
    /* Given a message and an index convert the value to an instance of T */
    PycraftConverterRegistry registry = null;
    Class targetClass = null;

    AsyncPlayerChatEventConverter(PycraftConverterRegistry registry, Class targetClass) {
        this.registry = registry;
        this.targetClass = targetClass;
    }

    public Object toJava(PycraftAPI api, Object value, Class finalType) {
        throw new InvalidParameterException(String.format("Do not current support python-side event generation"));
    }

    public String fromJava(PycraftAPI api, Object value) {
        AsyncPlayerChatEvent asEvent = (AsyncPlayerChatEvent) value;
        Map<String, Object> asMap = new HashMap<String, Object>();
        asMap.put("__type__", asEvent.getClass().getSimpleName());
        asMap.put("__namespace__", "Event");
        asMap.put("type", asEvent.getEventName());
        asMap.put("player", asEvent.getPlayer());
        asMap.put("message", asEvent.getMessage());
        return registry.fromJava(api, asMap);
    }
}
