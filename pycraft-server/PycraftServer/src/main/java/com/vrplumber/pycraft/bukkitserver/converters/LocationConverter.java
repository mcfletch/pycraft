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
import java.util.stream.Stream;
import java.util.stream.IntStream;
import java.util.stream.DoubleStream;
import org.bukkit.Location;
import org.bukkit.World;

public class LocationConverter implements Converter {
    /* Given a message and an index convert the value to an instance of T */
    PycraftConverterRegistry registry = null;
    Class targetClass = null;

    LocationConverter(PycraftConverterRegistry registry, Class targetClass) {
        this.registry = registry;
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
        if (allOfType(value, targetType)) {
            return value;
        }
        List<Object> result = new ArrayList<Object>();
        for (Object item : (List<Object>) value) {
            if (!targetType.isInstance(item)) {
                result.add(registry.toJava(targetType, api, item));
            }
        }
        return result;
    }

    public Object toJava(PycraftAPI api, Object value, Class finalType) {
        World world;
        if (value instanceof List<?>) {
            List<Object> asList = (List<Object>) value;
            if (asList.size() == 4 || asList.size() == 6) {
                if (asList.get(0) == null) {
                    world = api.getWorld();
                } else {
                    world = (World) registry.toJava(World.class, api, asList.get(0));
                }
                asList = asList.subList(1, asList.size());
            } else {
                world = api.getWorld();
            }
            if (asList.size() == 3) {
                if (allOfType(asList, Double.class)) {
                    return new Location(world, (Double) asList.get(0), (Double) asList.get(1), (Double) asList.get(2));
                } else if (allOfType(asList, Integer.class)) {
                    return new Location(world, (Integer) asList.get(0), (Integer) asList.get(1),
                            (Integer) asList.get(2));
                } else if (allOfType(asList, Float.class)) {
                    return new Location(world, (Float) asList.get(0), (Float) asList.get(1), (Float) asList.get(2));
                } else {
                    asList = toType(api, asList, Double.class);
                    return new Location(world, (Double) asList.get(0), (Double) asList.get(1), (Double) asList.get(2));
                }
            } else if (asList.size() == 5) {
                if (allOfType(asList, Double.class)) {
                    return new Location(world, (Double) asList.get(0), (Double) asList.get(1), (Double) asList.get(2),
                            (Float) asList.get(3), (Float) asList.get(4));
                } else if (allOfType(asList, Integer.class)) {
                    return new Location(world, Double.valueOf((Integer) asList.get(0)),
                            Double.valueOf((Integer) asList.get(1)), Double.valueOf((Integer) (Integer) asList.get(2)),
                            Float.valueOf((Integer) asList.get(3)), Float.valueOf((Integer) asList.get(4)));
                } else {
                    asList = toType(api, asList, Double.class);
                    return new Location(world, (Double) asList.get(0), (Double) asList.get(1), (Double) asList.get(2),
                            ((Double) asList.get(3)).floatValue(), ((Double) asList.get(4)).floatValue());
                }
            } else {
                throw new InvalidParameterException(
                        String.format("Expected 3 or 5 values in Location, got %d", asList.size()));
            }
        }
        throw new InvalidParameterException(
                String.format("Expected 3 or 5 integers in a list for Location, got %s", value.toString()));

    }

    public String fromJava(PycraftAPI api, Object value) {
        Location location = (Location) value;
        List<String> content = new ArrayList<String>();
        content.add(registry.fromJava(api, location.getWorld().getName()));
        content.add(registry.fromJava(api, location.getX()));
        content.add(registry.fromJava(api, location.getY()));
        content.add(registry.fromJava(api, location.getZ()));
        content.add(registry.fromJava(api, location.getYaw()));
        content.add(registry.fromJava(api, location.getPitch()));
        return String.format("[%s]", String.join(",", content));
    }
}
