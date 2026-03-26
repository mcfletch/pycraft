# Pycraft Project Plan

## Summary Table

| Project / Task | Status | Summary |
|---|---|---|
| **Bugs & Fixes** | | |
| Live pytest timeout | ✅ | Fixed: set `asyncio_default_test_loop_scope = "session"` and `asyncio_default_fixture_loop_scope = "session"` in `pyproject.toml` |
| Item Drag Not Working | ✅ | HTML5 drag-and-drop between all inventory sections (main, hotbar, armor, offhand); shared `useInventoryDrag` hook; `SlotBox`/`InventoryGrid` reusable components; `move_item` backend endpoint |
| Polling | ✅ | `usePlayers` no longer polls; SSE join/quit events update the React Query cache directly; reconnect invalidates to resync |
| Player death event has no player | ✅ | `EntityEventConverter` sends entity as `"entity"` not `"player"`; fixed in Java + Python fallback (entity-is-Player → also set `player`) |
| Player position is 1 meter off | ✅ | All coordinate displays now use `.toFixed(1)` for floats; map icon positions use raw float coords; block lookups use `Math.floor` |
| Very Long Response Glitch | ✅ | Output Paper gets `overflow: hidden` + `wordBreak: break-all`; prevents horizontal overflow from expanding the window |
| Query Backlog | ✅ | Map block query params debounced 250 ms; rapid scroll-wheel events no longer flood the server |
| teleport into ground | ✅ | `Location.safe_above()` scans upward for two passable blocks; `set_location(safe=True)` default; dashboard teleport endpoint also safe by default |
| getBlocks typing.List subtype | ✅ | `log.warning` → `log.debug` (unparameterised List fallback is harmless) |
| Map re-renders on interpreter resize | ✅ | ResizeObserver debounced 300 ms; prevents map refetch on every interpreter panel resize |
| Map center not persisted across tabs | ✅ | `worldName`, center, y-level, zoom stored in `sessionStorage`; restored on tab return |
| elevators() sign text | ✅ | `BlockData.get_key()` overrode `Reference.get_key()` in dynamic class MRO; fixed by falling back to `super().get_key()` when `string_value` is None |
| Dashboard traceback display | ✅ | Backend sends `traceback` field on errors; clicking red error line opens a modal dialog with full traceback and copy button (CodeEditor + map interpreter) |
| No-player guards | ✅ | `@requires_player` decorator raises `RuntimeError('No player selected')` for absent or fake players; all commands in `acommands.py` and `buildings.py` guarded |
| elevators() height bug | ✅ | `column_up` returns string on failure; `assert height` passes for non-empty string, string passed as slice index |
| help() & expose.py bugs | ✅ | Fixed `formatargspec` removal and undefined `name` variable |
| Dev container | ✅ | `.devcontainer/` for agentic Claude Code with Docker socket access |
| **Dashboard Features** | | |
| Player Management | TODO | Whitelist management UI |
| Event Handlers (persistent) | TODO | Persistent handlers for world events, reload on reconnect |
| Dashboard Authentication | Done | Username/password login to control access to the dashboard |
| Web Dashboard (core) | Partial | Live map, player markers, inventory, teleport, search, events, code editor all done |
| Entity Management | TODO | Allow for selecting entities, searching by entity type or name, and applying a menu of commands to an entity, such as kill, delete, edit inventory, etc |
| **Map Enhancements** | | |
| Configurable Resource Pack | TODO | Let users specify a resource pack URL so block textures reflect their chosen pack |
| Map Block Painting | TODO | Click-to-paint blocks with material palette and brush sizes |
| Map Height Shadows | TODO | Terrain elevation shadows based on sun angle / time of day |
| Transparent Block Layering | TODO | Render water/glass/leaves with transparency showing block below |
| **API & Backend** | | |
| Paper Interfaces | TODO | Dialogs and recipes via Paper API |
| Missing Bukkit APIs | TODO | Audit spigot javadocs for unimplemented APIs |
| Separate API Introspections | TODO | Split 20+ MB introspection into lazy-loaded subsets with version-keyed client cache |
| Introspection Zip Cache | TODO | Replace monolithic `.introspection.json` with a per-class zip cache in `~/.cache`; lazy-load class definitions on first use; optionally fetch missing classes live from server |
| Chunk-Aware Block I/O | TODO | Batch get/set block calls by chunk; buffer writes within a single tick for atomic multi-block updates |
| Standard RPC Protocol | TODO | Replace custom TCP/RPC with a standard protocol (JSON-RPC, gRPC, WebSockets, etc.) |
| Particle Effects | TODO | Expose particle API and create demos |
| **Potions & Crafting** | | |
| Persistent Scripts | TODO | Named scripts/modules loadable from dashboard; persist on server, handle events, create long-running player-triggered operations |
| Command Handlers | TODO | Register custom `/commands` from Python with tab completion |
| Clean Event Handlers | TODO | Documented handlers for craft/break/place/interact events |
| Item Crafting Hooks | TODO | Expose and modify crafting recipes from Python |
| Potion Crafting | Partial | Custom potions via Give/Enchant done; brewing stand & recipe APIs TODO |
| Potion Python API | ✅ | `potion_of()` and `mikes_potion()` fixed: effect types namespaced to `minecraft:`, old Bukkit names updated, docstrings updated |
| **World Generation** | | |
| Python-to-Redstone | TODO | Translate Python logic into in-world redstone circuits |
| Procedural City Generation | TODO | Auto-generate cities with configurable layouts |
| Topology-Aware Creation | TODO | Roads, docks, stairs, bridges that adapt to terrain |
| Parametric Building/Tree Gen | TODO | Parameterized buildings and procedural trees |
| Structure Generation | TODO | Generate vanilla/custom structures at specified coordinates |
| Location/Structure Finding | Partial | Map search done; Python `locate`-style API TODO |
| **AI & Automation** | | |
| LLM Building Assistant | TODO | LLM agent with building primitives (wall, window, column, roof) executes natural-language build requests interactively |
| **Project Structure** | | |
| Multi-Server Runner | TODO | Web UI to launch/manage N Docker server+dashboard pairs, with world selection, snapshots, and idle-suspend |
| Dashboard as Sample Repo | TODO | Extract dashboard into a separate repo that depends on pycraft as a library |

