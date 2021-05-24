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
import org.bukkit.NamespacedKey;

public class EnumConverter implements Converter {
    /* Given a message and an index convert the value to an instance of T */
    PycraftConverterRegistry registry;

    EnumConverter(PycraftConverterRegistry registry) {
        this.registry = registry;
    }

    public Object toJava(PycraftAPI api, Object value, Class finalType) {
        if (value instanceof String) {
            String asString = (String) value;
            if (Keyed.class.isAssignableFrom(finalType)) {
                if (asString.indexOf(":") == -1) {
                    asString = String.format("minecraft:%s", asString.toLowerCase());
                }
                for (Object defined : finalType.getEnumConstants()) {
                    try {
                        if (((Keyed) defined).getKey().toString().equals(asString)) {
                            return defined;
                        }
                    } catch (IllegalArgumentException err) {
                        // Failed because of legacy api protections...
                        continue;
                    }
                }
            }
            // Okay, maybe a simple string enum-name
            asString = (String) value;
            for (Object defined : finalType.getEnumConstants()) {
                Enum asEnum = (Enum) defined;
                if (asEnum.name().toLowerCase() == asString.toLowerCase()) {
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
            try {
                return registry.fromJava(api, ((Keyed) value).getKey().toString());
            } catch (IllegalArgumentException err) {
                err.printStackTrace();
            }
        }
        return registry.fromJava(api, ((Enum) value).name());
    }
}
