package com.vrplumber.pycraft.bukkitserver;
import com.vrplumber.pycraft.bukkitserver.APIServer;
import com.vrplumber.pycraft.bukkitserver.EchoHandler;
import com.vrplumber.pycraft.bukkitserver.MessageHandler;
import com.vrplumber.pycraft.bukkitserver.PycraftMessage;
import java.util.ArrayList;
import java.util.List;
import org.bukkit.plugin.java.JavaPlugin;
import java.util.HashMap;
import java.util.logging.Handler;

class HandlerRegistry {
    private static List<Class> handlers;

    static { 
        handlers = new ArrayList<Class>();
        handlers.add(EchoHandler.class); 
    }

    private static HandlerRegistry instance = null;
    static public HandlerRegistry getInstance() {
        if (instance == null) {
            instance = new HandlerRegistry();
        }
        return instance;
    }
    private HashMap<String, MessageHandler> implementations;

    private HandlerRegistry() {
        implementations = new HashMap<String, MessageHandler>();
    }


    void registerImplementation(String name, MessageHandler payload) {
      implementations.put(name, payload);
    }
  
    public void registerHandlers() {
        for (Class handlerCls : handlers) {
            try {
            MessageHandler handler =
                (MessageHandler)(handlerCls.getDeclaredConstructor().newInstance());
            if (handler == null) {
                // getLogger().warning(String.format("Unable to create %s instance",
                //                                 handlerCls.getName()));
                continue;
            }
            // getLogger().info(
            //     String.format("Registering command %s", handler.getMethod()));
            registerImplementation(handler.getMethod(), handler);

            } catch (Exception err) {
            err.printStackTrace();
            }
        }
    }
    public MessageHandler getHandler(String name) {
        return implementations.get(name);
    }
}