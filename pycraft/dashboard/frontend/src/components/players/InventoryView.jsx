import { Box, Tooltip, Typography, IconButton } from '@mui/material';
import AutoFixHighIcon from '@mui/icons-material/AutoFixHigh';

function shortName(material) {
  if (!material) return '';
  return material.replace('minecraft:', '').replace(/_/g, ' ');
}

function textureUrl(material) {
  if (!material) return null;
  const name = material.replace('minecraft:', '');
  return `/api/textures/items/${encodeURIComponent(name)}.png`;
}

function formatEnchantments(enchantments) {
  if (!enchantments || typeof enchantments !== 'object') return '';
  const entries = Object.entries(enchantments);
  if (entries.length === 0) return '';
  return entries.map(([name, level]) => {
    const short = String(name).replace('minecraft:', '').replace(/_/g, ' ');
    return `${short} ${level}`;
  }).join(', ');
}

const ARMOR_LABELS = ['Boots', 'Leggings', 'Chestplate', 'Helmet'];

function SlotBox({ slot, index, label, onEnchant }) {
  const enchStr = slot ? formatEnchantments(slot.enchantments) : '';
  const tipText = slot
    ? `${label ? label + ': ' : ''}${shortName(slot.material)} x${slot.amount}${enchStr ? `\n${enchStr}` : ''}`
    : label || `Empty slot ${index}`;
  return (
    <Tooltip title={<span style={{ whiteSpace: 'pre-line' }}>{tipText}</span>}>
      <Box
        sx={{
          width: 48,
          height: 48,
          bgcolor: 'rgba(139,139,139,0.35)',
          border: enchStr ? '2px solid #ab47bc' : '1px solid rgba(255,255,255,0.2)',
          borderRadius: 0.5,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          cursor: slot ? 'pointer' : 'default',
          position: 'relative',
          '&:hover .enchant-btn': { opacity: 1 },
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
            {onEnchant && (
              <IconButton
                className="enchant-btn"
                size="small"
                onClick={(e) => { e.stopPropagation(); onEnchant(index); }}
                sx={{
                  position: 'absolute', top: -4, left: -4,
                  opacity: 0, transition: 'opacity 0.15s',
                  bgcolor: 'rgba(0,0,0,0.7)', color: '#ab47bc',
                  width: 18, height: 18,
                  '&:hover': { bgcolor: 'rgba(0,0,0,0.9)' },
                }}
              >
                <AutoFixHighIcon sx={{ fontSize: 12 }} />
              </IconButton>
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

export default function InventoryView({ inventory, onEnchant }) {
  if (!inventory) return null;
  const contents = inventory.contents || [];

  // Bukkit PlayerInventory layout:
  // 0-8: hotbar, 9-35: main inventory, 36-39: armor (boots,legs,chest,helm), 40: offhand
  const mainSlots = contents.slice(9, 36);   // 27 main slots (3 rows of 9)
  const hotbar = contents.slice(0, 9);        // 9 hotbar slots
  const armor = contents.slice(36, 40);       // 4 armor slots
  const offhand = contents[40] || null;        // offhand slot

  const usedCount = contents.filter((s) => s).length;

  return (
    <Box>
      <Typography variant="body2" color="text.secondary" sx={{ mb: 1 }}>
        {usedCount} / {inventory.size} slots used
      </Typography>

      {/* Equipment: armor + offhand */}
      <Box sx={{ display: 'flex', gap: 2, mb: 1.5, alignItems: 'center' }}>
        <Box>
          <Typography variant="caption" color="text.secondary" sx={{ fontSize: 10 }}>Equipment</Typography>
          <Box sx={{ display: 'flex', gap: 0.5 }}>
            {[3, 2, 1, 0].map((ai) => (
              <SlotBox key={36 + ai} slot={armor[ai]} index={36 + ai} label={ARMOR_LABELS[ai]} onEnchant={onEnchant} />
            ))}
            <Box sx={{ mx: 0.5, borderLeft: '1px solid rgba(255,255,255,0.15)', height: 48 }} />
            <SlotBox slot={offhand} index={40} label="Offhand" onEnchant={onEnchant} />
          </Box>
        </Box>
      </Box>

      {/* Main inventory (3 rows of 9) */}
      <Box sx={{ display: 'grid', gridTemplateColumns: 'repeat(9, 48px)', gap: 0.5, mb: 1 }}>
        {mainSlots.map((slot, i) => (
          <SlotBox key={9 + i} slot={slot} index={9 + i} onEnchant={onEnchant} />
        ))}
      </Box>

      {/* Hotbar */}
      <Box>
        <Typography variant="caption" color="text.secondary" sx={{ fontSize: 10 }}>Hotbar</Typography>
        <Box sx={{ display: 'grid', gridTemplateColumns: 'repeat(9, 48px)', gap: 0.5, borderTop: '2px solid rgba(255,255,255,0.2)', pt: 0.5 }}>
          {hotbar.map((slot, i) => (
            <SlotBox key={i} slot={slot} index={i} onEnchant={onEnchant} />
          ))}
        </Box>
      </Box>
    </Box>
  );
}
