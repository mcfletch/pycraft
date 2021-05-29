package com.vrplumber.pycraft.bukkitserver;

import com.vrplumber.pycraft.bukkitserver.MessageHandler;
import com.vrplumber.pycraft.bukkitserver.PycraftAPI;
import com.vrplumber.pycraft.bukkitserver.PycraftMessage;

import org.bukkit.Keyed;

import java.lang.reflect.Class;
import java.util.regex.Pattern;
import java.util.stream.StreamSupport;
import java.util.HashMap;
import java.util.Map;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

public abstract class NamespaceHandler implements MessageHandler {
    /* Interface for things which need to handle messages */
    public Class cls = null;
    public Map<String, MessageHandler> subcommands;

    NamespaceHandler() {
        subcommands = new HashMap<String, MessageHandler>();
    }

    NamespaceHandler(Class cls) {
        this.cls = cls;
        subcommands = new HashMap<String, MessageHandler>();
    }

    public Map<String, Object> getClassDescription(Class cls) {
        /* Describe the class if it is present */
        Map<String, Object> clsDesc = new HashMap<String, Object>();
        clsDesc.put("name", cls.getSimpleName());
        clsDesc.put("isEnum", cls.isEnum());
        clsDesc.put("isKeyed", Keyed.class.isAssignableFrom(cls));
        List<String> interfaceNames = new ArrayList<String>();
        for (Class interfaceClass : cls.getInterfaces()) {
            interfaceNames.add(interfaceClass.getSimpleName());
        }
        clsDesc.put("interfaces", interfaceNames);
        return clsDesc;

    }

    public Map<String, Object> getDescription() {
        Map<String, Object> result = new HashMap<String, Object>();
        result.put("type", "namespace");
        result.put("name", getMethod());
        if (cls != null) {
            result.put("cls", getClassDescription(cls));
        }
        List<Map<String, Object>> commands = new ArrayList<Map<String, Object>>();
        for (String key : subcommands.keySet()) {
            MessageHandler handler = subcommands.get(key);
            commands.add(handler.getDescription());
        }
        result.put("commands", commands);
        return result;
    }

    public void addHandler(String name, MessageHandler handler) {
        MessageHandler other = subcommands.get(name);
        if (other != null) {
            if (other instanceof MethodHandler && handler instanceof MethodHandler) {
                MethodHandler newMethod = ((MethodHandler) handler);
                MethodHandler otherMethod = ((MethodHandler) other);
                MultiDispatchHandler multi = new MultiDispatchHandler();
                multi.addHandler(otherMethod);
                multi.addHandler(newMethod);
                handler = multi;
            } else if (other instanceof MultiDispatchHandler && handler instanceof MethodHandler) {
                ((MultiDispatchHandler) other).addHandler((MethodHandler) handler);
                return;
            } else {
                throw new RuntimeException(String.format("Got conflicting name for %s", other.getMethod()));
            }
        }
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