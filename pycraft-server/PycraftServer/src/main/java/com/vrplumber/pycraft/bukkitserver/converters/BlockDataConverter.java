package com.vrplumber.pycraft.bukkitserver.converters;

import java.security.InvalidParameterException;
import java.util.List;
import java.util.Map;
import java.util.HashMap;
import java.util.Arrays;
import org.bukkit.block.data.BlockData;
import org.bukkit.util.Vector;
import org.bukkit.Location;

import com.vrplumber.pycraft.bukkitserver.PycraftAPI;
import com.vrplumber.pycraft.bukkitserver.converters.Converter;

public class BlockDataConverter implements Converter {
    /* Given a message and an index convert the value to an instance of T */
    PycraftConverterRegistry registry;

    BlockDataConverter(PycraftConverterRegistry registry) {
        this.registry = registry;
    }

    public Object toJava(PycraftAPI api, Object value, Class finalType) {
        if (value instanceof String) {
            return api.getServer().createBlockData((String) value);
        }
        throw new InvalidParameterException(String.format("Need a string block-data, got %s", value.toString()));
    }

    public String fromJava(PycraftAPI api, Object value) {
        return registry.fromJava(api, ((BlockData) value).getAsString(false));
    }
}
