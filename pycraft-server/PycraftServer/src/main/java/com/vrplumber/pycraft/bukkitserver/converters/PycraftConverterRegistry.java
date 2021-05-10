package com.vrplumber.pycraft.bukkitserver.converters;

import java.util.Map;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.lang.Class;
import org.bukkit.block.Block;
import org.bukkit.block.data.BlockData;
import org.bukkit.entity.Entity;
import org.bukkit.util.Vector;
import org.bukkit.Location;
import org.bukkit.World;
import org.bukkit.event.block.BlockBreakEvent;
import org.bukkit.event.player.AsyncPlayerChatEvent;
import com.vrplumber.pycraft.bukkitserver.PycraftAPI;
import com.vrplumber.pycraft.bukkitserver.converters.Converter;
import com.vrplumber.pycraft.bukkitserver.converters.StringConverter;
import com.vrplumber.pycraft.bukkitserver.converters.BooleanConverter;
import com.vrplumber.pycraft.bukkitserver.converters.ListConverter;
import com.vrplumber.pycraft.bukkitserver.converters.FloatConverter;
import com.vrplumber.pycraft.bukkitserver.converters.DoubleConverter;

import com.vrplumber.pycraft.bukkitserver.converters.ArrayConverter;
import com.vrplumber.pycraft.bukkitserver.converters.EnumConverter;
import com.vrplumber.pycraft.bukkitserver.converters.BlockConverter;
import com.vrplumber.pycraft.bukkitserver.converters.EntityConverter;
import com.vrplumber.pycraft.bukkitserver.converters.WorldConverter;

public class PycraftConverterRegistry {
    /* Registers .class => Converter.toJava(api, value, finalType) converter */
    public Map<Class<?>, Converter> mapping;

    private class InterfaceConverter {
        Class cls;
        Converter converter;

        InterfaceConverter(Class cls, Converter converter) {
            this.cls = cls;
            this.converter = converter;
        }

        boolean target(Class finalCls) {
            return this.cls.isAssignableFrom(finalCls);
        }

        boolean match(Object value) {
            return cls.isInstance(value);
        }

    }

    public List<InterfaceConverter> interfaceConverters;

    public PycraftConverterRegistry() {
        mapping = new HashMap<Class<?>, Converter>();
        interfaceConverters = new ArrayList<InterfaceConverter>();
        mapping.put(String.class, new StringConverter());
        mapping.put(Boolean.class, new BooleanConverter());
        mapping.put(Integer.class, new IntegerConverter());
        mapping.put(Double.class, new DoubleConverter());
        mapping.put(Float.class, new FloatConverter());

        mapping.put(HashMap.class, new MapConverter(this));
        mapping.put(ArrayList.class, new ListConverter(this));
        mapping.put(String[].class, new ArrayConverter(this));
        mapping.put(Integer[].class, new ArrayConverter(this));
        mapping.put(Double[].class, new ArrayConverter(this));
        mapping.put(int[].class, new ArrayConverter(this));
        mapping.put(float[].class, new ArrayConverter(this));
        mapping.put(double[].class, new ArrayConverter(this));

        mapping.put(Vector.class, new VectorConverter(this, 3, Vector.class));
        mapping.put(Location.class, new LocationConverter(this, Location.class));
        mapping.put(BlockBreakEvent.class, new BlockBreakEventConverter(this, BlockBreakEvent.class));
        mapping.put(AsyncPlayerChatEvent.class, new AsyncPlayerChatEventConverter(this, AsyncPlayerChatEvent.class));
        mapping.put(World.class, new WorldConverter(this));

        // Now the interfaces, which require a linear scan, so we want to reduce
        // usage...
        interfaceConverters.add(new InterfaceConverter(List.class, new ListConverter(this)));
        interfaceConverters.add(new InterfaceConverter(Map.class, new MapConverter(this)));
        interfaceConverters.add(new InterfaceConverter(Enum.class, new EnumConverter(this)));
        interfaceConverters.add(new InterfaceConverter(Block.class, new BlockConverter(this)));
        interfaceConverters.add(new InterfaceConverter(Entity.class, new EntityConverter(this)));
        // This is really *just* for the test server's mocked worlds
        interfaceConverters.add(new InterfaceConverter(World.class, new WorldConverter(this)));
        interfaceConverters.add(new InterfaceConverter(BlockData.class, new BlockDataConverter(this)));
    }

    public Object toJava(Class targetType, PycraftAPI api, Object value) {
        Converter converter = mapping.get(targetType);
        if (converter == null) {
            converter = getConverterByTarget(targetType);
        }
        if (converter != null) {
            return converter.toJava(api, value, targetType);
        }

        return (Object) null;
    }

    public Converter getConverterByTarget(Class targetType) {
        for (InterfaceConverter converter : interfaceConverters) {
            if (converter.target(targetType)) {
                return converter.converter;
            }
        }
        return null;

    }

    public Converter getConverterByInterface(Object value) {
        /* Scan interfaceConverters looking for a match */
        for (InterfaceConverter converter : interfaceConverters) {
            if (converter.match(value)) {
                return converter.converter;
            }
        }
        return null;
    }

    public String fromJava(PycraftAPI api, Object value) {
        if (value == null) {
            return "null";
        }
        Converter converter = mapping.get(value.getClass());
        if (converter == null) {
            converter = getConverterByInterface(value);
        }
        if (converter != null) {
            return converter.fromJava(api, value);
        }
        api.getLogger().info(String.format("No converter found for type %s", value.getClass().getName()));
        return "null";

    }
}
