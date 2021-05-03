package com.vrplumber.pycraft.bukkitserver;

import java.util.List;

import org.bukkit.event.EventHandler;
import org.bukkit.event.Listener;
import org.bukkit.event.EventPriority;
import org.bukkit.event.player.AsyncPlayerChatEvent;
import org.bukkit.event.player.PlayerInteractEvent;
import org.bukkit.event.player.PlayerInteractEntityEvent;
import org.bukkit.event.block.BlockBreakEvent;

public class PycraftListener implements Listener {
    PycraftServerPlugin plugin = null;

    PycraftListener(PycraftServerPlugin plugin) {
        this.plugin = plugin;
    }

    @EventHandler(priority = EventPriority.NORMAL)
    public void onPlayerChat(AsyncPlayerChatEvent event) {
        try {
            for (PycraftAPI client : this.plugin.getClients()) {
                client.onEvent(event);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    @EventHandler(priority = EventPriority.NORMAL)
    public void onPlayerInteract(PlayerInteractEvent event) {
        for (PycraftAPI client : this.plugin.getClients()) {
            client.onEvent(event);
        }
    }

    @EventHandler(priority = EventPriority.NORMAL)
    public void onPlayerInteractEntity(PlayerInteractEntityEvent event) {
        for (PycraftAPI client : this.plugin.getClients()) {
            client.onEvent(event);
        }
    }

    @EventHandler(priority = EventPriority.NORMAL)
    public void onBlockEvent(BlockBreakEvent event) {
        for (PycraftAPI client : this.plugin.getClients()) {
            client.onEvent(event);
        }
    }

}
