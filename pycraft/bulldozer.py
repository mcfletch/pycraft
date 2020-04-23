from mcpi import block, minecraft
import numpy as np
import logging
log = logging.getLogger(__name__)
from . import expose
from .expose import V
from . import entity
from . import uniqueblocks
from . import lockedmc

@expose.expose()
def bulldoze(depth=10,width=6,height=2,material=block.AIR,*,user=None,mc=None):
    """Set blocks ahead of the user to the given material

    This aligns the block of material with the direction
    the user is currently facing, so it wipes out whatever
    is in front of you.
    """
    x,y,z = position = user.position
    direction = user.direction
    with lockedmc.locked(mc):
        for to_clear in uniqueblocks.unique_blocks_only(generate_blocks_ahead(
            V(x,y+1,z),
            direction,
            depth,
            width=width,
            height=height,
        )):
            # log.info("Clearing: %s", to_clear)
            mc.setBlock(*to_clear,material)

def unit_vector(v):
    length = np.linalg.norm(v)
    if length:
        v /= length
    return v


def generate_blocks_ahead(position,direction,depth,width,height,step=.25):
    """Given a starting position generate point-cloud in direction"""
    start = np.array(tuple(position),dtype='f')
    forward = np.array(tuple(direction),dtype='f')
    above = np.array([0,1,0],dtype='f')

    if not np.allclose(forward, above):
        cross = unit_vector(np.cross(forward,above))
        above = unit_vector(np.cross(forward,cross))
    else:
        cross = np.array(0,0,1)

    start = start + forward
    for f_step in np.arange(0.0,depth,step):
        forward_start = start + (forward * step)
        for c_step in np.arange(-((width)/2),((width)/2),step):
            cross_base = forward_start + (cross * c_step)
            for h_step in np.arange(1.0,height+1.0,step):
                yield cross_base + (above*h_step)

