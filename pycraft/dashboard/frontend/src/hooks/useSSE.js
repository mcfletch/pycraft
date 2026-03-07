import { useEffect, useRef, useState, useCallback } from 'react';
import { useQueryClient } from '@tanstack/react-query';
import { createSSEConnection } from '../api/sse';

const MAX_LOG_ENTRIES = 200;

export function useSSE() {
  const queryClient = useQueryClient();
  const connectionRef = useRef(null);
  const connectedOnceRef = useRef(false);
  const [connected, setConnected] = useState(false);
  const [eventLog, setEventLog] = useState([]);

  const addLogEntry = useCallback((type, data) => {
    setEventLog((prev) => {
      const entry = { type, data, timestamp: Date.now() };
      const next = [entry, ...prev];
      if (next.length > MAX_LOG_ENTRIES) next.length = MAX_LOG_ENTRIES;
      return next;
    });
  }, []);

  useEffect(() => {
    const connection = createSSEConnection(
      '/api/events',
      (type, data) => {
        setConnected(true);
        if (type === 'heartbeat') return;
        addLogEntry(type, data);

        if (type === 'player_join' && data.player?.uuid) {
          const player = { ...data.player, online: true };
          queryClient.setQueryData(['players'], (old) => {
            if (!old) return old;
            const online = old.online || (Array.isArray(old) ? old : []);
            const offline = Array.isArray(old) ? [] : (old.offline || []);
            const newOnline = online.some((p) => p.uuid === player.uuid)
              ? online.map((p) => (p.uuid === player.uuid ? { ...p, ...player } : p))
              : [...online, player];
            const newOffline = offline.filter((p) => p.uuid !== player.uuid);
            if (Array.isArray(old)) return newOnline;
            return { ...old, online: newOnline, offline: newOffline };
          });
        } else if (type === 'player_quit' && data.player?.uuid) {
          const uuid = data.player.uuid;
          queryClient.setQueryData(['players'], (old) => {
            if (!old) return old;
            const online = old.online || (Array.isArray(old) ? old : []);
            const offline = Array.isArray(old) ? [] : (old.offline || []);
            const quitter = online.find((p) => p.uuid === uuid) || data.player;
            const newOnline = online.filter((p) => p.uuid !== uuid);
            const newOffline = offline.some((p) => p.uuid === uuid)
              ? offline
              : [{ ...quitter, online: false }, ...offline];
            if (Array.isArray(old)) return newOnline;
            return { ...old, online: newOnline, offline: newOffline };
          });
        } else if (type === 'player_move' && data.uuid) {
          queryClient.setQueryData(['players'], (old) => {
            if (!old) return old;
            if (old.online) {
              return {
                ...old,
                online: old.online.map((p) =>
                  p.uuid === data.uuid ? { ...p, location: data.location } : p
                ),
              };
            }
            if (Array.isArray(old)) {
              return old.map((p) =>
                p.uuid === data.uuid ? { ...p, location: data.location } : p
              );
            }
            return old;
          });
        }
      },
      () => setConnected(false),
      () => {
        // On (re)connect: resync player list to catch any events missed during disconnect
        if (connectedOnceRef.current) {
          queryClient.invalidateQueries({ queryKey: ['players'] });
        }
        connectedOnceRef.current = true;
        setConnected(true);
      }
    );
    connectionRef.current = connection;

    return () => connection.close();
  }, [queryClient, addLogEntry]);

  return { connected, eventLog };
}
