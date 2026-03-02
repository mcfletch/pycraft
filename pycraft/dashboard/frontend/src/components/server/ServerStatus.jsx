import {
  Card,
  CardContent,
  Typography,
  CircularProgress,
  Alert,
  List,
  ListItem,
  ListItemText,
  Chip,
  Box,
  Table,
  TableBody,
  TableRow,
  TableCell,
} from '@mui/material';
import { useServerInfo } from '../../api/queries';

export default function ServerStatus() {
  const { data, isLoading, error } = useServerInfo();

  if (isLoading) return <CircularProgress />;
  if (error) return <Alert severity="error">Failed to load server info: {error.message}</Alert>;

  const plugin = data.plugin || {};

  return (
    <Card>
      <CardContent>
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 1 }}>
          <Typography variant="h5">Server Info</Typography>
          <Chip
            label={data.connected ? 'Connected' : 'Disconnected'}
            color={data.connected ? 'success' : 'error'}
            size="small"
            variant="outlined"
          />
        </Box>
        <Table size="small" sx={{ '& td': { border: 0, py: 0.3 }, '& td:first-of-type': { color: 'text.secondary', pr: 2, whiteSpace: 'nowrap' } }}>
          <TableBody>
            <TableRow>
              <TableCell>Minecraft</TableCell>
              <TableCell>{data.version || 'unknown'}</TableCell>
            </TableRow>
            <TableRow>
              <TableCell>PycraftServer</TableCell>
              <TableCell>{plugin.version || 'unknown'} (API {plugin.api || '?'})</TableCell>
            </TableRow>
            <TableRow>
              <TableCell>Python</TableCell>
              <TableCell>{data.python_version || 'unknown'}</TableCell>
            </TableRow>
            <TableRow>
              <TableCell>MC Server</TableCell>
              <TableCell>{data.mc_server || 'unknown'}</TableCell>
            </TableRow>
            <TableRow>
              <TableCell>Dashboard</TableCell>
              <TableCell>{data.dashboard_host || 'unknown'}</TableCell>
            </TableRow>
          </TableBody>
        </Table>
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