---

## Priority: Fix Before Next Feature Work

These issues were identified during the current session and should be resolved first.

### 1. ✅ No-player guards (DONE)

### 2. ✅ elevators() sign text fails: `'Expected non-null argument at 0'`

**Fixed.** `BlockData.get_key()` (returns `string_value`) overrode `Reference.get_key()` (returns `__reference__`) in the dynamically-generated MRO for `CraftSign` BlockState objects. The MRO is `CraftSign → Sign → BlockData → … → Reference`, so `BlockData.get_key()` was found first and returned `None` (since BlockState objects have `string_value=None`). Fix in `world.py`: `BlockData.get_key()` now falls back to `super().get_key()` when `string_value` is None, reaching `Reference.get_key()` via cooperative MRO lookup.

### 3. ✅ Live pytest tests timeout on RPC calls (event loop issue)

**Fixed.** The `channel` fixture used `scope='session', loop_scope='session'`, but `asyncio_mode = "auto"` defaults test functions to `loop_scope='function'`. Each test got its own event loop while the fixture's reader/writer tasks ran on the session loop, so RPC responses were never received. Fix: added `asyncio_default_test_loop_scope = "session"` and `asyncio_default_fixture_loop_scope = "session"` to `[tool.pytest.ini_options]` in `pyproject.toml`.

### 4. help() and expose.py bugs (FIXED)

- `inspect.formatargspec` removed in Python 3.11 → replaced with `inspect.signature()` in `expose.py:89`
- `name` variable undefined in `command_details()` → fixed to `name_or_instance` in `expose.py:73,79,82`
- Non-live tests passing: `pytest tests/test_commands.py -v -k "not live"` (3/3 pass)

## Recently Completed (This Session)

- **Enchant dialog for inventory items**: Click "Enchant" in inventory context menu → dialog shows only applicable enchantments (filtered by `canEnchantItem`), with level sliders. For potions, shows base type + custom effects. Backend: `applicable_enchantments` endpoint in `players.py`. Frontend: `EnchantmentSelector.jsx` shared component, `InventoryView.jsx` dialog.
- **Follow player Y level**: Map tracks followed player's Y coordinate, not just X/Z. `WorldMap.jsx` follow-player useEffect.
- **Drop item fix**: `inventory.clear(slot)` instead of `setItem(slot, None)` which caused NPE.
- **Y_RANGE = 16**: Map vertical slice set to 16 blocks (was 30, briefly 4). `handlers/world.py`.
- **Reference MRO fix**: Changed `Reference.__init__(self, struct)` to `Reference.__init__(self, **named)` to match `ServerObjectProxy.__init__` signature. Fixed `string_value` kwargs error but revealed the deeper `setLine` issue.
- **elevators() sign text fix**: `BlockData.get_key()` was shadowing `Reference.get_key()` in the dynamic MRO for `CraftSign` BlockState objects (MRO: `Sign → BlockData → … → Reference`). `BlockData.get_key()` returned `string_value=None`; fixed by falling back to `super().get_key()` when `string_value` is None. `elevators()` now works end-to-end.
- **Potion API fix**: `potion_of()` effect types were passed lowercase to the Java API (which expects uppercase). Fixed to uppercase types, strip `minecraft:` prefix from base type, and explicitly extract effect fields — matching the working dashboard `_apply_potion_meta` pattern. Removed stray debug `print`. `mikes_potion()` docstring updated with correct potion names and parameter types.

