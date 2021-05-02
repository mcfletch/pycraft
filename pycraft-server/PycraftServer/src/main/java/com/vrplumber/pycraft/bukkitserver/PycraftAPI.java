package com.vrplumber.pycraft.bukkitserver;

import com.vrplumber.pycraft.bukkitserver.IPycraftAPI;
import com.vrplumber.pycraft.bukkitserver.APIServer;
import com.vrplumber.pycraft.bukkitserver.PycraftEncoder;
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
  public PycraftServerPlugin getPlugin() {
    return this.server.getPlugin();
  }

  private boolean wanted = true;

  public void setWanted(boolean wanted) {
    this.wanted = wanted;
  }

  private IHandlerRegistry registry;

  public APIServer server;
  public Socket socket;
  public BufferedWriter sender;
  public BufferedReader reader;
  public PycraftEncoder encoder;

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
      handler.handle(this, message);
    } else {
      List<String> response = Arrays.asList("unknown-method", message.method.get(0));
      this.sendError(message.messageId, 1, response);
    }
  }
}