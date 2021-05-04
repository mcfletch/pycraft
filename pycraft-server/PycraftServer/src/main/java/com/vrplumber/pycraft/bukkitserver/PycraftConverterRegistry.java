package com.vrplumber.pycraft.bukkitserver;

import java.util.Map;
import java.util.List;
import java.util.ArrayList;
import java.util.HashMap;
import java.lang.Class;
import com.vrplumber.pycraft.bukkitserver.Converter;
import com.vrplumber.pycraft.bukkitserver.StringConverter;
import com.vrplumber.pycraft.bukkitserver.BooleanConverter;
import com.vrplumber.pycraft.bukkitserver.ListConverter;
import com.vrplumber.pycraft.bukkitserver.FloatConverter;
import com.vrplumber.pycraft.bukkitserver.DoubleConverter;

public class PycraftConverterRegistry {
    /* Registers .class => Converter.toJava(api, value, finalType) converter */
    public Map<Class<?>, Converter> mapping;

    PycraftConverterRegistry() {
        mapping = new HashMap<Class<?>, Converter>();
        mapping.put(String.class, new StringConverter());
        mapping.put(Boolean.class, new BooleanConverter());
        mapping.put(Integer.class, new IntegerConverter());
        mapping.put(Double.class, new DoubleConverter());
        mapping.put(Float.class, new FloatConverter());
        mapping.put(ArrayList.class, new ListConverter(this));
    }

    public Object toJava(Class targetType, PycraftAPI api, Object value) {
        Converter converter = mapping.get(targetType);
        if (converter != null) {
            return converter.toJava(api, value, targetType);
        }
        return (Object) null;
    }

    public String fromJava(PycraftAPI api, Object value) {
        Converter converter = mapping.get(value.getClass());
        if (converter != null) {
            return converter.fromJava(api, value);
        }
        api.getLogger().info(String.format("No converter found for type %s", value.getClass().getName()));
        return "null";

    }
}
