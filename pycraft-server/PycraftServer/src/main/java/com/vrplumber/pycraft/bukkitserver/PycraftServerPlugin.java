package com.vrplumber.pycraft.bukkitserver;

import org.bukkit.event.Listener;
import com.vrplumber.pycraft.bukkitserver.APIServer;
import com.vrplumber.pycraft.bukkitserver.EchoHandler;
import com.vrplumber.pycraft.bukkitserver.MessageHandler;
import com.vrplumber.pycraft.bukkitserver.PycraftMessage;
import com.vrplumber.pycraft.bukkitserver.HandlerRegistry;
import com.vrplumber.pycraft.bukkitserver.PycraftListener;
import java.util.ArrayList;
import java.io.File;
import java.util.List;
import org.bukkit.plugin.java.JavaPlugin;
import org.bukkit.plugin.java.JavaPluginLoader;
import org.bukkit.plugin.PluginDescriptionFile;

public class PycraftServerPlugin extends JavaPlugin {

  private APIServer endpoint;
  private PycraftListener listener;
  private IHandlerRegistry registry;

  public void setAPIServer(APIServer endpoint) {
    /* For test cases, set api server externally */
    this.endpoint = endpoint;
  }

  public List<PycraftAPI> getClients() {
    return endpoint.clients;
  }

  public void setRegistry(IHandlerRegistry registry) {
    this.registry = registry;
  }

  public PycraftServerPlugin() {
    super();
  }

  protected PycraftServerPlugin(JavaPluginLoader loader, PluginDescriptionFile description, File dataFolder,
      File file) {
    super(loader, description, dataFolder, file);
  }

  @Override
  public void onEnable() {
    getLogger().info("Hello, SpigotMC!");
    registry = HandlerRegistry.getInstance();
    registry.registerHandlers();
    endpoint = new APIServer(registry);
    endpoint.setPlugin(this);
    getServer().getPluginManager().registerEvents(new PycraftListener(this), this);
  }

  @Override
  public void onDisable() {
    getLogger().info("See you again, SpigotMC!");
    if (endpoint != null) {
      endpoint.setWanted(false);
    }
  }
}
