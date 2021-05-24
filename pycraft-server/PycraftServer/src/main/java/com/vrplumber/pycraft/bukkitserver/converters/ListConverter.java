package com.vrplumber.pycraft.bukkitserver.converters;

import java.lang.Math;
import java.lang.reflect.ParameterizedType;
import java.security.InvalidParameterException;
import com.vrplumber.pycraft.bukkitserver.PycraftAPI;
import com.vrplumber.pycraft.bukkitserver.converters.Converter;
import java.util.List;
import java.util.ArrayList;

public class ListConverter implements Converter {
    /* Given a message and an index convert the value to an instance of T */
    PycraftConverterRegistry registry = null;

    ListConverter(PycraftConverterRegistry registry) {
        this.registry = registry;
    }

    public Object toJava(PycraftAPI api, Object value, Class finalType) {
        if (value instanceof List<?>) {
            return value;
        }
        return null;
    }

    public String fromJava(PycraftAPI api, Object value) {
        List<Object> asArray = (List) value;
        List<String> content = new ArrayList<String>();
        for (Object item : asArray) {
            content.add(registry.fromJava(api, item));
        }
        return String.format("[%s]", String.join(",", content));
    }
}
