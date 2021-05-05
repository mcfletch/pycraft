package com.vrplumber.pycraft.bukkitserver.converters;

import java.lang.Math;
import java.security.InvalidParameterException;
import com.vrplumber.pycraft.bukkitserver.PycraftAPI;
import com.vrplumber.pycraft.bukkitserver.converters.Converter;

public class IntegerConverter implements Converter {
    /* Given a message and an index convert the value to an instance of T */
    public Object toJava(PycraftAPI api, Object value, Class finalType) {
        if (value instanceof Integer) {
            return (Integer) value;
        } else if (value instanceof Boolean) {
            if ((Boolean) value) {
                return 1;
            } else {
                return 0;
            }
        } else if (value == null) {
            return 0;
        } else if (value instanceof Double) {
            // TODO: deprecated here, but what replaces it?
            return (new Double(Math.floor((Double) value))).intValue();
        } else if (value instanceof Float) {
            return (new Double(Math.floor((Float) value))).intValue();
        }
        throw new InvalidParameterException(String.format("Expected Integer, got %s", value.toString()));
    }

    public String fromJava(PycraftAPI api, Object value) {
        return value.toString();
    }
}
