package com.vrplumber.pycraft.bukkitserver.converters;

import java.lang.Class;
import com.vrplumber.pycraft.bukkitserver.PycraftAPI;

public interface Converter {
    /* Given a message and an index convert the value to an instance of T */
    public Object toJava(PycraftAPI api, Object value, Class finalType);

    public String fromJava(PycraftAPI api, Object value);
}
