/**
 * SSE connection manager with automatic reconnection.
 * Returns an EventSource wrapper that dispatches typed events.
 */
export function createSSEConnection(url = '/api/events', onEvent, onError) {
  let source = null;
  let reconnectTimer = null;

  function connect() {
    source = new EventSource(url);

    source.addEventListener('player_join', (e) => {
      onEvent('player_join', JSON.parse(e.data));
    });
    source.addEventListener('player_quit', (e) => {
      onEvent('player_quit', JSON.parse(e.data));
    });
    source.addEventListener('player_move', (e) => {
      onEvent('player_move', JSON.parse(e.data));
    });
    source.addEventListener('chat', (e) => {
      onEvent('chat', JSON.parse(e.data));
    });
    source.addEventListener('block_break', (e) => {
      onEvent('block_break', JSON.parse(e.data));
    });
    source.addEventListener('block_place', (e) => {
      onEvent('block_place', JSON.parse(e.data));
    });
    source.addEventListener('player_death', (e) => {
      onEvent('player_death', JSON.parse(e.data));
    });
    source.addEventListener('entity_death', (e) => {
      onEvent('entity_death', JSON.parse(e.data));
    });
    source.addEventListener('heartbeat', () => {
      // Connection alive — no action needed
    });

    source.onerror = () => {
      if (onError) onError();
      source.close();
      // Reconnect after 3 seconds
      reconnectTimer = setTimeout(connect, 3000);
    };
  }

  connect();

  return {
    close() {
      if (reconnectTimer) clearTimeout(reconnectTimer);
      if (source) source.close();
    },
  };
}
