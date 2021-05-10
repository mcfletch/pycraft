package com.vrplumber.pycraft.bukkitserver;

// import static org.hamcrest.Matchers.*;

import com.vrplumber.pycraft.bukkitserver.PycraftMessage;
import com.vrplumber.pycraft.bukkitserver.HandlerRegistry;
import com.vrplumber.pycraft.bukkitserver.PycraftEncoder;
import com.vrplumber.pycraft.bukkitserver.APIServer;
import com.vrplumber.pycraft.bukkitserver.PycraftServerPlugin;
import com.vrplumber.pycraft.bukkitserver.converters.PycraftConverterRegistry;

import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.logging.Handler;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Set;
import java.util.HashSet;
import java.util.stream.Collectors;
import java.util.stream.Stream;
import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.Socket;
import org.bukkit.material.MaterialData;
import org.bukkit.plugin.PluginManager;
import org.bukkit.Location;
import org.bukkit.Material;
import org.bukkit.Server;
import org.bukkit.World;
import org.bukkit.util.Vector;
import org.bukkit.entity.Player;
import org.bukkit.event.player.AsyncPlayerChatEvent;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.TestInstance;

// import static org.junit.Assert.assertEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assertions.assertNotEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertNull;
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
  private ServerMock server;

  @BeforeAll
  public void setUp() {
    server = new ServerMock();
    MockBukkit.mock(server);
    server.addSimpleWorld("sample-world");
    server.addPlayer("sam");
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
    apiServer.clients.add(api);
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
    assertEquals("[1,2,3]", encoder.encode(api, response));

    api.dispatch("0,echo,[1,2,3]", false);

    assertEquals("0,0,[1,2,3]", api.lastResponse);

  }

  @Test
  public void encodeMap() {
    PycraftEncoder encoder = new PycraftEncoder();
    PycraftAPI api = getMockApi();
    HashMap<String, Object> response = new HashMap<String, Object>();
    response.put("testing", "Value");
    assertEquals("{\"testing\":\"Value\"}", encoder.encode(api, response));
  }

  @Test
  public void worldList() {

    PycraftAPI api = getMockApi();
    api.dispatch("1,World.getWorlds,[]", false);
    assertEquals("1,0,[\"sample-world\"]", api.lastResponse);
  }

  @Test
  public void getWorld() {

    PycraftAPI api = getMockApi();
    api.dispatch("1,World.getWorld,[null]", false);
    assertTrue(api.lastResponse.indexOf("sample-world") > -1);
  }

  @Test
  public void getMaterialTypes() {

    PycraftAPI api = getMockApi();
    api.dispatch("1,World.getMaterialTypes,[]", false);
    assertTrue(api.lastResponse.indexOf("netherite_block") > -1);
  }

  @Test
  public void getEntityTypes() {

    PycraftAPI api = getMockApi();
    api.dispatch("1,World.getEntityTypes,[]", false);
    assertTrue(api.lastResponse.indexOf("spider") > -1);
  }

  @Test
  public void setWorld() {

    PycraftAPI api = getMockApi();
    api.dispatch("1,World.setWorld,[\"sample-world\"]", false);
    assertEquals("1,0,\"sample-world\"", api.lastResponse);
  }

  // @Test
  // public void getBlock() {

  // PycraftAPI api = getMockApi();
  // api.dispatch("1,World.getBlock,[[\"sample-world\",0,0,0]]", false);
  // assertEquals("1,0,\"sample-world\"", api.lastResponse);
  // }

  // @Test
  // public void setBlock() {

  // PycraftAPI api = getMockApi();
  // api.dispatch("1,World.setBlock,[[0,0,0],\"air\"]", false);
  // assertEquals("1,0,\"sample-world\"", api.lastResponse);
  // }

  // @Test
  // public void setBlocks() {

  // PycraftAPI api = getMockApi();
  // api.dispatch("1,World.setBlocks,[null,[0,0,0],[5,5,5],\"air\"]", false);
  // assertEquals("1,0,[[0,0,0],[5,5,5],\"air\"]", api.lastResponse);
  // }

  @Test
  public void getGameRules() {

    PycraftAPI api = getMockApi();
    api.dispatch("1,World.getGameRules,[\"sample-world\"]", false);
    assertTrue(api.lastResponse.startsWith("1,0"));
  }

  // @Test
  // public void isHardcore() {

  // PycraftAPI api = getMockApi();
  // api.dispatch("1,World.isHardcore,[]",false);
  // assertEquals("1,0,false", api.lastResponse);
  // }

  @Test
  public void getPlayers() {

    PycraftAPI api = getMockApi();
    api.dispatch("1,World.getPlayers,[\"sample-world\"]", false);
    assertTrue(api.lastResponse.startsWith("1,0"), api.lastResponse);
  }

  @Test
  public void postToChat() {

    PycraftAPI api = getMockApi();
    api.dispatch("1,World.postToChat,[\"Hello Chat\"]", false);
    assertTrue(api.lastResponse.startsWith("1,0"), api.lastResponse);
  }

  @Test
  public void subscribeToChat() {
    PycraftAPI api = getMockApi();
    World world = server.getWorlds().get(0);
    PluginManager pluginManager = server.getPluginManager();
    api.dispatch("1,subscribe,[\"AsyncPlayerChatEvent\",true]", false);
    assertTrue(api.lastResponse.startsWith("1,0"), api.lastResponse);

    Set<Player> targets = new HashSet<>();
    AsyncPlayerChatEvent event = new AsyncPlayerChatEvent(true, world.getPlayers().get(0), "Sample Message", targets);
    pluginManager.callEvent(event);
    assertTrue(api.lastResponse.indexOf("Sample Message") > 0, api.lastResponse);

  }

  @Test
  public void testConverterByClass() {
    PycraftConverterRegistry registry = new PycraftConverterRegistry();
    PycraftAPI api = getMockApi();

    Object result = registry.toJava(String.class, api, (String) "Sample String");
    assertTrue(result.equals("Sample String"));
    String encoded = null;
    encoded = registry.fromJava(api, "\n\t");
    assertEquals(encoded, "\"\\n\\t\"");

    result = registry.toJava(String.class, api, (Object) Boolean.TRUE);
    assertTrue(result.equals("true"));
    encoded = registry.fromJava(api, Boolean.TRUE);
    assertEquals(encoded, "true");

    result = registry.toJava(Double.class, api, (Double) 3.1415);
    assertEquals((double) result, 3.1415, 0.001);
    encoded = registry.fromJava(api, (Double) 3.1415);
    assertEquals(encoded, "3.1415");

    result = registry.toJava(Integer.class, api, (Double) 3.1415);
    assertTrue(result == (Integer) 3);
    encoded = registry.fromJava(api, (Integer) 31415);
    assertEquals(encoded, "31415");

    List<Integer> intList = new ArrayList<Integer>(Arrays.asList(1, 2, 3));
    result = registry.toJava(intList.getClass(), api, intList);
    assertTrue(result == intList);
    encoded = registry.fromJava(api, intList);
    assertEquals(encoded, "[1,2,3]");

    Map<String, Integer> intMap = new HashMap<String, Integer>();
    intMap.put("x", 3);
    result = registry.toJava(intMap.getClass(), api, intMap);
    assertTrue(result == intMap);
    encoded = registry.fromJava(api, intMap);
    assertEquals(encoded, "{\"x\":3}");

    Integer[] intArray = new Integer[] { (Integer) 1, (Integer) 2, (Integer) 3 };
    result = registry.toJava(Integer[].class, api, intArray);
    assertTrue(result == intArray);
    encoded = registry.fromJava(api, intArray);
    assertEquals(encoded, "[1,2,3]");

    result = registry.toJava(Material.class, api, (String) "AIR");
    assertTrue(result == Material.AIR);
    encoded = registry.fromJava(api, Material.AIR);
    assertEquals(encoded, "\"AIR\"");

    encoded = registry.fromJava(api, api.getWorld().getPlayers());
    assertTrue(encoded.startsWith("[{"));
    assertTrue(encoded.endsWith("}]"));

    // Back and forth to a vector...
    result = registry.toJava(Vector.class, api, intList);
    assertNotNull(result);
    assertTrue(result instanceof Vector);
    assertTrue(((Vector) result).getX() == 1);
    assertTrue(((Vector) result).getZ() == 3);

    result = registry.fromJava(api, result);
    assertEquals(result, "[1.0,2.0,3.0]");

    // Back and forth to a Location object
    result = registry.toJava(Location.class, api, intList);
    assertNotNull(result);
    assertTrue(result instanceof Location);
    assertTrue(((Location) result).getX() == 1);
    assertTrue(((Location) result).getZ() == 3);

    result = registry.fromJava(api, result);
    assertEquals(result, "[\"sample-world\",1.0,2.0,3.0,0.0,0.0]");

    intList.add((Integer) 8);
    intList.add((Integer) 10);
    result = registry.toJava(Location.class, api, intList);
    result = registry.fromJava(api, result);
    assertEquals(result, "[\"sample-world\",1.0,2.0,3.0,8.0,10.0]");

    AsyncPlayerChatEvent chatEvent = new AsyncPlayerChatEvent(true, server.getPlayer("sam"), "Testing message",
        server.getWorlds().get(0).getPlayers().stream().collect(Collectors.toSet()));
    registry.fromJava(api, chatEvent);
    assertNotNull(result);
    assertTrue(encoded.startsWith("[{"));
    assertTrue(encoded.endsWith("}]"));

  }

}
