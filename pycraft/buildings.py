"""Draw a parabolic dome over the user"""
from mcpi import block, minecraft, vec3
import numpy as np
import random, os
import logging
from . import expose, blocks, uniqueblocks
HERE = os.path.dirname(os.path.abspath(__file__))
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
    """Create pyramid centered at position in material
    
    position -- center of the pyramid
    width -- size in the x direction
    depth -- size in the y direction
    material -- name of the material to use 
    zstep -- 1 for upward, -1 for downward
    """
    if position is None:
        position = user.position + vec3.Vec3(0,0,depth//2 + 1)
    material = expose.as_block(material)
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
    floor_material = expose.as_block(floor_material)
    carpet_material = expose.as_block(carpet_material)
    wall_material = expose.as_block(wall_material)
    roof_material = expose.as_block(roof_material)

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

@expose.expose()
def from_template(template,*,mc=None):
    """Load a template file from disk and render as blocks"""
    # Your code here...


def load_template(template, abbreviations=None):
    """Find template file, load it into memory as block-names

    Templates as in `CSV` format, which is a 
    plain-text format that looks like this:

        S,S,D,S,S
        S, , , ,S
        S,S,G,S,S
        -
        S,S,D,S,S
        S, , , ,S
        S,S,G,S,S

    where a bunch of abbreviations are available
    for common types, but full block-names can
    be used as well.

    CSV is a common format, find pre-existing code
    (a module) for reading the CSV information.

    To read the template, you'll need to find the 
    file on disk. Given a filename `filename`, the
    final location would be:

        os.path.join(HERE,'templates',os.path.basename(filename))
    
    You will need to pass the CSV module a `file` object
    which you get by calling `open` on the filename
    above.

    The csv module will give you a sequence of rows from
    your spreadsheet, like `['S','S','D','S','S']` which
    you can iterate over with a `for` loop.

    You will need to separate the rows into layers by
    looking for the `-` value in the first column
    of the row (`row[0]`). How will you gather the
    rows into layers?

    You will need to translate abbreviations into
    full block-names to pass them to the server.
    To do that, you'll need to setup a `mapping`
    from each abbreviation to its full block-name.

    Mappings in Python are generally written with
    `{}` characters and are called `dicts`. So a 
    mapping might look like:

        abbreviations = {
            'S': 'STONE',
            'G': 'WHITE_STAINED_GLASS',
        }

    You can find `_blocknames.py` in this project
    which includes all of the block names that are
    currently known to work with the server.
    
    return should be [
        layer,
        layer,
        layer,
    ]
    layer being [
        [name,name,name],
        [name,name,name],
    ]
    """