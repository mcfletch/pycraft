"""Draw a parabolic dome over the user"""
from mcpi import block, minecraft, vec3
import numpy as np
import logging
from . import expose, blocks, uniqueblocks
log = logging.getLogger(__name__)

@expose.expose()
def pyramid(
    position=None,
    width=15,
    depth=15,
    material=blocks.BLOCK_NAMES['GRANITE'], 
    xstep=1,
    zstep=1,
    ystep=1,
    *, 
    user=None,
    mc=None 
):
    """Create pyramid centered at position in material"""
    if position is None:
        position = user.position + vec3.Vec3(0,0,depth//2 + 1)
    material = expose.find_blocks(material)
    x,y,z = [int(c) for c in position]
    startx = x-width//2
    endx = startx+width
    startz = z-depth//2
    endz = z+depth 
    cury = y
    while startx <= endx and startz <= endz:
        mc.setBlocks(
            startx,
            cury,
            startz,
            endx,
            cury,
            endz,
            material,
        )
        cury += ystep
        startx += xstep
        startz += zstep 
        endx -= xstep 
        endz -= zstep 
    return position

