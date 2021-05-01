package com.vrplumber.pycraft.bukkitserver;

import com.vrplumber.pycraft.bukkitserver.IPycraftAPI;
import com.vrplumber.pycraft.bukkitserver.APIServer;
import com.vrplumber.pycraft.bukkitserver.IHandlerRegistry;
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
  public PycraftServerPlugin getPlugin() { return this.server.getPlugin(); }

  private boolean wanted = true;
  public void setWanted(boolean wanted) { this.wanted = wanted; }

  private IHandlerRegistry registry;

  public APIServer server;
  public Socket socket;
  public BufferedWriter sender;
  public BufferedReader reader;

  public String lastResponse;

  public void send(String formatted) {
    /* Send a fully formatted message to sender */
    lastResponse = formatted;
    if (wanted && sender != null) {
      try {
        sender.write(formatted);
        sender.newLine();
      } catch (IOException err) {
        err.printStackTrace();
        wanted = false;
      }
    }
  }
  public String sendResponse(Integer request, Object message) {
    return sendResponse(request, encodeMessage(message));
  }
  public String sendResponse(Integer request, String formatted) {
    /* Send a response to the particular request */
    return sendError(request,0,formatted);
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
  //   List<String> content = new ArrayList<String>();
  //   for (Object item: message) {
  //     content.add(encodeMessage(item));
  //   }
  //   return String.format("[%s]",String.join(",",content));
  // }
  // public String encodeMessage(List<String> message) {
  //   List<String> content = new ArrayList<String>();
  //   for (Object item: message) {
  //     content.add(encodeMessage(item));
  //   }
  //   return String.format("[%s]",String.join(",",content));
  // }
  public String encodeMessage(Object message) {
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
        content.add(encodeMessage(item));
      }
      return String.format("[%s]",String.join(",",content));
    } else if (message instanceof Map<?,?>) {
      Map<String,Object> asMap = (Map<String,Object>) message;
      List<String> content = new ArrayList<String>();
      Iterator it = asMap.entrySet().iterator();
      while (it.hasNext()) {
        Map.Entry<String,Object> entry = (Map.Entry<String,Object>) it.next();
        content.add(String.format("%s:%s",
          encodeMessage(entry.getKey()),
          encodeMessage(entry.getValue())
        ));
      }
      return String.format("{%s}",String.join(",",content));
    }
    return (String)"null";
  }

  public void dispatch(String line) {
    /* Given an incoming string line, parse into a message and handle if possible */
    PycraftMessage message = PycraftMessage.parseHeader(line, this);
    if (message == null) {
      return;
    }
    MessageHandler handler = registry.getHandler(message.method);
    if (handler!=null) {
      message.setImplementation(handler);
      handler.handle(this,message);
    } else { 
      List<String> response = Arrays.asList("unknown-method",message.method);
      this.sendError(
        message.messageId,
        1,
        encodeMessage(response)
      );
    }
  }
}