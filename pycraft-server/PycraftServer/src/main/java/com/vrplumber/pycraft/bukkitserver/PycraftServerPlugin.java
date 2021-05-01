package com.vrplumber.pycraft.bukkitserver;
import com.vrplumber.pycraft.bukkitserver.APIServer;
import com.vrplumber.pycraft.bukkitserver.EchoHandler;
import com.vrplumber.pycraft.bukkitserver.MessageHandler;
import com.vrplumber.pycraft.bukkitserver.PycraftMessage;
import java.util.ArrayList;
import org.bukkit.plugin.java.JavaPlugin;
import com.vrplumber.pycraft.bukkitserver.HandlerRegistry;

public class PycraftServerPlugin extends JavaPlugin {


  private APIServer endpoint;
  private IHandlerRegistry registry;


  @Override
  public void onEnable() {
    getLogger().info("Hello, SpigotMC!");
    registry = HandlerRegistry.getInstance();
    registry.registerHandlers();
    endpoint = new APIServer(registry);
    endpoint.setPlugin(this);
  }
  @Override
  public void onDisable() {
    getLogger().info("See you again, SpigotMC!");
    if (endpoint != null) {
      endpoint.setWanted(false);
    }
  }
}
