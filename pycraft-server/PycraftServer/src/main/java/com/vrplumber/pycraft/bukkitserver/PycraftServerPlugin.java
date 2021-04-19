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
  private HandlerRegistry registry;


  @Override
  public void onEnable() {
    getLogger().info("Hello, SpigotMC!");
    endpoint = new APIServer();
    endpoint.setPlugin(this);
    registry = HandlerRegistry.getInstance();
    registry.registerHandlers();
  }
  @Override
  public void onDisable() {
    getLogger().info("See you again, SpigotMC!");
    if (endpoint != null) {
      endpoint.setWanted(false);
    }
  }
}
