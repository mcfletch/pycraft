package com.vrplumber.pycraft.bukkitserver;

// import static org.hamcrest.Matchers.*;

import com.vrplumber.pycraft.bukkitserver.PycraftMessage;
import com.vrplumber.pycraft.bukkitserver.HandlerRegistry;
import com.vrplumber.pycraft.bukkitserver.PycraftEncoder;
import com.vrplumber.pycraft.bukkitserver.APIServer;
import com.vrplumber.pycraft.bukkitserver.PycraftServerPlugin;

import java.util.Arrays;
import java.util.List;
import java.util.logging.Handler;
import java.util.ArrayList;
import java.util.HashMap;
import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.Socket;
import org.bukkit.material.MaterialData;
import org.bukkit.Server;
import org.bukkit.World;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.TestInstance;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assertions.assertNotEquals;
import static org.mockito.Mockito.*;

import be.seeseemelk.mockbukkit.MockBukkit;
import be.seeseemelk.mockbukkit.ServerMock;

// import com.eclipsesource.json.Json;
// import com.eclipsesource.json.JsonValue;

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
public class AppTest {
  private PycraftServerPlugin plugin;
  private APIServer apiServer;
  private HandlerRegistry registry;
  private PycraftAPI api;

  @BeforeAll
  public void setUp() {
    ServerMock server = new ServerMock();
    MockBukkit.mock(server);
    server.addSimpleWorld("sample-world");
    plugin = (PycraftServerPlugin) MockBukkit.load(PycraftServerPlugin.class);
    HandlerRegistry registry = new HandlerRegistry();
    registry.registerHandlers();
    APIServer apiServer = new APIServer(registry);
    apiServer.setPlugin(plugin);
    plugin.setAPIServer(apiServer);
    Socket fakeSocket = mock(Socket.class);
    OutputStream fakeOutputStream = mock(OutputStream.class);
    InputStream fakeInputStream = mock(InputStream.class);
    try {
      when(fakeSocket.getOutputStream()).thenReturn(fakeOutputStream);
      when(fakeSocket.getInputStream()).thenReturn(fakeInputStream);
    } catch (IOException err) {
      err.printStackTrace();
    }

    api = new PycraftAPI(apiServer, fakeSocket, registry);
  }

  @AfterAll
  public void tearDown() {
    MockBukkit.unmock();
  }

  public PycraftAPI getMockApi() {
    return api;
    // APIServer server = mock(APIServer.class);
    // when(server.getPlugin()).thenReturn(plugin);
    // // when(plugin.getServer()).thenReturn(bukkitServer);
    // // when(bukkitServer.getWorlds()).thenReturn(Arrays.asList(world));

    // HandlerRegistry registry = HandlerRegistry.getInstance();
    // registry.registerHandlers();
    // return api;
  }

  @Test
  public void testParseInts() {
    PycraftEncoder encoder = new PycraftEncoder();
    List<Object> result = encoder.decode("[1,2]");
    assertEquals(result.size(), 2);
    Object first = result.get(0);
    assertTrue(first instanceof Integer);
    assertTrue(first == (Integer) 1);
    Object second = result.get(1);
    assertTrue(second instanceof Integer);
    assertTrue(second == (Integer) 2);
  }

  @Test
  public void testParseSimpleString() {
    PycraftEncoder encoder = new PycraftEncoder();
    List<Object> result = encoder.decode("[\"this\",\"those\"]");
    assertEquals(result.size(), 2);
    Object first = result.get(0);
    assertTrue(first instanceof String);
    assertEquals(first, "this");
    Object second = result.get(1);
    assertTrue(second instanceof String);
    assertEquals(second, "those");
  }

  @Test
  public void testParseStringEscapes() {
    PycraftEncoder encoder = new PycraftEncoder();
    String test = "this\"\n";
    List<Object> result = encoder.decode("[\"" + test.replace("\n", "\\n").replace("\"", "\\\"") + "\"]");
    assertEquals(result.size(), 1);
    Object first = result.get(0);
    assertTrue(first instanceof String);
    assertEquals(first, test);
  }

  @Test
  public void testParseList() {
    PycraftEncoder encoder = new PycraftEncoder();
    String test = "[1,2,3]";
    List<Object> result = encoder.decode(test);
    assertEquals(result.size(), 3);
    ArrayList<Object> expected = new ArrayList<Object>(Arrays.asList(1, 2, 3));
    assertEquals(result, expected);
  }

  @Test
  public void registerHandler() {
    HandlerRegistry registry = HandlerRegistry.getInstance();
    registry.registerHandlers();
    MessageHandler registered = registry.getHandler("echo");
    assertNotEquals(registered, null);
  }

  @Test
  public void echoTestArray() {
    PycraftEncoder encoder = new PycraftEncoder();

    PycraftAPI api = getMockApi();
    List<Integer> response = new ArrayList<Integer>(Arrays.asList(1, 2, 3));
    assertEquals("[1,2,3]", encoder.encode(response));

    api.dispatch("0,echo,[1,2,3]");

    assertEquals("0,0,[1,2,3]", api.lastResponse);

  }

  @Test
  public void encodeMap() {
    PycraftEncoder encoder = new PycraftEncoder();
    PycraftAPI api = getMockApi();
    HashMap<String, Object> response = new HashMap<String, Object>();
    response.put("testing", "Value");
    assertEquals("{\"testing\":\"Value\"}", encoder.encode(response));
  }

  @Test
  public void worldList() {

    PycraftAPI api = getMockApi();
    api.dispatch("1,World.getWorlds,[]");
    assertEquals("1,0,[\"sample-world\"]", api.lastResponse);
  }

  @Test
  public void getWorld() {

    PycraftAPI api = getMockApi();
    api.dispatch("1,World.getWorld,[]");
    assertEquals("1,0,\"sample-world\"", api.lastResponse);
  }

  @Test
  public void setWorld() {

    PycraftAPI api = getMockApi();
    api.dispatch("1,World.setWorld,[\"sample-world\"]");
    assertEquals("1,0,\"sample-world\"", api.lastResponse);
  }

  // @Test
  // public void loadJson() {
  // JsonValue value = Json.parse("[\"this\",23,null,false,true,[],{}]");
  // assertEquals(value.isArray(), true);
  // assertEquals(value.asArray().get(0).asString(),"this");
  // assertEquals(value.asArray().get(1).asInt(),23);
  // assertEquals(value.asArray().get(1).isNumber(), true);
  // assertEquals(value.asArray().get(3).isFalse(),true);
  // assertEquals(value.asArray().get(4).isTrue(),true);
  // assertEquals(value.asArray().get(5).isArray(),true);
  // assertEquals(value.asArray().get(6).isObject(),true);
  // }
}
