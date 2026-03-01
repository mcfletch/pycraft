import unittest
from pycraft import ainterpreter as interpreter
from pycraft import expose
from pycraft import acommands as commands
from pycraft.server import world, channel, proxyobjects
import pytest
import pytest_asyncio
import ast
import numpy as np
import uuid

pytestmark = pytest.mark.live


async def test_introspect_cached(channel):
    struct = {
        '__type__': 'CraftHorse',
        'uuid': str(uuid.uuid4()),
        '__namespace__': 'Horse',
    }
    cls = proxyobjects._dict_cls(struct)

    assert hasattr(cls, 'get_key'), dir(cls)

    inst = proxyobjects.type_coerce(struct, 'Entity')
    assert inst.__class__.__name__ == 'CraftHorse', inst.__class__
    assert isinstance(inst, world.Entity), cls.__mro__


async def test_ItemMeta(channel):
    cls = proxyobjects._dict_cls(
        {
            '__type__': 'CraftPotionMeta',
            '__namespace__': 'PotionMeta',
        }
    )
    assert 'PotionMeta' in cls.__namespace__, cls.__namespace__
    assert world.ItemMeta in cls.mro(), cls.mro()


async def test_PlayerMeta(channel):
    cls = proxyobjects._dict_cls(
        {
            '__type__': 'CraftPlayer',
            '__namespace__': 'Player',
        }
    )
    assert 'Player' in cls.__namespace__, cls.__namespace__
    assert world.Player in cls.mro(), cls.mro()


async def test_World(channel):
    from pycraft.server import final

    worlds = await final.Server.getWorlds('server')
    for w in worlds:
        for expected in [
            'spawnEntity',
            'setBlocks',
        ]:
            assert hasattr(w, expected), f'{expected} not found on World'


async def test_VillagerSpawn(channel):
    from pycraft import acommands
    from pycraft.server import final

    v = await acommands.spawn(
        'villager', position=("world", 0, 320, 0), world=final.World(name='world')
    )

    assert isinstance(v, world.Entity), f'Expected Entity, got {type(v)}: {v}'
    assert hasattr(v, 'getInventory'), 'Villager entity missing getInventory method'
