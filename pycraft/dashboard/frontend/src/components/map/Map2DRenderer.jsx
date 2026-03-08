import { useRef, useEffect, useCallback } from 'react';

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
export const textureImages = new Map();

export function getTextureUrl(material) {
  const name = material.startsWith('minecraft:') ? material.slice(10) : material;
  return `/api/textures/${name}.png`;
}

export function loadTexture(material, onLoaded) {
  if (textureImages.has(material)) return;
  textureImages.set(material, 'loading');
  const img = new Image();
  img.onload = () => { textureImages.set(material, img); onLoaded(); };
  img.onerror = () => { textureImages.set(material, 'failed'); onLoaded(); };
  img.src = getTextureUrl(material);
}

const ENTITY_COLORS = {
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

/**
 * Map2DRenderer — the 2D canvas-based top-down map.
 *
 * Props:
 *   blockData        — server block response { blocks, heights, entities, x1, z1 }
 *   players          — online player list
 *   worldName        — current world name
 *   canvasW / canvasH — canvas pixel dimensions
 *   effectiveZoom    — pixels per block (for coordinate hit-testing)
 *   followPlayer     — UUID of followed player
 *   selectedPlayer   — UUID of selected player
 *   teleportTarget   — { uuid, name } or null
 *   interactionMode  — 'normal' | 'teleport-pick-player' | 'teleport-pick-dest' | 'paste-preview'
 *   pasteFootprint   — rotated footprint grid [[mat,...],...]
 *   pastePosition    — anchored { x, z } or null
 *   pasteMousePos    — hover { x, z } or null
 *   cursor           — CSS cursor string
 *   visualOffset     — { x, y } CSS translate for drag pan
 *   texturesReady    — incrementing counter to trigger redraws when textures load
 *   onMouseDown / onMouseMove / onMouseLeave — forwarded to the canvas element
 */
export default function Map2DRenderer({
  blockData, players, worldName,
  canvasW, canvasH, effectiveZoom,
  followPlayer, selectedPlayer, teleportTarget,
  interactionMode, pasteFootprint, pastePosition, pasteMousePos,
  cursor, visualOffset, texturesReady,
  onMouseDown, onMouseMove, onMouseLeave,
}) {
  const canvasRef = useRef(null);

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
  }, [blockData, players, worldName, canvasW, canvasH, texturesReady, followPlayer, selectedPlayer, teleportTarget, interactionMode, pasteFootprint, pastePosition, pasteMousePos]); // eslint-disable-line react-hooks/exhaustive-deps

  useEffect(() => { drawMap(); }, [drawMap]);

  return (
    <canvas
      ref={canvasRef}
      onMouseDown={onMouseDown}
      onMouseMove={onMouseMove}
      onMouseLeave={onMouseLeave}
      style={{
        cursor,
        display: 'block',
        transform: (visualOffset.x || visualOffset.y)
          ? `translate(${visualOffset.x}px, ${visualOffset.y}px)`
          : undefined,
        userSelect: 'none',
      }}
    />
  );
}
