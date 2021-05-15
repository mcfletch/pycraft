package com.vrplumber.pycraft.bukkitserver.converters;

import java.lang.Math;
import java.lang.reflect.Constructor;
import java.security.InvalidParameterException;
import com.vrplumber.pycraft.bukkitserver.PycraftAPI;
import com.vrplumber.pycraft.bukkitserver.converters.Converter;
import com.vrplumber.pycraft.bukkitserver.converters.VectorConverter;
import java.util.List;
import java.util.Map;
import java.util.HashMap;
import java.util.stream.Collectors;
import java.util.stream.Stream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.stream.IntStream;
import java.util.stream.DoubleStream;
import org.bukkit.Material;
import org.bukkit.inventory.Inventory;
import org.bukkit.inventory.ItemStack;
import org.bukkit.World;
import org.bukkit.enchantments.Enchantment;

public class ItemStackConverter implements Converter {
    /* Given a message and an index convert the value to an instance of T */
    PycraftConverterRegistry registry = null;

    ItemStackConverter(PycraftConverterRegistry registry) {
        this.registry = registry;
    }

    public Object toJava(PycraftAPI api, Object value, Class finalType) {
        World world;
        if (value instanceof String) {
            Material material = (Material) registry.toJava(Material.class, api, value);
            if (material == null) {
                throw new InvalidParameterException(String.format("Could not find Material %s", value.toString()));
            }
            if (!material.isItem()) {
                throw new InvalidParameterException(
                        String.format("Material %s is not an Item, cannot be in an ItemStack", material.toString()));
            }
            return new ItemStack(material);
        } else if (value instanceof List<?>) {
            List<Object> asList = (List<Object>) value;
            if (asList.size() == 2 && asList.get(0) instanceof String && asList.get(1) instanceof Integer) {
                Material material = (Material) registry.toJava(Material.class, api, asList.get(0));
                Integer count = (Integer) asList.get(1);
                return new ItemStack(material, count);
            } else if (asList.size() == 2 && asList.get(0) instanceof Integer
                    && (asList.get(1) instanceof String || asList.get(1) instanceof List<?>)) {
                Inventory inventory = (Inventory) registry.toJava(Inventory.class, api, asList.get(1));
                Integer index = (Integer) asList.get(0);
                return inventory.getItem(index);
            } else {
                throw new InvalidParameterException(String.format(
                        "Need (material, count) or (slot, (uuid or location)) to construct ItemStack from list, got %s",
                        asList.toString()));
            }
        } else if (value instanceof Map<?, ?>) {
            return ItemStack.deserialize((Map<String, Object>) value);
        }
        throw new InvalidParameterException(
                String.format("Expected 3 or 5 integers in a list for Location, got %s", value.toString()));

    }

    public String fromJava(PycraftAPI api, Object value) {
        ItemStack itemStack = (ItemStack) value;
        Map<String, Object> asMap = new HashMap<String, Object>();
        asMap.put("__type__", itemStack.getClass().getSimpleName());
        asMap.put("__namespace__", "ItemStack");
        asMap.put("material", itemStack.getType().getKey().toString());
        asMap.put("amount", itemStack.getAmount());
        Map<String, Integer> enchantments = new HashMap<String, Integer>();
        Map<Enchantment, Integer> onStack = itemStack.getEnchantments();
        for (Enchantment key : onStack.keySet()) {
            enchantments.put(key.getKey().toString(), onStack.get(key));
        }
        asMap.put("enchantments", enchantments);
        return registry.fromJava(api, asMap);
    }
}
