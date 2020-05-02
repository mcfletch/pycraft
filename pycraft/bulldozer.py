"""Clear (create) a set of blocks in front of the user"""
from mcpi import minecraft, vec3
import numpy as np
import logging
log = logging.getLogger(__name__)
from . import expose
from .commands import V
from . import entity
from . import uniqueblocks
from . import blocks

def roughly_forward(direction):
    """Given a direction, figure out cartesian forward"""
    dx,dy,dz = direction
    if dx and dz:
        adx = np.abs(dx)
        adz = np.abs(dz)
        if adx > adz:
            if dx > 0:
                forward = vec3.Vec3(1,0,0)
            else:
                forward = vec3.Vec3(-1,0,0)
        else:
            if dz > 0:
                forward = vec3.Vec3(0,0,1)
            else:
                forward = vec3.Vec3(0,0,-1)
    else:
        forward = vec3.Vec3(0,1,0)
    return forward

@expose.expose()
def bulldoze(depth=10,width=6,height=2,material=blocks.AIR,*,user=None,mc=None):
    """Set blocks ahead of the user to the given material

    This (loosely) aligns the block of material with the direction
    the user is currently facing, so it wipes out whatever
    is in front of you.
    """
    x,y,z = position = user.position
    material = blocks.Block.as_instance(material)
    direction = user.direction

    forward = roughly_forward(direction)
    if forward == vec3.Vec3(0,1,0):
        cross = vec3.Vec3(1,0,0)
    else:
        cross = vec3.Vec3(*tuple(forward)[::-1])

    start = position+ forward + (-cross * (width//2))
    stop = start + (cross*width) + (forward*depth) + (vec3.Vec3(0,1,0)*height)

    mc.setBlocks(
        *start,
        *stop,
        material
    )