### 5. Dev container for agentic Claude Code

Create a dev container (`.devcontainer/`) so Claude Code can run in agentic mode without constant approval prompts. Requirements:
- Python 3.14 + pnpm + Java 21 (for building PycraftServer)
- Access to host Docker socket (`/var/run/docker.sock` mount) so it can start/stop/inspect the Minecraft server container
- Network access to `172.17.0.3:4712` (PycraftServer plugin) and ability to run the dashboard
- `.venv` and `node_modules` should persist across container rebuilds (named volumes or bind mounts)
- Pre-install project dependencies on build

---

## Feature Ideas

### Web Dashboard with Live Map and Code Editor

A local website providing:

- [x] **Live map** rendered from in-game data (efficient server-side capture), displayed on an HTML canvas
- [x] **Player markers** showing all connected players and their real-time locations on the map (colored circles, name labels, facing arrows, follow mode)
- [x] **Player detail panel** - click a player to see their inventory, location, health, game mode, etc.
- [x] **Inventory views** - player inventory with hotbar, armor slots, offhand, item counts, enchantment indicators, context menu (enchant/drop)
- [x] **Player Teleport** - click map to select player, click again to teleport to destination (uses block height for Y)
- [x] **Search** - search for blocks, entities, and map features (players, structures, biomes) via SearchPanel and `/api/search/map`
- [ ] **Player Management** - whitelist management
- [x] **Event log** - EventLog.jsx displays server events (join/quit, chat, block place/break, deaths)
- [ ] **Event Handlers** - Write handlers for events for the world (store in game, reloading on reconnection)
- [x] **Code editor window** - CodeEditor.jsx with per-player script execution, history tracking, Python evaluator
- [x] **Script output** displayed in the panel alongside the editor
- [x] **Give items** - material autocomplete, quantity, optional enchantments
- [x] **Enchant items** - applicable enchantments dialog with level sliders, potion options (base type, custom effects)
- [x] **Entity spawning** - EntityPanel.jsx for spawning entities at coordinates
- [x] **Template paste** - preview and paste structure templates on map with visual footprint
- [x] **SSE events** - real-time server events via Server-Sent Events

### Dashboard Authentication

- [x] Protect the dashboard with a username/password login screen
- [x] Backend: HMAC-signed session auth on aiohttp server; credentials configured via `--add-user` CLI flag, stored in `~/.pycraft-dashboard-users.json`
- [x] Frontend: login page shown when unauthenticated; session stored in httponly secure cookie
- [x] All API routes and SSE endpoint require a valid session token
- [ ] Optional: multiple users with different roles (read-only vs. admin)
- [x] Designed for local-network use — not a full enterprise auth system, but enough to prevent casual unauthorized access

### Configurable Resource Pack

- [ ] Allow the user to specify a resource pack URL (or local path) in dashboard settings
- [ ] Download and unzip the pack in the browser (or via a backend helper) to extract block textures
- [ ] Map renderer uses textures from the chosen pack instead of the default hardcoded set
- [ ] Fall back to default textures for any block not present in the chosen pack
- [ ] Setting persists in `localStorage` so it survives page reloads
- [ ] Could support Faithful, SEUS, or any vanilla-compatible pack

### Map Block Painting

- [ ] **Painting mode**: click a material from a palette, then draw on the map to place blocks
- [ ] Two modes: **additive** (place on top of air) and **replace** (replace existing blocks)
- [ ] **Material palette**: drag-and-drop reorderable palette of selected materials shown alongside the map
- [ ] **Search to add**: search bar (reusing existing block search endpoint) to find and add materials to the palette
- [ ] Brush sizes: single block, 3x3, 5x5
- Use cases: drawing roads, quickly sketching building footprints layer by layer, landscaping
- Backend: reuse existing `POST /api/worlds/{name}/blocks` endpoint with collected locations

