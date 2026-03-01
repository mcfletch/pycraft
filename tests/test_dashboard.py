"""Tests for the dashboard module — import and basic structure verification"""
import pytest


def test_dashboard_imports():
    """Verify all dashboard modules can be imported without errors"""
    from pycraft.dashboard import app
    from pycraft.dashboard import routes
    from pycraft.dashboard import services
    from pycraft.dashboard import serialization
    from pycraft.dashboard import sse
    from pycraft.dashboard.handlers import server
    from pycraft.dashboard.handlers import players
    from pycraft.dashboard.handlers import world
    from pycraft.dashboard.handlers import commands
    from pycraft.dashboard.handlers import search


def test_serialization_primitives():
    """Test serialization of basic Python types"""
    from pycraft.dashboard.serialization import serialize

    assert serialize(None) is None
    assert serialize('hello') == 'hello'
    assert serialize(42) == 42
    assert serialize(3.14) == 3.14
    assert serialize(True) is True
    assert serialize([1, 2, 3]) == [1, 2, 3]
    assert serialize({'a': 1}) == {'a': 1}


def test_serialization_uuid():
    """Test serialization of UUID objects"""
    import uuid
    from pycraft.dashboard.serialization import serialize

    u = uuid.UUID('12345678-1234-5678-1234-567812345678')
    assert serialize(u) == '12345678-1234-5678-1234-567812345678'


def test_serialization_numpy():
    """Test serialization of numpy types"""
    import numpy as np
    from pycraft.dashboard.serialization import serialize

    assert serialize(np.int64(42)) == 42
    assert serialize(np.float64(3.14)) == 3.14
    arr = np.array([1, 2, 3])
    assert serialize(arr) == [1, 2, 3]


def test_serialization_location():
    """Test serialization of Location objects"""
    from pycraft.server.world import Location
    from pycraft.dashboard.serialization import serialize

    loc = Location(['world', 100.5, 64.0, -200.3])
    result = serialize(loc)
    assert result['world'] == 'world'
    assert result['x'] == 100.5
    assert result['y'] == 64.0
    assert result['z'] == -200.3


def test_serialization_vector():
    """Test serialization of Vector objects"""
    from pycraft.server.world import Vector
    from pycraft.dashboard.serialization import serialize

    vec = Vector(1.0, 2.0, 3.0)
    result = serialize(vec)
    assert result['x'] == 1.0
    assert result['y'] == 2.0
    assert result['z'] == 3.0


def test_services_container():
    """Test DashboardServices holds references"""
    from pycraft.dashboard.services import DashboardServices

    svc = DashboardServices(channel='ch', sse_manager='sse')
    assert svc.channel == 'ch'
    assert svc.sse_manager == 'sse'


def test_sse_manager_init():
    """Test SSEManager initializes cleanly"""
    from pycraft.dashboard.sse import SSEManager

    mgr = SSEManager()
    assert len(mgr.clients) == 0
    assert len(mgr.position_buffer) == 0


def test_create_app():
    """Test app factory creates an aiohttp Application"""
    from pycraft.dashboard.app import create_app

    app = create_app(mc_host='127.0.0.1', mc_port=4712)
    assert 'services' in app
    assert app['services'].channel is not None
    assert app['services'].sse_manager is not None


