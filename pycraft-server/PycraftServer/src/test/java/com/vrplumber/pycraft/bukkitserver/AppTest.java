package com.vrplumber.pycraft.bukkitserver;

// import static org.hamcrest.Matchers.*;
import static org.junit.Assert.*;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import com.vrplumber.pycraft.bukkitserver.PycraftMessage;
import com.vrplumber.pycraft.bukkitserver.HandlerRegistry;

import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;
import java.util.HashMap;
import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.Socket;
import org.bukkit.material.MaterialData;
import org.junit.Test;
import static org.mockito.Mockito.*;

// import com.eclipsesource.json.Json;
// import com.eclipsesource.json.JsonValue;

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
  public void testParseList() {
    String test = "[1,2,3]";
    List<Object> result = PycraftMessage.parseArgs(test);
    assertEquals(result.size(), 1);
    Object first = result.get(0);
    assertTrue(first instanceof ArrayList<?>);
    ArrayList<Object> arg = (ArrayList<Object>) first;
    ArrayList<Object> expected = new ArrayList<Object>(Arrays.asList(1,2,3));
    assertEquals(arg, expected);
  }

  @Test
  public void registerHandler() {
    HandlerRegistry registry = HandlerRegistry.getInstance();
    registry.registerHandlers();
    MessageHandler registered = registry.getHandler("echo");
    assertNotEquals(registered, null);
  }

  public PycraftAPI getMockApi() {
      HandlerRegistry registry = HandlerRegistry.getInstance();
      registry.registerHandlers();
      Socket fakeSocket = mock(Socket.class);
      OutputStream fakeOutputStream = mock(OutputStream.class);
      InputStream fakeInputStream = mock(InputStream.class);
      try {
        when(fakeSocket.getOutputStream()).thenReturn(fakeOutputStream);
        when(fakeSocket.getInputStream()).thenReturn(fakeInputStream);
      }catch (IOException err) {
        err.printStackTrace();
      }

      PycraftAPI api = new PycraftAPI(null, fakeSocket, registry );
      return api;

  }

  @Test
  public void echoTestArray() {

    PycraftAPI api = getMockApi();
    List<Integer> response = new ArrayList<Integer>(Arrays.asList(1,2,3));
    assertEquals("[1,2,3]", api.encodeMessage(response));
    
    api.dispatch("0,echo,[1,2,3]");

    assertEquals("0,0,[[1,2,3]]", api.lastResponse);

  }

  @Test
  public void encodeMap() {
    PycraftAPI api = getMockApi();
    HashMap<String,Object> response = new HashMap<String,Object>();
    response.put("testing","Value");
    assertEquals("{\"testing\":\"Value\"}", api.encodeMessage(response));
  }


//   @Test 
//   public void loadJson() {
//     JsonValue value = Json.parse("[\"this\",23,null,false,true,[],{}]");
//     assertEquals(value.isArray(), true);
//     assertEquals(value.asArray().get(0).asString(),"this");
//     assertEquals(value.asArray().get(1).asInt(),23);
//     assertEquals(value.asArray().get(1).isNumber(), true);
//     assertEquals(value.asArray().get(3).isFalse(),true);
//     assertEquals(value.asArray().get(4).isTrue(),true);
//     assertEquals(value.asArray().get(5).isArray(),true);
//     assertEquals(value.asArray().get(6).isObject(),true);
//   }
}

