import { useState, useRef, useEffect, useCallback } from 'react';
import {
  Card,
  CardContent,
  Typography,
  Box,
  TextField,
  Stack,
  Slider,
  Select,
  MenuItem,
  FormControl,
  InputLabel,
  CircularProgress,
  Link,
  Chip,
  IconButton,
  Tooltip,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  List,
  ListItem,
  ListItemButton,
  ListItemText,
  Button,
} from '@mui/material';
import SearchIcon from '@mui/icons-material/Search';
import GpsFixedIcon from '@mui/icons-material/GpsFixed';
import ContentPasteIcon from '@mui/icons-material/ContentPaste';
import RotateRightIcon from '@mui/icons-material/RotateRight';
import CloseIcon from '@mui/icons-material/Close';
import ZoomInIcon from '@mui/icons-material/ZoomIn';
import VisibilityIcon from '@mui/icons-material/Visibility';
import InfoOutlinedIcon from '@mui/icons-material/InfoOutlined';
import InputAdornment from '@mui/material/InputAdornment';
import Popper from '@mui/material/Popper';
import Paper from '@mui/material/Paper';
import ClickAwayListener from '@mui/material/ClickAwayListener';
import { useWorldBlocks, useOnlinePlayers, useTemplates, useTemplateDetail, useMapSearch } from '../../api/queries';
import { useTeleportPlayer, usePasteTemplate, useEvalCode } from '../../api/mutations';
import PlayerDetail from '../players/PlayerDetail';
import { TracebackDialog, parseLocation } from '../editor/CodeEditor';
import { fetchApi } from '../../api/client';

/* ── Fallback colors for blocks without a loaded texture ── */
const BLOCK_COLORS = {
  'minecraft:air': '#111111',
  'minecraft:cave_air': '#111111',
  'minecraft:void_air': '#0a0a0a',
  'minecraft:stone': '#808080',
  'minecraft:dirt': '#8B6914',
  'minecraft:grass_block': '#5B8C3E',
  'minecraft:water': '#3366CC',
  'minecraft:lava': '#FF4500',
  'minecraft:sand': '#E8D672',
  'minecraft:gravel': '#A0A0A0',
  'minecraft:bedrock': '#333333',
  'minecraft:cobblestone': '#6B6B6B',
  'minecraft:oak_planks': '#B8945F',
  'minecraft:deepslate': '#505050',
};

function getBlockColor(material) {
  if (!material) return '#87CEEB';
  return BLOCK_COLORS[material] || '#808080';
}

/* ── Texture cache: shared across renders, persistent for session ── */
const textureImages = new Map();

function getTextureUrl(material) {
  const name = material.startsWith('minecraft:') ? material.slice(10) : material;
  return `/api/textures/${name}.png`;
}

function loadTexture(material, onLoaded) {
  if (textureImages.has(material)) return;
  textureImages.set(material, 'loading');
  const img = new Image();
  img.onload = () => { textureImages.set(material, img); onLoaded(); };
  img.onerror = () => { textureImages.set(material, 'failed'); onLoaded(); };
  img.src = getTextureUrl(material);
}

/* ── Entity type colors ── */
const ENTITY_COLORS = {
  'minecraft:player': '#FF0000',
  'minecraft:zombie': '#2B5B2B',
  'minecraft:skeleton': '#C8C8C8',
  'minecraft:creeper': '#30B030',
  'minecraft:spider': '#3B2B1B',
  'minecraft:enderman': '#1B0B2E',
  'minecraft:cow': '#6B4423',
  'minecraft:pig': '#F0A0A0',
  'minecraft:sheep': '#E0D8D0',
  'minecraft:chicken': '#F0F0F0',
  'minecraft:villager': '#8B6914',
  'minecraft:item': '#FFFF00',
};

function getEntityColor(type) {
  return ENTITY_COLORS[type] || '#FF8800';
}

/** Draw a facing-direction triangle on the canvas */
function drawFacingArrow(ctx, cx, cy, yaw, radius, color) {
  const angle = ((yaw + 180) * Math.PI) / 180;
  const tipX = cx + Math.sin(angle) * radius;
  const tipY = cy - Math.cos(angle) * radius;
  const backL = angle - Math.PI * 0.8;
  const backR = angle + Math.PI * 0.8;
  const tailR = radius * 0.4;
  ctx.fillStyle = color;
  ctx.beginPath();
  ctx.moveTo(tipX, tipY);
  ctx.lineTo(cx + Math.sin(backL) * tailR, cy - Math.cos(backL) * tailR);
  ctx.lineTo(cx + Math.sin(backR) * tailR, cy - Math.cos(backR) * tailR);
  ctx.closePath();
  ctx.fill();
}

/** Rotate a 2D footprint array [z][x] by steps * 90 degrees CW */
function rotateFootprint(footprint, steps) {
  if (!footprint || steps === 0) return footprint;
  let grid = footprint;
  for (let s = 0; s < steps; s++) {
    const rows = grid.length;
    const cols = grid[0]?.length || 0;
    const rotated = [];
    for (let x = 0; x < cols; x++) {
      const newRow = [];
      for (let z = rows - 1; z >= 0; z--) {
        newRow.push(grid[z][x]);
      }
      rotated.push(newRow);
    }
    grid = rotated;
  }
  return grid;
}

/** Count materials in blocks grid for debug display */
function countMaterials(blocks) {
  if (!blocks) return {};
  const counts = {};
  for (const col of blocks) {
    for (const b of col) {
      const mat = b || 'null';
      counts[mat] = (counts[mat] || 0) + 1;
    }
  }
  return counts;
}

const MAX_QUERY = 128;  // cap per-axis; 128x128x60 = ~1M blocks, safe for MC server

