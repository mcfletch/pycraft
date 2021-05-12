package com.vrplumber.pycraft.bukkitserver;

import com.vrplumber.pycraft.bukkitserver.MessageHandler;
import com.vrplumber.pycraft.bukkitserver.PycraftAPI;
import com.vrplumber.pycraft.bukkitserver.PycraftMessage;

import java.util.logging.Handler;
import java.util.regex.Pattern;
import java.util.Map;
import java.util.HashMap;

public abstract class BaseHandler implements MessageHandler {
  /* Interface for things which need to handle messages */
  public Object handle(PycraftAPI api, PycraftMessage message) {
    return (Object) null;
  };

  public void register(HandlerRegistry registry) {
    /* Base class does nothing other than get registered... */
  }

  public Map<String, Object> getDescription() {
    Map<String, Object> result = new HashMap<String, Object>();
    result.put("__doc__", "Undocumented");
    return result;
  }
}