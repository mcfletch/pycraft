package com.vrplumber.pycraft.bukkitserver;

import com.vrplumber.pycraft.bukkitserver.PycraftServerPlugin;
import com.vrplumber.pycraft.bukkitserver.IHandlerRegistry;
import com.vrplumber.pycraft.bukkitserver.IPycraftAPI;
import com.vrplumber.pycraft.bukkitserver.PycraftAPI;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.URL;
import java.util.List;
import java.util.ArrayList;
import java.util.Objects;
import javax.net.ServerSocketFactory;

public class APIServer implements Runnable {
  private int port = 4712;
  private boolean wanted = true;

  public void setWanted(boolean wanted) {
    this.wanted = wanted;
  }

  private PycraftServerPlugin plugin;

  public void setPlugin(PycraftServerPlugin plugin) {
    this.plugin = plugin;
  }

  public PycraftServerPlugin getPlugin() {
    return this.plugin;
  }

  public ServerSocket serverSocket;

  public Thread serverThread;
  public List<PycraftAPI> clients;
  public List<Thread> clientThreads;
  public IHandlerRegistry handlerRegistry;

  public APIServer(IHandlerRegistry registry) {
    clients = new ArrayList<PycraftAPI>();
    handlerRegistry = registry;
  }

  public void createServer() {
    serverThread = new Thread(this);
    serverThread.start();
  }

  public void run() {
    ServerSocketFactory serverSocketFactory = ServerSocketFactory.getDefault();
    serverSocket = null;
    try {
      serverSocket = serverSocketFactory.createServerSocket(port);
    } catch (IOException ignored) {
      return;
    }
    System.out.printf("API Server running on port: %s%n", port);
    try {
      while (wanted) {
        Socket socket = null;
        try {
          socket = serverSocket.accept();
          InputStream is = socket.getInputStream();
          BufferedReader br = new BufferedReader(new InputStreamReader(is, "UTF-8"));
          PycraftAPI handler = new PycraftAPI(this, socket, handlerRegistry);
          clients.add(handler);
          Thread clientThread = new Thread(handler);
          clientThreads.add(clientThread);

        } catch (IOException err) {
          // Just handle next request.
          err.printStackTrace();
        }
      }
    } finally {
      if (serverSocket != null) {
        try {
          serverSocket.close();
        } catch (IOException err) {
          err.printStackTrace();
        }
        serverSocket = null;
        for (PycraftAPI client : clients) {
          client.setWanted(false);
        }
        clients.clear();
        clientThreads.clear();
      }
    }
  }
}