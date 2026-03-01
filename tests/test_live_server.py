"""Live integration tests for PycraftServer 1.1.0 (Paper API 1.21.11).

These tests verify that the upgraded plugin exposes new entity types,
block data types, and API features introduced in Minecraft 1.20-1.21
and that the Python client can exercise them over the wire.

Run with::

    pytest -m live tests/test_live_server.py
"""

import pytest
from pycraft.server import proxyobjects

pytestmark = pytest.mark.live


# ── basic connectivity ───────────────────────────────────────────────


async def test_server_connection(channel):
    """Verify the channel is open and introspection completed."""
    assert channel.writer is not None
    assert channel.reader is not None


async def test_introspection_loaded(channel):
    """Verify introspection populated proxy types."""
    assert len(proxyobjects.PROXY_TYPES) > 0, 'No proxy types loaded'


async def test_server_worlds(channel):
    from pycraft.server import final

    worlds = await final.Server.getWorlds('server')
    assert len(worlds) >= 1, 'Expected at least one world'
    assert hasattr(worlds[0], 'name'), 'World object missing name attribute'


# ── new 1.20+ entity types ──────────────────────────────────────────


@pytest.mark.parametrize(
    'name',
    [
        'Camel',
        'Sniffer',
        'Breeze',
        'Bogged',
        'Armadillo',
        'TextDisplay',
        'BlockDisplay',
        'ItemDisplay',
        'Interaction',
        'WindCharge',
    ],
)
async def test_entity_type_exposed(channel, name):
    """New entity type is present in introspection proxy types."""
    from pycraft.server import final

    assert hasattr(final, name), (
        f'{name} not found in final module. '
        f'Available types: {[k for k in sorted(proxyobjects.PROXY_TYPES.keys()) if "display" in k.lower() or name.lower() in k.lower()]}'
    )


# ── new 1.21+ block data types ──────────────────────────────────────


@pytest.mark.parametrize(
    'name',
    [
        'Crafter',
        'TrialSpawner',
        'Vault',
        'HangingSign',
        'WallHangingSign',
        'ChiseledBookshelf',
        'CopperBulb',
        'DecoratedPot',
    ],
)
async def test_block_data_type_exposed(channel, name):
    """New block data type is present in introspection proxy types."""
    from pycraft.server import final

    assert hasattr(final, name), (
        f'{name} not found in final module. '
        f'Available types: {[k for k in sorted(proxyobjects.PROXY_TYPES.keys()) if name.lower() in k.lower()]}'
    )


# ── new API features (Phase 7) ──────────────────────────────────────


@pytest.mark.parametrize(
    'name',
    [
        'DamageType',
        'DamageSource',
        'ArmorMeta',
        'BundleMeta',
        'Transformation',
    ],
)
async def test_api_type_exposed(channel, name):
    """New API type is present in introspection proxy types."""
    from pycraft.server import final

    assert hasattr(final, name), (
        f'{name} not found in final module. '
        f'Available types: {[k for k in sorted(proxyobjects.PROXY_TYPES.keys()) if name.lower() in k.lower()]}'
    )


# ── world manipulation with new types ────────────────────────────────


async def test_set_block_trial_spawner(channel):
    """Can set a block to a 1.21 block type (trial_spawner)."""
    from pycraft.server import final
    from pycraft.server.world import Location

    block = final.Block(location=Location(['world', 0, 319, 0]))
    await block.setBlockData('minecraft:trial_spawner')
    data = await block.getBlockData()
    assert 'trial_spawner' in str(data), f'Expected trial_spawner, got {data}'


async def test_set_block_crafter(channel):
    """Can set a block to a 1.21 block type (crafter)."""
    from pycraft.server import final
    from pycraft.server.world import Location

    block = final.Block(location=Location(['world', 1, 319, 0]))
    await block.setBlockData('minecraft:crafter')
    data = await block.getBlockData()
    assert 'crafter' in str(data), f'Expected crafter, got {data}'


# ── spawn new entity types ──────────────────────────────────────────


async def test_spawn_breeze(channel):
    """Can spawn a Breeze entity (1.21)."""
    from pycraft.server import final
    from pycraft.server.world import Location

    world = final.World(name='world')
    entity = await world.spawnEntity(
        Location(['world', 0, 320, 0]), 'minecraft:breeze'
    )
    assert entity is not None, 'Failed to spawn Breeze entity'


async def test_spawn_armadillo(channel):
    """Can spawn an Armadillo entity (1.21)."""
    from pycraft.server import final
    from pycraft.server.world import Location

    world = final.World(name='world')
    entity = await world.spawnEntity(
        Location(['world', 2, 320, 0]), 'minecraft:armadillo'
    )
    assert entity is not None, 'Failed to spawn Armadillo entity'
