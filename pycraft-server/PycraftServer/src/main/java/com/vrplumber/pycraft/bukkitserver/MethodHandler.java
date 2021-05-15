package com.vrplumber.pycraft.bukkitserver;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.lang.reflect.Modifier;
import java.lang.reflect.Parameter;
import java.lang.reflect.ParameterizedType;
import java.lang.reflect.Type;
import java.lang.Class;
import java.util.List;
import java.util.Map;
import java.util.HashMap;
import java.util.concurrent.Callable;
import java.util.stream.Collectors;
import java.util.Arrays;
import java.util.ArrayList;
import java.security.InvalidParameterException;

import java.util.stream.Stream;

import com.google.common.collect.Interner;
import com.vrplumber.pycraft.bukkitserver.MessageHandler;

class MethodHandler implements MessageHandler {
    /* Handle a method by dispatching to a method on a class instance */
    public Class cls = null;
    public Boolean staticMethod = false;
    public Method pointer = null;

    public void register(HandlerRegistry registry) {
        /* Called when we are registered with the registry (api likely not up yet) */
    }

    public static List<MethodHandler> forClass(Class cls) {
        return forClass(cls, null);
    }

    public Map<String, Object> getDescription() {
        Map<String, Object> result = new HashMap<String, Object>();
        int modifiers = pointer.getModifiers();
        result.put("type", "method");
        result.put("static", (Boolean) Modifier.isStatic(modifiers));
        result.put("name", pointer.getName());
        result.put("__doc__", pointer.toGenericString());
        result.put("argcount", pointer.getParameterCount());
        List<String> typeNames = new ArrayList<String>();
        for (Class cls : pointer.getParameterTypes()) {
            typeNames.add(cls.getSimpleName());
        }
        result.put("argtypes", typeNames);
        result.put("returntype", pointer.getReturnType().getSimpleName());
        Type genericReturn = pointer.getGenericReturnType();
        if (genericReturn instanceof ParameterizedType) {
            ParameterizedType parameterized = (ParameterizedType) genericReturn;
            List<String> subTypeNames = new ArrayList<String>();
            for (Type innerType : parameterized.getActualTypeArguments()) {
                if (innerType instanceof Class) {
                    subTypeNames.add(((Class) innerType).getSimpleName());
                } else {
                    subTypeNames.add(innerType.getTypeName());
                }
            }
            result.put("returntype_subtypes", subTypeNames);
        }
        return result;
        // List<String> parameterList = new ArrayList<String>();
        // for (Parameter parameter : pointer.getParameters()) {
        // parameterList.add(String.format("%s: %s",
        // parameter.getType().getSimpleName(), parameter.getName()));
        // }
        // return String.format("%s(%s) => %s", pointer.getName(), String.join(", ",
        // parameterList),
        // pointer.getReturnType().getSimpleName());

    }

    public static List<MethodHandler> forClass(Class cls, List<String> names) {
        /*
         * Create MethodHandler instances for methods on cls
         * 
         */
        Method[] methods = cls.getMethods();
        List<MethodHandler> handlers = new ArrayList<MethodHandler>();
        for (Method method : methods) {
            int modifiers = method.getModifiers();
            if (!(Modifier.isPublic(modifiers))) {
                continue;
            }
            if (names == null || names.indexOf(method.getName()) > -1) {
                MethodHandler handler = new MethodHandler(cls, method, Modifier.isStatic(modifiers));
                handlers.add(handler);
            }
        }
        return handlers;
    }

    public String getMethod() {
        return pointer.getName();
    }

    public MethodHandler(Class cls, Method pointer, boolean isStatic) {
        /*
         * Create a new MethodHandler that operates on cls instances of the given Method
         */
        this.cls = cls;
        this.pointer = pointer;
        this.staticMethod = isStatic;
    }

    private Object argumentCoerce(PycraftAPI api, List<Object> arguments, Integer index, List<Class> parameterTypes) {
        return api.converterRegistry.toJava(parameterTypes.get(index), api, arguments.get(index));
    }

