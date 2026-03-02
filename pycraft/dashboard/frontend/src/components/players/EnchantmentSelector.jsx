import {
  Box,
  Typography,
  FormControlLabel,
  Checkbox,
  Slider,
  Stack,
  FormControl,
  InputLabel,
  Select,
  MenuItem,
  TextField,
  IconButton,
} from '@mui/material';
import AddCircleOutlineIcon from '@mui/icons-material/AddCircleOutline';
import RemoveCircleOutlineIcon from '@mui/icons-material/RemoveCircleOutline';

export function shortEnchName(key) {
  return key.replace('minecraft:', '').replace(/_/g, ' ');
}

export function shortPotionName(key) {
  return key.replace('minecraft:', '').replace(/_/g, ' ');
}

export function isPotion(material, potionMaterials) {
  if (!material) return false;
  const m = material.toLowerCase();
  if (potionMaterials?.length) {
    return potionMaterials.some((pm) => m === pm || m === pm.replace('minecraft:', ''));
  }
  return m.includes('potion') || m === 'minecraft:tipped_arrow' || m === 'tipped_arrow';
}

/**
 * Enchantment selector panel with checkboxes and level sliders.
 *
 * Props:
 *   allEnchantments: [{key, max_level, desirable}, ...]
 *   selections: {key: level, ...}
 *   onToggle: (key, maxLevel) => void
 *   onSetLevel: (key, level) => void
 */
export function EnchantmentSelector({ allEnchantments, selections, onToggle, onSetLevel }) {
  return (
    <Box sx={{ p: 1.5, bgcolor: 'rgba(171,71,188,0.08)', borderRadius: 1, border: '1px solid rgba(171,71,188,0.2)' }}>
      <Typography variant="caption" sx={{ mb: 1, display: 'block', fontWeight: 'bold' }}>
        Enchantments ({Object.keys(selections).length} selected)
      </Typography>
      <Box sx={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(260px, 1fr))', gap: 0.5 }}>
        {allEnchantments.map((ench) => {
          const checked = ench.key in selections;
          const level = selections[ench.key] || ench.max_level;
          return (
            <Box key={ench.key} sx={{ display: 'flex', alignItems: 'center', gap: 0.5 }}>
              <FormControlLabel
                sx={{ flex: '0 0 auto', mr: 0, '& .MuiFormControlLabel-label': { fontSize: 12 } }}
                control={
                  <Checkbox
                    checked={checked}
                    onChange={() => onToggle(ench.key, ench.max_level)}
                    size="small"
                    sx={{ p: 0.3 }}
                  />
                }
                label={shortEnchName(ench.key)}
              />
              {checked && ench.max_level > 1 && (
                <Stack direction="row" alignItems="center" spacing={0.5} sx={{ flex: 1, minWidth: 80 }}>
                  <Slider
                    value={level}
                    min={1}
                    max={ench.max_level}
                    step={1}
                    size="small"
                    onChange={(_, v) => onSetLevel(ench.key, v)}
                    sx={{ flex: 1 }}
                  />
                  <Typography variant="caption" sx={{ minWidth: 16, textAlign: 'right' }}>{level}</Typography>
                </Stack>
              )}
            </Box>
          );
        })}
      </Box>
    </Box>
  );
}

/**
 * Potion options panel with base type, display name, and custom effects.
 *
 * Props:
 *   potionTypes: [string, ...]
 *   effectTypes: [string, ...]
 *   potionType: string
 *   onPotionTypeChange: (value) => void
 *   potionName: string
 *   onPotionNameChange: (value) => void
 *   potionEffects: [{type, duration, amplifier}, ...]
 *   onAddEffect: () => void
 *   onRemoveEffect: (idx) => void
 *   onUpdateEffect: (idx, field, value) => void
 */
export function PotionOptionsPanel({
  potionTypes, effectTypes,
  potionType, onPotionTypeChange,
  potionName, onPotionNameChange,
  potionEffects, onAddEffect, onRemoveEffect, onUpdateEffect,
}) {
  return (
    <Box sx={{ p: 1.5, bgcolor: 'rgba(33,150,243,0.08)', borderRadius: 1, border: '1px solid rgba(33,150,243,0.2)' }}>
      <Typography variant="caption" sx={{ mb: 1, display: 'block', fontWeight: 'bold' }}>
        Potion Options
      </Typography>
      <Stack spacing={1.5}>
        <Stack direction="row" spacing={1} sx={{ flexWrap: 'wrap', alignItems: 'center' }}>
          <FormControl size="small" sx={{ minWidth: 200 }}>
            <InputLabel>Base Type</InputLabel>
            <Select value={potionType} label="Base Type" onChange={(e) => onPotionTypeChange(e.target.value)}>
              <MenuItem value=""><em>None</em></MenuItem>
              {potionTypes.map((pt) => (
                <MenuItem key={pt} value={pt}>{shortPotionName(pt)}</MenuItem>
              ))}
            </Select>
          </FormControl>
          <TextField
            size="small" label="Display Name" value={potionName}
            onChange={(e) => onPotionNameChange(e.target.value)}
            placeholder="My Potion" sx={{ minWidth: 160 }}
          />
        </Stack>

        <Box>
          <Stack direction="row" alignItems="center" spacing={0.5} sx={{ mb: 0.5 }}>
            <Typography variant="caption" sx={{ fontWeight: 'bold' }}>
              Custom Effects ({potionEffects.length})
            </Typography>
            <IconButton size="small" onClick={onAddEffect} color="primary" sx={{ p: 0.25 }}>
              <AddCircleOutlineIcon fontSize="small" />
            </IconButton>
          </Stack>
          {potionEffects.map((pe, idx) => (
            <Stack key={idx} direction="row" spacing={0.5} alignItems="center" sx={{ mb: 0.5 }}>
              <FormControl size="small" sx={{ minWidth: 160 }}>
                <Select value={pe.type} onChange={(e) => onUpdateEffect(idx, 'type', e.target.value)} sx={{ fontSize: 12 }}>
                  {effectTypes.map((et) => (
                    <MenuItem key={et} value={et} sx={{ fontSize: 12 }}>
                      {et.replace(/_/g, ' ').toLowerCase()}
                    </MenuItem>
                  ))}
                </Select>
              </FormControl>
              <TextField
                size="small" label="Seconds" type="number" value={pe.duration}
                onChange={(e) => onUpdateEffect(idx, 'duration', e.target.value)} sx={{ width: 90 }}
              />
              <TextField
                size="small" label="Level" type="number" value={pe.amplifier}
                onChange={(e) => onUpdateEffect(idx, 'amplifier', e.target.value)} sx={{ width: 70 }}
              />
              <IconButton size="small" onClick={() => onRemoveEffect(idx)} color="error" sx={{ p: 0.25 }}>
                <RemoveCircleOutlineIcon fontSize="small" />
              </IconButton>
            </Stack>
          ))}
        </Box>
      </Stack>
    </Box>
  );
}
