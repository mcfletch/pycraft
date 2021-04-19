package com.vrplumber.pycraft.bukkitserver;

import com.vrplumber.pycraft.bukkitserver.APIServer;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.net.Socket;
import java.util.HashMap;

public class PycraftAPI implements Runnable {
  private PycraftServerPlugin getPlugin() { return this.server.getPlugin(); }

  private boolean wanted = true;
  public void setWanted(boolean wanted) { this.wanted = wanted; }

  public APIServer server;
  public Socket socket;
  public BufferedWriter sender;

  public void send(String formatted) {
    /* Send a fully formatted message to sender */
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
  public void sendResponse(Integer request, String formatted) {
    /* Send a response to the particular request */
    send(String.format("%d,%s", request, formatted));
  }

  PycraftAPI(APIServer server, Socket socket) {
    this.server = server;
    this.socket = socket;
  }

  public void run() {
    try {
      InputStream is = socket.getInputStream();
      OutputStream os = socket.getOutputStream();

      BufferedReader br =
          new BufferedReader(new InputStreamReader(is, "UTF-8"));
      sender = new BufferedWriter(new OutputStreamWriter(os, "UTF-8"));
      while (wanted) {
        String line = br.readLine();
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
  }

  public void dispatch(String line) {
    PycraftMessage message = PycraftMessage.parseHeader(line, this);
    if (message == null) {
      return;
    }
    message.dispatch(this);
  }
}