package com.vrplumber.pycraft.bukkitserver;

import java.lang.Math;
import java.security.InvalidParameterException;
import com.vrplumber.pycraft.bukkitserver.Converter;

public class FloatConverter implements Converter {
    /* Given a message and an index convert the value to an instance of T */
    public Object toJava(PycraftAPI api, Object value, Class finalType) {
        if (value instanceof Integer) {
            return Float.valueOf((Integer) value);
        } else if (value instanceof Boolean) {
            if ((Boolean) value) {
                return ((Double) 1.0).floatValue();
            } else {
                return ((Double) 0.0).floatValue();
            }
        } else if (value == null) {
            return ((Double) 0.0).floatValue();
        } else if (value instanceof Float) {
            return value;
        } else if (value instanceof Double) {
            return ((Double) value).floatValue();
        }
        throw new InvalidParameterException(String.format("Expected Float, got %s", value.toString()));
    }

    public String fromJava(PycraftAPI api, Object value) {
        return value.toString();
    }
}
