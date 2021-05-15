package com.vrplumber.pycraft.bukkitserver;

import com.vrplumber.pycraft.bukkitserver.MessageHandler;
import com.vrplumber.pycraft.bukkitserver.PycraftAPI;
import com.vrplumber.pycraft.bukkitserver.PycraftMessage;
import java.util.regex.Pattern;
import java.util.stream.StreamSupport;
import java.util.HashMap;
import java.util.Map;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

public abstract class NamespaceHandler implements MessageHandler {
    /* Interface for things which need to handle messages */
    public Map<String, MessageHandler> subcommands;

    NamespaceHandler() {
        subcommands = new HashMap<String, MessageHandler>();
    }

    public Map<String, Object> getDescription() {
        Map<String, Object> result = new HashMap<String, Object>();
        result.put("type", "namespace");
        result.put("name", getMethod());
        List<Map<String, Object>> commands = new ArrayList<Map<String, Object>>();
        for (String key : subcommands.keySet()) {
            MessageHandler handler = subcommands.get(key);
            commands.add(handler.getDescription());
        }
        result.put("commands", commands);
        return result;
    }

    public void addHandler(String name, MessageHandler handler) {
        subcommands.put(name, handler);
    };

    public MessageHandler getHandler(String name) {
        /* Find our sub-handler by name */
        return subcommands.get(name);
    }

    public Object handle(PycraftAPI api, PycraftMessage message) {
        String name = message.nextName();
        MessageHandler subHandler = null;
        if (name != null) {
            if (name.equals("__methods__")) {
                return getDescription();
            }
            subHandler = subcommands.get(name);
        }
        if (subHandler == null) {
            List<String> response = Arrays.asList("unknown-method", String.join(name));
            message.finished = true;
            api.sendError(message.messageId, 1, response);
            return (Object) null;
        }
        message.addImplementation(subHandler);
        return subHandler.handle(api, message);
    };
}