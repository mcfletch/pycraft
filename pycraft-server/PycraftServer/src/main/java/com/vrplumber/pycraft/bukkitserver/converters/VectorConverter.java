package com.vrplumber.pycraft.bukkitserver.converters;

import java.lang.Math;
import java.lang.reflect.Constructor;
import java.security.InvalidParameterException;
import com.vrplumber.pycraft.bukkitserver.PycraftAPI;
import com.vrplumber.pycraft.bukkitserver.converters.Converter;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.stream.Stream;
import java.util.stream.IntStream;
import java.util.stream.DoubleStream;
import org.bukkit.util.Vector;

public class VectorConverter implements Converter {
    /* Given a message and an index convert the value to an instance of T */
    PycraftConverterRegistry registry = null;
    int targetSize = 0;
    Class targetClass = null;

    VectorConverter(PycraftConverterRegistry registry, int targetSize, Class targetClass) {
        this.registry = registry;
        this.targetSize = 3;
        this.targetClass = targetClass;
    }

    public boolean allOfType(List<Object> value, Class targetType) {
        for (Object item : (List<Object>) value) {
            if (!targetType.isInstance(item)) {
                return false;
            }
        }
        return true;
    }

    public List<Object> toType(PycraftAPI api, List<Object> value, Class targetType) {
        List<Object> result = new ArrayList<Object>();
        for (Object item : (List<Object>) value) {
            if (!targetType.isInstance(item)) {
                result.add(registry.toJava(targetType, api, item));
            }
        }
        return result;
    }

    public Object toJava(PycraftAPI api, Object value, Class finalType) {
        if (value instanceof List<?>) {
            List<Object> asList = (List<Object>) value;
            if (asList.size() != this.targetSize) {
                throw new InvalidParameterException(
                        String.format("Expected %d values in Vector, got %d", this.targetSize, asList.size()));
            }

            if (allOfType(asList, Double.class)) {
                return new Vector((Double) asList.get(0), (Double) asList.get(1), (Double) asList.get(2));
            } else if (allOfType(asList, Integer.class)) {
                return new Vector((Integer) asList.get(0), (Integer) asList.get(1), (Integer) asList.get(2));
            } else if (allOfType(asList, Float.class)) {
                return new Vector((Float) asList.get(0), (Float) asList.get(1), (Float) asList.get(2));
            } else {
                asList = toType(api, asList, Double.class);
                return new Vector((Double) asList.get(0), (Double) asList.get(1), (Double) asList.get(2));
            }
        }
        return null;
    }

    public String fromJava(PycraftAPI api, Object value) {
        Vector vector = (Vector) value;
        List<String> content = new ArrayList<String>();
        content.add(registry.fromJava(api, (Double) vector.getX()));
        content.add(registry.fromJava(api, (Double) vector.getY()));
        content.add(registry.fromJava(api, (Double) vector.getZ()));
        return String.format("[%s]", String.join(",", content));
    }
}
