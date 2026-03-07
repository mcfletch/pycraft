import {
  Card,
  CardContent,
  Typography,
  CircularProgress,
  Alert,
  List,
  ListItem,
  ListItemButton,
  ListItemText,
  ListItemAvatar,
  Avatar,
  Chip,
  Box,
  Divider,
} from '@mui/material';
import PersonIcon from '@mui/icons-material/Person';
import PersonOffIcon from '@mui/icons-material/PersonOff';
import { usePlayers } from '../../api/queries';

function formatLocation(loc) {
  if (!loc) return 'Unknown';
  return `${loc.world} (${loc.x.toFixed(1)}, ${loc.y.toFixed(1)}, ${loc.z.toFixed(1)})`;
}

function PlayerEntry({ player, onSelect, offline }) {
  return (
    <ListItem disablePadding>
      <ListItemButton onClick={() => onSelect?.(player.uuid)} sx={offline ? { opacity: 0.6 } : undefined}>
        <ListItemAvatar>
          <Avatar sx={offline ? { bgcolor: 'grey.700' } : undefined}>
            {offline ? <PersonOffIcon /> : <PersonIcon />}
          </Avatar>
        </ListItemAvatar>
        <ListItemText
          primary={player.display_name || player.name}
          secondary={offline ? 'Offline' : formatLocation(player.location)}
        />
      </ListItemButton>
    </ListItem>
  );
}

export default function PlayerList({ onSelect }) {
  const { data, isLoading, error } = usePlayers();

  if (isLoading) return <CircularProgress />;
  if (error)
    return <Alert severity="error">Failed to load players: {error.message}</Alert>;

  // Support both new {online, offline} and legacy flat array
  const online = data?.online || (Array.isArray(data) ? data : []);
  const offline = data?.offline || [];

  return (
    <Card>
      <CardContent>
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 1 }}>
          <Typography variant="h5">Players</Typography>
          <Chip label={`${online.length} online`} size="small" color="success" />
          {offline.length > 0 && (
            <Chip label={`${offline.length} offline`} size="small" variant="outlined" />
          )}
        </Box>
        {online.length === 0 && offline.length === 0 ? (
          <Typography color="text.secondary">No players known</Typography>
        ) : (
          <>
            {online.length > 0 && (
              <List dense>
                {online.map((player) => (
                  <PlayerEntry key={player.uuid} player={player} onSelect={onSelect} />
                ))}
              </List>
            )}
            {online.length > 0 && offline.length > 0 && <Divider sx={{ my: 1 }} />}
            {offline.length > 0 && (
              <>
                <Typography variant="caption" color="text.secondary" sx={{ ml: 1 }}>
                  Previously seen
                </Typography>
                <List dense>
                  {offline.map((player) => (
                    <PlayerEntry key={player.uuid} player={player} onSelect={onSelect} offline />
                  ))}
                </List>
              </>
            )}
          </>
        )}
      </CardContent>
    </Card>
  );
}
