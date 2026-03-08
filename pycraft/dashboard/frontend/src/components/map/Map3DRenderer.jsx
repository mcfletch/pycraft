import { useRef, useEffect } from 'react';
import * as THREE from 'three';

/* ── Three.js texture cache (shared, session-persistent) ── */
const threeTopCache = new Map();
const threeSideCache = new Map();

function loadThreeTexture(url, cache, key) {
  if (cache.has(key)) return cache.get(key);
  const loader = new THREE.TextureLoader();
  const tex = loader.load(url);
  tex.magFilter = THREE.NearestFilter;
  tex.minFilter = THREE.NearestFilter;
  tex.colorSpace = THREE.SRGBColorSpace;
  cache.set(key, tex);
  return tex;
}

function getTopTexture(material) {
  const name = material.startsWith('minecraft:') ? material.slice(10) : material;
  return loadThreeTexture(`/api/textures/${name}.png`, threeTopCache, material);
}

function getSideTexture(material) {
  const name = material.startsWith('minecraft:') ? material.slice(10) : material;
  return loadThreeTexture(`/api/textures/side/${name}.png`, threeSideCache, material);
}

const AIR_MATERIALS = new Set(['minecraft:air', 'minecraft:cave_air', 'minecraft:void_air']);

const FOV = 60;
const HALF_FOV_RAD = (FOV / 2) * Math.PI / 180;

/** Camera distance so blocksH world-units fill the vertical FOV looking straight down. */
function camDist(blocksH) {
  return (blocksH / 2) / Math.tan(HALF_FOV_RAD);
}

/**
 * Map3DRenderer — perspective top-down 3D map.
 *
 * Camera points straight down (90°), north (-Z) at the top of the screen.
 * Three lights give depth cues at block edges without tilting the view:
 *
 *   • AmbientLight (white, high)  — keeps top faces true-to-texture, like 2D
 *   • DirectionalLight (reddish)  — comes from the lower-right (SE), tints the
 *     east- and south-facing sides of elevated blocks
 *   • DirectionalLight (bluish)   — comes from the upper-left (NW), tints the
 *     west- and north-facing sides
 *
 * Materials are MeshLambertMaterial so the lights actually affect them.
 * Block positions: (worldX−cx, worldY−queryY, worldZ−cz) so the scene is
 * always centred on the current map position.
 */
