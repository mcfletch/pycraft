package com.vrplumber.pycraft.bukkitserver;
import com.vrplumber.pycraft.bukkitserver.BaseHandler;
import com.vrplumber.pycraft.bukkitserver.MessageHandler;
import com.vrplumber.pycraft.bukkitserver.PycraftAPI;
import com.vrplumber.pycraft.bukkitserver.PycraftMessage;
import java.util.List;

public class EchoHandler extends BaseHandler {
  /* Interface for things which need to handle messages */
  public String getMethod() { return "echo"; }
  public void handle(PycraftAPI api, PycraftMessage message) {
    List<Object> args = message.payload;
    api.sendResponse(message.messageId, args);
  };
}