package com.vrplumber.pycraft.bukkitserver;

import com.vrplumber.pycraft.bukkitserver.APIServer;
import com.vrplumber.pycraft.bukkitserver.MessageHandler;
import java.security.InvalidParameterException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class PycraftMessage {

  static private Pattern headerPattern = Pattern.compile("^(\\d+),([a-z_A-Z0-9.]+),(.*)$");

  public Integer messageId = 0;
  public List<String> method = null;
  public List<Object> payload = null;
  public List<MessageHandler> implementation = null;
  public Object instance = null;

  public void addImplementation(MessageHandler handler) {
    if (implementation == null) {
      implementation = new ArrayList<MessageHandler>();
    }
    implementation.add(handler);
  }

  public String nextName() {
    if (method != null) {
      if (implementation == null) {
        return method.get(0);
      } else if (method.size() > implementation.size()) {
        return method.get(implementation.size());
      }
    }
    return null;
  }

  static public PycraftMessage parseHeader(String line, PycraftAPI api) {
    /* Parse message header from the raw over-the-wire line */
    Matcher match = headerPattern.matcher(line);
    if (match.find()) {
      PycraftMessage result = new PycraftMessage();
      result.messageId = Integer.parseInt(match.group(1));
      String fullMethod = match.group(2);
      result.method = new ArrayList<String>();
      for (String fragment : fullMethod.split("[.]")) {
        result.method.add(fragment);
      }
      result.payload = api.encoder.decode(match.group(3));
      return result;
    } else {
      return null;
    }
  }

}