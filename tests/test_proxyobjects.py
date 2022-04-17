import unittest
from pycraft import ainterpreter as interpreter
from pycraft import expose
from pycraft import acommands as commands
from pycraft.server import world, channel, proxyobjects
import pytest
import ast
import numpy as np
import uuid


@pytest.mark.asyncio
async def test_introspect_cached():
    chan = channel.Channel(debug=True)
    await chan.introspect(cached=True)
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
async def test_ItemMeta():
    chan = channel.Channel(debug=True)
    await chan.introspect(cached=True)
    cls = proxyobjects._dict_cls(
        {
            '__type__': 'CraftPotionMeta',
            '__namespace__': 'PotionMeta',
        }
    )
    assert cls.__namespace__ == 'PotionMeta'
    assert world.ItemMeta in cls.mro(), cls.mro()


@pytest.mark.asyncio
async def test_PlayerMeta():
    chan = channel.Channel(debug=True)
    await chan.introspect(cached=True)
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
async def test_World():
    chan = channel.Channel(debug=True)
    await chan.open()
    try:
        await chan.introspect(cached=True)
        from pycraft.server import final

        worlds = await final.Server.getWorlds('server')
        for world in worlds:
            for expected in [
                'spawnEntity',
                'setBlocks',
            ]:
                assert hasattr(world, expected), expected
    finally:
        await chan.close()
