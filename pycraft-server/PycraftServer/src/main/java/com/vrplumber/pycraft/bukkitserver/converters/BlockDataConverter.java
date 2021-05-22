package com.vrplumber.pycraft.bukkitserver.converters;

import java.security.InvalidParameterException;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;
import java.util.Arrays;

import org.bukkit.block.Block;
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
        if (value instanceof List<?>) {
            Block block = (Block) registry.toJava(Block.class, api, value);
            return block.getBlockData();
        } else if (value instanceof String) {
            /* Free floating block data */
            return api.getServer().createBlockData((String) value);
        }
        throw new InvalidParameterException(String.format("Need a string block-data, got %s", value.toString()));
    }

    public String fromJava(PycraftAPI api, Object value) {
        BlockData blockdata = (BlockData) value;
        Map<String, Object> asMap = new HashMap<String, Object>();
        asMap.put("__type__", blockdata.getClass().getSimpleName());
        asMap.put("__namespace__", "BlockData");
        List<String> interfaces = new ArrayList<String>();
        for (Class provided : blockdata.getClass().getInterfaces()) {
            interfaces.add(provided.getSimpleName());
        }
        asMap.put("interfaces", interfaces);
        try {
            asMap.put("string_value", blockdata.getAsString());
        } catch (Exception err) {
            // MockBukkit doesn't support getAsString()
            asMap.put("string_value", blockdata.getMaterial().getKey().toString());
        }
        return registry.fromJava(api, asMap);
    }
}
