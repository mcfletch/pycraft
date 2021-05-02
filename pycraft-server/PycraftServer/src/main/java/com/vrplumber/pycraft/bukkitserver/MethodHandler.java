package com.vrplumber.pycraft.bukkitserver;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.lang.Class;
import java.util.List;
import java.util.ArrayList;
import java.security.InvalidParameterException;
import java.security.IllegalAccessExceptionJava;
import com.vrplumber.pycraft.bukkitserver.MessageHandler;

class MethodHandler implements MessageHandler {
    /* Handle a method by dispatching to a method on a class instance */
    public Class cls = null;
    public Method pointer = null;

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
            if (names == null || names.indexOf(method.getName()) > -1) {
                MethodHandler handler = new MethodHandler(cls, method);
                handlers.add(handler);
            }
        }
        return handlers;
    }

    public String getMethod() {
        return pointer.getName();
    }

    public MethodHandler(Class cls, Method pointer) {
        /*
         * Create a new MethodHandler that operates on cls instances of the given Method
         */
        this.cls = cls;
        this.pointer = pointer;
    }

    public List<Object> checkArguments(PycraftAPI api, PycraftMessage message) throws InvalidParameterException {
        /*
         * Can arguments in message be converted to our type signature?
         * 
         * Attempts the conversion, raise InvalidArgumentException if not returns the
         * converted records;
         */
        if (message.payload.size() != pointer.getParameterCount()) {
            throw new InvalidParameterException(String.format("%s takes %d arguments, got %d", getMethod(),
                    pointer.getParameterCount(), message.payload.size()));
        }
        List<Object> args = new ArrayList<Object>();
        return args;

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
        if (message.instance == null) {
            throw new InvalidParameterException(
                    String.format("%s.%s passed null instance", pointer.getName(), getMethod()));
        }

        if (!this.cls.isInstance(message.instance)) {
            throw new InvalidParameterException(String.format("%s.%s passed instance %s", pointer.getName(),
                    getMethod(), message.instance.toString()));
        }

        List<Object> arguments = this.checkArguments(api, message);
        Object result;
        try {
            result = pointerInvoke(api, message, arguments);
        } catch (IllegalAccessException | IllegalArgumentException | InvocationTargetException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
            throw new InvalidParameterException(
                    String.format("%s failed with %s", pointer.toGenericString(), e.getMessage()));
        }
        return result;
    };

}