### Map Height Shadows

- [ ] Add crude shadow rendering to the map to highlight terrain elevation differences
- Sun position derived from time of day (obtainable via `world.getTime()`)
- For each block column, compare height to neighboring columns; if neighbor is taller, darken the block proportionally
- Shadow direction and length determined by sun angle (east in morning, overhead at noon, west in evening)
- Rendered as a semi-transparent dark overlay on the canvas after block textures are drawn
- Backend: return height data alongside block data in the blocks endpoint (or compute client-side from a separate heightmap query)

### Transparent Block Layering

- [ ] Transparent/translucent blocks (water, glass, ice, leaves) should render as a semi-transparent layer on top of the block beneath them
- Backend: when the surface block is transparent, also return the block below it in the blocks response
- Frontend: draw the base block first, then draw the transparent block on top with reduced alpha
- Applicable materials: water, glass (all colors), ice variants, leaves, slime blocks, honey blocks, barriers
- Makes underwater terrain visible through water, and interiors visible through glass roofs/walls

### Paper Interfaces

- [ ] Dialogs
- [ ] Recipes

### Missing Bukkit APIs

- [ ] Scan https://hub.spigotmc.org/javadocs/spigot/overview-tree.html and look for anything missing
- [ ] Plan out parts we think could be useful

### Introspection Zip Cache

Replace the monolithic `pycraft/server/.introspection.json` (~20 MB, checked into the repo) with a versioned, per-class zip cache stored outside the source tree.

**Format**
- One zip file per server version, stored at `~/.cache/pycraft/introspection-<mc_version>-<plugin_version>.zip`
- Each entry in the zip is `<ClassName>.json` — minimal-whitespace JSON for a single class definition
- The zip index (list of class names) is a small `index.json` entry at the root

**Loading**
- On connect, download only the index from the server (or read it from the zip if cached)
- **Lazy-load** individual class definitions: when a proxy class is first instantiated, load its `<ClassName>.json` from the zip and register it
- Never load the entire introspection into memory at once

**Cache invalidation**
- Cache key is `(minecraft_version, plugin_version)` — a new plugin build automatically gets a fresh cache file
- Old cache files can be pruned manually or by a `--clear-cache` flag

**Extension: live fallback**
- If a class is not in the local zip (e.g. cache was built against an older plugin), fetch its definition live from the server via a new `introspect/<ClassName>` endpoint
- On success, write the result into the zip for future use

**Benefits**
- Eliminates the 20 MB file from the repo (`.introspection.json` moves to `.gitignore`)
- Startup time drops dramatically — only the index is fetched/parsed up front
- Memory footprint is proportional to the classes actually used in a session

### Chunk-Aware Block I/O

Minecraft organises the world into 16×16 column chunks. Block reads and writes that cross chunk boundaries currently generate one RPC call per block, which is slow and wasteful. This feature makes the Python layer chunk-aware.

**Chunk-batched reads (`getBlocks` / `get_blocks`)**
- Group the requested coordinates by chunk `(cx, cz) = (x // 16, z // 16)`
- Issue one server call per chunk (`getChunkBlocks(cx, cz, y_min, y_max)`) rather than one call per block
- Cache the returned chunk slice for the duration of the operation so repeated reads from the same chunk are free
- Fall back to individual `getBlock` for single-block reads outside a bulk call

**Tick-buffered writes (`setBlock` / `set_block` / `fill`)**
- Accumulate `setBlock` calls into a per-chunk write buffer instead of sending immediately
- Flush all buffered changes in a single `setChunkBlocks(cx, cz, changes)` call per chunk at the end of the tick (or when the buffer is explicitly flushed)
- The server side applies all changes atomically within one game tick, avoiding inter-tick lighting/physics glitches during large fills
- Expose `async with mc.block_batch():` context manager that opens and auto-flushes the buffer

**Single-tick atomicity**
- All writes submitted inside one `block_batch()` context are queued and sent to the Java plugin as a single batched message
- The plugin defers the actual `world.setBlock()` calls to the next server tick using `Bukkit.getScheduler().runTask(...)`, so all placements happen in one tick regardless of Python async timing
- Eliminates the "flickering fill" effect where partially-placed structures are visible mid-operation

**Scope**
- `pycraft/acommands.py`: `block()`, `get_blocks()` updated to use chunk I/O
- `pycraft/buildings.py`, `pycraft/copypaste.py`, `pycraft/bulldozer.py`: opt-in to `block_batch()` for their fill loops
- Java plugin: new `getChunkBlocks` and `setChunkBlocks` message handlers
- Python channel: `block_batch()` context manager on `Channel`

