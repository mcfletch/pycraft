/**
 * Shared slot box component for inventory grids.
 * Used by player inventory, chest/container inventories, etc.
 */
import { Box, Tooltip, Typography } from '@mui/material';
import AutoFixHighIcon from '@mui/icons-material/AutoFixHigh';

export function shortName(material) {
  if (!material) return '';
  return material.replace('minecraft:', '').replace(/_/g, ' ');
}

export function textureUrl(material) {
  if (!material) return null;
  const name = material.replace('minecraft:', '');
  return `/api/textures/items/${encodeURIComponent(name)}.png`;
}

export function formatEnchantments(enchantments) {
  if (!enchantments || typeof enchantments !== 'object') return '';
  const entries = Object.entries(enchantments);
  if (entries.length === 0) return '';
  return entries.map(([name, level]) => {
    const short = String(name).replace('minecraft:', '').replace(/_/g, ' ');
    return `${short} ${level}`;
  }).join(', ');
}

/**
 * SlotBox renders a single inventory slot.
 *
 * Props:
 *   slot       — item stack object (null/undefined = empty slot)
 *   index      — inventory slot index (used for drag/click events)
 *   label      — optional label shown in empty slots (e.g. "Helmet")
 *   onClick    — (index, anchorEl) => void — called when a non-empty slot is clicked
 *   onDragStart — (e, index) => void
 *   onDragOver  — (e, index) => void
 *   onDrop      — (e, index) => void
 *   isDragOver  — boolean — highlights slot as a drop target
 */
export function SlotBox({ slot, index, label, onClick, onDragStart, onDragOver, onDrop, isDragOver }) {
  const enchStr = slot ? formatEnchantments(slot.enchantments) : '';
  const tipText = slot
    ? `${label ? label + ': ' : ''}${shortName(slot.material)} x${slot.amount}${enchStr ? `\n${enchStr}` : ''}`
    : label || `Empty slot ${index}`;
  return (
    <Tooltip title={<span style={{ whiteSpace: 'pre-line' }}>{tipText}</span>}>
      <Box
        draggable={!!slot}
        onClick={slot && onClick ? (e) => onClick(index, e.currentTarget) : undefined}
        onDragStart={slot && onDragStart ? (e) => onDragStart(e, index) : undefined}
        onDragOver={onDragOver ? (e) => onDragOver(e, index) : undefined}
        onDrop={onDrop ? (e) => onDrop(e, index) : undefined}
        sx={{
          width: 48,
          height: 48,
          bgcolor: isDragOver ? 'rgba(100,180,255,0.25)' : 'rgba(139,139,139,0.35)',
          border: isDragOver
            ? '2px solid #64b4ff'
            : enchStr ? '2px solid #ab47bc' : '1px solid rgba(255,255,255,0.2)',
          borderRadius: 0.5,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          cursor: slot ? 'grab' : 'default',
          position: 'relative',
          transition: 'background-color 0.1s, border-color 0.1s',
        }}
      >
        {slot && (
          <>
            <Box
              component="img"
              src={textureUrl(slot.material)}
              alt={shortName(slot.material)}
              onError={(e) => { e.target.style.display = 'none'; }}
              sx={{ width: 32, height: 32, imageRendering: 'pixelated' }}
            />
            {slot.amount > 1 && (
              <Typography
                variant="caption"
                sx={{
                  position: 'absolute', bottom: 0, right: 2,
                  fontSize: 11, fontWeight: 'bold',
                  textShadow: '1px 1px 2px rgba(0,0,0,0.8)',
                }}
              >
                {slot.amount}
              </Typography>
            )}
            {enchStr && (
              <AutoFixHighIcon sx={{ position: 'absolute', top: 0, right: 0, fontSize: 10, color: '#ab47bc' }} />
            )}
          </>
        )}
        {!slot && label && (
          <Typography variant="caption" sx={{ fontSize: 7, color: 'text.disabled', textAlign: 'center' }}>
            {label}
          </Typography>
        )}
      </Box>
    </Tooltip>
  );
}
