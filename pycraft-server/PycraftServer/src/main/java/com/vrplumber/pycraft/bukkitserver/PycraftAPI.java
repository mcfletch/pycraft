package com.vrplumber.pycraft.bukkitserver;

import com.vrplumber.pycraft.bukkitserver.IPycraftAPI;
import com.vrplumber.pycraft.bukkitserver.APIServer;
import com.vrplumber.pycraft.bukkitserver.PycraftEncoder;
import com.vrplumber.pycraft.bukkitserver.converters.PycraftConverterRegistry;
import com.vrplumber.pycraft.bukkitserver.IHandlerRegistry;

import org.bukkit.Server;
import org.bukkit.World;
import org.bukkit.util.Vector;
import org.bukkit.Location;
import org.bukkit.block.data.BlockData;
import org.bukkit.block.Block;
import org.bukkit.entity.EntityType;
import org.bukkit.entity.Player;
import org.bukkit.event.Event;
import org.bukkit.plugin.Plugin;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.net.Socket;
import java.security.InvalidParameterException;

import java.util.logging.Logger;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.concurrent.Callable;

import javax.security.auth.callback.Callback;
import javax.swing.text.html.parser.Entity;

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

  public World getWorld(String name) {
    return getServer().getWorld(name);
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
  public PycraftConverterRegistry converterRegistry;
  public Map<String, PycraftMessage> subscriptions;

  public String lastResponse;

  public synchronized boolean send(String formatted) {
    /* Send a fully formatted message to sender */
    lastResponse = formatted;
    if (wanted && sender != null) {
      try {
        sender.write(formatted);
        sender.newLine();
        sender.flush();
        return true;
      } catch (IOException err) {
        err.printStackTrace();
        wanted = false;
      }
    }
    return false;
  }

  public String sendResponse(Integer request, Object message) {
    return sendResponse(request, encoder.encode(this, message));
  }

  public String sendResponse(Integer request, String formatted) {
    /* Send a response to the particular request */
    return sendError(request, 0, formatted);
  }

  public String sendError(Integer request, Integer errCode, Object message) {
    return sendError(request, errCode, encoder.encode(this, message));
  }

  public String sendError(Integer request, Integer errCode, String formatted) {
    /* Send a response to the particular request */
    Logger log = getLogger();
    String to_send = String.format("%d,%d,%s", request, errCode, formatted);
    log.info(String.format("sending %s", to_send));
    send(to_send);
    return to_send;
  }

  PycraftAPI(APIServer server, Socket socket, IHandlerRegistry registry) {
    this.server = server;
    this.socket = socket;
    this.registry = registry;
    this.converterRegistry = new PycraftConverterRegistry();
    this.encoder = new PycraftEncoder(this.converterRegistry);
    this.subscriptions = new HashMap<String, PycraftMessage>();
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

  public Logger getLogger() {
    if (server != null) {
      return server.getLogger();
    }
    return null;
  }

  public void run() {
    Logger log = getLogger();
    try {
      while (wanted) {
        String line = reader.readLine();
        if (line == null) {
          log.warning(String.format("Disconnection from %s", this.socket.getInetAddress().toString()));
          this.wanted = false;
        } else {
          log.warning(String.format("Incoming line %s", line));
          try {
            this.dispatch(line, true);
          } catch (Exception err) {
            err.printStackTrace();
          }
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
  public boolean onEvent(Event event) {
    /* Handle user's subscriptions and sending them the events */
    PycraftMessage request = this.subscriptions.get(event.getEventName());
    if (request != null) {
      this.sendResponse(request.messageId, event);
      return true;
    }
    return false;
  };

  public void dispatch(String line, boolean async) {
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
      Plugin plugin = server.getPlugin();
      Callable operation = (Callable) () -> {
        try {
          Object response = handler.handle(this, message);
          this.sendResponse(message.messageId, response);
          return response;
        } catch (InvalidParameterException e) {
          e.printStackTrace();
          List<String> response = Arrays.asList("error", e.getMessage());
          this.sendError(message.messageId, 1, response);
          return response;
        }
      };
      if (async) {
        plugin.getServer().getScheduler().callSyncMethod(plugin, operation);
      } else {
        try {
          operation.call();
        } catch (Exception e) {
          e.printStackTrace();
          this.sendError(message.messageId, 1, Arrays.asList("Error handling request"));
        }
      }
    } else if (message.method.get(0).equals("__methods__")) {
      this.sendResponse(message.messageId, registry.getMethodDescriptions());
    } else {
      List<String> response = Arrays.asList("unknown-method", message.method.get(0));
      this.sendError(message.messageId, 1, response);
    }
  }

  public Object getMessageItem(PycraftMessage message, Integer index) throws InvalidParameterException {
    return getMessageItem(message, index, false);
  }

  public Object getMessageItem(PycraftMessage message, Integer index, boolean nullOk) throws InvalidParameterException {
    if (index < 0 || index >= message.payload.size()) {
      if (nullOk) {
        return (Object) null;
      }
      throw new InvalidParameterException(String.format("Missing argument %d", index));
    }
    Object item = message.payload.get(index);
    if (item == null) {
      if (nullOk) {
        return (Object) null;
      }
      throw new InvalidParameterException(String.format("Expected non-null argument at %d", index));
    }
    return item;
  }

  public Object expectType(PycraftMessage message, Integer index, Class finalType) {
    return expectType(message, index, finalType, false);
  }

  public Object expectType(PycraftMessage message, Integer index, Class finalType, boolean nullOk) {
    Object item = getMessageItem(message, index, nullOk);
    if (finalType.isInstance(item)) {
      return item;
    }
    return this.converterRegistry.toJava(finalType, this, item);
  }

  public String expectString(PycraftMessage message, Integer index) throws InvalidParameterException {
    return (String) expectType(message, index, String.class);
  }

  public Boolean expectBoolean(PycraftMessage message, Integer index) throws InvalidParameterException {
    return (Boolean) expectType(message, index, Boolean.class);
  }

  public Integer expectInteger(PycraftMessage message, Integer index) throws InvalidParameterException {
    return (Integer) expectType(message, index, Boolean.class);
  }

  // public EntityType expectEntityType(PycraftMessage message, Integer index)
  // throws InvalidParameterException {
  // String value = expectString(message, index);
  // return EntityType.valueOf((String) value);
  // }

}