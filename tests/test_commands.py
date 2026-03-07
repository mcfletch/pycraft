"""Tests for help() and elevators() chat commands.

Non-live tests verify Python-side logic (formatargspec fix, etc.).
Live tests exercise actual server interactions (sign text, elevator building).

Run non-live only::

    pytest tests/test_commands.py -v -k "not live"

Run live tests (requires Minecraft server on localhost:4712)::

    pytest -m live tests/test_commands.py -v
"""

import pytest
from pycraft.expose import command_details, command_list
from pycraft.server.world import Location, Vector


# ── non-live tests ───────────────────────────────────────────────────


def test_help_no_args():
    """help() with no args should produce a command list."""
    # Import acommands to trigger @expose() registrations
    import pycraft.acommands  # noqa: F401
    import pycraft.buildings  # noqa: F401

    result = command_list()
    assert isinstance(result, list)
    assert len(result) > 0
    # Each entry should be "name -- description"
    assert any('--' in line for line in result)


def test_help_with_function():
    """command_details(function) should format the signature without crashing.

    Regression test for inspect.formatargspec removal in Python 3.11.
    """
    from pycraft.buildings import elevators

    result = command_details(elevators)
    assert isinstance(result, list)
    assert len(result) > 0
    # First line should contain the function name and signature
    assert 'elevators' in result[0]
    assert '(' in result[0]


def test_help_with_name():
    """command_details('help') should return details for a known command."""
    import pycraft.acommands  # noqa: F401

    result = command_details('help')
    assert isinstance(result, list)
    assert len(result) > 0


# ── live tests ───────────────────────────────────────────────────────


@pytest.mark.live
async def test_set_sign_text(channel):
    """Place a sign and set text on it.

    Isolates the sign_state.setLine() failure from elevators().
    """
    from pycraft.server import final
    from pycraft.acommands import set_sign_text

    loc = Location(['world', 10, 319, 10])

    # Place a sign block
    await final.World(name='world').setBlockList(
        [loc],
        ['oak_sign'],
    )

    # Set text — this exercises getState() + setLine() on a Reference proxy
    result = await set_sign_text(loc, ['Test Line 1', 'Test Line 2'])
    assert result is not None, 'set_sign_text returned None — sign state was not a Sign instance'


@pytest.mark.live
async def test_elevators(channel):
    """Full elevator construction test.

    Uses explicit position and height to avoid needing a real player.
    """
    from pycraft.server import final
    from pycraft.buildings import elevators

    world = final.World(name='world')
    # Create a mock player with position and direction
    position = Location(['world', 20, 300, 20])

    class MockPlayer:
        pass

    player = MockPlayer()
    player.location = position
    player.position = position
    player.direction = position.direction

    await elevators(
        position=position,
        height=5,
        walls='glass',
        player=player,
        world=world,
    )
