package com.vrplumber.pycraft.bukkitserver;

import com.vrplumber.pycraft.bukkitserver.NamespaceHandler;
import com.vrplumber.pycraft.bukkitserver.MessageHandler;
import com.vrplumber.pycraft.bukkitserver.PycraftAPI;
import com.vrplumber.pycraft.bukkitserver.PycraftMessage;
import java.lang.Math;
import java.util.List;
import java.util.Arrays;
import java.security.InvalidParameterException;
import java.util.ArrayList;
import org.bukkit.Server;
import org.bukkit.World;
import org.bukkit.util.Vector;
import org.bukkit.Location;
import org.bukkit.Material;
import org.bukkit.block.data.BlockData;
import org.bukkit.block.Block;
import org.bukkit.entity.Entity;
import org.bukkit.entity.EntityType;
import org.bukkit.entity.Player;

public class GenericHandler extends NamespaceHandler {
    /* Interface for things which need to handle messages */
    Class cls = null;

    public GenericHandler(Class cls) {
        this.cls = cls;
    }

    public String getMethod() {
        return cls.getSimpleName();
    }

    public void register(HandlerRegistry registry) {
        /* Called when we are registered with the registry (api likely not up yet) */
        for (MessageHandler handler : MethodHandler.forClass(cls)) {
            this.addHandler(handler.getMethod(), handler);
        }
    }

    public Object handle(PycraftAPI api, PycraftMessage message) {
        String name = message.nextName();
        Object result = null;
        boolean handled = false;
        /* Registered method on the current World */
        MessageHandler subHandler = getHandler(name);
        if (subHandler != null) {
            result = subHandler.handle(api, message);
            handled = true;
        }
        if (handled) {
            return result;
        } else {
            throw new InvalidParameterException(String.format("unknown-method %s.%s", getMethod(), name));
        }
    };
}