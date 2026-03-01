import { useState } from 'react';
import {
  Card,
  CardContent,
  Typography,
  TextField,
  ToggleButton,
  ToggleButtonGroup,
  List,
  ListItem,
  ListItemText,
  Box,
  CircularProgress,
} from '@mui/material';
import { useSearchBlocks, useSearchEntities } from '../../api/queries';

export default function SearchPanel() {
  const [query, setQuery] = useState('');
  const [searchType, setSearchType] = useState('blocks');

  const blocksQuery = useSearchBlocks(searchType === 'blocks' ? query : '');
  const entitiesQuery = useSearchEntities(searchType === 'entities' ? query : '');

  const activeQuery = searchType === 'blocks' ? blocksQuery : entitiesQuery;
  const results = activeQuery.data?.results || [];

  return (
    <Card>
      <CardContent>
        <Typography variant="h5" gutterBottom>Search</Typography>
        <Box sx={{ display: 'flex', gap: 1, mb: 2, alignItems: 'center' }}>
          <ToggleButtonGroup
            value={searchType}
            exclusive
            onChange={(_, v) => v && setSearchType(v)}
            size="small"
          >
            <ToggleButton value="blocks">Blocks</ToggleButton>
            <ToggleButton value="entities">Entities</ToggleButton>
          </ToggleButtonGroup>
          <TextField
            size="small"
            label={`Search ${searchType}`}
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="e.g. stone, diamond, zombie..."
            sx={{ flexGrow: 1 }}
          />
        </Box>
        {activeQuery.isLoading && <CircularProgress size={24} />}
        {results.length > 0 ? (
          <List dense sx={{ maxHeight: 400, overflow: 'auto' }}>
            {results.map((item) => (
              <ListItem key={item}>
                <ListItemText primary={item} />
              </ListItem>
            ))}
          </List>
        ) : (
          query.length >= 2 &&
          !activeQuery.isLoading && (
            <Typography color="text.secondary">No results found</Typography>
          )
        )}
      </CardContent>
    </Card>
  );
}
