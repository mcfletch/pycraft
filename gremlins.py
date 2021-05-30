"""Lets you create gremlins from outside the game

run with::

    python3 gremlins.py -i 

to be dropped into an interactive session with the 
pycraft API available.

Basically, when your kids are having a Minecraft party
you can introduce wild/wacky events, like pyramids of
TNT showing up and blowing up, spawning dozens of 
cows in their house, giving them boats or minecarts
when they're stuck.
"""

from pycraft import (
    blocks,
    entity,
    commands,
    buildings,
    tunnels,
    parabolic,
    copypaste,
    bulldozer,
)
from mcpi import minecraft

mc = minecraft.Minecraft.create('127.0.0.1')

es = entity.EntityAPI(mc=mc)

print(dir())

import mcpi.connection

for i in range(0, 255):
    try:
        mc.conn.send(b'world.convertMaterial', i, 0)
        print(i, mc.conn.receive())
    except mcpi.connection.RequestError:
        print('ERR:', i)
