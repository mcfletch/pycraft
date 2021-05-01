package com.vrplumber.pycraft.bukkitserver;
import com.vrplumber.pycraft.bukkitserver.APIServer;
import com.vrplumber.pycraft.bukkitserver.MessageHandler;
import java.security.InvalidParameterException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class PycraftMessage {

  static private Pattern headerPattern =
      Pattern.compile("^(\\d+),([a-zA-Z0-9.]+),(.*)$");


  public Integer messageId = 0;
  public String method = "";
  public List<Object> payload = null;
  public MessageHandler implementation = null;

  public void setImplementation(MessageHandler handler) {
    if (implementation == null) {
      implementation = handler;
    } else {
      throw new InvalidParameterException("Handler is already set on this message");
    }
  }

  static public PycraftMessage parseHeader(String line, PycraftAPI api) {
    /* Parse message header from the raw over-the-wire line */
    Matcher match = headerPattern.matcher(line);
    if (match.find()) {
      PycraftMessage result = new PycraftMessage();
      result.messageId = Integer.parseInt(match.group(1));
      result.method = match.group(2);
      result.payload = api.encoder.decode(match.group(3));
      return result;
    } else {
      api.sendResponse(0,
                       String.format("\"error\",\"bad-header\",\"%s\"", line));
      return null;
    }
  }


}