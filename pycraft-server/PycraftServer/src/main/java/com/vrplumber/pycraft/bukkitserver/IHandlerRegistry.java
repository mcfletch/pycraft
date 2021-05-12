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

public interface IHandlerRegistry {
    public void registerImplementation(String name, MessageHandler payload);

    public void registerHandlers();

    public MessageHandler getHandler(String name);

    public List<String> getMethodDescriptions();
}