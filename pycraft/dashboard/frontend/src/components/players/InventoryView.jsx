import { useState, useEffect } from 'react';
import {
  Box, Typography, Menu, MenuItem, ListItemIcon, ListItemText,
  Dialog, DialogTitle, DialogContent, DialogActions, Button, CircularProgress,
} from '@mui/material';
import AutoFixHighIcon from '@mui/icons-material/AutoFixHigh';
import DeleteIcon from '@mui/icons-material/Delete';
import { useApplicableEnchantments } from '../../api/queries';
import { EnchantmentSelector, PotionOptionsPanel, isPotion } from './EnchantmentSelector';
import { SlotBox, shortName } from '../inventory/SlotBox';
import { InventoryGrid } from '../inventory/InventoryGrid';
import { useInventoryDrag } from '../inventory/useInventoryDrag';

const ARMOR_LABELS = ['Boots', 'Leggings', 'Chestplate', 'Helmet'];

export default function InventoryView({
  inventory, onEnchant, onDrop, onMove,
  enchantDialogSlot, onCloseEnchantDialog,
  uuid, enchantMutation, potionData,
}) {
  const [menuAnchor, setMenuAnchor] = useState(null);
  const [menuSlot, setMenuSlot] = useState(null);

  const { dragOverSlot, handleDragStart, handleDragOver, handleDrop } = useInventoryDrag(onMove);

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

  const armor = contents.slice(36, 40);
  const offhand = contents[40] || null;
  const usedCount = contents.filter((s) => s).length;

  const dragProps = { onDragStart: handleDragStart, onDragOver: handleDragOver, onDrop: handleDrop };

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
              <SlotBox
                key={36 + ai} slot={armor[ai]} index={36 + ai} label={ARMOR_LABELS[ai]}
                onClick={handleSlotClick} isDragOver={dragOverSlot === 36 + ai}
                {...dragProps}
              />
            ))}
            <Box sx={{ mx: 0.5, borderLeft: '1px solid rgba(255,255,255,0.15)', height: 48 }} />
            <SlotBox
              slot={offhand} index={40} label="Offhand"
              onClick={handleSlotClick} isDragOver={dragOverSlot === 40}
              {...dragProps}
            />
          </Box>
        </Box>
      </Box>

      {/* Main inventory (3 rows of 9) */}
      <Box sx={{ mb: 1 }}>
        <InventoryGrid
          slots={contents} startIndex={9} count={27} columns={9}
          onSlotClick={handleSlotClick} dragOverSlot={dragOverSlot}
          {...dragProps}
        />
      </Box>

      {/* Hotbar */}
      <Box>
        <Typography variant="caption" color="text.secondary" sx={{ fontSize: 10 }}>Hotbar</Typography>
        <Box sx={{ borderTop: '2px solid rgba(255,255,255,0.2)', pt: 0.5 }}>
          <InventoryGrid
            slots={contents} startIndex={0} count={9} columns={9}
            onSlotClick={handleSlotClick} dragOverSlot={dragOverSlot}
            {...dragProps}
          />
        </Box>
      </Box>

      {/* Context menu */}
      <Menu anchorEl={menuAnchor} open={!!menuAnchor} onClose={closeMenu}>
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
      <Dialog open={enchantDialogSlot != null} onClose={onCloseEnchantDialog} maxWidth="md" fullWidth>
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
