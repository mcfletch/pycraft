package com.vrplumber.pycraft.bukkitserver;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.lang.reflect.Modifier;
import java.lang.reflect.Parameter;
import java.lang.reflect.ParameterizedType;
import java.lang.reflect.Type;
import java.lang.Class;
import java.lang.annotation.Annotation;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.HashMap;
import java.util.HashSet;
import java.util.concurrent.Callable;
import java.util.stream.Collectors;
import java.util.Arrays;
import java.util.ArrayList;
import java.security.InvalidParameterException;

import java.util.stream.Stream;

import javax.xml.stream.events.Namespace;

import com.google.common.collect.Interner;
import com.vrplumber.pycraft.bukkitserver.MessageHandler;
import com.vrplumber.pycraft.bukkitserver.MethodHandler;

class MultiDispatchHandler implements MessageHandler {
    List<MethodHandler> methodHandlers;

    public MultiDispatchHandler(MethodHandler... handlers) {
        methodHandlers = new ArrayList<MethodHandler>();
        for (MethodHandler handler : handlers) {
            addHandler(handler);
        }
    }

    public String getMethod() {
        return methodHandlers.get(0).getMethod();
    }

    public void register(HandlerRegistry registry) {
        /* Called when we are registered with the registry (api likely not up yet) */
    }

    public MethodHandler addHandler(MethodHandler handler) {
        methodHandlers.add(handler);
        methodHandlers.sort((MethodHandler a, MethodHandler b) -> {
            int a_count = a.pointer.getParameterCount();
            int b_count = b.pointer.getParameterCount();
            return a_count < b_count ? -1 : (a_count > b_count ? 1 : 0);
        });
        return handler;
    }

    public Map<String, Object> getDescription() {
        Map<String, Object> result = new HashMap<String, Object>();
        result.put("type", "multidispatch");
        result.put("name", methodHandlers.get(0).getMethod());
        result.put("__doc__", "Dispatches to the multiple-dispatch method based on argument types");
        List<Object> commands = new ArrayList<Object>();
        for (MethodHandler handler : methodHandlers) {
            commands.add(handler.getDescription());
        }
        result.put("commands", commands);

        return result;
    }

    public String formatArgList(List<Object> args) {
        List<String> result = new ArrayList<String>();
        for (Object arg : args) {
            result.add(arg == null ? "null" : arg.toString());
        }
        return String.join(", ", result);
    }

    public Object handle(PycraftAPI api, PycraftMessage message) {
        List<Object> arguments = message.payload;
        List<String> errorResponse = new ArrayList<String>();
        for (MethodHandler handler : methodHandlers) {
            if (arguments.size() == handler.parameterCount) {
                /* Potential match */
                try {
                    return handler.handle(api, message);
                } catch (InvalidParameterException err) {
                    errorResponse.add(String.format("%s => %s", handler.pointer.toGenericString(), err.getMessage()));
                } catch (RuntimeException err) {
                    errorResponse.add(String.format("%s => %s", handler.pointer.toGenericString(), err.getMessage()));
                }
            }
        }
        if (errorResponse != null) {
            throw new RuntimeException(String.join("\n", errorResponse));
        }
        return (Object) null;
    }

}
