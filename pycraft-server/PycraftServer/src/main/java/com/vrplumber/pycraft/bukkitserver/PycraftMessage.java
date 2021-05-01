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
  static private Pattern intPattern = Pattern.compile("^([-+]*[0-9]+)[,]?");
  static private Pattern stringPattern =
      //   Pattern.compile("[\"]"
      //                   + "(([\\\\][n\"]|[^\\\"])*)"
      //                   + "[\"][,]?");
      Pattern.compile("^\"([^\"\\\\]*(?:\\\\.|[^\"\\\\]*)*)\"[,]?");


  public Integer messageId = 0;
  public String method = "";
  public String payload = "";
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
    Matcher intMatch;
    Matcher stringMatch;
    Integer consumed = 0;
    while (line.length() > 0) {
      intMatch = intPattern.matcher(line);
      if (intMatch.find()) {
        result.add(Integer.parseInt(intMatch.group(1)));
        consumed = intMatch.end();
      } else {
        stringMatch = stringPattern.matcher(line);
        if (stringMatch.find()) {
          String rawString = stringMatch.group(1);
          result.add(rawString.replace("\\n", "\n").replace("\\\"", "\""));
          consumed = stringMatch.end();
        } else {
          if (line.startsWith("[")) {
            System.out.printf("Starting array: %s", line);
            List<Object> child = new ArrayList<Object>();
            result.add(child);
            result = child;
            stack.add(result);
            consumed = 1;
          } else if (line.startsWith("]")) {
            consumed = 1;
            if (stack.size() > 1) {
              System.out.printf("Finished array: %s", line);
              stack.remove(result);
              result = stack.get(stack.size() - 1);
            } else {
              System.out.printf("Unable to pop array: %s", stack);
              throw new InvalidParameterException(String.format(
                  "Malformed list, more closing brackets then opening ones"));
            }
          } else {
            throw new InvalidParameterException(
                String.format("Unknown data-format for %s", line));
          }
        }
      }
      if (consumed != 0) {
        line = line.substring(consumed);
      } else {
        throw new InvalidParameterException(
          String.format("Unexpected content at %s", line)
        );
      }
    }
    return stack.get(0);
  }

}