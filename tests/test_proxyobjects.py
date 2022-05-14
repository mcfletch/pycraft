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


@pytest_asyncio.fixture()
async def chan():
    chan = channel.Channel(debug=True)
    await chan.open()
    await chan.introspect(cached=True)
    yield chan
    await chan.close()


@pytest.mark.asyncio
async def test_introspect_cached(chan):
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


@pytest.mark.asyncio
async def test_ItemMeta(chan):
    cls = proxyobjects._dict_cls(
        {
            '__type__': 'CraftPotionMeta',
            '__namespace__': 'PotionMeta',
        }
    )
    assert cls.__namespace__ == 'PotionMeta'
    assert world.ItemMeta in cls.mro(), cls.mro()


@pytest.mark.asyncio
async def test_PlayerMeta(chan):
    cls = proxyobjects._dict_cls(
        {
            '__type__': 'CraftPlayer',
            '__namespace__': 'Player',
        }
    )
    assert cls.__namespace__ == 'Player'
    assert world.Player in cls.mro(), cls.mro()

    for expected in []:
        assert hasattr(world.Player, expected), expected


@pytest.mark.asyncio
async def test_World(chan):
    from pycraft.server import final

    worlds = await final.Server.getWorlds('server')
    for world in worlds:
        for expected in [
            'spawnEntity',
            'setBlocks',
        ]:
            assert hasattr(world, expected), expected


@pytest.mark.asyncio
async def test_VillagerInventory(chan):
    from pycraft.server import final

    v = await final.World(name='world').spawnEntity([0, 1, 0], 'minecraft:villager')

    assert isinstance(v, world.Entity)

    inventory = await v.getInventory()
    assert False, inventory
