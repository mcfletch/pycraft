import { useState, useEffect, useMemo } from 'react';
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
  Tooltip,
  IconButton,
  Collapse,
  Slider,
  Select,
  MenuItem,
  InputLabel,
  FormControl,
} from '@mui/material';
import FavoriteIcon from '@mui/icons-material/Favorite';
import RestaurantIcon from '@mui/icons-material/Restaurant';
import MapIcon from '@mui/icons-material/Map';
import AddCircleOutlineIcon from '@mui/icons-material/AddCircleOutline';
import RemoveCircleOutlineIcon from '@mui/icons-material/RemoveCircleOutline';
import { usePlayerDetail, usePlayerInventory, useSearchBlocks, useEnchantments, usePotionTypes } from '../../api/queries';
import { useTeleportPlayer, useGiveItem, useEnchantItem } from '../../api/mutations';
import InventoryView from './InventoryView';

/** Format health as hearts (each heart = 2 HP), rounded to nearest 1/4 heart */
function formatHealth(health) {
  if (health == null) return null;
  const hearts = health / 2;
  return Math.round(hearts * 4) / 4;
}

function shortEnchName(key) {
  return key.replace('minecraft:', '').replace(/_/g, ' ');
}

function shortPotionName(key) {
  return key.replace('minecraft:', '').replace(/_/g, ' ');
}

/** Check if a material name is a potion type */
function isPotion(material, potionMaterials) {
  if (!material) return false;
  const m = material.toLowerCase();
  if (potionMaterials?.length) {
    return potionMaterials.some((pm) => m === pm || m === pm.replace('minecraft:', ''));
  }
  return m.includes('potion') || m === 'minecraft:tipped_arrow' || m === 'tipped_arrow';
}