### Separate API Introspections

- [ ] Currently the introspection payload is *far* too large (~20 MB) — causes a slow startup download
- [ ] Split into domain subsets (e.g. `world`, `player`, `inventory`, `entities`, `blocks`) served as separate endpoints
- [ ] Load subsets on demand (lazy) rather than all at once on connect
- [ ] **Version-keyed client cache**: server exposes its version string (e.g. `1.1.0`); client stores each subset in `localStorage` keyed by `introspection/{version}/{subset}` and skips the download when the version matches
- [ ] Invalidate cache automatically when the server version changes
- [ ] Consider gzip compression and/or a more compact binary format (MsgPack) to shrink payloads further

### Particle Effects

- [ ] Expose the API, create some fun demos

### Potion Crafting

- [x] Programmatic creation of custom potions with specific effects (via Give Item and Enchant dialog)
- [ ] Expose potion brewing stand manipulation
- [ ] Python API for brewing recipes and potion effect combinations

### Potion Python API

- [x] `potion_of(type, name, *extra)` and `mikes_potion(name)` are `@expose()`-decorated commands available in the code editor and chat interpreter
- [x] Fixed: effect types uppercased, `minecraft:` prefix stripped, explicit field extraction — matches dashboard `_apply_potion_meta` logic
- [x] Docstrings document parameter types and effect dict schema

### Persistent Scripts / Event Handlers

Allow the dashboard code window to define named **scripts** (Python modules) that are loaded into the running server and persist across interpreter sessions.

**Dashboard UI**
- A "Scripts" tab or panel alongside the code editor: list of named scripts, each with a name, enabled/disabled toggle, and "Edit" button
- Editing opens the full multi-line code editor (not just the single-line REPL)
- "Load" sends the script to the server, registering any event handlers or background tasks it defines
- "Unload" removes the script and de-registers its handlers

**Python API**
- Scripts can use `@on_event('block_break')`, `@on_event('player_join')`, etc. to subscribe to Minecraft events
- Handlers receive a live event proxy object (same as existing event system)
- Scripts can define persistent background coroutines (e.g. a timer that fires every N seconds)
- Scripts share a persistent namespace that survives individual REPL evaluations; changes made in the REPL (e.g. `player_storage`) can be accessed by scripts

**Server side**
- A `ScriptManager` holds loaded script modules and their registered handlers
- On script load, execute the module body in a clean namespace with the full pycraft namespace available
- Handlers registered by the module are registered with the existing event dispatcher
- On unload, de-register all handlers from that script

**Storage**
- Scripts are stored in a `scripts/` directory (configurable) so they survive dashboard restarts
- Metadata (enabled/disabled, load order) stored alongside

### Command Handlers

- [ ] Allow defining custom `/commands` from Python that players can invoke in-game
- [ ] Registration API: `channel.register_command(name, handler, description, usage, aliases)`
- [ ] Handler receives a context object with the player, arguments, and command metadata
- [ ] Support tab-completion callbacks for argument suggestions
- [ ] Commands persist across reconnections (re-register on channel reconnect)
- [ ] Web dashboard integration: define, edit, enable/disable command handlers from the browser UI
- [ ] Java side: PycraftServer plugin registers a dynamic command dispatcher that forwards unknown `/pycraft-*` commands (or a configurable prefix) over TCP to the Python handler

### Clean Event Handlers

- [ ] Clean, documented handlers for common events (craft, break, place, interact, etc.)
- [ ] Make it easy for Python scripts to subscribe to and react to specific event types
- [ ] Expose event cancellation and modification from Python

### Item Crafting Hooks

- [ ] Expose crafting recipes to Python
- [ ] Allow adding/removing/modifying crafting recipes programmatically
- [ ] Hook into craft events to create custom crafting logic

### Python-to-Redstone Translation

- [ ] Translate Python logic (if/else, loops, boolean expressions) into equivalent redstone circuits
- [ ] Place the generated redstone machines in-world automatically
- [ ] Visual representation of the logic flow

### Procedural City Generation

- [ ] Semi-automatic or fully automatic creation of cities
- [ ] Configurable city layouts (grid, organic, medieval, modern, etc.)
- [ ] Building variety, road networks, public spaces, infrastructure

### Topology-Aware Creation

