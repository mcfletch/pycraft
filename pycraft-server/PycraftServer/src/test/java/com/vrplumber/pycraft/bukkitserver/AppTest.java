package com.vrplumber.pycraft.bukkitserver;

// import static org.hamcrest.Matchers.*;
import static org.junit.Assert.*;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import com.vrplumber.pycraft.bukkitserver.PycraftMessage;
import com.vrplumber.pycraft.bukkitserver.HandlerRegistry;
import java.util.List;
import org.bukkit.material.MaterialData;
import org.junit.Test;

public class AppTest {
  //   @Test
  //   public void serverSetup() {
  //     APIServer server = new APIServer();
  //     server.createServer();
  //     assertNotEquals(server.server, null);
  //   }

  @Test
  public void testParseInts() {
    List<Object> result = PycraftMessage.parseArgs("1,2");
    assertEquals(result.size(), 2);
    Object first = result.get(0);
    assertTrue(first instanceof Integer);
    assertTrue(first == (Integer)1);
    Object second = result.get(1);
    assertTrue(second instanceof Integer);
    assertTrue(second == (Integer)2);
  }
  @Test
  public void testParseSimpleString() {
    List<Object> result = PycraftMessage.parseArgs("\"this\",\"those\"");
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
    String test = "this\"\n";
    List<Object> result = PycraftMessage.parseArgs(
        "\"" + test.replace("\n", "\\n").replace("\"", "\\\"") + "\"");
    assertEquals(result.size(), 1);
    Object first = result.get(0);
    assertTrue(first instanceof String);
    assertEquals(first, test);
  }

  @Test
  public void registerHandler() {
    HandlerRegistry registry = HandlerRegistry.getInstance();
    registry.registerHandlers();
    MessageHandler registered = registry.getHandler("echo");
    assertNotEquals(registered, null);
  }
}
