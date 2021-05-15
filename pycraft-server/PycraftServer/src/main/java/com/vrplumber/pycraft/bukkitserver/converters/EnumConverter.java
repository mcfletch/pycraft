package com.vrplumber.pycraft.bukkitserver.converters;

import java.lang.Math;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.lang.Enum;
import java.security.InvalidParameterException;
import java.util.Arrays;

import com.vrplumber.pycraft.bukkitserver.PycraftAPI;
import com.vrplumber.pycraft.bukkitserver.converters.Converter;

import org.bukkit.Keyed;

public class EnumConverter implements Converter {
    /* Given a message and an index convert the value to an instance of T */
    PycraftConverterRegistry registry;

    EnumConverter(PycraftConverterRegistry registry) {
        this.registry = registry;
    }

    public Object toJava(PycraftAPI api, Object value, Class finalType) {
        if (value instanceof String) {
            String asString = (String) value;
            for (Object defined : finalType.getEnumConstants()) {
                if (defined instanceof Keyed) {
                    if (((Keyed) defined).getKey().toString().equals(value)) {
                        return defined;
                    }
                }
                Enum asEnum = (Enum) defined;
                if (asEnum.name() == asString) {
                    return defined;
                }
            }
            throw new InvalidParameterException(
                    String.format("Did not find String constant %s in %s", value.toString(), finalType.getName()));
        }
        throw new InvalidParameterException(
                String.format("Unknown %s name in %s", value.toString(), finalType.getName()));
    }

    public String fromJava(PycraftAPI api, Object value) {
        if (value instanceof Keyed) {
            return registry.fromJava(api, ((Keyed) value).getKey().toString());
        }
        return registry.fromJava(api, ((Enum) value).name());
    }
}
