package com.vrplumber.pycraft.bukkitserver;
import com.vrplumber.pycraft.bukkitserver.PycraftAPI;
import com.vrplumber.pycraft.bukkitserver.PycraftMessage;

public abstract interface MessageHandler {
  /* Interface for things which need to handle messages */
  public String getMethod();
  // public void register();
  public void handle(PycraftAPI api, PycraftMessage message);
}