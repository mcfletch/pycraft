import { useState, useEffect } from 'react';
import {
  Box, Tooltip, Typography, Menu, MenuItem, ListItemIcon, ListItemText,
  Dialog, DialogTitle, DialogContent, DialogActions, Button, CircularProgress,
} from '@mui/material';
import AutoFixHighIcon from '@mui/icons-material/AutoFixHigh';
import DeleteIcon from '@mui/icons-material/Delete';
import { useApplicableEnchantments } from '../../api/queries';
import { EnchantmentSelector, PotionOptionsPanel, isPotion } from './EnchantmentSelector';

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

function SlotBox({ slot, index, label, onClick }) {
  const enchStr = slot ? formatEnchantments(slot.enchantments) : '';
  const tipText = slot
    ? `${label ? label + ': ' : ''}${shortName(slot.material)} x${slot.amount}${enchStr ? `\n${enchStr}` : ''}`
    : label || `Empty slot ${index}`;
  return (
    <Tooltip title={<span style={{ whiteSpace: 'pre-line' }}>{tipText}</span>}>
      <Box
        onClick={slot ? (e) => onClick(index, e.currentTarget) : undefined}
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

export default function InventoryView({
  inventory, onEnchant, onDrop,
  enchantDialogSlot, onCloseEnchantDialog,
  uuid, enchantMutation, potionData,
}) {
  const [menuAnchor, setMenuAnchor] = useState(null);
  const [menuSlot, setMenuSlot] = useState(null);

  // Enchant dialog state
  const [dialogEnchSelections, setDialogEnchSelections] = useState({});
  const [dialogPotionType, setDialogPotionType] = useState('');
  const [dialogPotionName, setDialogPotionName] = useState('');
  const [dialogPotionEffects, setDialogPotionEffects] = useState([]);

  // Fetch applicable enchantments when the dialog is open
  const { data: applicableData, isLoading: enchLoading } = useApplicableEnchantments(uuid, enchantDialogSlot);
  const applicableEnchantments = applicableData?.enchantments || [];

  // Dialog item and potion detection
  const contents = inventory?.contents || [];
  const dialogItem = enchantDialogSlot != null ? contents[enchantDialogSlot] : null;
  const potionMaterials = potionData?.potion_materials || [];
  const showPotionOptions = dialogItem && isPotion(dialogItem.material, potionMaterials);

  // Initialize dialog state when slot changes
  useEffect(() => {
    if (enchantDialogSlot != null && contents.length > 0) {
      const item = contents[enchantDialogSlot];
      if (item?.enchantments && typeof item.enchantments === 'object') {
        const existing = {};
        for (const [key, level] of Object.entries(item.enchantments)) {
          existing[key] = level;
        }
        setDialogEnchSelections(existing);
      } else {
        setDialogEnchSelections({});
      }
      setDialogPotionType('');
      setDialogPotionName('');
      setDialogPotionEffects([]);
    }
  }, [enchantDialogSlot]); // eslint-disable-line react-hooks/exhaustive-deps

  // Dialog enchantment helpers
  const toggleDialogEnch = (key, maxLevel) => {
    setDialogEnchSelections((prev) => {
      if (key in prev) {
        const next = { ...prev };
        delete next[key];
        return next;
      }
      return { ...prev, [key]: maxLevel };
    });
  };
  const setDialogEnchLevel = (key, level) => {
    setDialogEnchSelections((prev) => ({ ...prev, [key]: level }));
  };

  // Dialog potion helpers
  const effectTypes = potionData?.effect_types || [];
  const addDialogPotionEffect = () => {
    setDialogPotionEffects((prev) => [...prev, { type: effectTypes[0] || 'SPEED', duration: '480', amplifier: '0' }]);
  };
  const removeDialogPotionEffect = (idx) => {
    setDialogPotionEffects((prev) => prev.filter((_, i) => i !== idx));
  };
  const updateDialogPotionEffect = (idx, field, value) => {
    setDialogPotionEffects((prev) => prev.map((pe, i) => i === idx ? { ...pe, [field]: value } : pe));
  };

  const handleApply = () => {
    const enchantments = Object.entries(dialogEnchSelections).map(([key, level]) => ({ key, level }));
    const params = { uuid, slot: enchantDialogSlot, enchantments };
    if (showPotionOptions) {
      if (dialogPotionType) params.potion_type = dialogPotionType;
      if (dialogPotionName) params.potion_name = dialogPotionName;
      if (dialogPotionEffects.length > 0) {
        params.potion_effects = dialogPotionEffects.map((pe) => ({
          type: pe.type,
          duration_seconds: parseFloat(pe.duration) || 60,
          amplifier: parseInt(pe.amplifier, 10) || 0,
        }));
      }
    }
    enchantMutation.mutate(params);
    onCloseEnchantDialog();
  };

  if (!inventory) return null;

  const mainSlots = contents.slice(9, 36);
  const hotbar = contents.slice(0, 9);
  const armor = contents.slice(36, 40);
  const offhand = contents[40] || null;

  const usedCount = contents.filter((s) => s).length;

  const handleSlotClick = (index, anchorEl) => {
    setMenuSlot(index);
    setMenuAnchor(anchorEl);
  };

  const closeMenu = () => {
    setMenuAnchor(null);
    setMenuSlot(null);
  };

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
              <SlotBox key={36 + ai} slot={armor[ai]} index={36 + ai} label={ARMOR_LABELS[ai]} onClick={handleSlotClick} />
            ))}
            <Box sx={{ mx: 0.5, borderLeft: '1px solid rgba(255,255,255,0.15)', height: 48 }} />
            <SlotBox slot={offhand} index={40} label="Offhand" onClick={handleSlotClick} />
          </Box>
        </Box>
      </Box>

      {/* Main inventory (3 rows of 9) */}
      <Box sx={{ display: 'grid', gridTemplateColumns: 'repeat(9, 48px)', gap: 0.5, mb: 1 }}>
        {mainSlots.map((slot, i) => (
          <SlotBox key={9 + i} slot={slot} index={9 + i} onClick={handleSlotClick} />
        ))}
      </Box>

      {/* Hotbar */}
      <Box>
        <Typography variant="caption" color="text.secondary" sx={{ fontSize: 10 }}>Hotbar</Typography>
        <Box sx={{ display: 'grid', gridTemplateColumns: 'repeat(9, 48px)', gap: 0.5, borderTop: '2px solid rgba(255,255,255,0.2)', pt: 0.5 }}>
          {hotbar.map((slot, i) => (
            <SlotBox key={i} slot={slot} index={i} onClick={handleSlotClick} />
          ))}
        </Box>
      </Box>

      {/* Context menu */}
      <Menu
        anchorEl={menuAnchor}
        open={!!menuAnchor}
        onClose={closeMenu}
      >
        <MenuItem onClick={() => { if (onEnchant) onEnchant(menuSlot); closeMenu(); }}>
          <ListItemIcon><AutoFixHighIcon fontSize="small" color="secondary" /></ListItemIcon>
          <ListItemText>Enchant</ListItemText>
        </MenuItem>
        <MenuItem onClick={() => { if (onDrop) onDrop(menuSlot); closeMenu(); }}>
          <ListItemIcon><DeleteIcon fontSize="small" color="error" /></ListItemIcon>
          <ListItemText>Drop</ListItemText>
        </MenuItem>
      </Menu>

      {/* Enchant dialog */}
      <Dialog
        open={enchantDialogSlot != null}
        onClose={onCloseEnchantDialog}
        maxWidth="md"
        fullWidth
      >
        <DialogTitle>
          Enchant: {dialogItem ? shortName(dialogItem.material) : ''} (slot {enchantDialogSlot})
        </DialogTitle>
        <DialogContent>
          {enchLoading ? (
            <Box sx={{ display: 'flex', justifyContent: 'center', py: 3 }}>
              <CircularProgress />
            </Box>
          ) : applicableEnchantments.length > 0 ? (
            <EnchantmentSelector
              allEnchantments={applicableEnchantments}
              selections={dialogEnchSelections}
              onToggle={toggleDialogEnch}
              onSetLevel={setDialogEnchLevel}
            />
          ) : (
            <Typography variant="body2" color="text.secondary" sx={{ py: 1 }}>
              No applicable enchantments for this item.
            </Typography>
          )}
          {showPotionOptions && (
            <Box sx={{ mt: 1.5 }}>
              <PotionOptionsPanel
                potionTypes={potionData?.potion_types || []}
                effectTypes={effectTypes}
                potionType={dialogPotionType}
                onPotionTypeChange={setDialogPotionType}
                potionName={dialogPotionName}
                onPotionNameChange={setDialogPotionName}
                potionEffects={dialogPotionEffects}
                onAddEffect={addDialogPotionEffect}
                onRemoveEffect={removeDialogPotionEffect}
                onUpdateEffect={updateDialogPotionEffect}
              />
            </Box>
          )}
        </DialogContent>
        <DialogActions>
          <Button onClick={onCloseEnchantDialog}>Cancel</Button>
          <Button variant="contained" onClick={handleApply} disabled={enchantMutation?.isPending}>
            Apply
          </Button>
        </DialogActions>
      </Dialog>
    </Box>
  );
}