    private Object pointerInvoke(PycraftAPI api, PycraftMessage message, List<Object> arguments)
            throws IllegalAccessException, IllegalArgumentException, InvocationTargetException {
        /*
         * Invoke our pointer doing (manual) unpacking of arguments
         * 
         * for i in range(0,10):
         * 
         * 
         */
        List<Class> parameterTypes = Arrays.asList(this.pointer.getParameterTypes());
        List<Object> parameters = new ArrayList<Object>();
        if (parameterTypes.size() != arguments.size()) {
            throw new InvalidParameterException(
                    String.format("Needed %s parameters, got %s", parameterTypes.size(), arguments.size()));
        }
        for (int index = 0; index < arguments.size(); index++) {
            parameters.add(api.converterRegistry.toJava(parameterTypes.get(index), api, arguments.get(index)));
        }

        if (parameters.size() == 0) {
            return (Object) this.pointer.invoke(cls.cast(message.instance));
        } else if (parameters.size() == 1) {
            return (Object) this.pointer.invoke(cls.cast(message.instance), parameters.get(0));
        } else if (parameters.size() == 2) {
            return (Object) this.pointer.invoke(cls.cast(message.instance), parameters.get(0), parameters.get(1));
        } else if (parameters.size() == 3) {
            return (Object) this.pointer.invoke(cls.cast(message.instance), parameters.get(0), parameters.get(1),
                    parameters.get(2));
        } else if (parameters.size() == 4) {
            return (Object) this.pointer.invoke(cls.cast(message.instance), parameters.get(0), parameters.get(1),
                    parameters.get(2), parameters.get(3));
        } else if (parameters.size() == 5) {
            return (Object) this.pointer.invoke(cls.cast(message.instance), parameters.get(0), parameters.get(1),
                    parameters.get(2), parameters.get(3), parameters.get(4));
        } else if (parameters.size() == 6) {
            return (Object) this.pointer.invoke(cls.cast(message.instance), parameters.get(0), parameters.get(1),
                    parameters.get(2), parameters.get(3), parameters.get(4), parameters.get(5));
        } else if (parameters.size() == 7) {
            return (Object) this.pointer.invoke(cls.cast(message.instance), parameters.get(0), parameters.get(1),
                    parameters.get(2), parameters.get(3), parameters.get(4), parameters.get(5), parameters.get(6));
        } else if (parameters.size() == 8) {
            return (Object) this.pointer.invoke(cls.cast(message.instance), parameters.get(0), parameters.get(1),
                    parameters.get(2), parameters.get(3), parameters.get(4), parameters.get(5), parameters.get(6),
                    parameters.get(7));
        } else if (parameters.size() == 9) {
            return (Object) this.pointer.invoke(cls.cast(message.instance), parameters.get(0), parameters.get(1),
                    parameters.get(2), parameters.get(3), parameters.get(4), parameters.get(5), parameters.get(6),
                    parameters.get(7), parameters.get(8));
        } else {
            throw new InvalidParameterException("Only currently support up to 6 parameters");
        }
    }

    public Object handle(PycraftAPI api, PycraftMessage message) {
        List<Object> arguments = message.payload;
        if (!staticMethod) {
            int consumed = 0;
            message.instance = api.expectType(message, 0, cls);
            consumed = 1;
            arguments = message.payload.subList(consumed, message.payload.size());
        } else {
            message.instance = null;
        }
        Object result;
        try {
            api.getLogger().info(String.format("%s result call", pointer.getName()));
            result = pointerInvoke(api, message, arguments);
            api.getLogger().info(
                    String.format("%s result %s", pointer.getName(), result == null ? "null" : result.toString()));
            if (pointer.getReturnType() == Void.TYPE) {
                result = Boolean.TRUE;
            } else if (pointer == null) {
                result = Boolean.TRUE;
            }
        } catch (IllegalAccessException | IllegalArgumentException | InvocationTargetException e) {
            e.printStackTrace();
            throw new InvalidParameterException(
                    String.format("%s failed with %s", pointer.toGenericString(), e.getMessage()));
        }
        return result;
    };

}