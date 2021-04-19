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
  static private Pattern intPattern = Pattern.compile("([-+]*[0-9]+)[,]?");
  static private Pattern stringPattern =
      //   Pattern.compile("[\"]"
      //                   + "(([\\\\][n\"]|[^\\\"])*)"
      //                   + "[\"][,]?");
      Pattern.compile("\"([^\"\\\\]*(?:\\\\.|[^\"\\\\]*)*)\"[,]?");


  Integer messageId = 0;
  String method = "";
  String payload = "";
  MessageHandler implementation = null;

  static public PycraftMessage parseHeader(String line, PycraftAPI api) {
    /* Parse message header from the raw over-the-wire line */
    Matcher match = headerPattern.matcher(line);
    if (match.find()) {
      PycraftMessage result = new PycraftMessage();
      result.messageId = Integer.parseInt(match.group(1));
      result.method = match.group(2);
      result.payload = match.group(3);
      return result;
    } else {
      api.sendResponse(0,
                       String.format("\"error\",\"bad-header\",\"%s\"", line));
      return null;
    }
  }

  static public List<Object> parseArgs(String line) {
    List<Object> result = new ArrayList<Object>();
    List<List<Object>> stack = new ArrayList<List<Object>>();
    stack.add(result);
    Matcher match;
    while (line.length() > 0) {
      match = intPattern.matcher(line);
      if (match.find()) {
        result.add(Integer.parseInt(match.group(1)));
      } else {
        match = stringPattern.matcher(line);
        if (match.find()) {
          String rawString = match.group(1);
          result.add(rawString.replace("\\n", "\n").replace("\\\"", "\""));
        } else {
          if (line.startsWith("[")) {
            result = new ArrayList<Object>();
            stack.add(result);
            line = line.substring(1);
          } else if (line.startsWith("]")) {
            if (stack.size() > 1) {
              stack.remove(result);
              result = stack.get(stack.size() - 1);
              line = line.substring(1);
            } else {
              throw new InvalidParameterException(String.format(
                  "Malformed list, more closing brackets then opening ones"));
            }
          } else {
            throw new InvalidParameterException(
                String.format("Unknown data-format for %s", line));
          }
        }
      }
      if (match != null) {
        line = line.substring(match.end());
        match = null;
      }
    }
    return stack.get(0);
  }

  public void dispatch(PycraftAPI api) {
    /* Lookup our implementation and ask it to handle us */
    MessageHandler implementation = implementations.get(method);
    if (implementation == null) {
      api.sendResponse(messageId,
                       String.format("\"error\",\"no-method\",\"%s\"", method));
      return;
    } else {
      this.implementation = implementation;
      try {
        implementation.handle(api, this);
        return;
      } catch (Exception err) {
        api.sendResponse(messageId,
                         String.format("\"error\",\"%s\"",
                                       err.toString().replace("\n", "\\n")));
        return;
      }
    }
  }
}