import { useState } from 'react';
import { Box, Stack } from '@mui/material';
import AppShell from './components/layout/AppShell';
import ServerStatus from './components/server/ServerStatus';
import PlayerList from './components/players/PlayerList';
import EventLog from './components/server/EventLog';
import { useSSE } from './hooks/useSSE';

export default function App() {
  const [activeTab, setActiveTab] = useState('server');
  const { connected, eventLog } = useSSE();

  return (
    <AppShell activeTab={activeTab} onTabChange={setActiveTab} sseConnected={connected}>
      {activeTab === 'server' && (
        <Stack spacing={2}>
          <ServerStatus />
          <PlayerList />
        </Stack>
      )}
      {activeTab === 'players' && <PlayerList />}
      {activeTab === 'events' && <EventLog eventLog={eventLog} />}
    </AppShell>
  );
}
