package com.vrplumber.pycraft.bukkitserver;

import com.vrplumber.pycraft.bukkitserver.IPycraftAPI;
import com.vrplumber.pycraft.bukkitserver.APIServer;
import com.vrplumber.pycraft.bukkitserver.PycraftEncoder;
import com.vrplumber.pycraft.bukkitserver.IHandlerRegistry;

import org.bukkit.Server;
import org.bukkit.World;
import org.bukkit.util.Vector;
import org.bukkit.Location;
import org.bukkit.block.data.BlockData;
import org.bukkit.block.Block;
import org.bukkit.entity.EntityType;
import org.bukkit.entity.Player;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.net.Socket;
import java.security.InvalidParameterException;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class PycraftAPI implements Runnable, IPycraftAPI {
  public PycraftServerPlugin getPlugin() {
    return this.server.getPlugin();
  }

  public Server getServer() {
    return this.getPlugin().getServer();
  }

  private boolean wanted = true;
  private World world = null;

  public void setWanted(boolean wanted) {
    this.wanted = wanted;
  }

  public World setWorld(String name) {
    /* Set our target world via name */
    World temp = this.getPlugin().getServer().getWorld(name);
    if (temp != null) {
      if (world != null) {
        /* Do any cleanup here */
      }
      world = temp;
    }
    return temp;

  }

  public World getWorld() {
    /* Get target world, defaulting to the first returned from getWorlds() */
    if (world == null) {
      for (World on_server : getServer().getWorlds()) {
        world = on_server;
        break;
      }
    }
    return world;
  }

  private IHandlerRegistry registry;

  public APIServer server;
  public Socket socket;
  public BufferedWriter sender;
  public BufferedReader reader;
  public PycraftEncoder encoder;

  public String lastResponse;

  public boolean send(String formatted) {
    /* Send a fully formatted message to sender */
    lastResponse = formatted;
    if (wanted && sender != null) {
      try {
        sender.write(formatted);
        sender.newLine();
        return true;
      } catch (IOException err) {
        err.printStackTrace();
        wanted = false;
      }
    }
    return false;
  }

  public String sendResponse(Integer request, Object message) {
    return sendResponse(request, encoder.encode(message));
  }

  public String sendResponse(Integer request, String formatted) {
    /* Send a response to the particular request */
    return sendError(request, 0, formatted);
  }

  public String sendError(Integer request, Integer errCode, Object message) {
    return sendError(request, errCode, encoder.encode(message));
  }

  public String sendError(Integer request, Integer errCode, String formatted) {
    /* Send a response to the particular request */
    String to_send = String.format("%d,%d,%s", request, errCode, formatted);
    send(to_send);
    return to_send;
  }

  PycraftAPI(APIServer server, Socket socket, IHandlerRegistry registry) {
    this.server = server;
    this.socket = socket;
    this.registry = registry;
    this.encoder = new PycraftEncoder();
    try {
      InputStream is = socket.getInputStream();
      OutputStream os = socket.getOutputStream();
      reader = new BufferedReader(new InputStreamReader(is, "UTF-8"));
      sender = new BufferedWriter(new OutputStreamWriter(os, "UTF-8"));
    } catch (IOException err) {
      err.printStackTrace();
      setWanted(false);
    }
  }

  public void run() {
    try {
      while (wanted) {
        String line = reader.readLine();
        if (line == null) {
          this.wanted = false;
        } else {
          this.dispatch(line);
        }
      }
    } catch (IOException err) {
      this.wanted = false;
      err.printStackTrace();
    }
    if (!this.socket.isClosed()) {
      try {
        this.socket.close();
      } catch (IOException err) {
        err.printStackTrace();
      }
    }
  }
  // public String encodeMessage(List<?> message) {
  // List<String> content = new ArrayList<String>();
  // for (Object item: message) {
  // content.add(encodeMessage(item));
  // }
  // return String.format("[%s]",String.join(",",content));
  // }
  // public String encodeMessage(List<String> message) {
  // List<String> content = new ArrayList<String>();
  // for (Object item: message) {
  // content.add(encodeMessage(item));
  // }
  // return String.format("[%s]",String.join(",",content));
  // }

  public void dispatch(String line) {
    /* Given an incoming string line, parse into a message and handle if possible */
    PycraftMessage message = PycraftMessage.parseHeader(line, this);
    if (message == null) {
      List<String> response = Arrays.asList("bad-header", "Unable to parse the message header");
      this.sendError(0, 1, response);
      return;
    }
    if (message.method == null || message.method.size() < 1) {
      List<String> response = Arrays.asList("invalid-request", "Method is not present or message could not be parsed");
      this.sendError(message.messageId, 1, response);
      return;
    }
    MessageHandler handler = registry.getHandler(message.method.get(0));
    if (handler != null) {
      message.addImplementation(handler);
      try {
        Object response = handler.handle(this, message);
        this.sendResponse(message.messageId, response);
      } catch (InvalidParameterException e) {
        e.printStackTrace();
        List<String> response = Arrays.asList("error", e.getMessage());
        this.sendError(message.messageId, 1, response);
      }
    } else {
      List<String> response = Arrays.asList("unknown-method", message.method.get(0));
      this.sendError(message.messageId, 1, response);
    }
  }

  public String expectString(PycraftMessage message, Integer index) throws InvalidParameterException {
    if (index < 0 || index >= message.payload.size()) {
      throw new InvalidParameterException(String.format("Missing String at argument %d", index));
    }
    Object item = message.payload.get(index);
    if (item == null) {
      throw new InvalidParameterException(String.format("Expected String at argument %d", index));
    }
    if (item instanceof String) {
      return (String) item;
    }
    throw new InvalidParameterException(String.format("Non-String at argument %d", index));
  }

  public Integer expectInteger(PycraftMessage message, Integer index) throws InvalidParameterException {
    if (index < 0 || index >= message.payload.size()) {
      throw new InvalidParameterException(String.format("Missing Integer at argument %d", index));
    }
    Object item = message.payload.get(index);
    if (item == null) {
      throw new InvalidParameterException(String.format("Expected Integer at argument %d", index));
    }
    if (item instanceof Integer) {
      return (Integer) item;
    }
    throw new InvalidParameterException(String.format("Non-Integer at argument %d", index));
  }

  private Double getNumber(List<Object> items, Integer index) {
    Object item = items.get(index);
    if (item instanceof Integer) {
      return ((Integer) item).doubleValue();
    } else if (item instanceof Double) {
      return (Double) item;
    } else if (item instanceof Float) {
      return ((Float) item).doubleValue();
    } else {
      throw new InvalidParameterException(String.format("Vector value %d is not a number %s", index, item.toString()));
    }
  }

  public Vector expectVector(PycraftMessage message, Integer index) throws InvalidParameterException {
    if (index < 0 || index >= message.payload.size()) {
      throw new InvalidParameterException(String.format("Missing Vector at argument %d", index));
    }
    Object item = message.payload.get(index);
    if (item == null) {
      throw new InvalidParameterException(String.format("Expected Vector at argument %d", index));
    }
    if (!(item instanceof List<?>)) {
      throw new InvalidParameterException(String.format("Did not get a list at argument %d", index));
    }
    List<Object> asList = (List<Object>) item;
    if (asList.size() != 3) {
      throw new InvalidParameterException(String.format("Did not get 3 items in list at argument %d", index));
    }
    Vector asVector = new Vector();
    asVector.setX(getNumber(asList, 0));
    asVector.setY(getNumber(asList, 1));
    asVector.setZ(getNumber(asList, 2));
    return asVector;
  }

  public BlockData expectBlockData(PycraftMessage message, Integer index) throws InvalidParameterException {
    String description = expectString(message, index);
    return getServer().createBlockData(description);
  }

  public EntityType expectEntityType(PycraftMessage message, Integer index) throws InvalidParameterException {

  }

}