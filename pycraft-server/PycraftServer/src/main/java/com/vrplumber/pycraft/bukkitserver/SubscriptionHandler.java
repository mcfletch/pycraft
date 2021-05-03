package com.vrplumber.pycraft.bukkitserver;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.lang.Class;
import java.util.List;
import java.util.ArrayList;
import java.security.InvalidParameterException;
import com.vrplumber.pycraft.bukkitserver.MessageHandler;

class SubscriptionHandler implements MessageHandler {
    /* Handle a method by dispatching to a method on a class instance */
    public String getMethod() {
        return "subscribe";
    }

    public void register(HandlerRegistry registry) {
    }

    public Object handle(PycraftAPI api, PycraftMessage message) {
        String name = api.expectString(message, 0);
        Boolean enabled = api.expectBoolean(message, 1);
        if (enabled) {
            api.subscriptions.put(name, message);
            return Boolean.TRUE;
        } else {
            api.subscriptions.remove(name);
            return Boolean.FALSE;
        }
    }

}