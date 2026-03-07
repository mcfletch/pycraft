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
  Tooltip,
  IconButton,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
} from '@mui/material';
import PlayArrowIcon from '@mui/icons-material/PlayArrow';
import ContentCopyIcon from '@mui/icons-material/ContentCopy';
import { useEvalCode } from '../../api/mutations';
import { useOnlinePlayers } from '../../api/queries';

/** Parse a serialized Location into {world, x, y, z}.
 *  Handles three formats the server may send:
 *   - array  [world, x, y, z, yaw, pitch]
 *   - object {world, vector: [x, y, z, yaw, pitch]}
 *   - object {world, x, y, z}
 */
export function parseLocation(loc) {
  if (!loc) return null;
  if (Array.isArray(loc)) return { world: loc[0], x: loc[1], y: loc[2], z: loc[3] };
  if (loc.vector) return { world: loc.world, x: loc.vector[0], y: loc.vector[1], z: loc.vector[2] };
  return { world: loc.world, x: loc.x, y: loc.y, z: loc.z };
}

export function TracebackDialog({ open, onClose, error, traceback, code, context }) {
  const [copied, setCopied] = useState(false);

  const fullText = [
    code ? `>>> ${code}` : null,
    context ? `# ${context}` : null,
    '',
    traceback || String(error),
  ].filter(s => s !== null).join('\n');

  const handleCopy = () => {
    navigator.clipboard.writeText(fullText);
    setCopied(true);
    setTimeout(() => setCopied(false), 1500);
  };

  return (
    <Dialog open={open} onClose={onClose} maxWidth="md" fullWidth>
      <DialogTitle sx={{ color: 'error.main', fontFamily: 'monospace', fontSize: 14 }}>
        {String(error)}
      </DialogTitle>
      <DialogContent dividers sx={{ p: 0 }}>
        <Box
          component="pre"
          sx={{
            m: 0,
            p: 2,
            bgcolor: '#0d0d0d',
            color: '#ff8a80',
            fontFamily: 'monospace',
            fontSize: 12,
            whiteSpace: 'pre-wrap',
            wordBreak: 'break-all',
            maxHeight: 480,
            overflowY: 'auto',
          }}
        >
          {code && <Box component="span" sx={{ color: '#90caf9' }}>{`>>> ${code}\n`}</Box>}
          {context && <Box component="span" sx={{ color: '#aaa' }}>{`# ${context}\n`}</Box>}
          {(code || context) && '\n'}
          {traceback || String(error)}
        </Box>
      </DialogContent>
      <DialogActions>
        <Tooltip title={copied ? 'Copied!' : 'Copy to clipboard'}>
          <Button onClick={handleCopy} startIcon={<ContentCopyIcon />} size="small">
            {copied ? 'Copied!' : 'Copy'}
          </Button>
        </Tooltip>
        <Button onClick={onClose} size="small">Close</Button>
      </DialogActions>
    </Dialog>
  );
}

function ErrorEntry({ error, traceback, code, context }) {
  const [open, setOpen] = useState(false);
  return (
    <>
      <Alert
        severity="error"
        sx={{ py: 0, cursor: traceback ? 'pointer' : 'default' }}
        onClick={() => traceback && setOpen(true)}
      >
        {String(error)}
        {traceback && <Box component="span" sx={{ ml: 1, fontSize: 11, opacity: 0.7 }}>(click for traceback)</Box>}
      </Alert>
      <TracebackDialog open={open} onClose={() => setOpen(false)} error={error} traceback={traceback} code={code} context={context} />
    </>
  );
}

export default function CodeEditor() {
  const [code, setCode] = useState('');
  const [playerUuid, setPlayerUuid] = useState('');
  const [history, setHistory] = useState([]);
  const [historyIndex, setHistoryIndex] = useState(-1);
  const evalMutation = useEvalCode();
  const { data: players } = useOnlinePlayers();

  const handleRun = () => {
    if (!code.trim()) return;
    const player = players?.find((p) => p.uuid === playerUuid);
    let context = 'Server context (no player)';
    if (player) {
      const parsed = parseLocation(player.location);
      const pos = parsed ? ` at (${parsed.x.toFixed(1)}, ${parsed.y.toFixed(1)}, ${parsed.z.toFixed(1)}) in ${parsed.world}` : '';
      context = `Player: ${player.display_name || player.name}${pos}`;
    }
    const entry = { code: code.trim(), timestamp: Date.now(), context };
    evalMutation.mutate(
      { code: code.trim(), player_uuid: playerUuid || undefined },
      {
        onSuccess: (data) => {
          setHistory((prev) => [{ ...entry, result: data.result, output: data.output, error: data.error, traceback: data.traceback }, ...prev]);
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
              <Paper key={i} sx={{ p: 1.5, mb: 1, bgcolor: 'background.default', overflow: 'hidden' }}>
                <Typography variant="caption" color="text.secondary">
                  {new Date(entry.timestamp).toLocaleTimeString()}
                </Typography>
                <Typography
                  variant="body2"
                  sx={{ fontFamily: 'monospace', color: 'primary.main', mb: 0.5, wordBreak: 'break-all' }}
                >
                  &gt;&gt;&gt; {entry.code}
                </Typography>
                {entry.error ? (
                  <ErrorEntry error={entry.error} traceback={entry.traceback} code={entry.code} context={entry.context} />
                ) : (
                  <>
                    {entry.output && (
                      <Typography variant="body2" sx={{ fontFamily: 'monospace', whiteSpace: 'pre-wrap', wordBreak: 'break-all', color: 'text.secondary' }}>
                        {entry.output}
                      </Typography>
                    )}
                    <Typography variant="body2" sx={{ fontFamily: 'monospace', whiteSpace: 'pre-wrap', wordBreak: 'break-all' }}>
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
