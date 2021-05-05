package com.vrplumber.pycraft.bukkitserver.converters;

import java.lang.Math;
import java.security.InvalidParameterException;
import com.vrplumber.pycraft.bukkitserver.PycraftAPI;
import com.vrplumber.pycraft.bukkitserver.converters.Converter;
import java.util.List;
import java.util.ArrayList;

public class ArrayConverter implements Converter {
    /* Given a message and an index convert the value to an instance of T */
    PycraftConverterRegistry registry = null;

    ArrayConverter(PycraftConverterRegistry registry) {
        this.registry = registry;
    }

    public Object toJava(PycraftAPI api, Object value, Class finalType) {
        if (finalType == value.getClass()) {
            return value;
        }
        if (value instanceof List) {
            List result = new ArrayList<Object>();
            List asList = (List) value;
            for (Object item : asList) {
                result.add(registry.toJava(finalType.arrayType(), api, item));
            }
            return finalType.cast(result.toArray());
        }
        return null;
    }

    public String fromJava(PycraftAPI api, Object value) {
        List<String> content = new ArrayList<String>();
        Object[] asArray = (Object[]) value;
        for (int i = 0; i < asArray.length; i++) {
            content.add(registry.fromJava(api, (Object) asArray[i]));
        }
        return String.format("[%s]", String.join(",", content));
    }
}
