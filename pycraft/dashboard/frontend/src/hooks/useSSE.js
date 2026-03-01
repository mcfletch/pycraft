import { useEffect, useRef, useState, useCallback } from 'react';
import { useQueryClient } from '@tanstack/react-query';
import { createSSEConnection } from '../api/sse';

const MAX_LOG_ENTRIES = 200;

export function useSSE() {
  const queryClient = useQueryClient();
  const connectionRef = useRef(null);
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
        addLogEntry(type, data);

        // Update TanStack Query cache based on event type
        if (type === 'player_join' || type === 'player_quit') {
          queryClient.invalidateQueries({ queryKey: ['players'] });
        } else if (type === 'player_move' && data.uuid) {
          queryClient.setQueryData(['players'], (old) => {
            if (!Array.isArray(old)) return old;
            return old.map((p) =>
              p.uuid === data.uuid ? { ...p, location: data.location } : p
            );
          });
        }
      },
      () => setConnected(false)
    );
    connectionRef.current = connection;

    return () => connection.close();
  }, [queryClient, addLogEntry]);

  return { connected, eventLog };
}
