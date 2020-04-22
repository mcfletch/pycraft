from mcpi import block, minecraft
import numpy as np
import logging
log = logging.getLogger(__name__)
from . import expose
from .expose import V

@expose.expose()
def bulldoze(depth=10,width=6,height=2,material=block.AIR,*,user=None,mc=None):
    x,y,z = position = user.position
    direction = user.direction

    log.info("Position: %s", position)
    log.info("Direction: %s", direction)

    for to_clear in generate_blocks_ahead(
        V(x,y+1,z),
        direction,
        depth,
        width=width,
        height=height,
    ):
        # log.info("Clearing: %s", to_clear)
        mc.setBlock(*to_clear,material)

def generate_blocks_ahead(position,direction,depth,width,height):
    dx,dy,dz = direction
    forward = V(dx,0,dz)
    above = V(0,1,0)
    cross = V(dz,0,dx) # todo: properly calculate

    for step in range(1,depth):
        delta = forward * step
        for c_step in range(-((width+1)//2),((width+1)//2)):
            cdelta = cross * c_step 
            base = position + delta + cdelta 
            for h_step in range(height):
                hdelta = above * h_step
                yield base + hdelta

    # top_left = x-size,y+1+size,z+size
    # bottom_right = x+size,y+1,z-size
    # mc.setBlocks(*top_left,*bottom_right,block.AIR)

def main():
    mc = minecraft.Minecraft.create()
    # players = [1,2,3]
    for player in mc.getPlayerEntityIds():
        position = mc.entity.getPos(player)
        bulldozer(mc,position)
    
if __name__ == "__main__":
    main()