class TestFindSurfaceBlock:
    """Test the _find_surface_block helper for top-down map collapse.

    Algorithm: at center Y, if air → scan down for floor; if solid → scan
    up for first air then return block below it; fallback to block at center.
    """

    def _make_layers(self, columns):
        """Build layers[y][z][x] from a single-column list (x=0, z=0).

        columns is a list of materials from y_lo to y_hi.
        """
        return [[[mat]] for mat in columns]

    def test_simple_surface(self):
        """Solid at center → scan up finds air → return center block."""
        from pycraft.dashboard.handlers.world import _find_surface_block

        # 5 layers: stone, stone, grass, air, air  (y indices 0-4)
        layers = self._make_layers([
            'minecraft:stone', 'minecraft:stone', 'minecraft:grass_block',
            'minecraft:air', 'minecraft:air',
        ])
        # center at index 2 (grass) is solid, scan up: air at 3 → surface = 2
        assert _find_surface_block(layers, 0, 0, 5, 2) == 'minecraft:grass_block'

    def test_cave_floor(self):
        """Air at center → scan down to find the floor below."""
        from pycraft.dashboard.handlers.world import _find_surface_block

        # stone, stone, dirt, air, air, air, stone, stone (indices 0-7)
        layers = self._make_layers([
            'minecraft:stone', 'minecraft:stone', 'minecraft:dirt',
            'minecraft:air', 'minecraft:air', 'minecraft:air',
            'minecraft:stone', 'minecraft:stone',
        ])
        # center at index 3 (cave air) → scan down: dirt at 2
        assert _find_surface_block(layers, 0, 0, 8, 3) == 'minecraft:dirt'

    def test_standing_on_floor(self):
        """Solid at center with air above → return center block."""
        from pycraft.dashboard.handlers.world import _find_surface_block

        layers = self._make_layers([
            'minecraft:stone', 'minecraft:grass_block',
            'minecraft:air', 'minecraft:air',
        ])
        # center at index 1 (grass), solid → scan up: air at 2 → surface = 1
        assert _find_surface_block(layers, 0, 0, 4, 1) == 'minecraft:grass_block'

    def test_all_air(self):
        """All air → scan down finds nothing → return air."""
        from pycraft.dashboard.handlers.world import _find_surface_block

        layers = self._make_layers(['minecraft:air'] * 5)
        assert _find_surface_block(layers, 0, 0, 5, 2) == 'minecraft:air'

    def test_solid_column(self):
        """All solid → scan up finds no air → return block at center."""
        from pycraft.dashboard.handlers.world import _find_surface_block

        layers = self._make_layers([
            'minecraft:stone', 'minecraft:stone', 'minecraft:stone',
        ])
        # center at 1, solid → scan up: stone at 2 (not air) → exhausted
        # fallback: return center block (stone)
        assert _find_surface_block(layers, 0, 0, 3, 1) == 'minecraft:stone'

    def test_cave_air(self):
        """cave_air counts as air → scan down for floor."""
        from pycraft.dashboard.handlers.world import _find_surface_block

        layers = self._make_layers([
            'minecraft:stone', 'minecraft:dirt',
            'minecraft:cave_air', 'minecraft:cave_air',
            'minecraft:stone',
        ])
        # center at index 2 (cave_air) → scan down: dirt at 1
        assert _find_surface_block(layers, 0, 0, 5, 2) == 'minecraft:dirt'

    def test_embedded_in_solid(self):
        """Center in solid, air is several blocks up → find the surface."""
        from pycraft.dashboard.handlers.world import _find_surface_block

        # stone, stone, dirt, stone, grass, air, air (indices 0-6)
        layers = self._make_layers([
            'minecraft:stone', 'minecraft:stone', 'minecraft:dirt',
            'minecraft:stone', 'minecraft:grass_block',
            'minecraft:air', 'minecraft:air',
        ])
        # center at 2 (dirt) is solid → scan up: stone at 3, grass at 4, air at 5
        # first air at 5 → surface = layers[4] = grass
        assert _find_surface_block(layers, 0, 0, 7, 2) == 'minecraft:grass_block'

    def test_air_above_void(self):
        """Air at center with no solid below → returns air."""
        from pycraft.dashboard.handlers.world import _find_surface_block

        layers = self._make_layers([
            'minecraft:air', 'minecraft:air', 'minecraft:air',
            'minecraft:stone', 'minecraft:stone',
        ])
        # center at 1 (air) → scan down: air at 0 → no solid found → air
        assert _find_surface_block(layers, 0, 0, 5, 1) == 'minecraft:air'

    def test_block_data_stripped(self):
        """Block state data (e.g. waterlogged=true) is stripped from result."""
        from pycraft.dashboard.handlers.world import _find_surface_block

        layers = self._make_layers([
            'minecraft:stone',
            'minecraft:oak_slab[type=bottom,waterlogged=false]',
            'minecraft:air',
        ])
        # center at 1 (slab), solid → scan up: air at 2 → surface = 1
        assert _find_surface_block(layers, 0, 0, 3, 1) == 'minecraft:oak_slab'
