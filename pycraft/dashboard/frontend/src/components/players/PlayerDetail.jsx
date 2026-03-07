import { useState, useEffect } from 'react';
import {
  Card,
  CardContent,
  Typography,
  CircularProgress,
  Alert,
  Box,
  Chip,
  TextField,
  Button,
  Stack,
  Autocomplete,
  FormControlLabel,
  Checkbox,
  Collapse,
} from '@mui/material';
import FavoriteIcon from '@mui/icons-material/Favorite';
import RestaurantIcon from '@mui/icons-material/Restaurant';
import { usePlayerDetail, usePlayerInventory, useSearchBlocks, useEnchantments, usePotionTypes } from '../../api/queries';
import { useGiveItem, useEnchantItem, useDropItem } from '../../api/mutations';
import { EnchantmentSelector, PotionOptionsPanel, isPotion } from './EnchantmentSelector';
import InventoryView from './InventoryView';

/** Format health as hearts (each heart = 2 HP), rounded to nearest 1/4 heart */
function formatHealth(health) {
  if (health == null) return null;
  const hearts = health / 2;
  return Math.round(hearts * 4) / 4;
}

export default function PlayerDetail({ uuid }) {
  const { data: player, isLoading, error } = usePlayerDetail(uuid);
  const { data: inventory } = usePlayerInventory(uuid);
  const { data: enchData } = useEnchantments();
  const { data: potionData } = usePotionTypes();
  const giveMutation = useGiveItem();
  const enchantMutation = useEnchantItem();
  const dropMutation = useDropItem();

  const [giveForm, setGiveForm] = useState({ material: '', count: '1' });
  const [enchantOnGive, setEnchantOnGive] = useState(false);
  const [materialSearch, setMaterialSearch] = useState('');
  const { data: searchResults } = useSearchBlocks(materialSearch);
  const materialOptions = searchResults?.results || [];

  // Enchantment selections for the Give form: { key: level }
  const [enchSelections, setEnchSelections] = useState({});

  // Potion state for the Give form
  const [potionType, setPotionType] = useState('');
  const [potionName, setPotionName] = useState('');
  const [potionEffects, setPotionEffects] = useState([]);

  // Enchant dialog state (slot number or null)
  const [enchantDialogSlot, setEnchantDialogSlot] = useState(null);

  const potionTypes = potionData?.potion_types || [];
  const effectTypes = potionData?.effect_types || [];
  const potionMaterials = potionData?.potion_materials || [];
  const showPotionPanel = isPotion(giveForm.material, potionMaterials);

  // Initialize Give form enchant selections — pre-select desirable ones at max level
  const allEnchantments = enchData?.enchantments || [];
  useEffect(() => {
    if (allEnchantments.length > 0 && Object.keys(enchSelections).length === 0) {
      const initial = {};
      for (const e of allEnchantments) {
        if (e.desirable) {
          initial[e.key] = e.max_level;
        }
      }
      setEnchSelections(initial);
    }
  }, [allEnchantments]); // eslint-disable-line react-hooks/exhaustive-deps

  if (isLoading) return <CircularProgress />;
  if (error) return <Alert severity="error">Failed to load player: {error.message}</Alert>;
  if (!player) return <Alert severity="warning">Player not found</Alert>;

  const handleGive = (e) => {
    e.preventDefault();
    const selectedEnchs = enchantOnGive
      ? Object.entries(enchSelections).map(([key, level]) => ({ key, level }))
      : undefined;
    const params = {
      uuid,
      material: giveForm.material,
      count: parseInt(giveForm.count, 10) || 1,
      enchant: enchantOnGive,
      enchantments: selectedEnchs,
    };
    if (showPotionPanel) {
      if (potionType) params.potion_type = potionType;
      if (potionName) params.potion_name = potionName;
      if (potionEffects.length > 0) {
        params.potion_effects = potionEffects.map((pe) => ({
          type: pe.type,
          duration_seconds: parseFloat(pe.duration) || 60,
          amplifier: parseInt(pe.amplifier, 10) || 0,
        }));
      }
    }
    giveMutation.mutate(params);
  };

  const toggleEnch = (key, maxLevel) => {
    setEnchSelections((prev) => {
      if (key in prev) {
        const next = { ...prev };
        delete next[key];
        return next;
      }
      return { ...prev, [key]: maxLevel };
    });
  };

  const setEnchLevel = (key, level) => {
    setEnchSelections((prev) => ({ ...prev, [key]: level }));
  };

  const handleEnchantSlot = (slot) => {
    setEnchantDialogSlot(slot);
  };
  const handleDropSlot = (slot) => {
    dropMutation.mutate({ uuid, slot });
  };

  // Potion effect helpers for the Give form
  const addPotionEffect = () => {
    setPotionEffects((prev) => [...prev, { type: effectTypes[0] || 'SPEED', duration: '480', amplifier: '0' }]);
  };
  const removePotionEffect = (idx) => {
    setPotionEffects((prev) => prev.filter((_, i) => i !== idx));
  };
  const updatePotionEffect = (idx, field, value) => {
    setPotionEffects((prev) => prev.map((pe, i) => i === idx ? { ...pe, [field]: value } : pe));
  };

  const hearts = formatHealth(player.health);

  return (
    <Stack spacing={2}>
      <Card>
        <CardContent>
          <Typography variant="h5" sx={{ mb: 1 }}>
            {player.display_name || player.name}
          </Typography>
          <Box sx={{ display: 'flex', gap: 1, flexWrap: 'wrap', mb: 2 }}>
            {player.game_mode && <Chip label={player.game_mode} size="small" />}
            {hearts != null && (
              <Chip icon={<FavoriteIcon />} label={`${hearts} hearts`} size="small" color="error" />
            )}
            {player.food_level != null && (
              <Chip icon={<RestaurantIcon />} label={`${player.food_level} Food`} size="small" color="warning" />
            )}
            {player.level != null && <Chip label={`Level ${player.level}`} size="small" color="info" />}
          </Box>
          <Typography variant="body2" color="text.secondary">
            UUID: {player.uuid}
          </Typography>
          {player.location && (
            <Typography variant="body2" color="text.secondary">
              Location: {player.location.world} ({player.location.x.toFixed(1)}, {player.location.y.toFixed(1)}, {player.location.z.toFixed(1)})
            </Typography>
          )}
        </CardContent>
      </Card>

      {inventory && (
        <Card>
          <CardContent>
            <Typography variant="h6" gutterBottom>Inventory</Typography>
            <InventoryView
              inventory={inventory}
              onEnchant={handleEnchantSlot}
              onDrop={handleDropSlot}
              enchantDialogSlot={enchantDialogSlot}
              onCloseEnchantDialog={() => setEnchantDialogSlot(null)}
              uuid={uuid}
              enchantMutation={enchantMutation}
              potionData={potionData}
            />
            {enchantMutation.isSuccess && (
              <Alert severity="success" sx={{ mt: 1 }}>
                Enchanted! Applied: {enchantMutation.data?.applied?.map(e => e.replace('minecraft:', '')).join(', ') || 'none applicable'}
              </Alert>
            )}
            {enchantMutation.isError && (
              <Alert severity="error" sx={{ mt: 1 }}>{enchantMutation.error.message}</Alert>
            )}
            {dropMutation.isError && (
              <Alert severity="error" sx={{ mt: 1 }}>{dropMutation.error.message}</Alert>
            )}
          </CardContent>
        </Card>
      )}

      <Card>
        <CardContent>
          <Typography variant="h6" gutterBottom>Give Item</Typography>
          <Box component="form" onSubmit={handleGive}>
            <Stack direction="row" spacing={1} sx={{ flexWrap: 'wrap', alignItems: 'center', mb: 1 }}>
              <Autocomplete
                freeSolo
                options={materialOptions}
                inputValue={materialSearch}
                onInputChange={(_, v) => {
                  setMaterialSearch(v);
                  setGiveForm({ ...giveForm, material: v });
                }}
                onChange={(_, v) => {
                  if (v) setGiveForm({ ...giveForm, material: v });
                }}
                renderInput={(params) => (
                  <TextField {...params} size="small" label="Material" placeholder="minecraft:diamond" sx={{ width: 280 }} />
                )}
                size="small"
                sx={{ width: 280 }}
              />
              <TextField
                size="small" label="Count" type="number" value={giveForm.count}
                onChange={(e) => setGiveForm({ ...giveForm, count: e.target.value })}
                sx={{ width: 80 }}
              />
              <FormControlLabel
                control={
                  <Checkbox
                    checked={enchantOnGive}
                    onChange={(e) => setEnchantOnGive(e.target.checked)}
                    size="small"
                  />
                }
                label="Enchant"
              />
              <Button type="submit" variant="contained" size="small" disabled={giveMutation.isPending}>
                Give
              </Button>
            </Stack>

            {/* Potion options panel */}
            <Collapse in={showPotionPanel}>
              <Box sx={{ mt: 1 }}>
                <PotionOptionsPanel
                  potionTypes={potionTypes}
                  effectTypes={effectTypes}
                  potionType={potionType}
                  onPotionTypeChange={setPotionType}
                  potionName={potionName}
                  onPotionNameChange={setPotionName}
                  potionEffects={potionEffects}
                  onAddEffect={addPotionEffect}
                  onRemoveEffect={removePotionEffect}
                  onUpdateEffect={updatePotionEffect}
                />
              </Box>
            </Collapse>

            {/* Enchantment selector panel */}
            <Collapse in={enchantOnGive}>
              <Box sx={{ mt: 1 }}>
                <EnchantmentSelector
                  allEnchantments={allEnchantments}
                  selections={enchSelections}
                  onToggle={toggleEnch}
                  onSetLevel={setEnchLevel}
                />
              </Box>
            </Collapse>
          </Box>
          {giveMutation.isError && (
            <Alert severity="error" sx={{ mt: 1 }}>{giveMutation.error.message}</Alert>
          )}
          {giveMutation.isSuccess && (
            <Alert severity="success" sx={{ mt: 1 }}>Item given!</Alert>
          )}
        </CardContent>
      </Card>

    </Stack>
  );
}