export default function PlayerDetail({ uuid, onBack, onShowOnMap }) {
  const { data: player, isLoading, error } = usePlayerDetail(uuid);
  const { data: inventory } = usePlayerInventory(uuid);
  const { data: enchData } = useEnchantments();
  const { data: potionData } = usePotionTypes();
  const teleportMutation = useTeleportPlayer();
  const giveMutation = useGiveItem();
  const enchantMutation = useEnchantItem();

  const [teleportForm, setTeleportForm] = useState({ world: '', x: '', y: '', z: '' });
  const [giveForm, setGiveForm] = useState({ material: '', count: '1' });
  const [enchantOnGive, setEnchantOnGive] = useState(false);
  const [materialSearch, setMaterialSearch] = useState('');
  const { data: searchResults } = useSearchBlocks(materialSearch);
  const materialOptions = searchResults?.results || [];

  // Enchantment selections: { key: level } for checked enchantments
  const [enchSelections, setEnchSelections] = useState({});

  // Potion state
  const [potionType, setPotionType] = useState('');
  const [potionName, setPotionName] = useState('');
  const [potionEffects, setPotionEffects] = useState([]);

  const potionTypes = potionData?.potion_types || [];
  const effectTypes = potionData?.effect_types || [];
  const potionMaterials = potionData?.potion_materials || [];
  const showPotionPanel = isPotion(giveForm.material, potionMaterials);

  // Initialize selections when enchantments data loads — pre-select desirable ones at max level
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

  const handleTeleport = (e) => {
    e.preventDefault();
    teleportMutation.mutate({
      uuid,
      world: teleportForm.world || player.location?.world,
      x: parseFloat(teleportForm.x),
      y: parseFloat(teleportForm.y),
      z: parseFloat(teleportForm.z),
    });
  };

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
    // Add potion params if this is a potion
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
    enchantMutation.mutate({ uuid, slot });
  };

  // Potion effect helpers
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
      <Box>
        <Button size="small" onClick={onBack}>&larr; Back to list</Button>
      </Box>

      <Card>
        <CardContent>
          <Stack direction="row" alignItems="center" spacing={1} sx={{ mb: 1 }}>
            <Typography variant="h5">
              {player.display_name || player.name}
            </Typography>
            {onShowOnMap && player.location && (
              <Tooltip title="Show on Map">
                <IconButton size="small" onClick={() => onShowOnMap(uuid)} color="primary">
                  <MapIcon />
                </IconButton>
              </Tooltip>
            )}
          </Stack>
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
            <Stack direction="row" alignItems="center" spacing={0.5}>
              <Typography variant="body2" color="text.secondary">
                Location: {player.location.world} ({Math.round(player.location.x)}, {Math.round(player.location.y)}, {Math.round(player.location.z)})
              </Typography>
              {onShowOnMap && (
                <Tooltip title="Show on Map">
                  <IconButton size="small" onClick={() => onShowOnMap(uuid)} color="primary" sx={{ p: 0.25 }}>
                    <MapIcon fontSize="small" />
                  </IconButton>
                </Tooltip>
              )}
            </Stack>
          )}
        </CardContent>
      </Card>

      <Card>
        <CardContent>
          <Typography variant="h6" gutterBottom>Teleport</Typography>
          <Box component="form" onSubmit={handleTeleport} sx={{ display: 'flex', gap: 1, flexWrap: 'wrap', alignItems: 'center' }}>
            <TextField
              size="small" label="World" value={teleportForm.world}
              onChange={(e) => setTeleportForm({ ...teleportForm, world: e.target.value })}
              placeholder={player.location?.world || 'world'}
            />
            <TextField
              size="small" label="X" type="number" value={teleportForm.x}
              onChange={(e) => setTeleportForm({ ...teleportForm, x: e.target.value })}
              sx={{ width: 100 }}
            />
            <TextField
              size="small" label="Y" type="number" value={teleportForm.y}
              onChange={(e) => setTeleportForm({ ...teleportForm, y: e.target.value })}
              sx={{ width: 100 }}
            />
            <TextField
              size="small" label="Z" type="number" value={teleportForm.z}
              onChange={(e) => setTeleportForm({ ...teleportForm, z: e.target.value })}
              sx={{ width: 100 }}
            />
            <Button type="submit" variant="contained" size="small" disabled={teleportMutation.isPending}>
              Teleport
            </Button>
          </Box>
          {teleportMutation.isError && (
            <Alert severity="error" sx={{ mt: 1 }}>{teleportMutation.error.message}</Alert>
          )}
          {teleportMutation.isSuccess && (
            <Alert severity="success" sx={{ mt: 1 }}>Teleported!</Alert>
          )}
        </CardContent>
      </Card>

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
              <Box sx={{ mt: 1, p: 1.5, bgcolor: 'rgba(33,150,243,0.08)', borderRadius: 1, border: '1px solid rgba(33,150,243,0.2)' }}>
                <Typography variant="caption" sx={{ mb: 1, display: 'block', fontWeight: 'bold' }}>
                  Potion Options
                </Typography>
                <Stack spacing={1.5}>
                  <Stack direction="row" spacing={1} sx={{ flexWrap: 'wrap', alignItems: 'center' }}>
                    <FormControl size="small" sx={{ minWidth: 200 }}>
                      <InputLabel>Base Type</InputLabel>
                      <Select
                        value={potionType}
                        label="Base Type"
                        onChange={(e) => setPotionType(e.target.value)}
                      >
                        <MenuItem value="">
                          <em>None</em>
                        </MenuItem>
                        {potionTypes.map((pt) => (
                          <MenuItem key={pt} value={pt}>{shortPotionName(pt)}</MenuItem>
                        ))}
                      </Select>
                    </FormControl>
                    <TextField
                      size="small"
                      label="Display Name"
                      value={potionName}
                      onChange={(e) => setPotionName(e.target.value)}
                      placeholder="My Potion"
                      sx={{ minWidth: 160 }}
                    />
                  </Stack>

                  {/* Custom effects */}
                  <Box>
                    <Stack direction="row" alignItems="center" spacing={0.5} sx={{ mb: 0.5 }}>
                      <Typography variant="caption" sx={{ fontWeight: 'bold' }}>
                        Custom Effects ({potionEffects.length})
                      </Typography>
                      <IconButton size="small" onClick={addPotionEffect} color="primary" sx={{ p: 0.25 }}>
                        <AddCircleOutlineIcon fontSize="small" />
                      </IconButton>
                    </Stack>
                    {potionEffects.map((pe, idx) => (
                      <Stack key={idx} direction="row" spacing={0.5} alignItems="center" sx={{ mb: 0.5 }}>
                        <FormControl size="small" sx={{ minWidth: 160 }}>
                          <Select
                            value={pe.type}
                            onChange={(e) => updatePotionEffect(idx, 'type', e.target.value)}
                            sx={{ fontSize: 12 }}
                          >
                            {effectTypes.map((et) => (
                              <MenuItem key={et} value={et} sx={{ fontSize: 12 }}>
                                {et.replace(/_/g, ' ').toLowerCase()}
                              </MenuItem>
                            ))}
                          </Select>
                        </FormControl>
                        <TextField
                          size="small"
                          label="Seconds"
                          type="number"
                          value={pe.duration}
                          onChange={(e) => updatePotionEffect(idx, 'duration', e.target.value)}
                          sx={{ width: 90 }}
                        />
                        <TextField
                          size="small"
                          label="Level"
                          type="number"
                          value={pe.amplifier}
                          onChange={(e) => updatePotionEffect(idx, 'amplifier', e.target.value)}
                          sx={{ width: 70 }}
                        />
                        <IconButton size="small" onClick={() => removePotionEffect(idx)} color="error" sx={{ p: 0.25 }}>
                          <RemoveCircleOutlineIcon fontSize="small" />
                        </IconButton>
                      </Stack>
                    ))}
                  </Box>
                </Stack>
              </Box>
            </Collapse>

            {/* Enchantment selector panel */}
            <Collapse in={enchantOnGive}>
              <Box sx={{ mt: 1, p: 1.5, bgcolor: 'rgba(171,71,188,0.08)', borderRadius: 1, border: '1px solid rgba(171,71,188,0.2)' }}>
                <Typography variant="caption" sx={{ mb: 1, display: 'block', fontWeight: 'bold' }}>
                  Enchantments ({Object.keys(enchSelections).length} selected)
                </Typography>
                <Box sx={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(260px, 1fr))', gap: 0.5 }}>
                  {allEnchantments.map((ench) => {
                    const checked = ench.key in enchSelections;
                    const level = enchSelections[ench.key] || ench.max_level;
                    return (
                      <Box key={ench.key} sx={{ display: 'flex', alignItems: 'center', gap: 0.5 }}>
                        <FormControlLabel
                          sx={{ flex: '0 0 auto', mr: 0, '& .MuiFormControlLabel-label': { fontSize: 12 } }}
                          control={
                            <Checkbox
                              checked={checked}
                              onChange={() => toggleEnch(ench.key, ench.max_level)}
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
                              onChange={(_, v) => setEnchLevel(ench.key, v)}
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

      {inventory && (
        <Card>
          <CardContent>
            <Typography variant="h6" gutterBottom>Inventory</Typography>
            <InventoryView inventory={inventory} onEnchant={handleEnchantSlot} />
            {enchantMutation.isSuccess && (
              <Alert severity="success" sx={{ mt: 1 }}>
                Enchanted! Applied: {enchantMutation.data?.applied?.map(e => e.replace('minecraft:', '')).join(', ') || 'none applicable'}
              </Alert>
            )}
            {enchantMutation.isError && (
              <Alert severity="error" sx={{ mt: 1 }}>{enchantMutation.error.message}</Alert>
            )}
          </CardContent>
        </Card>
      )}
    </Stack>
  );
}
