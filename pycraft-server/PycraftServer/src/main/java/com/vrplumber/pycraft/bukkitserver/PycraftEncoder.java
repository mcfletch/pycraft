package com.vrplumber.pycraft.bukkitserver;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.security.InvalidParameterException;
import java.lang.Iterable;
import java.lang.Enum;
import java.util.Iterator;
import java.util.Arrays;
import java.util.Map;

import org.bukkit.World;
import org.bukkit.block.data.BlockData;
import org.bukkit.block.Block;
import org.bukkit.Location;
import org.bukkit.util.Vector;
import org.bukkit.entity.Entity;
import org.bukkit.entity.Player;
import org.bukkit.event.block.BlockBreakEvent;
import org.bukkit.event.block.BlockEvent;
import org.bukkit.event.player.AsyncPlayerChatEvent;
import org.bukkit.event.player.PlayerInteractEvent;

public class PycraftEncoder {
    /* Encodes/Decodes a subset of JSON */

    static private Pattern intPattern = Pattern.compile("^([-+]*[0-9]+)");
    static private Pattern floatPattern = Pattern.compile("^([-+]?([0-9]*\\.[0-9]+))");
    static private Pattern stringPattern =
            // Pattern.compile("[\"]"
            // + "(([\\\\][n\"]|[^\\\"])*)"
            // + "[\"][,]?");
            Pattern.compile("^\"([^\"\\\\]*(?:\\\\.|[^\"\\\\]*)*)\"");
    static private Pattern whiteSpace = Pattern.compile("^[ \\t\\n\\r,]+");

