import { useState } from 'react';
import {
  Card,
  CardContent,
  Typography,
  TextField,
  Button,
  Box,
  Alert,
  Select,
  MenuItem,
  FormControl,
  InputLabel,
  Paper,
} from '@mui/material';
import PlayArrowIcon from '@mui/icons-material/PlayArrow';
import { useEvalCode } from '../../api/mutations';
import { useOnlinePlayers } from '../../api/queries';

export default function CodeEditor() {
  const [code, setCode] = useState('');
  const [playerUuid, setPlayerUuid] = useState('');
  const [history, setHistory] = useState([]);
  const [historyIndex, setHistoryIndex] = useState(-1);
  const evalMutation = useEvalCode();
  const { data: players } = useOnlinePlayers();

  const handleRun = () => {
    if (!code.trim()) return;
    const entry = { code: code.trim(), timestamp: Date.now() };
    evalMutation.mutate(
      { code: code.trim(), player_uuid: playerUuid || undefined },
      {
        onSuccess: (data) => {
          setHistory((prev) => [{ ...entry, result: data.result, output: data.output, error: data.error }, ...prev]);
        },
        onError: (err) => {
          setHistory((prev) => [{ ...entry, error: err.message }, ...prev]);
        },
      }
    );
    setCode('');
    setHistoryIndex(-1);
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter') {
      e.preventDefault();
      handleRun();
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      if (history.length > 0) {
        const newIdx = Math.min(historyIndex + 1, history.length - 1);
        setHistoryIndex(newIdx);
        setCode(history[newIdx].code);
      }
    } else if (e.key === 'ArrowDown') {
      e.preventDefault();
      if (historyIndex > 0) {
        const newIdx = historyIndex - 1;
        setHistoryIndex(newIdx);
        setCode(history[newIdx].code);
      } else if (historyIndex === 0) {
        setHistoryIndex(-1);
        setCode('');
      }
    }
  };

  return (
    <Card>
      <CardContent>
        <Typography variant="h5" gutterBottom>Code Editor</Typography>
        <Box sx={{ display: 'flex', gap: 1, mb: 2, alignItems: 'center' }}>
          <FormControl size="small" sx={{ minWidth: 200 }}>
            <InputLabel>Player Context</InputLabel>
            <Select
              value={playerUuid}
              label="Player Context"
              onChange={(e) => setPlayerUuid(e.target.value)}
            >
              <MenuItem value="">None (server only)</MenuItem>
              {players?.map((p) => (
                <MenuItem key={p.uuid} value={p.uuid}>
                  {p.display_name || p.name}
                </MenuItem>
              ))}
            </Select>
          </FormControl>
        </Box>
        <TextField
          fullWidth
          value={code}
          onChange={(e) => setCode(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Enter Python expression... Enter to run"
          variant="outlined"
          size="small"
          sx={{
            mb: 1,
            '& .MuiInputBase-input': { fontFamily: 'monospace', fontSize: 14 },
          }}
        />
        <Button
          variant="contained"
          startIcon={<PlayArrowIcon />}
          onClick={handleRun}
          disabled={evalMutation.isPending || !code.trim()}
          size="small"
        >
          Run
        </Button>

        {history.length > 0 && (
          <Box sx={{ mt: 2 }}>
            <Typography variant="h6" gutterBottom>Output</Typography>
            {history.map((entry, i) => (
              <Paper key={i} sx={{ p: 1.5, mb: 1, bgcolor: 'background.default' }}>
                <Typography variant="caption" color="text.secondary">
                  {new Date(entry.timestamp).toLocaleTimeString()}
                </Typography>
                <Typography
                  variant="body2"
                  sx={{ fontFamily: 'monospace', color: 'primary.main', mb: 0.5 }}
                >
                  &gt;&gt;&gt; {entry.code}
                </Typography>
                {entry.error ? (
                  <Alert severity="error" sx={{ py: 0 }}>{String(entry.error)}</Alert>
                ) : (
                  <>
                    {entry.output && (
                      <Typography variant="body2" sx={{ fontFamily: 'monospace', whiteSpace: 'pre-wrap', color: 'text.secondary' }}>
                        {entry.output}
                      </Typography>
                    )}
                    <Typography variant="body2" sx={{ fontFamily: 'monospace', whiteSpace: 'pre-wrap' }}>
                      {entry.result != null ? JSON.stringify(entry.result, null, 2) : 'None'}
                    </Typography>
                  </>
                )}
              </Paper>
            ))}
          </Box>
        )}
      </CardContent>
    </Card>
  );
}
