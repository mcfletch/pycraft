import { useState } from 'react';
import {
  Card,
  CardContent,
  Typography,
  CircularProgress,
  Alert,
  List,
  ListItem,
  ListItemText,
  Select,
  MenuItem,
  FormControl,
  InputLabel,
  Box,
  TextField,
  Button,
  Chip,
  Stack,
} from '@mui/material';
import { useWorldEntities } from '../../api/queries';
import { useSpawnEntity } from '../../api/mutations';

export default function EntityPanel({ worlds }) {
  const [worldName, setWorldName] = useState('');
  const [spawnForm, setSpawnForm] = useState({ type: '', x: '', y: '', z: '' });
  const { data: entities, isLoading, error } = useWorldEntities(worldName);
  const spawnMutation = useSpawnEntity();

  const worldList = worlds || [];

  // Auto-select first world
  if (!worldName && worldList.length > 0) {
    setWorldName(worldList[0].name);
  }

  const handleSpawn = (e) => {
    e.preventDefault();
    spawnMutation.mutate({
      worldName,
      type: spawnForm.type,
      x: parseFloat(spawnForm.x),
      y: parseFloat(spawnForm.y),
      z: parseFloat(spawnForm.z),
    });
  };

  return (
    <Stack spacing={2}>
      <Card>
        <CardContent>
          <Typography variant="h5" gutterBottom>Entities</Typography>
          <FormControl size="small" sx={{ minWidth: 150, mb: 2 }}>
            <InputLabel>World</InputLabel>
            <Select value={worldName} label="World" onChange={(e) => setWorldName(e.target.value)}>
              {worldList.map((w) => (
                <MenuItem key={w.name} value={w.name}>{w.name}</MenuItem>
              ))}
            </Select>
          </FormControl>

          {isLoading && <CircularProgress />}
          {error && <Alert severity="error">{error.message}</Alert>}
          {entities && (
            <>
              <Box sx={{ mb: 1 }}>
                <Chip label={`${entities.length} entities`} size="small" color="primary" />
              </Box>
              <List dense sx={{ maxHeight: 300, overflow: 'auto' }}>
                {entities.map((entity, i) => (
                  <ListItem key={entity.uuid || i}>
                    <ListItemText
                      primary={entity.display_name || entity.name || entity.type}
                      secondary={
                        entity.location
                          ? `(${entity.location.x.toFixed(1)}, ${entity.location.y.toFixed(1)}, ${entity.location.z.toFixed(1)})`
                          : ''
                      }
                    />
                    <Chip label={entity.type} size="small" variant="outlined" />
                  </ListItem>
                ))}
              </List>
            </>
          )}
        </CardContent>
      </Card>

      <Card>
        <CardContent>
          <Typography variant="h6" gutterBottom>Spawn Entity</Typography>
          <Box component="form" onSubmit={handleSpawn} sx={{ display: 'flex', gap: 1, flexWrap: 'wrap', alignItems: 'center' }}>
            <TextField
              size="small" label="Type" value={spawnForm.type}
              onChange={(e) => setSpawnForm({ ...spawnForm, type: e.target.value })}
              placeholder="minecraft:zombie"
            />
            <TextField
              size="small" label="X" type="number" value={spawnForm.x}
              onChange={(e) => setSpawnForm({ ...spawnForm, x: e.target.value })}
              sx={{ width: 80 }}
            />
            <TextField
              size="small" label="Y" type="number" value={spawnForm.y}
              onChange={(e) => setSpawnForm({ ...spawnForm, y: e.target.value })}
              sx={{ width: 80 }}
            />
            <TextField
              size="small" label="Z" type="number" value={spawnForm.z}
              onChange={(e) => setSpawnForm({ ...spawnForm, z: e.target.value })}
              sx={{ width: 80 }}
            />
            <Button type="submit" variant="contained" size="small" disabled={spawnMutation.isPending || !worldName}>
              Spawn
            </Button>
          </Box>
          {spawnMutation.isError && <Alert severity="error" sx={{ mt: 1 }}>{spawnMutation.error.message}</Alert>}
          {spawnMutation.isSuccess && <Alert severity="success" sx={{ mt: 1 }}>Entity spawned!</Alert>}
        </CardContent>
      </Card>
    </Stack>
  );
}