export default function Map3DRenderer({
  blockData, players, worldName,
  containerW, containerH, blocksW, blocksH,
  followPlayer, selectedPlayer, teleportTarget,
  cursor,
  onMouseDown, onMouseMove, onMouseLeave,
}) {
  const mountRef = useRef(null);
  const stateRef = useRef(null);

  /* ── Bootstrap Three.js once ── */
  useEffect(() => {
    const mount = mountRef.current;
    if (!mount) return;

    const renderer = new THREE.WebGLRenderer({ antialias: false, alpha: false });
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.setSize(containerW, containerH);
    mount.appendChild(renderer.domElement);

    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0x111111);

    // Perspective camera straight down.
    // up=(0,0,-1) → north (-Z) at top of screen, east (+X) at right.
    const camera = new THREE.PerspectiveCamera(FOV, containerW / containerH, 0.1, 5000);
    const dist = camDist(blocksH);
    camera.up.set(0, 0, -1);  // must be set BEFORE lookAt to avoid degenerate matrix
    camera.position.set(0, dist, 0);
    camera.lookAt(0, 0, 0);

    // ── Lighting ──────────────────────────────────────────────────────────────
    // Ambient: high so top faces look like the 2D flat map.
    const ambient = new THREE.AmbientLight(0xffffff, 0.75);

    // Reddish from the lower-right (SE corner when north is up):
    // position (1.5, 1, 1.5) → light comes from +X/+Z side → illuminates
    // east- (+X) and south-facing (+Z) sides of raised blocks.
    const redLight = new THREE.DirectionalLight(0xff6644, 0.65);
    redLight.position.set(1.5, 1, 1.5);

    // Bluish from the upper-left (NW corner):
    // illuminates west- (−X) and north-facing (−Z) sides.
    const blueLight = new THREE.DirectionalLight(0x4466ff, 0.65);
    blueLight.position.set(-1.5, 1, -1.5);

    scene.add(ambient, redLight, blueLight);
    // ─────────────────────────────────────────────────────────────────────────

    const blockGroup = new THREE.Group();
    const playerGroup = new THREE.Group();
    scene.add(blockGroup, playerGroup);

    let animId;
    function animate() {
      animId = requestAnimationFrame(animate);
      renderer.render(scene, camera);
    }
    animate();

    stateRef.current = { renderer, scene, camera, blockGroup, playerGroup };

    return () => {
      cancelAnimationFrame(animId);
      renderer.dispose();
      if (mount.contains(renderer.domElement)) mount.removeChild(renderer.domElement);
      stateRef.current = null;
    };
  }, []); // eslint-disable-line react-hooks/exhaustive-deps

  /* ── Resize / zoom ── */
  useEffect(() => {
    const s = stateRef.current;
    if (!s) return;
    const { renderer, camera } = s;
    renderer.setSize(containerW, containerH);
    camera.aspect = containerW / containerH;
    camera.position.set(0, camDist(blocksH), 0);
    camera.lookAt(0, 0, 0);
    camera.updateProjectionMatrix();
  }, [containerW, containerH, blocksW, blocksH]);

  /* ── Rebuild block meshes when blockData changes ── */
  useEffect(() => {
    const s = stateRef.current;
    if (!s || !blockData?.blocks) return;
    const { blockGroup } = s;

    while (blockGroup.children.length) {
      const mesh = blockGroup.children[0];
      blockGroup.remove(mesh);
      mesh.geometry?.dispose();
      if (Array.isArray(mesh.material)) mesh.material.forEach((m) => m.dispose());
      else mesh.material?.dispose();
    }

    const blocks = blockData.blocks;
    const heights = blockData.heights;
    const x1 = blockData.x1 || 0;
    const z1 = blockData.z1 || 0;
    const queryY = blockData.y || 64;
    const w = blocks.length;
    const h = blocks[0]?.length || 0;
    const cx = x1 + w / 2;
    const cz = z1 + h / 2;

    // Group by material for InstancedMesh batching.
    const groups = new Map();
    for (let x = 0; x < w; x++) {
      for (let z = 0; z < h; z++) {
        const mat = blocks[x][z];
        if (!mat || AIR_MATERIALS.has(mat)) continue;
        if (!groups.has(mat)) groups.set(mat, []);
        const worldY = heights?.[x]?.[z] ?? queryY;
        groups.get(mat).push({
          relX: x + x1 - cx,
          relY: worldY - queryY,
          relZ: z + z1 - cz,
        });
      }
    }

    // BoxGeometry face order: [+X, -X, +Y(top), -Y(bottom), +Z, -Z]
    const boxGeo = new THREE.BoxGeometry(1, 1, 1);
    const dummy = new THREE.Object3D();

    for (const [material, cells] of groups) {
      const topTex  = getTopTexture(material);
      const sideTex = getSideTexture(material);

      // MeshLambertMaterial responds to scene lights — required for depth cues.
      const topMat  = new THREE.MeshLambertMaterial({ map: topTex });
      const sideMat = new THREE.MeshLambertMaterial({ map: sideTex });
      // [+X, -X, +Y(top), -Y(bottom), +Z, -Z]
      const materials = [sideMat, sideMat, topMat, sideMat, sideMat, sideMat];

      const mesh = new THREE.InstancedMesh(boxGeo, materials, cells.length);
      mesh.frustumCulled = false;

      cells.forEach(({ relX, relY, relZ }, i) => {
        dummy.position.set(relX, relY, relZ);
        dummy.updateMatrix();
        mesh.setMatrixAt(i, dummy.matrix);
      });
      mesh.instanceMatrix.needsUpdate = true;
      blockGroup.add(mesh);
    }
  }, [blockData]); // eslint-disable-line react-hooks/exhaustive-deps

  /* ── Player markers ── */
  useEffect(() => {
    const s = stateRef.current;
    if (!s) return;
    const { playerGroup } = s;

    while (playerGroup.children.length) {
      const m = playerGroup.children[0];
      playerGroup.remove(m);
      m.geometry?.dispose();
      m.material?.dispose();
    }

    if (!players || !blockData) return;
    const x1 = blockData.x1 || 0;
    const z1 = blockData.z1 || 0;
    const queryY = blockData.y || 64;
    const w = blockData.blocks?.length || 0;
    const h = blockData.blocks?.[0]?.length || 0;
    const cx = x1 + w / 2;
    const cz = z1 + h / 2;

    const markerGeo = new THREE.SphereGeometry(0.6, 8, 8);

    for (const p of players) {
      if (!p.location || p.location.world !== worldName) continue;
      const isFollowed = p.uuid === followPlayer;
      const isSelected = p.uuid === selectedPlayer;
      const isTeleportTarget = teleportTarget?.uuid === p.uuid;
      const color = isTeleportTarget ? 0xFF00FF : isFollowed ? 0x00FF00 : isSelected ? 0xFFFFFF : 0xFF0000;

      const marker = new THREE.Mesh(
        markerGeo,
        new THREE.MeshBasicMaterial({ color, depthTest: false }),
      );
      marker.position.set(
        p.location.x - cx,
        p.location.y - queryY + 2,
        p.location.z - cz,
      );
      marker.renderOrder = 999;
      playerGroup.add(marker);
    }
  }, [players, blockData, worldName, followPlayer, selectedPlayer, teleportTarget]);

  return (
    <div
      ref={mountRef}
      onMouseDown={onMouseDown}
      onMouseMove={onMouseMove}
      onMouseLeave={onMouseLeave}
      style={{ width: containerW, height: containerH, cursor, display: 'block' }}
    />
  );
}
