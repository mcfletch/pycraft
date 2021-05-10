package com.vrplumber.pycraft.bukkitserver.converters;

import java.security.InvalidParameterException;
import java.util.UUID;

import com.vrplumber.pycraft.bukkitserver.PycraftAPI;
import com.vrplumber.pycraft.bukkitserver.converters.Converter;

public class UUIDConverter implements Converter {
    /* Given a message and an index convert the value to an instance of T */
    PycraftConverterRegistry registry;

    UUIDConverter(PycraftConverterRegistry registry) {
        this.registry = registry;
    }

    public Object toJava(PycraftAPI api, Object value, Class finalType) {
        if (value instanceof String) {
            return UUID.fromString((String) value);
        }
        throw new InvalidParameterException(
                String.format("Expected a canonical format UUID as a string, got: %s", value.toString()));
    }

    public String fromJava(PycraftAPI api, Object value) {
        return registry.fromJava(api, ((UUID) value).toString());
    }
}
