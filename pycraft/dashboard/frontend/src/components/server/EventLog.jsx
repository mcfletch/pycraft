import {
  Card,
  CardContent,
  Typography,
  List,
  ListItem,
  ListItemText,
  Chip,
  Box,
} from '@mui/material';

const EVENT_COLORS = {
  player_join: 'success',
  player_quit: 'error',
  player_move: 'default',
  chat: 'info',
  block_break: 'warning',
  block_place: 'secondary',
  player_death: 'error',
  entity_death: 'warning',
};

function formatEventData(type, data) {
  if (!data) return '';
  switch (type) {
    case 'player_join':
      return `${data.player?.name || data.name || 'Unknown'} joined`;
    case 'player_quit':
      return `${data.player?.name || data.name || 'Unknown'} left`;
    case 'player_move': {
      const loc = data.location;
      return `${data.name || data.uuid?.slice(0, 8)} moved to (${Math.round(loc?.x || 0)}, ${Math.round(loc?.y || 0)}, ${Math.round(loc?.z || 0)})`;
    }
    case 'chat':
      return `<${data.player?.name || data.player || 'Unknown'}> ${data.message}`;
    case 'block_break':
      return `${data.player?.name || 'Unknown'} broke ${data.block?.data || 'block'}`;
    case 'block_place':
      return `${data.player?.name || 'Unknown'} placed ${data.block?.data || 'block'}`;
    case 'player_death':
      return `${data.player?.name || 'Unknown'} died`;
    case 'entity_death':
      return `${data.entity?.name || 'Entity'} died`;
    default:
      return JSON.stringify(data).slice(0, 100);
  }
}

function formatTime(ts) {
  return new Date(ts).toLocaleTimeString();
}

export default function EventLog({ eventLog }) {
  return (
    <Card>
      <CardContent>
        <Typography variant="h5" gutterBottom>
          Event Log
        </Typography>
        {eventLog.length === 0 ? (
          <Typography color="text.secondary">Waiting for events...</Typography>
        ) : (
          <List dense sx={{ maxHeight: 500, overflow: 'auto' }}>
            {eventLog.map((entry, i) => (
              <ListItem key={i} sx={{ py: 0.25 }}>
                <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, width: '100%' }}>
                  <Typography variant="caption" color="text.secondary" sx={{ minWidth: 70 }}>
                    {formatTime(entry.timestamp)}
                  </Typography>
                  <Chip
                    label={entry.type}
                    size="small"
                    color={EVENT_COLORS[entry.type] || 'default'}
                    sx={{ minWidth: 90 }}
                  />
                  <ListItemText
                    primary={formatEventData(entry.type, entry.data)}
                    primaryTypographyProps={{ variant: 'body2', noWrap: true }}
                  />
                </Box>
              </ListItem>
            ))}
          </List>
        )}
      </CardContent>
    </Card>
  );
}
