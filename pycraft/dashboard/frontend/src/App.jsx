import { Routes, Route, useNavigate, useLocation, useParams, Navigate } from 'react-router-dom';
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

function ServerPage() {
  const navigate = useNavigate();
  return (
    <Stack spacing={2}>
      <ServerStatus />
      <PlayerList onSelect={(uuid) => navigate(`/players/${uuid}`)} />
    </Stack>
  );
}

function PlayersPage() {
  const navigate = useNavigate();
  return <PlayerList onSelect={(uuid) => navigate(`/players/${uuid}`)} />;
}

function PlayerDetailPage() {
  const { uuid } = useParams();
  return <PlayerDetail uuid={uuid} />;
}

function EventsPage({ eventLog }) {
  return <EventLog eventLog={eventLog} />;
}

function MapPage({ worlds }) {
  const location = useLocation();
  const params = new URLSearchParams(location.search);
  const followPlayer = params.get('follow') || null;
  return (
    <WorldMap
      worlds={worlds}
      initialFollowPlayer={followPlayer}
      onFollowConsumed={() => {}}
    />
  );
}

function EditorPage() {
  return <CodeEditor />;
}

function SearchPage() {
  return <SearchPanel />;
}

function EntitiesPage({ worlds }) {
  return <EntityPanel worlds={worlds} />;
}

export default function App() {
  const { connected, eventLog } = useSSE();
  const { data: serverInfo } = useServerInfo();
  const worlds = serverInfo?.worlds || [];

  return (
    <AppShell sseConnected={connected}>
      <Routes>
        <Route path="/" element={<MapPage worlds={worlds} />} />
        <Route path="/server" element={<ServerPage />} />
        <Route path="/players" element={<PlayersPage />} />
        <Route path="/players/:uuid" element={<PlayerDetailPage />} />
        <Route path="/events" element={<EventsPage eventLog={eventLog} />} />
        <Route path="/map" element={<MapPage worlds={worlds} />} />
        <Route path="/editor" element={<EditorPage />} />
        <Route path="/search" element={<SearchPage />} />
        <Route path="/entities" element={<EntitiesPage worlds={worlds} />} />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </AppShell>
  );
}
