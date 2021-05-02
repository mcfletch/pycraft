package com.vrplumber.pycraft.bukkitserver;

import com.vrplumber.pycraft.bukkitserver.MessageHandler;
import com.vrplumber.pycraft.bukkitserver.PycraftAPI;
import com.vrplumber.pycraft.bukkitserver.PycraftMessage;

import java.util.logging.Handler;
import java.util.regex.Pattern;

public abstract class BaseHandler implements MessageHandler {
  /* Interface for things which need to handle messages */
  public Object handle(PycraftAPI api, PycraftMessage message) {
  };

  public void register(HandlerRegistry registry) {
    /* Base class does nothing other than get registered... */
  }
}