import { Box, Tooltip, Typography, IconButton } from '@mui/material';
import AutoFixHighIcon from '@mui/icons-material/AutoFixHigh';

function slotColor(material) {
  if (!material) return 'rgba(255,255,255,0.05)';
  if (material.includes('diamond')) return '#4fc3f7';
  if (material.includes('gold')) return '#ffd54f';
  if (material.includes('iron')) return '#bdbdbd';
  if (material.includes('netherite')) return '#424242';
  if (material.includes('wood') || material.includes('plank')) return '#8d6e63';
  if (material.includes('stone') || material.includes('cobble')) return '#9e9e9e';
  return 'rgba(255,255,255,0.15)';
}

function shortName(material) {
  if (!material) return '';
  return material.replace('minecraft:', '').replace(/_/g, ' ');
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

export default function InventoryView({ inventory, onEnchant }) {
  if (!inventory) return null;
  const contents = inventory.contents || [];

  return (
    <Box>
      <Typography variant="body2" color="text.secondary" sx={{ mb: 1 }}>
        {contents.filter((s) => s).length} / {inventory.size} slots used
      </Typography>
      <Box sx={{ display: 'grid', gridTemplateColumns: 'repeat(9, 48px)', gap: 0.5 }}>
        {contents.map((slot, i) => {
          const enchStr = slot ? formatEnchantments(slot.enchantments) : '';
          const tipText = slot
            ? `${shortName(slot.material)} x${slot.amount}${enchStr ? `\n${enchStr}` : ''}`
            : `Empty slot ${i}`;
          return (
            <Tooltip key={i} title={<span style={{ whiteSpace: 'pre-line' }}>{tipText}</span>}>
              <Box
                sx={{
                  width: 48,
                  height: 48,
                  bgcolor: slotColor(slot?.material),
                  border: enchStr ? '2px solid #ab47bc' : '1px solid rgba(255,255,255,0.2)',
                  borderRadius: 0.5,
                  display: 'flex',
                  flexDirection: 'column',
                  alignItems: 'center',
                  justifyContent: 'center',
                  fontSize: 10,
                  cursor: slot ? 'pointer' : 'default',
                  position: 'relative',
                  '&:hover .enchant-btn': { opacity: 1 },
                }}
              >
                {slot && (
                  <>
                    <Typography variant="caption" sx={{ fontSize: 8, textAlign: 'center', lineHeight: 1.1 }}>
                      {shortName(slot.material)?.slice(0, 8)}
                    </Typography>
                    {slot.amount > 1 && (
                      <Typography
                        variant="caption"
                        sx={{ position: 'absolute', bottom: 0, right: 2, fontSize: 9, fontWeight: 'bold' }}
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
                        onClick={(e) => { e.stopPropagation(); onEnchant(i); }}
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
              </Box>
            </Tooltip>
          );
        })}
      </Box>
    </Box>
  );
}
