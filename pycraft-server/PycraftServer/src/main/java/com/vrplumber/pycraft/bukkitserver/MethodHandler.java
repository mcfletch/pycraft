package com.vrplumber.pycraft.bukkitserver;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.lang.reflect.Modifier;
import java.lang.Class;
import java.util.List;
import java.util.ArrayList;
import java.security.InvalidParameterException;
import com.vrplumber.pycraft.bukkitserver.MessageHandler;

class MethodHandler implements MessageHandler {
    /* Handle a method by dispatching to a method on a class instance */
    public Class cls = null;
    public Boolean staticMethod = false;
    public Method pointer = null;
    public Method defaultTarget = null; // Function.invoke(api,message) => producing instance of cls

    public void register(HandlerRegistry registry) {
        /* Called when we are registered with the registry (api likely not up yet) */
    }

    public static List<MethodHandler> forClass(Class cls) {
        return forClass(cls, null);
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

    private Object pointerInvoke(PycraftAPI api, PycraftMessage message, List<Object> arguments)
            throws IllegalAccessException, IllegalArgumentException, InvocationTargetException {
        /* Invoke our pointer doing (manual) unpacking of arguments */
        if (arguments.size() == 0) {
            return (Object) this.pointer.invoke(cls.cast(message.instance));
        } else if (arguments.size() == 1) {
            return (Object) this.pointer.invoke(cls.cast(message.instance), arguments.get(0));
        } else if (arguments.size() == 2) {
            return (Object) this.pointer.invoke(cls.cast(message.instance), arguments.get(0), arguments.get(1));
        } else if (arguments.size() == 3) {
            return (Object) this.pointer.invoke(cls.cast(message.instance), arguments.get(0), arguments.get(1),
                    arguments.get(2));
        } else if (arguments.size() == 4) {
            return (Object) this.pointer.invoke(cls.cast(message.instance), arguments.get(0), arguments.get(1),
                    arguments.get(2), arguments.get(3));
        } else if (arguments.size() == 5) {
            return (Object) this.pointer.invoke(cls.cast(message.instance), arguments.get(0), arguments.get(1),
                    arguments.get(2), arguments.get(3), arguments.get(4));
        } else if (arguments.size() == 6) {
            return (Object) this.pointer.invoke(cls.cast(message.instance), arguments.get(0), arguments.get(1),
                    arguments.get(2), arguments.get(3), arguments.get(4), arguments.get(5));
        } else {
            throw new InvalidParameterException("Only currently support up to 6 parameters");
        }
    }

    public Object handle(PycraftAPI api, PycraftMessage message) {
        List<Object> arguments = message.payload;
        if (!staticMethod) {
            int consumed = 0;
            if (message.payload.size() < 1) {
                if (defaultTarget != null) {
                    try {
                        message.instance = defaultTarget.invoke(api, message);
                    } catch (IllegalAccessException | IllegalArgumentException | InvocationTargetException e) {
                        e.printStackTrace();
                        throw new InvalidParameterException(String.format("Unable to run defaultTarget %s on %s.%s",
                                defaultTarget.getName(), cls.getName(), pointer.getName()));
                    }
                    consumed = 0;
                } else {
                    throw new InvalidParameterException("No target specified for self/this");
                }
            } else {
                message.instance = api.expectType(message, 0, cls);
                consumed = 1;
            }
            arguments = message.payload.subList(consumed, message.payload.size());
        } else {
            message.instance = null;
        }
        Object result;
        try {
            result = pointerInvoke(api, message, arguments);
        } catch (IllegalAccessException | IllegalArgumentException | InvocationTargetException e) {
            e.printStackTrace();
            throw new InvalidParameterException(
                    String.format("%s failed with %s", pointer.toGenericString(), e.getMessage()));
        }
        return result;
    };

}