package com.vrplumber.pycraft.bukkitserver;

import com.vrplumber.pycraft.bukkitserver.NamespaceHandler;
import com.vrplumber.pycraft.bukkitserver.MessageHandler;
import com.vrplumber.pycraft.bukkitserver.PycraftAPI;
import com.vrplumber.pycraft.bukkitserver.PycraftMessage;
import java.util.List;
import java.util.Arrays;
import java.util.ArrayList;
import org.bukkit.World;

public class WorldHandler extends NamespaceHandler {
    /* Interface for things which need to handle messages */
    public String getMethod() {
        return "World";
    }

    public void handle(PycraftAPI api, PycraftMessage message) {
        String name = message.nextName();
        Object result = null;
        if (name.equals("getWorlds")) {
            List<String> names = new ArrayList<String>();
            for (World world : api.getPlugin().getServer().getWorlds()) {
                names.add(world.getName());
            }
            ;
            result = (Object) names;
        }
        if (result != null) {
            api.sendResponse(message.messageId, result);
        } else {
            List<String> response = Arrays.asList("unknown-method", name);
            api.sendError(message.messageId, 1, response);
        }
    };
}