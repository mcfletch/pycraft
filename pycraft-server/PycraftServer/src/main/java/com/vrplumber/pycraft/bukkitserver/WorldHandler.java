package com.vrplumber.pycraft.bukkitserver;

import com.vrplumber.pycraft.bukkitserver.NamespaceHandler;
import com.vrplumber.pycraft.bukkitserver.MessageHandler;
import com.vrplumber.pycraft.bukkitserver.PycraftAPI;
import com.vrplumber.pycraft.bukkitserver.PycraftMessage;
import java.util.List;
import java.util.Arrays;
import java.security.InvalidParameterException;
import java.util.ArrayList;
import org.bukkit.Server;
import org.bukkit.World;

public class WorldHandler extends NamespaceHandler {
    /* Interface for things which need to handle messages */
    public String getMethod() {
        return "World";
    }

    private List<String> error(PycraftMessage message, String category, String description) {
        List<String> response = Arrays.asList(category, description);
        return response;
    }

    private String expectString(PycraftMessage message, Integer index) throws InvalidParameterException {
        if (index < 0 || index >= message.payload.size()) {
            throw new InvalidParameterException(String.format("Missing String at argument %d", index));
        }
        Object item = message.payload.get(index);
        if (item == null) {
            throw new InvalidParameterException(String.format("Expected String at argument %d", index));
        }
        if (item instanceof String) {
            return (String) item;
        }
        throw new InvalidParameterException(String.format("Non-String at argument %d", index));
    }

    private Integer expectInteger(PycraftMessage message, Integer index) throws InvalidParameterException {
        if (index < 0 || index >= message.payload.size()) {
            throw new InvalidParameterException(String.format("Missing Integer at argument %d", index));
        }
        Object item = message.payload.get(index);
        if (item == null) {
            throw new InvalidParameterException(String.format("Expected Integer at argument %d", index));
        }
        if (item instanceof Integer) {
            return (Integer) item;
        }
        throw new InvalidParameterException(String.format("Non-Integer at argument %d", index));
    }

    public Object getWorlds(PycraftAPI api, PycraftMessage message) {
        List<String> names = new ArrayList<String>();
        for (World world : api.getPlugin().getServer().getWorlds()) {
            names.add(world.getName());
        }
        return (Object) names;
    }

    public Object setWorld(PycraftAPI api, PycraftMessage message) {
        /* Set the world on which we will operate */
        String name = expectString(message, 0);
        if (name != null) {
            api.setWorld(name);
        }
        return (Object) name;
    }

    public Object getWorld(PycraftAPI api, PycraftMessage message) {
        /* Get the current world, it not yet set, set to the first world */
        World world = api.getWorld();
        if (world != null) {
            return (Object) world.getName();
        } else {
            return null;
        }
    }

    public void handle(PycraftAPI api, PycraftMessage message) {
        String name = message.nextName();
        Object result = null;
        if (name.equals("getWorlds")) {
            result = getWorlds(api, message);
        } else if (name.equals("setWorld")) {
            result = setWorld(api, message);
        } else if (name.equals("getWorld")) {
            result = getWorld(api, message);
        }
        if (result != null) {
            api.sendResponse(message.messageId, result);
        } else {
            List<String> response = Arrays.asList("unknown-method", name);
            api.sendError(message.messageId, 1, response);
        }
    };
}