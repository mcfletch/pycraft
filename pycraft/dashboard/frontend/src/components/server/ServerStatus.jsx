import {
  Card,
  CardContent,
  Typography,
  CircularProgress,
  Alert,
  List,
  ListItem,
  ListItemText,
} from '@mui/material';
import { useServerInfo } from '../../api/queries';

export default function ServerStatus() {
  const { data, isLoading, error } = useServerInfo();

  if (isLoading) return <CircularProgress />;
  if (error) return <Alert severity="error">Failed to load server info: {error.message}</Alert>;

  return (
    <Card>
      <CardContent>
        <Typography variant="h5" gutterBottom>
          Server Info
        </Typography>
        <Typography variant="body1" color="text.secondary">
          Version: {data.version}
        </Typography>
        <Typography variant="h6" sx={{ mt: 2 }}>
          Worlds
        </Typography>
        <List dense>
          {data.worlds?.map((world) => (
            <ListItem key={world.name}>
              <ListItemText
                primary={world.name}
                secondary={`${world.player_count} player${world.player_count !== 1 ? 's' : ''}`}
              />
            </ListItem>
          ))}
        </List>
      </CardContent>
    </Card>
  );
}
