package com.vrplumber.pycraft.bukkitserver;

import java.lang.Math;
import java.security.InvalidParameterException;
import com.vrplumber.pycraft.bukkitserver.Converter;

public class DoubleConverter implements Converter {
    /* Given a message and an index convert the value to an instance of T */
    public Object toJava(PycraftAPI api, Object value, Class finalType) {
        if (value instanceof Integer) {
            return Double.valueOf((Integer) value);
        } else if (value instanceof Boolean) {
            if ((Boolean) value) {
                return (Double) 1.0;
            } else {
                return (Double) 0.0;
            }
        } else if (value == null) {
            return (Double) 0.0;
        } else if (value instanceof Double) {
            return value;
        } else if (value instanceof Float) {
            return Double.valueOf((Float) value);
        }
        throw new InvalidParameterException(String.format("Expected Double, got %s", value.toString()));
    }

    public String fromJava(PycraftAPI api, Object value) {
        return value.toString();
    }
}
