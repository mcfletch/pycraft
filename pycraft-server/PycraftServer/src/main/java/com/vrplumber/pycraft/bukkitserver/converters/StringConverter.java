package com.vrplumber.pycraft.bukkitserver.converters;

import com.vrplumber.pycraft.bukkitserver.PycraftAPI;
import com.vrplumber.pycraft.bukkitserver.converters.Converter;

public class StringConverter implements Converter {
    /* Given a message and an index convert the value to an instance of T */
    public Object toJava(PycraftAPI api, Object value, Class finalType) {
        if (value instanceof String) {
            return value;
        } else if (value instanceof Integer || value instanceof Double || value instanceof Float
                || value instanceof Boolean) {
            return value.toString();
        } else {
            return value.toString();
        }
    }

    public String fromJava(PycraftAPI api, Object value) {
        return String.format("\"%s\"",
                ((String) value).replace("\\", "\\\\").replace("\t", "\\t").replace("\b", "\\b").replace("\n", "\\n")
                        .replace("\r", "\\r").replace("\f", "\\f").replace("\'", "\\'").replace("\"", "\\\""));
    }
}
