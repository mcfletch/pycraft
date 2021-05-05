package com.vrplumber.pycraft.bukkitserver.converters;

import java.lang.Class;
import java.lang.Math;
import java.security.InvalidParameterException;
import com.vrplumber.pycraft.bukkitserver.PycraftAPI;
import com.vrplumber.pycraft.bukkitserver.converters.Converter;
import java.util.Map;
import java.util.List;
import java.util.ArrayList;
import java.util.Iterator;

public class MapConverter implements Converter {
    /* Given a message and an index convert the value to an instance of T */
    PycraftConverterRegistry registry = null;

    MapConverter(PycraftConverterRegistry registry) {
        this.registry = registry;
    }

    public Object toJava(PycraftAPI api, Object value, Class finalType) {
        if (value instanceof Map<?, ?>) {
            return value;
        }
        return null;
    }

    public String fromJava(PycraftAPI api, Object value) {
        Map<String, Object> asMap = (Map<String, Object>) value;
        List<String> content = new ArrayList<String>();
        Iterator it = asMap.entrySet().iterator();
        while (it.hasNext()) {
            Map.Entry<String, Object> entry = (Map.Entry<String, Object>) it.next();
            content.add(String.format("%s:%s", registry.fromJava(api, entry.getKey()),
                    registry.fromJava(api, entry.getValue())));
        }
        return String.format("{%s}", String.join(",", content));
    }
}
