package com.vrplumber.pycraft.bukkitserver.converters;

import java.lang.Math;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.security.InvalidParameterException;
import java.util.Arrays;
import java.util.Collection;
import java.util.stream.Stream;
import java.util.stream.Collectors;

import org.bukkit.enchantments.Enchantment;
import org.bukkit.inventory.EnchantingInventory;

import com.vrplumber.pycraft.bukkitserver.PycraftAPI;
import com.vrplumber.pycraft.bukkitserver.converters.Converter;

import org.bukkit.Keyed;
import org.bukkit.NamespacedKey;

public class EnchantmentConverter implements Converter {
    /* Given a message and an index convert the value to an instance of T */
    PycraftConverterRegistry registry;

    EnchantmentConverter(PycraftConverterRegistry registry) {
        this.registry = registry;
    }

    public Object toJava(PycraftAPI api, Object value, Class finalType) {
        if (value instanceof String) {
            for (Enchantment enchantment : Enchantment.values()) {
                if (enchantment.getKey().toString().equals((String) value)) {
                    return enchantment;
                }
            }
            throw new InvalidParameterException(String.format("Did not find Enchantment %s", value.toString()));

        }
        throw new InvalidParameterException(
                String.format("Need a namespaced key for Enchantment, got %s", value.toString()));

    }

    public String fromJava(PycraftAPI api, Object value) {
        return registry.fromJava(api, ((Enchantment) value).getKey().toString());
    }
}
