package com.vrplumber.pycraft.bukkitserver;

import com.vrplumber.pycraft.bukkitserver.PycraftAPI;
import com.vrplumber.pycraft.bukkitserver.PycraftMessage;
import com.vrplumber.pycraft.bukkitserver.HandlerRegistry;
import java.util.Map;

public abstract interface MessageHandler {
  /* Interface for things which need to handle messages */
  public String getMethod();

  // public void register();
  public Object handle(PycraftAPI api, PycraftMessage message);

  public void register(HandlerRegistry registry);

  public Map<String, Object> getDescription();
}