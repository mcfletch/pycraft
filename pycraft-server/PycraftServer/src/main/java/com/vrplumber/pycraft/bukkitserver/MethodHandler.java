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

class MethodHandler implements MessageHandler {
    /* Handle a method by dispatching to a method on a class instance */
    public Class cls = null;
    public Boolean staticMethod = false;
    public Boolean injectedMethod = false;
    public Object injectionTarget = (Object) null;
    public Method pointer = null;
    public Integer parameterCount = 0;

    public void register(HandlerRegistry registry) {
        /* Called when we are registered with the registry (api likely not up yet) */
    }

    public static List<MethodHandler> forClass(Class cls) {
        return forClass(cls, null);
    }

    public Map<String, Object> getDescription() {
        Map<String, Object> result = new HashMap<String, Object>();
        result.put("type", "method");
        result.put("static", (staticMethod && !injectedMethod));
        result.put("injected", injectedMethod);
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
            String methodName = method.getName();
            if (methodName.equals("spigot") || methodName.equals("clone") || methodName.equals("wait")) {
                continue;
            } else if (methodName.equals("getAsString")) {
                /* Just use the simple form for this common operation */
                if (method.getParameterCount() != 0) {
                    continue;
                }
            }
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

    public static void forHandler(Class cls, NamespaceHandler handler) {
        /*
         * Create MethodHandler instances for methods on cls
         * 
         */
        Method[] methods = handler.getClass().getMethods();
        for (Method method : methods) {
            int modifiers = method.getModifiers();
            boolean isHelper = false;
            boolean isInjected = false;
            String name = method.getName();
            for (Annotation annotation : method.getDeclaredAnnotations()) {
                if (annotation instanceof HelperMethod) {
                    isHelper = true;
                } else if (annotation instanceof InjectedMethod) {
                    isInjected = true;
                }
            }
            if (!isHelper) {
                continue;
            }
            MethodHandler mHandler = new MethodHandler(cls, method, Modifier.isStatic(modifiers));
            if (isInjected) {
                mHandler.injectedMethod = true;
                mHandler.injectionTarget = handler;
            }
            handler.addHandler(method.getName(), mHandler);
        }
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
        this.parameterCount = pointer.getParameterCount() + getSelfConsumption();
    }

    public List<Object> coerceParameters(PycraftAPI api, PycraftMessage message, List<Object> arguments) {
        /* Attempt to coerce parameters to the required types */
        List<Class> parameterTypes = Arrays.asList(this.pointer.getParameterTypes());
        List<Object> parameters = new ArrayList<Object>();
        if (parameterTypes.size() != arguments.size()) {
            throw new RuntimeException(
                    String.format("Wrong parameter count, expect %d got %d", parameterTypes.size(), arguments.size()));
        }
        for (int index = 0; index < arguments.size(); index++) {
            parameters.add(api.converterRegistry.toJava(parameterTypes.get(index), api, arguments.get(index)));
        }
        return parameters;
    }

    private Object pointerInvoke(PycraftAPI api, PycraftMessage message, List<Object> parameters)
            throws IllegalAccessException, IllegalArgumentException, InvocationTargetException {
        /*
         * Invoke our pointer doing (manual) unpacking of arguments
         * 
         * for i in range(0,10):
         * 
         * 
         */

        if (parameters.size() == 0) {
            return (Object) this.pointer.invoke(message.instance);
        } else if (parameters.size() == 1) {
            return (Object) this.pointer.invoke(message.instance, parameters.get(0));
        } else if (parameters.size() == 2) {
            return (Object) this.pointer.invoke(message.instance, parameters.get(0), parameters.get(1));
        } else if (parameters.size() == 3) {
            return (Object) this.pointer.invoke(message.instance, parameters.get(0), parameters.get(1),
                    parameters.get(2));
        } else if (parameters.size() == 4) {
            return (Object) this.pointer.invoke(message.instance, parameters.get(0), parameters.get(1),
                    parameters.get(2), parameters.get(3));
        } else if (parameters.size() == 5) {
            return (Object) this.pointer.invoke(message.instance, parameters.get(0), parameters.get(1),
                    parameters.get(2), parameters.get(3), parameters.get(4));
        } else if (parameters.size() == 6) {
            return (Object) this.pointer.invoke(message.instance, parameters.get(0), parameters.get(1),
                    parameters.get(2), parameters.get(3), parameters.get(4), parameters.get(5));
        } else if (parameters.size() == 7) {
            return (Object) this.pointer.invoke(message.instance, parameters.get(0), parameters.get(1),
                    parameters.get(2), parameters.get(3), parameters.get(4), parameters.get(5), parameters.get(6));
        } else if (parameters.size() == 8) {
            return (Object) this.pointer.invoke(message.instance, parameters.get(0), parameters.get(1),
                    parameters.get(2), parameters.get(3), parameters.get(4), parameters.get(5), parameters.get(6),
                    parameters.get(7));
        } else if (parameters.size() == 9) {
            return (Object) this.pointer.invoke(message.instance, parameters.get(0), parameters.get(1),
                    parameters.get(2), parameters.get(3), parameters.get(4), parameters.get(5), parameters.get(6),
                    parameters.get(7), parameters.get(8));
        } else {
            throw new InvalidParameterException("Only currently support up to 6 parameters");
        }
    }

    public int getSelfConsumption() {
        /* Calculate the parameter count for the method */
        int consumed;
        if (injectedMethod) {
            consumed = 0;
        } else {
            if (staticMethod) {
                consumed = 0;
            } else {
                consumed = 1;
            }
        }
        return consumed;
    }

    public Object handle(PycraftAPI api, PycraftMessage message) {
        List<Object> arguments = message.payload;
        int consumed = 0;
        if (injectedMethod) {
            message.instance = injectionTarget;
        } else {
            if (!staticMethod) {
                message.instance = api.expectType(message, 0, cls);
                consumed = 1;
            } else {
                message.instance = null;
            }
        }
        arguments = message.payload.subList(consumed, message.payload.size());
        List<Object> parameters = coerceParameters(api, message, arguments);
        Object result;
        try {
            api.getLogger().info(String.format("%s result call", pointer.getName()));
            result = pointerInvoke(api, message, parameters);
            api.getLogger().info(
                    String.format("%s result %s", pointer.getName(), result == null ? "null" : result.toString()));
            if (pointer.getReturnType() == Void.TYPE) {
                result = Boolean.TRUE;
            } else if (pointer == null) {
                result = Boolean.TRUE;
            }
        } catch (IllegalAccessException | IllegalArgumentException | InvocationTargetException e) {
            e.printStackTrace();
            throw new RuntimeException(String.format("%s failed with %s", pointer.toGenericString(), e.getMessage()));
        }
        return result;
    };

}