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

# Singleton — opened once on first request
_zip_file: zipfile.ZipFile | None = None
_block_index: dict[str, str] | None = None  # bare name → zip entry path
_tinted_cache: dict[str, bytes] = {}  # material → tinted PNG bytes
PROCESSED_DIR = CACHE_DIR / "textures_processed"

# Blocks whose textures are greyscale and need biome-color tinting.
# Tint color is approximate plains biome grass/foliage color.
GRASS_TINT = (124, 189, 107)  # #7CBD6B — plains grass
FOLIAGE_TINT = (87, 162, 63)  # #57A23F — plains foliage
WATER_TINT = (63, 118, 228)   # #3F76E4 — plains water
ICE_TINT = (160, 200, 255)    # light blue tint for ice blocks
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
    """Open the ZIP file and build a name → path index of block textures."""
    global _zip_file, _block_index
    if _zip_file is not None:
        return
    _ensure_downloaded()
    _zip_file = zipfile.ZipFile(ZIP_PATH, "r")
    _block_index = {}
    for entry in _zip_file.namelist():
        if entry.startswith(BLOCK_PREFIX) and entry.endswith(".png"):
            bare = entry[len(BLOCK_PREFIX):-4]  # e.g. "oak_log_top"
            _block_index[bare] = entry


def _resolve_top_texture(material: str) -> str | None:
    """Given a material like 'minecraft:grass_block', return the ZIP entry path
    for the best top-face texture, or None if not found."""
    _open_zip()
    assert _block_index is not None
    name = material.split(":")[-1] if ":" in material else material
    if name + "_top" in _block_index:
        return _block_index[name + "_top"]
    if name in ("water", "lava") and name + "_still" in _block_index:
        return _block_index[name + "_still"]
    if name in _block_index:
        return _block_index[name]
    return None


def _texture_name_from_path(entry_path: str) -> str:
    """Extract bare texture name from ZIP entry path."""
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


async def list_textures(request):
    """GET /api/textures — list available block texture names."""
    try:
        _open_zip()
        assert _block_index is not None
        return web.json_response(sorted(_block_index.keys()))
    except Exception as err:
        log.exception("Failed to list textures")
        return web.Response(status=500, text=str(err))