- [ ] Create roads that follow the surface terrain
- [ ] Build docks when reaching water
- [ ] Generate stairs that climb mountains
- [ ] Bridge generation across valleys/rivers
- [ ] Terrain-adaptive placement of structures

### Parametric Building/Tree Generation

- [ ] Parameterized creation of buildings (width, height, floors, style, materials)
- [ ] Procedural tree generation with controllable species, size, shape
- [ ] Template system with variable substitution for repeated structures

### Location/Structure Finding

- [x] Search for structures, biomes from map (via `/api/search/map` endpoint)
- [ ] Find the nearest village, biome of a given type, structure, etc. from Python
- [ ] Expose Minecraft's locate command functionality to Python
- [ ] Search by radius, direction, or type

### Structure Generation at Location

- [ ] Generate a village or other vanilla structure at a specified location
- [ ] Place custom structure templates (schematics) at coordinates
- [ ] Populate generated structures with appropriate entities and loot

### LLM Building Assistant

- [ ] Define a library of building **tool-functions** exposed as LLM tools: `build_wall(x, z, length, height, direction, material)`, `add_window(wall_ref, offset, width, height)`, `build_column(x, z, height, material)`, `build_roof(footprint, style, material)`, `build_floor(x1, z1, x2, z2, y, material)`, `build_doorway(wall_ref, offset)`, etc.
- [ ] Each tool is a thin wrapper over existing `@expose()` / block-placement commands, so the LLM controls the game through the same API humans use
- [ ] User types a natural-language prompt in the dashboard code editor or a dedicated "Build with AI" panel: *"Build me a small stone cottage with two windows, a wooden door, and a pitched roof"*
- [ ] Backend sends the prompt + tool definitions to an LLM (Claude API); receives a sequence of tool calls; executes them one-by-one against the live server, streaming progress back to the UI
- [ ] **Interactive loop**: after each step the LLM can inspect what was placed (via the blocks endpoint) and adjust subsequent calls — e.g. snap a roof to the actual wall height
- [ ] User can interrupt, undo the last N placements, or give follow-up instructions mid-build
- [ ] Tool results (block counts placed, bounding box, errors) are fed back to the LLM so it can self-correct
- [ ] Dashboard shows a live preview on the map as blocks are placed

### Standard RPC Protocol

- [ ] Replace the current custom TCP framing / RPC protocol with a well-supported standard
- [ ] Candidates: JSON-RPC 2.0 over WebSocket, gRPC (with protobuf), or MsgPack-RPC
- [ ] Goals: interoperability (other languages can call in without a Python client), better tooling (Postman, grpcurl), and easier debugging
- [ ] Java side: rewrite `PycraftServer` plugin transport layer to speak the chosen protocol
- [ ] Python side: replace `channel.py` / `proxyobjects.py` framing with a standard client library
- [ ] Keep the high-level `@expose()` / proxy-object API surface unchanged for existing user scripts

### Multi-Server Runner

A hosted runner that lets users launch and manage multiple Minecraft + dashboard server pairs from a single web UI.

- [ ] **Server management UI**: list of named server instances, each with a user-chosen world name and status (running / idle / stopped)
- [ ] **Launch/stop**: start and stop individual Docker container pairs (Minecraft + pycraft-dashboard) on demand
- [ ] **World directory mapping**: each instance gets its own world directory, named by the user; mounted into the container at start
- [ ] **Multiplexing**: reverse proxy (e.g. Caddy or Traefik) routes each instance's dashboard to a sub-path or subdomain
- [ ] **Snapshots / backups**: snapshot the world directory on demand or on a schedule; list and restore snapshots from the UI
- [ ] **Idle suspend**: detect when no players are connected and no dashboard sessions are active; pause the container to save resources; resume automatically on next connection
- [ ] **Resource limits**: configure CPU/memory limits per container pair
- [ ] **Auth**: the runner UI itself is protected by login; each server instance optionally has its own dashboard password
- [ ] **Persistence**: runner state (instance list, config, snapshot metadata) stored in a small SQLite DB or config file

### Dashboard as Sample Repository

- [ ] Extract `pycraft/dashboard/` into a standalone repo (e.g. `pycraft-dashboard`)
- [ ] Repo depends on `pycraft` as an installable PyPI package (or git dependency)
- [ ] Demonstrates how to build a full application on top of the pycraft library
- [ ] Serves as a reference implementation and onboarding example for new users
- [ ] CI in the sample repo installs pycraft from PyPI (or a release tag) and runs its own tests
- [ ] Keeps the main `pycraft` repo focused on core library, plugin, and protocol concerns
