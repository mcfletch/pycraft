package com.vrplumber.pycraft.bukkitserver.converters;

import java.lang.Math;
import java.security.InvalidParameterException;
import com.vrplumber.pycraft.bukkitserver.PycraftAPI;
import com.vrplumber.pycraft.bukkitserver.converters.Converter;
import java.util.Collection;
import java.util.List;
import java.lang.reflect.Array;
import java.util.ArrayList;

public class CollectionConverter implements Converter {
    /* Given a message and an index convert the value to an instance of T */
    PycraftConverterRegistry registry = null;

    CollectionConverter(PycraftConverterRegistry registry) {
        this.registry = registry;
    }

    public Object toJava(PycraftAPI api, Object value, Class finalType) {
        if (finalType == value.getClass()) {
            return value;
        }
        if (value instanceof List) {
            /* Only collection type in json */
            Class subType = finalType.componentType();
            List asList = (List) value;
            Object result = Array.newInstance(subType, (int) asList.size());
            for (int i = 0; i < asList.size(); i++) {
                Object item = asList.get(i);
                Object converted = registry.toJava(subType, api, item);
                Array.set(result, i, subType.cast(converted));
            }
            return result;
        }
        return null;
    }

    public String fromJava(PycraftAPI api, Object value) {
        List<String> content = new ArrayList<String>();
        Collection<Object> asCollection = (Collection<Object>) value;
        for (Object item : asCollection) {
            content.add(registry.fromJava(api, item));
        }
        return String.format("[%s]", String.join(",", content));
    }
}
