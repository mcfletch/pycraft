"""Texture pack provider — downloads Faithful 32x on first use, serves PNGs from ZIP at runtime."""
import io
import logging
import os
import pathlib
import zipfile

from aiohttp import web

log = logging.getLogger(__name__)

FAITHFUL_URL = (
    "https://database.faithfulpack.net/packs/32x-Java/"
    "December%202025/Faithful%2032x%20-%201.21.11.zip"
)
CACHE_DIR = pathlib.Path(os.environ.get("PYCRAFT_CACHE", pathlib.Path.home() / ".cache" / "pycraft"))
ZIP_PATH = CACHE_DIR / "faithful-32x-1.21.11.zip"
BLOCK_PREFIX = "assets/minecraft/textures/block/"
ITEM_PREFIX = "assets/minecraft/textures/item/"
SLOT_PREFIX = "assets/minecraft/textures/gui/sprites/container/slot/"

# Singleton — opened once on first request
_zip_file: zipfile.ZipFile | None = None
_block_index: dict[str, str] | None = None  # bare name → zip entry path
_item_index: dict[str, str] | None = None   # bare name → zip entry path
_slot_index: dict[str, str] | None = None  # bare name → zip entry path (GUI slot icons)
_tinted_cache: dict[str, bytes] = {}  # material → tinted PNG bytes
PROCESSED_DIR = CACHE_DIR / "textures_processed"

# Blocks whose textures are greyscale and need biome-color tinting.
# Tint color is approximate plains biome grass/foliage color.
GRASS_TINT = (124, 189, 107)  # #7CBD6B — plains grass
FOLIAGE_TINT = (87, 162, 63)  # #57A23F — plains foliage
WATER_TINT = (63, 118, 228)   # #3F76E4 — plains water
ICE_TINT = (160, 200, 255)    # light blue tint for ice blocks
LEAF_LITTER_TINT = (139, 105, 61)  # brown tint for leaf litter
TINT_MAP = {}
for _name in (
    'grass_block_top', 'short_grass', 'tall_grass_top', 'tall_grass_bottom',
    'fern', 'large_fern_top', 'large_fern_bottom',
):
    TINT_MAP[_name] = GRASS_TINT
for _name in (
    'oak_leaves', 'birch_leaves', 'spruce_leaves', 'jungle_leaves',
    'acacia_leaves', 'dark_oak_leaves', 'mangrove_leaves', 'vine',
):
    TINT_MAP[_name] = FOLIAGE_TINT
for _name in ('water_still', 'water_flow'):
    TINT_MAP[_name] = WATER_TINT
for _name in ('ice', 'packed_ice', 'blue_ice', 'frosted_ice_0', 'frosted_ice_1', 'frosted_ice_2', 'frosted_ice_3'):
    TINT_MAP[_name] = ICE_TINT
for _name in ('leaf_litter',):
    TINT_MAP[_name] = LEAF_LITTER_TINT

# Suffixes stripped to find the base material texture (e.g. oak_slab → oak → oak_planks)
_VARIANT_SUFFIXES = (
    '_slab', '_stairs', '_fence', '_fence_gate', '_wall',
    '_button', '_pressure_plate', '_sign', '_wall_sign',
    '_hanging_sign', '_wall_hanging_sign',
    '_door', '_trapdoor',
)

# Explicit block → texture name overrides
_TEXTURE_ALIASES = {
    'farmland': 'dirt',
    'grass_path': 'dirt',
    'dirt_path': 'dirt',
    'podzol': 'podzol_top',
    'mycelium': 'mycelium_top',
    'snow': 'snow',
    'snow_block': 'snow',
}

# Wood type bases: stripping a variant suffix yields e.g. "oak" but the
# texture file is "oak_planks"
_PLANKS_BASES = {
    'oak', 'birch', 'spruce', 'jungle', 'acacia', 'dark_oak',
    'mangrove', 'cherry', 'bamboo', 'crimson', 'warped', 'pale_oak',
}


