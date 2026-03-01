import { useState } from 'react';
import { Stack } from '@mui/material';
import AppShell from './components/layout/AppShell';
import ServerStatus from './components/server/ServerStatus';
import PlayerList from './components/players/PlayerList';
import PlayerDetail from './components/players/PlayerDetail';
import EventLog from './components/server/EventLog';
import WorldMap from './components/map/WorldMap';
import CodeEditor from './components/editor/CodeEditor';
import SearchPanel from './components/server/SearchPanel';
import EntityPanel from './components/server/EntityPanel';
import { useSSE } from './hooks/useSSE';
import { useServerInfo } from './api/queries';

export default function App() {
  const [activeTab, setActiveTab] = useState('server');
  const [selectedPlayer, setSelectedPlayer] = useState(null);
  const [mapFollowPlayer, setMapFollowPlayer] = useState(null);
  const { connected, eventLog } = useSSE();
  const { data: serverInfo } = useServerInfo();

  const worlds = serverInfo?.worlds || [];

  const handleShowOnMap = (uuid) => {
    setMapFollowPlayer(uuid);
    setActiveTab('map');
  };

  return (
    <AppShell activeTab={activeTab} onTabChange={setActiveTab} sseConnected={connected}>
      {activeTab === 'server' && (
        <Stack spacing={2}>
          <ServerStatus />
          <PlayerList onSelect={(uuid) => { setSelectedPlayer(uuid); setActiveTab('players'); }} />
        </Stack>
      )}
      {activeTab === 'players' && (
        selectedPlayer ? (
          <PlayerDetail uuid={selectedPlayer} onBack={() => setSelectedPlayer(null)} onShowOnMap={handleShowOnMap} />
        ) : (
          <PlayerList onSelect={setSelectedPlayer} />
        )
      )}
      {activeTab === 'events' && <EventLog eventLog={eventLog} />}
      {activeTab === 'map' && (
        <WorldMap
          worlds={worlds}
          initialFollowPlayer={mapFollowPlayer}
          onFollowConsumed={() => setMapFollowPlayer(null)}
        />
      )}
      {activeTab === 'editor' && <CodeEditor />}
      {activeTab === 'search' && <SearchPanel />}
      {activeTab === 'entities' && <EntityPanel worlds={worlds} />}
    </AppShell>
  );
}
