package com.vrplumber.pycraft.bukkitserver;

import java.security.InvalidParameterException;
import com.vrplumber.pycraft.bukkitserver.Converter;

public class BooleanConverter implements Converter {
    /* Given a message and an index convert the value to an instance of T */
    public Object toJava(PycraftAPI api, Object value, Class finalType) {
        if (value instanceof Integer) {
            return ((Integer) value) != 0;
        } else if (value instanceof Boolean) {
            return (Boolean) value;
        } else if (value == null) {
            return Boolean.FALSE;
        }
        throw new InvalidParameterException(String.format("Expected Boolean, got %s", value.toString()));
    }

    public String fromJava(PycraftAPI api, Object value) {
        Boolean asBoolean = (Boolean) value;
        if (asBoolean) {
            return "true";
        } else {
            return "false";
        }
    }
}