    public List<Object> decode(String line) {
        if (!(line.startsWith("[") && line.endsWith("]"))) {
            throw new InvalidParameterException(String.format("Parameters must be wrapped with [] characters", line));
        }
        line = line.substring(1, line.length() - 1);
        List<Object> result = new ArrayList<Object>();
        List<List<Object>> stack = new ArrayList<List<Object>>();
        stack.add(result);
        Matcher match;
        Integer consumed = 0;
        while (line.length() > 0) {
            consumed = 0;
            match = whiteSpace.matcher(line);
            if (match.find()) {
                consumed = match.end();
            } else {
                match = floatPattern.matcher(line);
                if (match.find()) {
                    result.add(Double.parseDouble(match.group(1)));
                    consumed = match.end();
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
                                List<Object> child = new ArrayList<Object>();
                                result.add(child);
                                result = child;
                                stack.add(result);
                                consumed = 1;
                            } else if (line.startsWith("]")) {
                                consumed = 1;
                                if (stack.size() > 1) {
                                    stack.remove(result);
                                    result = stack.get(stack.size() - 1);
                                } else {
                                    throw new InvalidParameterException(
                                            String.format("Malformed list, more closing brackets then opening ones"));
                                }
                            } else if (line.startsWith("true")) {
                                result.add(Boolean.TRUE);
                                consumed = 4;
                            } else if (line.startsWith("false")) {
                                result.add(Boolean.FALSE);
                                consumed = 5;
                            } else if (line.startsWith("null")) {
                                result.add((Object) null);
                                consumed = 4;
                            } else {
                                throw new InvalidParameterException(String.format("Unknown data-format for %s", line));
                            }
                        }
                    }
                }
            }
            if (consumed != 0) {
                line = line.substring(consumed);
            } else {
                throw new InvalidParameterException(String.format("Unexpected content at %s", line));
            }
        }
        return stack.get(0);
    }

    public String encode(Object message) {
        if (message instanceof Enum) {
            return encode(((Enum) message).name());
        } else if (message instanceof Integer || message instanceof Double || message instanceof Float
                || message instanceof Boolean) {
            return message.toString();
        } else if (message instanceof String) {
            return String.format("\"%s\"",
                    ((String) message).replace("\\", "\\\\").replace("\t", "\\t").replace("\b", "\\b")
                            .replace("\n", "\\n").replace("\r", "\\r").replace("\f", "\\f").replace("\'", "\\'")
                            .replace("\"", "\\\""));
        } else if (message instanceof List<?>) {
            List<Object> asArray = (List<Object>) message;
            List<String> content = new ArrayList<String>();
            for (Object item : asArray) {
                content.add(encode(item));
            }
            return String.format("[%s]", String.join(",", content));
        } else if (message instanceof Map<?, ?>) {
            Map<String, Object> asMap = (Map<String, Object>) message;
            List<String> content = new ArrayList<String>();
            Iterator it = asMap.entrySet().iterator();
            while (it.hasNext()) {
                Map.Entry<String, Object> entry = (Map.Entry<String, Object>) it.next();
                content.add(String.format("%s:%s", encode(entry.getKey()), encode(entry.getValue())));
            }
            return String.format("{%s}", String.join(",", content));
        } else if (message instanceof String[] || message instanceof Object[] || message instanceof Integer[]
                || message instanceof Double[] || message instanceof Float[]) {
            List<String> content = new ArrayList<String>();
            Object[] asArray = (Object[]) message;
            for (int i = 0; i < asArray.length; i++) {
                content.add(encode((Object) asArray[i]));
            }
            return String.format("[%s]", String.join(",", content));
        } else if (message instanceof World) {
            return encode(((World) message).getName());
        } else if (message instanceof BlockData) {
            return encode(((BlockData) message).getAsString());
        } else if (message instanceof Player) {
            Map<String, Object> asMap = new HashMap<String, Object>();
            Player asPlayer = (Player) message;
            asMap.put("uuid", asPlayer.getUniqueId());
            asMap.put("type", asPlayer.getType());
            asMap.put("name", asPlayer.getName());
            asMap.put("location", asPlayer.getLocation());
            asMap.put("direction", asPlayer.getLocation().getDirection());
            return encode(asMap);
        } else if (message instanceof Entity) {
            Map<String, Object> asMap = new HashMap<String, Object>();
            Entity asEntity = (Entity) message;
            asMap.put("id", asEntity.getEntityId());
            asMap.put("type", asEntity.getType());
            asMap.put("name", asEntity.getName());
            asMap.put("location", asEntity.getLocation());
            return encode(asMap);
        } else if (message instanceof Block) {
            org.bukkit.block.Block asBlock = (Block) message;
            Location loc = asBlock.getLocation();
            Map<String, Object> asMap = new HashMap<String, Object>();
            asMap.put("loc", loc);
            asMap.put("mat", asBlock.getBlockData());
            return encode(asMap);
        } else if (message instanceof Location) {
            Location loc = (Location) message;
            List<Double> asList = Arrays.asList((Double) loc.getX(), (Double) loc.getY(), (Double) loc.getZ());
            return encode(asList);
        } else if (message instanceof Vector) {
            Vector vec = (Vector) message;
            List<Double> asList = Arrays.asList((Double) vec.getX(), (Double) vec.getY(), (Double) vec.getZ());
            return encode(asList);
        } else if (message instanceof AsyncPlayerChatEvent) {
            AsyncPlayerChatEvent asEvent = (AsyncPlayerChatEvent) message;
            Map<String, Object> asMap = new HashMap<String, Object>();
            asMap.put("type", asEvent.getEventName());
            asMap.put("player", asEvent.getPlayer());
            asMap.put("message", asEvent.getMessage());
            return encode(asMap);
        } else if (message instanceof BlockBreakEvent) {
            BlockBreakEvent asEvent = (BlockBreakEvent) message;
            Map<String, Object> asMap = new HashMap<String, Object>();
            asMap.put("type", asEvent.getEventName());
            asMap.put("block", asEvent.getBlock());
            asMap.put("player", asEvent.getPlayer());
            return encode(asMap);
        }
        return (String) "null";
    }

}