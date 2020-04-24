"""Draw a parabolic dome over the user"""
from mcpi import block, minecraft, vec3
import numpy as np
import random
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
    endz = startz+depth 
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

@expose.expose()
def hall(
    position=None,
    width=8,
    depth=12,
    height=4,
    wall_material='STONE',
    floor_material='DARK_OAK_WOOD_SLAB',
    carpet_material='RED_CARPET',
    roof_material='RED_GLAZED_TERRACOTTA',
    *,
    mc=None,
    user=None,
):
    if position is None:
        position = user.position
    x,y,z = [int(c) for c in position]
    left = x - width//2
    right = left + width 
    front = z - depth //2
    back = front + depth 
    bottom = y-1
    top = y+height
    floor_material = expose.find_blocks(floor_material)
    carpet_material = expose.find_blocks(carpet_material)
    wall_material = expose.find_blocks(wall_material)
    roof_material = expose.find_blocks(roof_material)
    # clear 
    mc.setBlocks(
        left+1,bottom+1,front+1,
        right-1,top-1,back-1,
        block.AIR,
    )
    # subfloor...
    mc.setBlocks(
        left,bottom,front,
        right,bottom,back,
        floor_material,
    )
    if width > 4 and depth > 4:
        # Carpet on top...
        mc.setBlocks(
            left+2,y,front+2,
            right-2,y,back-2,
            carpet_material,
        )
    # walls...
    for start,stop in [
        ((left,bottom,front),(right,top,front)),
        ((left,bottom,front),(left,top,back)),
        ((left,bottom,back),(right,top,back)),
        ((right,bottom,front),(right,top,back)),
    ]:
        mc.setBlocks(
            *start,
            *stop,
            wall_material,
        )
    # front doorway
    front_blocks = width - 1
    log.info("Front blocks: %s", front_blocks)
    if front_blocks % 2:
        doorwidth = 1
    else:
        doorwidth = 2
    log.info("Width of %s means door width is %s", width, doorwidth)
    delta = (front_blocks - doorwidth)//2
    log.info("delta %s", delta)
    doorleft = left+delta+1
    mc.setBlocks(
        doorleft,bottom+1,front,
        doorleft+(doorwidth-1),bottom+3,front,
        block.AIR,
    )
    # Cornice...
    roofstart,roofstop = left-1,right+1
    roofy = top
    while roofstart <= roofstop:
        mc.setBlocks(
            roofstart,roofy,front-1,
            roofstart,roofy,back+1,
            roof_material,
        )
        mc.setBlocks(
            roofstop,roofy,front-1,
            roofstop,roofy,back+1,
            roof_material,
        )
        mc.setBlocks(
            roofstart+1,roofy,front,
            roofstop-1,roofy,front,
            wall_material,
        )
        mc.setBlocks(
            roofstart+1,roofy,back,
            roofstop-1,roofy,back,
            wall_material,
        )
        roofstart += 1
        roofstop -= 1
        roofy += 1
    
    # Torches...
    torches = []
    for step in range(front+2,back-2,3):
        torches.append(step)
        mc.setBlock(
            left+1,bottom+3,step,
            block.TORCH.id,
            1,
        )
        mc.setBlock(
            right-1,bottom+3,step,
            block.TORCH.id,
            2,
        )
        mc.setBlocks(
            left+1,top+1,step,
            right-1,top+1,step,
            block.WOODEN_SLAB,
        )
    for step in range(front+1,back-1):
        if not step in torches:
            mc.setBlocks(
                left,bottom+1,step,
                left,top-1,step,
                block.STAINED_GLASS.id,
                random.randint(0,15),
            )
            mc.setBlocks(
                right,bottom+1,step,
                right,top-1,step,
                block.STAINED_GLASS.id,
                random.randint(0,15),
            )
        


    # Facilities...