export default function WorldMap({ worlds, initialFollowPlayer, onFollowConsumed }) {
  const canvasRef = useRef(null);
  const containerRef = useRef(null);
  const [containerSize, setContainerSize] = useState({ w: 800, h: 500 });
  const [worldName, setWorldName] = useState(() => sessionStorage.getItem('map_worldName') || '');
  const [centerXStr, setCenterXStr] = useState(() => sessionStorage.getItem('map_centerX') || '0');
  const [centerZStr, setCenterZStr] = useState(() => sessionStorage.getItem('map_centerZ') || '0');
  const [yLevel, setYLevel] = useState(() => parseInt(sessionStorage.getItem('map_yLevel') || '64', 10));
  const [zoom, setZoom] = useState(() => parseInt(sessionStorage.getItem('map_zoom') || '4', 10));
  const [texturesReady, setTexturesReady] = useState(0);
  const [followPlayer, setFollowPlayer] = useState(null);
  const [selectedPlayer, setSelectedPlayer] = useState(null);
  const [examinePlayer, setExaminePlayer] = useState(null);
  const examineAnchorRef = useRef(null);
  const [hoverInfo, setHoverInfo] = useState(null);

  /* Interaction modes: 'normal' | 'teleport-pick-player' | 'teleport-pick-dest' | 'paste-preview' */
  const [interactionMode, setInteractionMode] = useState('normal');
  const [teleportTarget, setTeleportTarget] = useState(null); // { uuid, name }

  /* Paste state */
  const [pasteDialogOpen, setPasteDialogOpen] = useState(false);
  const [selectedTemplateName, setSelectedTemplateName] = useState(null);
  const [pastePosition, setPastePosition] = useState(null); // { x, y, z } world coords
  const [pasteRotation, setPasteRotation] = useState(0); // 0-3
  const [pasteMousePos, setPasteMousePos] = useState(null); // { x, z } world coords for hover preview

  /* Inline code editor state */
  const [evalCode, setEvalCode] = useState('');
  const [evalHistory, setEvalHistory] = useState([]);
  const [evalHistoryIdx, setEvalHistoryIdx] = useState(-1);
  const [tracebackEntry, setTracebackEntry] = useState(null); // { error, traceback }
  const evalMutation = useEvalCode();

  /* Search state */
  const [searchText, setSearchText] = useState('');
  const [debouncedSearch, setDebouncedSearch] = useState('');
  const [searchOpen, setSearchOpen] = useState(false);
  const searchAnchorRef = useRef(null);

  /* Zoom popover */
  const [zoomAnchorEl, setZoomAnchorEl] = useState(null);
  const [yLevelStr, setYLevelStr] = useState(() => sessionStorage.getItem('map_yLevel') || '64');

  /*
   * Drag-to-pan state:
   * - visualOffset: CSS transform applied to canvas, persists after drag until new data loads
   * - dragStartRef: tracks mouse-down position for active drag
   */
  const [visualOffset, setVisualOffset] = useState({ x: 0, y: 0 });
  const dragStartRef = useRef(null);
  const dragOriginOffset = useRef({ x: 0, y: 0 });

  const centerX = parseInt(centerXStr, 10) || 0;
  const centerZ = parseInt(centerZStr, 10) || 0;

  const { data: players } = useOnlinePlayers();
  const teleportPlayer = useTeleportPlayer();
  const pasteTemplate = usePasteTemplate();
  const { data: templates } = useTemplates();
  const { data: templateDetail } = useTemplateDetail(selectedTemplateName);

  // Persist map position/zoom/world across tab switches
  useEffect(() => { sessionStorage.setItem('map_centerX', centerXStr); }, [centerXStr]);
  useEffect(() => { sessionStorage.setItem('map_centerZ', centerZStr); }, [centerZStr]);
  useEffect(() => { sessionStorage.setItem('map_yLevel', yLevelStr); }, [yLevelStr]);
  useEffect(() => { sessionStorage.setItem('map_zoom', String(zoom)); }, [zoom]);
  useEffect(() => { if (worldName) sessionStorage.setItem('map_worldName', worldName); }, [worldName]);

  // Debounce search input
  useEffect(() => {
    const timer = setTimeout(() => setDebouncedSearch(searchText), 500);
    return () => clearTimeout(timer);
  }, [searchText]);

  const { data: searchResults } = useMapSearch(debouncedSearch, worldName, centerX, centerZ);

  // Load textures for template footprint materials
  useEffect(() => {
    if (!templateDetail?.footprint) return;
    const onLoaded = () => setTexturesReady((n) => n + 1);
    for (const row of templateDetail.footprint) {
      for (const mat of row) {
        if (mat && mat !== 'minecraft:air') {
          loadTexture(mat, onLoaded);
        }
      }
    }
  }, [templateDetail]);

  /* Measure container with ResizeObserver — debounced so interpreter panel
     height changes don't immediately trigger a map refetch */
  useEffect(() => {
    const el = containerRef.current;
    if (!el) return;
    let timer;
    const ro = new ResizeObserver((entries) => {
      const { width, height } = entries[0].contentRect;
      if (width > 0 && height > 0) {
        clearTimeout(timer);
        timer = setTimeout(() => {
          setContainerSize({ w: Math.floor(width), h: Math.floor(height) });
        }, 300);
      }
    });
    ro.observe(el);
    return () => { ro.disconnect(); clearTimeout(timer); };
  }, []);

  // Auto-select first world
  useEffect(() => {
    if (!worldName && worlds?.length) {
      setWorldName(worlds[0].name);
    }
  }, [worlds, worldName]);

  // Accept initial follow player from parent
  useEffect(() => {
    if (!initialFollowPlayer) return;
    setFollowPlayer(initialFollowPlayer);
    if (onFollowConsumed) onFollowConsumed();
  }, [initialFollowPlayer, onFollowConsumed]);

  // Follow player: update center from their position
  useEffect(() => {
    if (!followPlayer || !players) return;
    const p = players.find((pl) => pl.uuid === followPlayer);
    if (p?.location && p.location.world === worldName) {
      const nx = Math.round(p.location.x);
      const nz = Math.round(p.location.z);
      const ny = Math.round(p.location.y);
      if (Math.abs(nx - centerX) > 2 || Math.abs(nz - centerZ) > 2) {
        setCenterXStr(String(nx));
        setCenterZStr(String(nz));
      }
      if (Math.abs(ny - yLevel) > 2) {
        setYLevelStr(String(ny));
      }
    }
  }, [followPlayer, players, worldName]); // deliberately omit centerX/centerZ/yLevel

  // Sync yLevelStr → yLevel
  useEffect(() => {
    const parsed = parseInt(yLevelStr, 10);
    if (!isNaN(parsed) && parsed !== yLevel) setYLevel(parsed);
  }, [yLevelStr]); // eslint-disable-line react-hooks/exhaustive-deps

  // ESC key to cancel interaction mode
  useEffect(() => {
    const onKey = (e) => {
      if (e.key === 'Escape' && interactionMode !== 'normal') {
        setInteractionMode('normal');
        setTeleportTarget(null);
        setSelectedTemplateName(null);
        setPastePosition(null);
        setPasteMousePos(null);
        setPasteRotation(0);
      }
    };
    document.addEventListener('keydown', onKey);
    return () => document.removeEventListener('keydown', onKey);
  }, [interactionMode]);

  // Minimum zoom: don't allow zooming out past what fits MAX_QUERY blocks
  const minZoom = Math.max(1, Math.ceil(Math.max(containerSize.w, containerSize.h) / MAX_QUERY));

  // Query size derived from container and zoom
  const effectiveZoom = Math.max(zoom, minZoom);
  const blocksW = Math.min(Math.floor(containerSize.w / effectiveZoom), MAX_QUERY);
  const blocksH = Math.min(Math.floor(containerSize.h / effectiveZoom), MAX_QUERY);
  const canvasW = blocksW * effectiveZoom;
  const canvasH = blocksH * effectiveZoom;
  const halfW = Math.floor(blocksW / 2);
  const halfH = Math.floor(blocksH / 2);

  const params = worldName && blocksW > 0 && blocksH > 0
    ? {
        x1: String(centerX - halfW),
        z1: String(centerZ - halfH),
        x2: String(centerX + halfW),
        z2: String(centerZ + halfH),
        y: String(yLevel),
      }
    : null;

  // Debounce params so rapid scroll-wheel events don't flood the server
  const [debouncedParams, setDebouncedParams] = useState(params);
  useEffect(() => {
    const timer = setTimeout(() => setDebouncedParams(params), 250);
    return () => clearTimeout(timer);
  }, [params?.x1, params?.z1, params?.x2, params?.z2, params?.y, worldName]); // eslint-disable-line react-hooks/exhaustive-deps

  const { data: blockData, isLoading } = useWorldBlocks(worldName, debouncedParams);

  // When new blockData arrives, clear visual offset
  const lastRenderedCenterRef = useRef({ x: centerX, z: centerZ });
  useEffect(() => {
    if (!blockData) return;
    setVisualOffset({ x: 0, y: 0 });
    lastRenderedCenterRef.current = { x: centerX, z: centerZ };
  }, [blockData]); // eslint-disable-line react-hooks/exhaustive-deps

  // Load textures for new materials
  useEffect(() => {
    if (!blockData?.blocks) return;
    const onLoaded = () => setTexturesReady((n) => n + 1);
    for (const col of blockData.blocks) {
      for (const material of col) {
        if (material && material !== 'minecraft:air') {
          loadTexture(material, onLoaded);
        }
      }
    }
  }, [blockData]);

  // Get the paste footprint (rotated) for rendering
  const pasteFootprint = templateDetail?.footprint
    ? rotateFootprint(templateDetail.footprint, pasteRotation)
    : null;

  const drawMap = useCallback(() => {
    const canvas = canvasRef.current;
    if (!canvas || !blockData?.blocks) return;
    const ctx = canvas.getContext('2d');
    const blocks = blockData.blocks;
    const w = blocks.length;
    const h = blocks[0]?.length || 0;

    canvas.width = canvasW;
    canvas.height = canvasH;
    ctx.imageSmoothingEnabled = false;

    const bpx = canvasW / w;
    const bpz = canvasH / h;

    for (let x = 0; x < w; x++) {
      for (let z = 0; z < h; z++) {
        const material = blocks[x][z];
        const cached = material ? textureImages.get(material) : null;
        if (cached instanceof HTMLImageElement) {
          ctx.drawImage(cached, x * bpx, z * bpz, bpx, bpz);
        } else {
          ctx.fillStyle = getBlockColor(material);
          ctx.fillRect(x * bpx, z * bpz, bpx, bpz);
        }
      }
    }

    const ox = blockData.x1 || 0;
    const oz = blockData.z1 || 0;

    if (blockData.entities) {
      for (const e of blockData.entities) {
        if (!e.location || e.type === 'minecraft:player') continue;
        const ex = e.location.x - ox;
        const ez = e.location.z - oz;
        if (ex < -0.5 || ex >= w + 0.5 || ez < -0.5 || ez >= h + 0.5) continue;
        const sz = Math.max(2, bpx * 0.6);
        ctx.fillStyle = getEntityColor(e.type);
        ctx.fillRect(ex * bpx - sz / 2, ez * bpz - sz / 2, sz, sz);
      }
    }

    // Draw paste preview overlay
    if (interactionMode === 'paste-preview' && pasteFootprint) {
      const pos = pastePosition || pasteMousePos;
      if (pos) {
        const fpDepth = pasteFootprint.length;
        const fpWidth = pasteFootprint[0]?.length || 0;
        const startX = pos.x - Math.floor(fpWidth / 2);
        const startZ = pos.z - Math.floor(fpDepth / 2);

        ctx.save();
        ctx.globalAlpha = 0.6;
        for (let fz = 0; fz < fpDepth; fz++) {
          for (let fx = 0; fx < fpWidth; fx++) {
            const mat = pasteFootprint[fz][fx];
            if (!mat) continue;
            const canvX = (startX + fx - ox) * bpx;
            const canvZ = (startZ + fz - oz) * bpz;
            if (canvX + bpx < 0 || canvX > canvasW || canvZ + bpz < 0 || canvZ > canvasH) continue;
            const cached = textureImages.get(mat);
            if (cached instanceof HTMLImageElement) {
              ctx.drawImage(cached, canvX, canvZ, bpx, bpz);
            } else {
              ctx.fillStyle = getBlockColor(mat);
              ctx.fillRect(canvX, canvZ, bpx, bpz);
            }
          }
        }
        ctx.globalAlpha = 1.0;
        // Draw border around paste region
        ctx.strokeStyle = pastePosition ? '#00FF00' : '#FFFF00';
        ctx.lineWidth = 2;
        ctx.setLineDash(pastePosition ? [] : [4, 4]);
        ctx.strokeRect(
          (startX - ox) * bpx,
          (startZ - oz) * bpz,
          fpWidth * bpx,
          fpDepth * bpz,
        );
        ctx.setLineDash([]);
        ctx.restore();
      }
    }

    if (players) {
      for (const p of players) {
        if (!p.location || p.location.world !== worldName) continue;
        const px = p.location.x - ox;
        const pz = p.location.z - oz;
        if (px < -0.5 || px >= w + 0.5 || pz < -0.5 || pz >= h + 0.5) continue;
        const cx = px * bpx;
        const cz = pz * bpz;
        const r = Math.max(3, bpx * 0.4);

        const isFollowed = p.uuid === followPlayer;
        const isSelected = p.uuid === selectedPlayer;
        const isTeleportTarget = teleportTarget?.uuid === p.uuid;
        const color = isTeleportTarget ? '#FF00FF' : isFollowed ? '#00FF00' : isSelected ? '#FFFFFF' : '#FF0000';
        ctx.fillStyle = color;
        ctx.beginPath();
        ctx.arc(cx, cz, r, 0, Math.PI * 2);
        ctx.fill();

        if (isFollowed || isSelected || isTeleportTarget) {
          ctx.strokeStyle = color;
          ctx.lineWidth = 2;
          ctx.beginPath();
          ctx.arc(cx, cz, r + 3, 0, Math.PI * 2);
          ctx.stroke();
        }

        if (p.location.yaw !== undefined) {
          drawFacingArrow(ctx, cx, cz, p.location.yaw, r + 6, isFollowed ? '#00FF00' : '#FFFFFF');
        }

        ctx.fillStyle = '#FFFFFF';
        ctx.strokeStyle = '#000000';
        ctx.lineWidth = 2;
        ctx.font = `bold ${Math.max(10, bpx * 0.5)}px sans-serif`;
        const label = p.name;
        const tx = cx + r + 4;
        const ty = cz + 4;
        ctx.strokeText(label, tx, ty);
        ctx.fillText(label, tx, ty);
      }
    }
  }, [blockData, players, worldName, canvasW, canvasH, texturesReady, followPlayer, teleportTarget, interactionMode, pasteFootprint, pastePosition, pasteMousePos]);

  useEffect(() => { drawMap(); }, [drawMap]);

  /* ── Drag-to-pan ── */
  const handleMouseDown = (e) => {
    if (!blockData) return;
    e.preventDefault();
    dragStartRef.current = { x: e.clientX, y: e.clientY };
    dragOriginOffset.current = { ...visualOffset };
  };

  // Stable refs for values needed in document event listeners
  const blockDataRef = useRef(blockData);
  blockDataRef.current = blockData;
  const centerXRef = useRef(centerX);
  centerXRef.current = centerX;
  const centerZRef = useRef(centerZ);
  centerZRef.current = centerZ;
  const effectiveZoomRef = useRef(effectiveZoom);
  effectiveZoomRef.current = effectiveZoom;
  const interactionModeRef = useRef(interactionMode);
  interactionModeRef.current = interactionMode;

  /** Convert a mouse event to world coordinates */
  const eventToWorldCoords = useCallback((e) => {
    const bd = blockDataRef.current;
    if (!bd?.blocks) return null;
    const canvas = canvasRef.current;
    if (!canvas) return null;
    const rect = canvas.getBoundingClientRect();
    const ez = effectiveZoomRef.current;
    const clickX = Math.floor((e.clientX - rect.left) / ez) + (bd.x1 || 0);
    const clickZ = Math.floor((e.clientY - rect.top) / ez) + (bd.z1 || 0);
    return { x: clickX, z: clickZ };
  }, []);

  /** Find a player near the given world coordinates */
  const findPlayerAt = useCallback((worldX, worldZ) => {
    if (!players) return null;
    for (const p of players) {
      if (!p.location || p.location.world !== worldName) continue;
      const dx = Math.floor(p.location.x) - worldX;
      const dz = Math.floor(p.location.z) - worldZ;
      if (Math.abs(dx) <= 2 && Math.abs(dz) <= 2) return p;
    }
    return null;
  }, [players, worldName]);

  const handleClick = useCallback((e) => {
    const coords = eventToWorldCoords(e);
    if (!coords) return;
    const mode = interactionModeRef.current;

    if (mode === 'teleport-pick-player') {
      const p = findPlayerAt(coords.x, coords.z);
      if (p) {
        setTeleportTarget({ uuid: p.uuid, name: p.name });
        setInteractionMode('teleport-pick-dest');
      }
      return;
    }

    if (mode === 'teleport-pick-dest') {
      // Teleport the target player to the clicked position using map height data
      const bd = blockDataRef.current;
      const bx = coords.x - (bd?.x1 || 0);
      const bz = coords.z - (bd?.z1 || 0);
      const clickY = (bd?.heights?.[bx]?.[bz] ?? yLevel) + 1;
      teleportPlayer.mutate({
        uuid: teleportTarget.uuid,
        world: worldName,
        x: coords.x,
        y: clickY,
        z: coords.z,
      });
      setInteractionMode('normal');
      setTeleportTarget(null);
      return;
    }

    if (mode === 'paste-preview') {
      // Click to anchor/finalize position — capture Y from block height data
      const bd = blockDataRef.current;
      const bx = coords.x - (bd?.x1 || 0);
      const bz = coords.z - (bd?.z1 || 0);
      const clickY = bd?.heights?.[bx]?.[bz] ?? yLevel;
      setPastePosition({ x: coords.x, y: clickY, z: coords.z });
      return;
    }

    // Normal mode: click player to toggle follow
    const p = findPlayerAt(coords.x, coords.z);
    if (p) {
      setFollowPlayer((prev) => prev === p.uuid ? null : p.uuid);
    }
  }, [eventToWorldCoords, findPlayerAt, worldName, teleportTarget, teleportPlayer, yLevel]);

  useEffect(() => {
    const onMove = (e) => {
      if (!dragStartRef.current) return;
      const dx = e.clientX - dragStartRef.current.x;
      const dy = e.clientY - dragStartRef.current.y;
      setVisualOffset({
        x: dragOriginOffset.current.x + dx,
        y: dragOriginOffset.current.y + dy,
      });
    };
    const onUp = (e) => {
      if (!dragStartRef.current) return;
      const dx = e.clientX - dragStartRef.current.x;
      const dy = e.clientY - dragStartRef.current.y;
      dragStartRef.current = null;

      if (Math.abs(dx) <= 3 && Math.abs(dy) <= 3) {
        handleClick(e);
        return;
      }

      // Convert pixel drag to block offset using effectiveZoom (pixels per block)
      const ez = effectiveZoomRef.current;
      const blocksDX = Math.round(dx / ez);
      const blocksDZ = Math.round(dy / ez);

      setFollowPlayer(null);
      setCenterXStr(String(centerXRef.current - blocksDX));
      setCenterZStr(String(centerZRef.current - blocksDZ));
    };

    document.addEventListener('mousemove', onMove);
    document.addEventListener('mouseup', onUp);
    return () => {
      document.removeEventListener('mousemove', onMove);
      document.removeEventListener('mouseup', onUp);
    };
  }, [handleClick]);

  /* ── Hover tooltip + paste preview position ── */
  const handleCanvasMouseMove = useCallback((e) => {
    if (dragStartRef.current) {
      setHoverInfo(null);
      return;
    }
    const bd = blockDataRef.current;
    if (!bd?.blocks) return;
    const canvas = canvasRef.current;
    if (!canvas) return;
    const rect = canvas.getBoundingClientRect();
    const ez = effectiveZoomRef.current;
    const bx = Math.floor((e.clientX - rect.left) / ez);
    const bz = Math.floor((e.clientY - rect.top) / ez);
    const blocks = bd.blocks;
    if (bx >= 0 && bx < blocks.length && bz >= 0 && bz < (blocks[0]?.length || 0)) {
      const worldX = bx + (bd.x1 || 0);
      const worldZ = bz + (bd.z1 || 0);
      const material = blocks[bx][bz] || 'minecraft:air';
      const blockY = bd.heights?.[bx]?.[bz] ?? bd.y;
      // Find entity at this position
      let entityName = null;
      if (bd.entities) {
        for (const ent of bd.entities) {
          if (!ent.location) continue;
          const ex = Math.floor(ent.location.x);
          const ez2 = Math.floor(ent.location.z);
          if (ex === worldX && ez2 === worldZ) {
            entityName = (ent.name || ent.type || '').replace('minecraft:', '');
            break;
          }
        }
      }
      setHoverInfo({
        material: material.replace('minecraft:', ''),
        x: worldX,
        y: blockY,
        z: worldZ,
        entityName,
        screenX: e.clientX,
        screenY: e.clientY,
      });
      // Update paste preview position when not anchored
      if (interactionModeRef.current === 'paste-preview' && !pastePosition) {
        setPasteMousePos({ x: worldX, z: worldZ });
      }
    } else {
      setHoverInfo(null);
    }
  }, [pastePosition]);

  const handleCanvasMouseLeave = useCallback(() => {
    setHoverInfo(null);
  }, []);

  /* ── Teleport mode toggle ── */
  const toggleTeleportMode = () => {
    if (interactionMode === 'teleport-pick-player' || interactionMode === 'teleport-pick-dest') {
      setInteractionMode('normal');
      setTeleportTarget(null);
    } else if ((selectedPlayer || followPlayer) && players) {
      // If a player is already selected/followed, skip to pick-destination
      const p = players.find((pl) => pl.uuid === (selectedPlayer || followPlayer));
      if (p) {
        setTeleportTarget({ uuid: p.uuid, name: p.name });
        setInteractionMode('teleport-pick-dest');
      } else {
        setInteractionMode('teleport-pick-player');
        setTeleportTarget(null);
      }
    } else {
      setInteractionMode('teleport-pick-player');
      setTeleportTarget(null);
    }
  };

  /* ── Paste mode ── */
  const openPasteDialog = () => {
    setPasteDialogOpen(true);
  };

  const selectTemplate = (name) => {
    setSelectedTemplateName(name);
    setPasteDialogOpen(false);
    setInteractionMode('paste-preview');
    setPastePosition(null);
    setPasteMousePos(null);
    setPasteRotation(0);
  };

  const cancelPaste = () => {
    setInteractionMode('normal');
    setSelectedTemplateName(null);
    setPastePosition(null);
    setPasteMousePos(null);
    setPasteRotation(0);
  };

  const confirmPaste = () => {
    if (!pastePosition || !selectedTemplateName || !worldName) return;
    pasteTemplate.mutate({
      worldName,
      template_name: selectedTemplateName,
      x: pastePosition.x,
      y: pastePosition.y,
      z: pastePosition.z,
      rotation: pasteRotation,
    });
    cancelPaste();
  };

  const followedName = followPlayer && players
    ? players.find((p) => p.uuid === followPlayer)?.name
    : null;
  const contextPlayer = selectedPlayer || followPlayer;
  const contextName = contextPlayer && players
    ? players.find((p) => p.uuid === contextPlayer)?.name
    : null;

  const worldList = worlds || [];

  // Determine cursor based on interaction mode
  let cursor = dragStartRef.current ? 'grabbing' : 'grab';
  if (interactionMode === 'teleport-pick-player') cursor = 'pointer';
  if (interactionMode === 'teleport-pick-dest') cursor = 'crosshair';
  if (interactionMode === 'paste-preview') cursor = pastePosition ? 'default' : 'crosshair';

  // Mode status message
  let modeLabel = null;
  if (interactionMode === 'teleport-pick-player') modeLabel = 'Click a player to teleport';
  if (interactionMode === 'teleport-pick-dest') modeLabel = `Click destination for ${teleportTarget?.name}`;
  if (interactionMode === 'paste-preview' && !pastePosition) modeLabel = `Placing ${selectedTemplateName} — click to position`;
  if (interactionMode === 'paste-preview' && pastePosition) modeLabel = `${selectedTemplateName} at (${pastePosition.x}, ${pastePosition.y}, ${pastePosition.z})`;

  return (
    <Card sx={{ display: 'flex', flexDirection: 'column', height: '100%' }}>
      <CardContent sx={{ display: 'flex', flexDirection: 'column', flexGrow: 1, overflow: 'hidden', pb: '8px !important' }}>
        <Typography variant="h5" gutterBottom>World Map</Typography>
        <Stack direction="row" spacing={2} sx={{ mb: 1, flexWrap: 'wrap', alignItems: 'center' }}>
          <FormControl size="small" sx={{ minWidth: 150 }}>
            <InputLabel>World</InputLabel>
            <Select value={worldName} label="World" onChange={(e) => setWorldName(e.target.value)}>
              {worldList.map((w) => (
                <MenuItem key={w.name} value={w.name}>{w.name}</MenuItem>
              ))}
            </Select>
          </FormControl>
          <TextField
            size="small" label="X" value={centerXStr}
            onChange={(e) => { setFollowPlayer(null); setCenterXStr(e.target.value); }}
            onWheel={(e) => { e.preventDefault(); setFollowPlayer(null); setCenterXStr((v) => String(Math.round(parseFloat(v) || 0) + (e.deltaY < 0 ? 5 : -5))); }}
            sx={{ width: 80 }}
            inputProps={{ inputMode: 'numeric', pattern: '-?[0-9]*' }}
          />
          <TextField
            size="small" label="Y" value={yLevelStr}
            onChange={(e) => setYLevelStr(e.target.value)}
            onWheel={(e) => { e.preventDefault(); setYLevelStr((v) => String(Math.round(parseFloat(v) || 0) + (e.deltaY < 0 ? 5 : -5))); }}
            sx={{ width: 80 }}
            inputProps={{ inputMode: 'numeric', pattern: '-?[0-9]*' }}
          />
          <TextField
            size="small" label="Z" value={centerZStr}
            onChange={(e) => { setFollowPlayer(null); setCenterZStr(e.target.value); }}
            onWheel={(e) => { e.preventDefault(); setFollowPlayer(null); setCenterZStr((v) => String(Math.round(parseFloat(v) || 0) + (e.deltaY < 0 ? 5 : -5))); }}
            sx={{ width: 80 }}
            inputProps={{ inputMode: 'numeric', pattern: '-?[0-9]*' }}
          />
          <Tooltip title={`Zoom: ${effectiveZoom}px (${blocksW}x${blocksH})`}>
            <IconButton size="small" onClick={(e) => setZoomAnchorEl(zoomAnchorEl ? null : e.currentTarget)}>
              <ZoomInIcon />
            </IconButton>
          </Tooltip>
          <Popper open={!!zoomAnchorEl} anchorEl={zoomAnchorEl} placement="bottom" sx={{ zIndex: 1300 }}>
            <ClickAwayListener onClickAway={() => setZoomAnchorEl(null)}>
              <Paper sx={{ p: 1.5, width: 180 }}>
                <Typography variant="caption">Zoom: {effectiveZoom}px ({blocksW}&times;{blocksH})</Typography>
                <Slider
                  value={zoom} min={minZoom} max={32} size="small"
                  onChange={(_, v) => setZoom(v)}
                />
              </Paper>
            </ClickAwayListener>
          </Popper>

          {/* Teleport button */}
          <Tooltip title="Teleport: click player, then click destination">
            <IconButton
              size="small"
              onClick={toggleTeleportMode}
              color={interactionMode.startsWith('teleport') ? 'primary' : 'default'}
            >
              <GpsFixedIcon />
            </IconButton>
          </Tooltip>

          {/* Paste button */}
          <Tooltip title="Paste template onto map">
            <IconButton
              size="small"
              onClick={interactionMode === 'paste-preview' ? cancelPaste : openPasteDialog}
              color={interactionMode === 'paste-preview' ? 'primary' : 'default'}
            >
              <ContentPasteIcon />
            </IconButton>
          </Tooltip>

          {/* Mode indicator */}
          {modeLabel && (
            <Chip
              label={modeLabel}
              color={interactionMode.startsWith('teleport') ? 'secondary' : 'warning'}
              size="small"
              onDelete={() => {
                setInteractionMode('normal');
                setTeleportTarget(null);
                cancelPaste();
              }}
            />
          )}

          {/* Paste controls (when in paste-preview with anchored position) */}
          {interactionMode === 'paste-preview' && (
            <Stack direction="row" spacing={0.5} alignItems="center">
              <Tooltip title="Rotate 90° clockwise">
                <IconButton size="small" onClick={() => setPasteRotation((r) => (r + 1) % 4)}>
                  <RotateRightIcon fontSize="small" />
                </IconButton>
              </Tooltip>
              <Typography variant="caption" sx={{ minWidth: 20, textAlign: 'center' }}>
                {pasteRotation * 90}°
              </Typography>
              {pastePosition && (
                <>
                  <Button size="small" variant="contained" color="success" onClick={confirmPaste} sx={{ minWidth: 0 }}>
                    Paste
                  </Button>
                  <Button size="small" variant="outlined" onClick={() => setPastePosition(null)} sx={{ minWidth: 0 }}>
                    Reposition
                  </Button>
                </>
              )}
              <Button size="small" variant="outlined" color="error" onClick={cancelPaste} sx={{ minWidth: 0 }}>
                Cancel
              </Button>
            </Stack>
          )}

          {/* Map search */}
          <Box sx={{ position: 'relative' }} ref={searchAnchorRef}>
            <TextField
              size="small"
              placeholder="Search map..."
              value={searchText}
              onChange={(e) => { setSearchText(e.target.value); setSearchOpen(true); }}
              onFocus={() => { if (searchText.length >= 2) setSearchOpen(true); }}
              sx={{ width: 180 }}
              InputProps={{
                startAdornment: (
                  <InputAdornment position="start"><SearchIcon fontSize="small" /></InputAdornment>
                ),
                endAdornment: searchText ? (
                  <InputAdornment position="end">
                    <IconButton size="small" onClick={() => { setSearchText(''); setSearchOpen(false); }}>
                      <CloseIcon fontSize="small" />
                    </IconButton>
                  </InputAdornment>
                ) : null,
              }}
            />
            <Popper
              open={searchOpen && !!searchResults?.results?.length}
              anchorEl={searchAnchorRef.current}
              placement="bottom-start"
              sx={{ zIndex: 1300 }}
            >
              <ClickAwayListener onClickAway={() => setSearchOpen(false)}>
                <Paper sx={{ maxHeight: 300, overflow: 'auto', minWidth: 280, mt: 0.5 }}>
                  <List dense>
                    {searchResults?.results?.map((r, i) => {
                      const dist = r.location
                        ? Math.round(Math.sqrt((r.location.x - centerX) ** 2 + (r.location.z - centerZ) ** 2))
                        : null;
                      return (
                        <ListItem key={i} disablePadding>
                          <ListItemButton onClick={() => {
                            if (r.location) {
                              setCenterXStr(String(Math.round(r.location.x)));
                              setCenterZStr(String(Math.round(r.location.z)));
                              if (r.location.y) setYLevel(Math.round(r.location.y));
                              setFollowPlayer(null);
                            }
                            setSearchOpen(false);
                          }}>
                            <ListItemText
                              primary={`${r.name}${r.count > 1 ? ` (x${r.count})` : ''}`}
                              secondary={`${r.type}${dist != null ? ` — ${dist} blocks away` : ''}`}
                            />
                          </ListItemButton>
                        </ListItem>
                      );
                    })}
                  </List>
                </Paper>
              </ClickAwayListener>
            </Popper>
          </Box>

          {followedName && (
            <Chip
              label={`Following ${followedName}`}
              color="success"
              size="small"
              onDelete={() => setFollowPlayer(null)}
            />
          )}
        </Stack>
        {/* Map + player sidebar */}
        <Box sx={{ display: 'flex', flexGrow: 1, minHeight: 200, overflow: 'hidden', gap: 0.5 }}>
        {/* Map container */}
        <Box
          ref={containerRef}
          sx={{
            flexGrow: 1,
            position: 'relative',
            overflow: 'hidden',
            border: '1px solid rgba(255,255,255,0.1)',
          }}
        >
          {isLoading && (
            <Box sx={{ position: 'absolute', top: '50%', left: '50%', transform: 'translate(-50%,-50%)', zIndex: 1 }}>
              <CircularProgress />
            </Box>
          )}
          <canvas
            ref={canvasRef}
            onMouseDown={handleMouseDown}
            onMouseMove={handleCanvasMouseMove}
            onMouseLeave={handleCanvasMouseLeave}
            style={{
              cursor,
              display: 'block',
              transform: (visualOffset.x || visualOffset.y)
                ? `translate(${visualOffset.x}px, ${visualOffset.y}px)`
                : undefined,
              userSelect: 'none',
            }}
          />
          {hoverInfo && (
            <Box
              sx={{
                position: 'fixed',
                left: hoverInfo.screenX + 12,
                top: hoverInfo.screenY - 8,
                bgcolor: 'rgba(0,0,0,0.85)',
                color: '#fff',
                px: 1,
                py: 0.5,
                borderRadius: 0.5,
                fontSize: 11,
                fontFamily: 'monospace',
                pointerEvents: 'none',
                zIndex: 1000,
                whiteSpace: 'nowrap',
              }}
            >
              <div>{hoverInfo.material} ({hoverInfo.x}, {hoverInfo.y}, {hoverInfo.z})</div>
              {hoverInfo.entityName && <div style={{ color: '#ffcc00' }}>{hoverInfo.entityName}</div>}
            </Box>
          )}
        </Box>
        {/* Player sidebar */}
        {players?.length > 0 && (
          <Box sx={{
            width: 200,
            flexShrink: 0,
            overflow: 'auto',
            borderLeft: '1px solid rgba(255,255,255,0.1)',
            pl: 0.5,
          }}>
            <Typography variant="caption" sx={{ fontWeight: 'bold', display: 'block', mb: 0.5 }}>Players</Typography>
            <Stack spacing={0.25}>
              {players.filter((p) => p.location?.world === worldName).map((p) => (
                <Box key={p.uuid} sx={{ display: 'flex', alignItems: 'center', gap: 0.25 }}>
                  <Typography
                    variant="body2"
                    noWrap
                    sx={{
                      flex: 1,
                      cursor: 'pointer',
                      fontWeight: selectedPlayer === p.uuid ? 'bold' : 'normal',
                      color: interactionMode === 'teleport-pick-player' ? 'secondary.main' : 'text.primary',
                      '&:hover': { textDecoration: 'underline' },
                      fontSize: 13,
                    }}
                    onClick={() => {
                      if (interactionMode === 'teleport-pick-player') {
                        setTeleportTarget({ uuid: p.uuid, name: p.name });
                        setInteractionMode('teleport-pick-dest');
                      } else {
                        setSelectedPlayer((prev) => prev === p.uuid ? null : p.uuid);
                        setCenterXStr(String(Math.round(p.location.x)));
                        setCenterZStr(String(Math.round(p.location.z)));
                        setYLevelStr(String(Math.round(p.location.y)));
                      }
                    }}
                  >
                    {p.name}
                  </Typography>
                  <Tooltip title={followPlayer === p.uuid ? 'Stop following' : 'Follow'}>
                    <IconButton
                      size="small"
                      color={followPlayer === p.uuid ? 'success' : 'default'}
                      onClick={() => setFollowPlayer((prev) => prev === p.uuid ? null : p.uuid)}
                      sx={{ p: 0.25 }}
                    >
                      <VisibilityIcon sx={{ fontSize: 16 }} />
                    </IconButton>
                  </Tooltip>
                  <Tooltip title="Details">
                    <IconButton
                      size="small"
                      color={examinePlayer === p.uuid ? 'info' : 'default'}
                      onClick={(e) => {
                        examineAnchorRef.current = e.currentTarget;
                        setExaminePlayer((prev) => prev === p.uuid ? null : p.uuid);
                      }}
                      sx={{ p: 0.25 }}
                    >
                      <InfoOutlinedIcon sx={{ fontSize: 16 }} />
                    </IconButton>
                  </Tooltip>
                </Box>
              ))}
            </Stack>
          </Box>
        )}
        {/* Player detail popover */}
        <Popper
          open={!!examinePlayer}
          anchorEl={examineAnchorRef.current}
          placement="left-start"
          sx={{ zIndex: 1300 }}
        >
          <ClickAwayListener onClickAway={() => setExaminePlayer(null)}>
            <Paper sx={{ width: 450, maxHeight: '70vh', overflow: 'auto', p: 1 }}>
              <Box sx={{ display: 'flex', justifyContent: 'flex-end', mb: -1 }}>
                <IconButton size="small" onClick={() => setExaminePlayer(null)}>
                  <CloseIcon fontSize="small" />
                </IconButton>
              </Box>
              {examinePlayer && (
                <PlayerDetail uuid={examinePlayer} />
              )}
            </Paper>
          </ClickAwayListener>
        </Popper>
        </Box>
        {/* Inline code editor */}
        <Box sx={{ mt: 0.5, display: 'flex', gap: 0.5, alignItems: 'center' }}>
          <Typography variant="caption" sx={{ opacity: 0.6, whiteSpace: 'nowrap', minWidth: 'fit-content' }}>
            {contextName ? `[${contextName}]` : '[server]'}
          </Typography>
          <TextField
            fullWidth
            size="small"
            value={evalCode}
            onChange={(e) => setEvalCode(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === 'Enter') {
                e.preventDefault();
                if (!evalCode.trim()) return;
                let context;
                if (contextPlayer && contextName) {
                  const cp = players?.find((p) => p.uuid === contextPlayer);
                  const parsed = parseLocation(cp?.location);
                  const pos = parsed ? ` at (${parsed.x.toFixed(1)}, ${parsed.y.toFixed(1)}, ${parsed.z.toFixed(1)}) in ${parsed.world}` : '';
                  context = `Player: ${cp?.display_name || contextName}${pos}`;
                } else {
                  context = `Map center: (${centerX.toFixed(1)}, ${yLevel}, ${centerZ.toFixed(1)}) in ${worldName}`;
                }
                const entry = { code: evalCode.trim(), timestamp: Date.now(), context };
                evalMutation.mutate(
                  {
                    code: evalCode.trim(),
                    player_uuid: contextPlayer || undefined,
                    map_context: !contextPlayer ? { x: centerX, y: yLevel, z: centerZ, world: worldName } : undefined,
                  },
                  {
                    onSuccess: (data) => {
                      setEvalHistory((prev) => [{ ...entry, result: data.result, output: data.output, error: data.error, traceback: data.traceback }, ...prev]);
                    },
                    onError: (err) => {
                      setEvalHistory((prev) => [{ ...entry, error: err.message }, ...prev]);
                    },
                  }
                );
                setEvalCode('');
                setEvalHistoryIdx(-1);
              } else if (e.key === 'ArrowUp') {
                e.preventDefault();
                if (evalHistory.length > 0) {
                  const newIdx = Math.min(evalHistoryIdx + 1, evalHistory.length - 1);
                  setEvalHistoryIdx(newIdx);
                  setEvalCode(evalHistory[newIdx].code);
                }
              } else if (e.key === 'ArrowDown') {
                e.preventDefault();
                if (evalHistoryIdx > 0) {
                  const newIdx = evalHistoryIdx - 1;
                  setEvalHistoryIdx(newIdx);
                  setEvalCode(evalHistory[newIdx].code);
                } else if (evalHistoryIdx === 0) {
                  setEvalHistoryIdx(-1);
                  setEvalCode('');
                }
              }
            }}
            placeholder="Python expression... Enter to run"
            sx={{
              '& .MuiInputBase-input': { fontFamily: 'monospace', fontSize: 13, py: 0.5 },
              '& .MuiInputBase-root': { py: 0 },
            }}
          />
        </Box>
        {evalHistory.length > 0 && (
          <Box sx={{ maxHeight: 120, overflow: 'auto', mt: 0.5 }}>
            {evalHistory.slice(0, 5).map((entry, i) => (
              <Box key={i} sx={{ fontFamily: 'monospace', fontSize: 11, lineHeight: 1.4, px: 0.5 }}>
                <span style={{ color: '#90caf9' }}>&gt;&gt;&gt; {entry.code}</span>
                {entry.error ? (
                  <span
                    style={{ color: '#f44336', marginLeft: 8, cursor: entry.traceback ? 'pointer' : 'default' }}
                    onClick={() => entry.traceback && setTracebackEntry({ error: entry.error, traceback: entry.traceback, code: entry.code, context: entry.context })}
                    title={entry.traceback ? 'Click for traceback' : undefined}
                  >
                    {String(entry.error)}{entry.traceback && ' ↗'}
                  </span>
                ) : (
                  <>
                    {entry.output && <span style={{ color: '#aaa', marginLeft: 8 }}>{entry.output}</span>}
                    <span style={{ color: '#a5d6a7', marginLeft: 8 }}>
                      {entry.result != null ? JSON.stringify(entry.result) : 'None'}
                    </span>
                  </>
                )}
              </Box>
            ))}
          </Box>
        )}
        {blockData && (
          <Typography variant="caption" component="div" sx={{ mt: 0.5, opacity: 0.7, fontFamily: 'monospace', fontSize: 11 }}>
            Y={blockData.y} region=[{blockData.x1},{blockData.z1}]-[{blockData.x2},{blockData.z2}]
            {blockData.entities?.length > 0 && ` | ${blockData.entities.length} entities`}
            {' | '}
            {Object.entries(countMaterials(blockData.blocks))
              .sort((a, b) => b[1] - a[1])
              .slice(0, 8)
              .map(([m, c]) => `${m.replace('minecraft:', '')}:${c}`)
              .join(', ')}
          </Typography>
        )}
        <Typography variant="caption" component="div" sx={{ mt: 0.5, opacity: 0.5, fontSize: 10 }}>
          Textures:{' '}
          <Link href="https://faithfulpack.net/" target="_blank" rel="noopener noreferrer" sx={{ fontSize: 'inherit', opacity: 0.8 }}>
            Faithful 32x
          </Link>
          {' '}by the Faithful team, used under the{' '}
          <Link href="https://faithfulpack.net/license" target="_blank" rel="noopener noreferrer" sx={{ fontSize: 'inherit', opacity: 0.8 }}>
            Faithful License
          </Link>
          {' | Drag to pan, click a player to follow'}
        </Typography>
      </CardContent>

      {/* Template selection dialog */}
      <Dialog
        open={pasteDialogOpen}
        onClose={() => setPasteDialogOpen(false)}
        maxWidth="sm"
        fullWidth
      >
        <DialogTitle sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          Select Template
          <IconButton size="small" onClick={() => setPasteDialogOpen(false)}>
            <CloseIcon />
          </IconButton>
        </DialogTitle>
        <DialogContent sx={{ p: 0 }}>
          <List dense>
            {templates?.map((t) => (
              <ListItem key={t.name} disablePadding>
                <ListItemButton onClick={() => selectTemplate(t.name)}>
                  <ListItemText
                    primary={t.name}
                    secondary={`${t.width}x${t.depth}x${t.height}${t.author ? ` by ${t.author}` : ''}${t.description ? ` — ${t.description}` : ''}`}
                  />
                </ListItemButton>
              </ListItem>
            ))}
            {(!templates || templates.length === 0) && (
              <ListItem>
                <ListItemText primary="No templates available" secondary="Use the copy command in-game to create templates" />
              </ListItem>
            )}
          </List>
        </DialogContent>
      </Dialog>
      <TracebackDialog
        open={!!tracebackEntry}
        onClose={() => setTracebackEntry(null)}
        error={tracebackEntry?.error}
        traceback={tracebackEntry?.traceback}
        code={tracebackEntry?.code}
        context={tracebackEntry?.context}
      />
    </Card>
  );
}
