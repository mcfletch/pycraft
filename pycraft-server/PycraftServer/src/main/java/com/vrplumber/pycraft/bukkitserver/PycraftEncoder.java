package com.vrplumber.pycraft.bukkitserver;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.security.InvalidParameterException;
import java.util.Iterator;
import java.util.Arrays;
import java.util.Map;

public class PycraftEncoder {
    /* Encodes/Decodes a subset of JSON */

    static private Pattern intPattern = Pattern.compile("^([-+]*[0-9]+)[,]?");
    static private Pattern stringPattern =
        //   Pattern.compile("[\"]"
        //                   + "(([\\\\][n\"]|[^\\\"])*)"
        //                   + "[\"][,]?");
        Pattern.compile("^\"([^\"\\\\]*(?:\\\\.|[^\"\\\\]*)*)\"[,]?");
    static private Pattern whiteSpace = Pattern.compile("^\s+");
    
    String stripLeadingWS(String line) {
    }
  
    public List<Object> decode(String line) {
        List<Object> result = new ArrayList<Object>();
        List<List<Object>> stack = new ArrayList<List<Object>>();
        stack.add(result);
        Matcher match;
        Integer consumed = 0;
        while (line.length() > 0) {
            consumed = 0;
            match = whiteSpace.matcher(line);
            if (match.find()) {
                consumed=match.end();
            } else {
                match = intPattern.matcher(line);
                if (match.find()) {
                    result.add(Integer.parseInt(match.group(1)));
                    consumed = match.end();
                } else {
                    match = stringPattern.matcher(line);
                    if (match.find()) {
                    String rawString = match.group(1);
                    result.add(rawString.replace("\\n", "\n").replace("\\\"", "\""));
                    consumed = match.end();
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

    public String encode(Object message) {
        if (message instanceof Integer || message instanceof Double || message instanceof Float) {
        return message.toString();
        } else if (message instanceof String) {
        return String.format("\"%s\"",((String)message).replace("\\", "\\\\")
            .replace("\t", "\\t")
            .replace("\b", "\\b")
            .replace("\n", "\\n")
            .replace("\r", "\\r")
            .replace("\f", "\\f")
            .replace("\'", "\\'")
            .replace("\"", "\\\""));
        } else if (message instanceof List<?>) {
        List<Object> asArray = (List<Object>) message;
        List<String> content = new ArrayList<String>();
        for (Object item: asArray) {
            content.add(encode(item));
        }
        return String.format("[%s]",String.join(",",content));
        } else if (message instanceof Map<?,?>) {
        Map<String,Object> asMap = (Map<String,Object>) message;
        List<String> content = new ArrayList<String>();
        Iterator it = asMap.entrySet().iterator();
        while (it.hasNext()) {
            Map.Entry<String,Object> entry = (Map.Entry<String,Object>) it.next();
            content.add(String.format("%s:%s",
            encode(entry.getKey()),
            encode(entry.getValue())
            ));
        }
        return String.format("{%s}",String.join(",",content));
        }
        return (String)"null";
    }

}