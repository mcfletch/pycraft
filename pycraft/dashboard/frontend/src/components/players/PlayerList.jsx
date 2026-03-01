import {
  Card,
  CardContent,
  Typography,
  CircularProgress,
  Alert,
  List,
  ListItem,
  ListItemText,
  ListItemAvatar,
  Avatar,
  Chip,
  Box,
} from '@mui/material';
import PersonIcon from '@mui/icons-material/Person';
import { usePlayers } from '../../api/queries';

function formatLocation(loc) {
  if (!loc) return 'Unknown';
  return `${loc.world} (${Math.round(loc.x)}, ${Math.round(loc.y)}, ${Math.round(loc.z)})`;
}

export default function PlayerList() {
  const { data: players, isLoading, error } = usePlayers();

  if (isLoading) return <CircularProgress />;
  if (error)
    return <Alert severity="error">Failed to load players: {error.message}</Alert>;

  return (
    <Card>
      <CardContent>
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 1 }}>
          <Typography variant="h5">Players</Typography>
          <Chip label={players?.length || 0} size="small" color="primary" />
        </Box>
        {players?.length === 0 ? (
          <Typography color="text.secondary">No players online</Typography>
        ) : (
          <List>
            {players?.map((player) => (
              <ListItem key={player.uuid}>
                <ListItemAvatar>
                  <Avatar>
                    <PersonIcon />
                  </Avatar>
                </ListItemAvatar>
                <ListItemText
                  primary={player.display_name || player.name}
                  secondary={formatLocation(player.location)}
                />
              </ListItem>
            ))}
          </List>
        )}
      </CardContent>
    </Card>
  );
}