def _ensure_downloaded():
    """Download the texture pack ZIP if not already cached."""
    if ZIP_PATH.exists():
        return
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    log.info("Downloading Faithful 32x texture pack to %s ...", ZIP_PATH)
    import urllib.request
    tmp = ZIP_PATH.with_suffix(".tmp")
    req = urllib.request.Request(FAITHFUL_URL, headers={"User-Agent": "pycraft-dashboard/1.0"})
    with urllib.request.urlopen(req) as resp, open(tmp, "wb") as f:
        f.write(resp.read())
    tmp.rename(ZIP_PATH)
    log.info("Texture pack downloaded (%d KB)", ZIP_PATH.stat().st_size // 1024)


def _open_zip():
    """Open the ZIP file and build name → path indexes for block and item textures."""
    global _zip_file, _block_index, _item_index, _slot_index
    if _zip_file is not None:
        return
    _ensure_downloaded()
    _zip_file = zipfile.ZipFile(ZIP_PATH, "r")
    _block_index = {}
    _item_index = {}
    _slot_index = {}
    for entry in _zip_file.namelist():
        if entry.endswith(".png"):
            if entry.startswith(BLOCK_PREFIX):
                bare = entry[len(BLOCK_PREFIX):-4]  # e.g. "oak_log_top"
                _block_index[bare] = entry
            elif entry.startswith(ITEM_PREFIX):
                bare = entry[len(ITEM_PREFIX):-4]  # e.g. "diamond_sword"
                _item_index[bare] = entry
            elif entry.startswith(SLOT_PREFIX):
                bare = entry[len(SLOT_PREFIX):-4]  # e.g. "shield"
                _slot_index[bare] = entry


def _resolve_top_texture(material: str) -> str | None:
    """Given a material like 'minecraft:grass_block', return the ZIP entry path
    for the best top-face texture, or None if not found.

    Tries, in order:
    1. Direct name + '_top' (e.g. grass_block_top)
    2. Water/lava '_still' variant
    3. Direct name match
    4. Explicit alias (e.g. farmland → dirt)
    5. Variant suffix stripping (e.g. oak_slab → oak_planks, stone_slab → stone)
    """
    _open_zip()
    assert _block_index is not None
    name = material.split(":")[-1] if ":" in material else material
    # 1. top-face variant
    if name + "_top" in _block_index:
        return _block_index[name + "_top"]
    # 2. water/lava still
    if name in ("water", "lava") and name + "_still" in _block_index:
        return _block_index[name + "_still"]
    # 3. direct match
    if name in _block_index:
        return _block_index[name]
    # 4. explicit alias
    alias = _TEXTURE_ALIASES.get(name)
    if alias:
        if alias + "_top" in _block_index:
            return _block_index[alias + "_top"]
        if alias in _block_index:
            return _block_index[alias]
    # 5. strip variant suffix and resolve base material
    for suffix in _VARIANT_SUFFIXES:
        if name.endswith(suffix):
            base = name[:-len(suffix)]
            # Wood types: oak_slab → oak → oak_planks
            if base in _PLANKS_BASES:
                planks = base + '_planks'
                if planks in _block_index:
                    return _block_index[planks]
            # General: stone_slab → stone, cobblestone_wall → cobblestone
            if base + "_top" in _block_index:
                return _block_index[base + "_top"]
            if base in _block_index:
                return _block_index[base]
            break
    return None


def _resolve_side_texture(material: str) -> str | None:
    """Given a material like 'minecraft:grass_block', return the ZIP entry path
    for the best side-face texture, or None if not found.

    Tries, in order:
    1. Direct name + '_side' (e.g. grass_block_side)
    2. Water/lava '_still' variant (no distinct side)
    3. Direct name match (most blocks have one texture for all faces)
    4. Explicit alias (e.g. farmland → dirt)
    5. Variant suffix stripping (e.g. oak_slab → oak_planks)
    """
    _open_zip()
    assert _block_index is not None
    name = material.split(":")[-1] if ":" in material else material
    # 1. side-face variant
    if name + "_side" in _block_index:
        return _block_index[name + "_side"]
    # 2. water/lava still
    if name in ("water", "lava") and name + "_still" in _block_index:
        return _block_index[name + "_still"]
    # 3. direct match
    if name in _block_index:
        return _block_index[name]
    # 4. explicit alias
    alias = _TEXTURE_ALIASES.get(name)
    if alias:
        if alias + "_side" in _block_index:
            return _block_index[alias + "_side"]
        if alias in _block_index:
            return _block_index[alias]
    # 5. strip variant suffix and resolve base material
    for suffix in _VARIANT_SUFFIXES:
        if name.endswith(suffix):
            base = name[:-len(suffix)]
            if base in _PLANKS_BASES:
                planks = base + '_planks'
                if planks in _block_index:
                    return _block_index[planks]
            if base + "_side" in _block_index:
                return _block_index[base + "_side"]
            if base in _block_index:
                return _block_index[base]
            break
    return None


def _get_side_texture_bytes(material: str) -> bytes | None:
    """Get the PNG bytes for the side-face texture of a material."""
    cache_key = "side:" + material
    if cache_key in _tinted_cache:
        return _tinted_cache[cache_key]
    safe_name = "side_" + material.replace(":", "_").replace("/", "_")
    disk_path = PROCESSED_DIR / f"{safe_name}.png"
    if disk_path.exists():
        raw = disk_path.read_bytes()
        _tinted_cache[cache_key] = raw
        return raw
    entry_path = _resolve_side_texture(material)
    if entry_path is None:
        return None
    _open_zip()
    assert _zip_file is not None
    raw = _zip_file.read(entry_path)
    tex_name = _texture_name_from_path(entry_path)
    tint = TINT_MAP.get(tex_name)
    if tint:
        try:
            raw = _apply_tint(raw, tint)
        except Exception:
            log.debug("Failed to tint side %s, serving raw", tex_name, exc_info=True)
    else:
        try:
            raw = _crop_first_frame(raw)
        except Exception:
            pass
    _tinted_cache[cache_key] = raw
    try:
        PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
        disk_path.write_bytes(raw)
    except Exception:
        log.debug("Failed to cache processed side texture to disk", exc_info=True)
    return raw


async def get_side_texture(request):
    """GET /api/textures/side/{name} — serve block side-face texture from ZIP."""
    try:
        raw_name = request.match_info["name"]
        if raw_name.endswith(".png"):
            raw_name = raw_name[:-4]
        material = f"minecraft:{raw_name}"
        data = _get_side_texture_bytes(material)
        if data is None:
            return web.Response(status=404, text=f"No side texture for {material}")
        return web.Response(body=data, content_type="image/png", headers={
            "Cache-Control": "public, max-age=3600",
        })
    except Exception as err:
        log.exception("Failed to serve side texture %s", request.match_info.get("name"))
        return web.Response(status=500, text=str(err))


def _resolve_item_texture(material: str) -> str | None:
    """Given a material like 'minecraft:diamond_sword', return the ZIP entry path
    for the item texture.  Falls back to block texture, then GUI slot icons."""
    _open_zip()
    assert _item_index is not None and _block_index is not None and _slot_index is not None
    name = material.split(":")[-1] if ":" in material else material
    # Direct item match
    if name in _item_index:
        return _item_index[name]
    # Many blocks don't have item textures — fall back to block top-face
    block = _resolve_top_texture(material)
    if block:
        return block
    # Entity-rendered items (shield, etc.) — fall back to GUI slot icons
    if name in _slot_index:
        return _slot_index[name]
    return None


def _texture_name_from_path(entry_path: str) -> str:
    """Extract bare texture name from ZIP entry path."""
    if entry_path.startswith(ITEM_PREFIX):
        return entry_path[len(ITEM_PREFIX):-4]
    return entry_path[len(BLOCK_PREFIX):-4]


def _apply_tint(png_bytes: bytes, tint: tuple[int, int, int]) -> bytes:
    """Multiply a greyscale PNG by a tint color and return tinted PNG bytes.

    For animated textures (height > width), only the first frame is used.
    """
    from PIL import Image
    img = Image.open(io.BytesIO(png_bytes)).convert("RGBA")
    # Animated textures are vertical strips: each frame is width x width
    if img.height > img.width:
        img = img.crop((0, 0, img.width, img.width))
    pixels = img.load()
    tr, tg, tb = tint
    for y in range(img.height):
        for x in range(img.width):
            r, g, b, a = pixels[x, y]
            pixels[x, y] = (r * tr // 255, g * tg // 255, b * tb // 255, a)
    out = io.BytesIO()
    img.save(out, format="PNG")
    return out.getvalue()


def _crop_first_frame(png_bytes: bytes) -> bytes:
    """For animated textures (height > width), crop to first frame."""
    from PIL import Image
    img = Image.open(io.BytesIO(png_bytes))
    if img.height > img.width:
        img = img.crop((0, 0, img.width, img.width))
        out = io.BytesIO()
        img.save(out, format="PNG")
        return out.getvalue()
    return png_bytes


def _get_texture_bytes(material: str) -> bytes | None:
    """Get the PNG bytes for a material, applying tint/crop if needed.

    Uses a three-tier cache: in-memory dict → disk cache → compute from ZIP.
    """
    if material in _tinted_cache:
        return _tinted_cache[material]
    # Check disk cache
    safe_name = material.replace(":", "_").replace("/", "_")
    disk_path = PROCESSED_DIR / f"{safe_name}.png"
    if disk_path.exists():
        raw = disk_path.read_bytes()
        _tinted_cache[material] = raw
        return raw
    # Compute from ZIP
    entry_path = _resolve_top_texture(material)
    if entry_path is None:
        return None
    _open_zip()
    assert _zip_file is not None
    raw = _zip_file.read(entry_path)
    tex_name = _texture_name_from_path(entry_path)
    tint = TINT_MAP.get(tex_name)
    if tint:
        try:
            raw = _apply_tint(raw, tint)
        except Exception:
            log.debug("Failed to tint %s, serving raw", tex_name, exc_info=True)
    else:
        try:
            raw = _crop_first_frame(raw)
        except Exception:
            pass
    _tinted_cache[material] = raw
    # Persist to disk
    try:
        PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
        disk_path.write_bytes(raw)
    except Exception:
        log.debug("Failed to cache processed texture to disk", exc_info=True)
    return raw


def _get_item_texture_bytes(material: str) -> bytes | None:
    """Get the PNG bytes for an item material, with animated-frame cropping.

    Uses the same three-tier cache as block textures.
    """
    cache_key = "item:" + material
    if cache_key in _tinted_cache:
        return _tinted_cache[cache_key]
    safe_name = "item_" + material.replace(":", "_").replace("/", "_")
    disk_path = PROCESSED_DIR / f"{safe_name}.png"
    if disk_path.exists():
        raw = disk_path.read_bytes()
        _tinted_cache[cache_key] = raw
        return raw
    entry_path = _resolve_item_texture(material)
    if entry_path is None:
        return None
    _open_zip()
    assert _zip_file is not None
    raw = _zip_file.read(entry_path)
    tex_name = _texture_name_from_path(entry_path)
    tint = TINT_MAP.get(tex_name)
    if tint:
        try:
            raw = _apply_tint(raw, tint)
        except Exception:
            log.debug("Failed to tint %s, serving raw", tex_name, exc_info=True)
    else:
        try:
            raw = _crop_first_frame(raw)
        except Exception:
            pass
    _tinted_cache[cache_key] = raw
    try:
        PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
        disk_path.write_bytes(raw)
    except Exception:
        log.debug("Failed to cache processed item texture to disk", exc_info=True)
    return raw


async def get_texture(request):
    """GET /api/textures/{name} — serve block top-face texture from ZIP.

    The {name} includes the .png suffix (e.g. 'stone.png') which we strip.
    """
    try:
        raw_name = request.match_info["name"]
        if raw_name.endswith(".png"):
            raw_name = raw_name[:-4]
        material = f"minecraft:{raw_name}"
        data = _get_texture_bytes(material)
        if data is None:
            return web.Response(status=404, text=f"No texture for {material}")
        return web.Response(body=data, content_type="image/png", headers={
            "Cache-Control": "public, max-age=3600",
        })
    except Exception as err:
        log.exception("Failed to serve texture %s", request.match_info.get("name"))
        return web.Response(status=500, text=str(err))


async def get_item_texture(request):
    """GET /api/textures/items/{name} — serve item texture from ZIP.

    Checks item textures first, then falls back to block textures for placeable items.
    """
    try:
        raw_name = request.match_info["name"]
        if raw_name.endswith(".png"):
            raw_name = raw_name[:-4]
        material = f"minecraft:{raw_name}"
        data = _get_item_texture_bytes(material)
        if data is None:
            return web.Response(status=404, text=f"No texture for {material}")
        return web.Response(body=data, content_type="image/png", headers={
            "Cache-Control": "public, max-age=3600",
        })
    except Exception as err:
        log.exception("Failed to serve item texture %s", request.match_info.get("name"))
        return web.Response(status=500, text=str(err))


async def list_textures(request):
    """GET /api/textures — list available block texture names."""
    try:
        _open_zip()
        assert _block_index is not None
        return web.json_response(sorted(_block_index.keys()))
    except Exception as err:
        log.exception("Failed to list textures")
        return web.Response(status=500, text=str(err))
