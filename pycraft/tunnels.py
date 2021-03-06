"""Create building-like structures for users"""
from mcpi import minecraft, vec3
import numpy as np
import random, os
import logging
from . import expose, blocks, uniqueblocks, commands
from .bulldozer import roughly_forward
HERE = os.path.dirname(os.path.abspath(__file__))
log = logging.getLogger(__name__)

@expose.expose()
def tunnel(
    depth=25,
    width=3,
    height=3,
    walls=blocks.WHITE_CONCRETE,
    floor=blocks.WHITE_CONCRETE,
    ceiling=blocks.WHITE_CONCRETE,
    track=blocks.RAIL,
    position=None,
    direction=None,
    *, 
    user=None,
    user_storage=None,
    mc=None 
):
    """Create a pyramid centered at position in material
    
    position -- start position
    direction -- rough direction to go (must be a unit block direction)
    width -- size in the x direction
    depth -- size in the y direction
    material -- name of the material to use 
    zstep -- 1 for upward, -1 for downward
    """
    log.info("Psition %s direction %s", position, direction)

    if direction is None and position is None:
        storage = user_storage()
    if direction is None:
        direction = user.direction
    direction = roughly_forward(direction)
    if position is None:
        position = user.tile_position + direction
    direction = np.array(tuple(direction))
    position = np.array(tuple(position))
    if not direction[1]:
        cross = np.array(direction[::-1])
        up = np.array((0,1,0),dtype='f')
    else:
        cross = np.array([1,0,0],dtype='f')
        up = np.array([0,0,1],dtype='f')

    start = position + direction
    log.info("Start %s direction %s", start, direction)

    
    # walls...
    left_front_bottom = start + (cross * (-width//2-1)) - up
    right_front_bottom = left_front_bottom + (cross * (width + 2))
    left_back_top = left_front_bottom + (up*(height+2)) + (depth*direction)
    right_back_top = right_front_bottom + (up*(height+2)) + (depth*direction)

    wall_mat = blocks.Block.as_instance(walls)
    floor_mat = blocks.Block.as_instance(floor)
    ceiling_mat = blocks.Block.as_instance(ceiling)
    track_mat = blocks.Block.as_instance(track)

    mc.setBlocks(
        *left_front_bottom,
        *left_back_top,
        wall_mat,
    )
    mc.setBlocks(
        *right_front_bottom,
        *right_back_top,
        wall_mat,
    )
    inner_lfb = left_front_bottom+cross
    inner_lbt = left_back_top+cross 
    inner_rfb = right_front_bottom-cross 
    inner_rbt = right_back_top-cross
    # floor
    mc.setBlocks(
        *inner_lfb,
        *(inner_rfb+(direction*depth)),
        floor_mat,
    )
    mc.setBlocks(
        *inner_lbt,
        *inner_rbt-(direction*depth),
        ceiling_mat,
    )
    # carve out the inner space...
    mc.setBlocks(
        *(inner_lfb+up),
        *(inner_rbt-up),
        blocks.AIR,
    )    
    # now lay the track...
    track_start = (inner_lfb + (cross * (width//2))) + up
    mc.setBlocks(
        *track_start,
        *(track_start + direction*depth),
        track_mat,
    )

    TORCH_DIR = {
        (0,0,-1): 2,
        (0,0,1): 1,
        (1,0,0): 3,
        (-1,0,0): 4,

    }

    # setup some torches every once in a while...
    torch_pos = inner_lbt-(up) # one below ceiling...
    for step in range(0,depth,5):
        mc.setBlock(
            *(torch_pos-(direction*step)),
            blocks.TORCH.id,
            TORCH_DIR.get(tuple(direction),3),
        )
    
    # setup some windows so the users can see...
    window_pos = left_back_top-(up) # one below ceiling...
    glass_color = blocks.WHITE_STAINED_GLASS.random_subtype()

    for step in range(1,depth,5):
        window_depth = window_pos-(direction*step)
        mc.setBlocks(
            *(window_depth),
            *(window_depth-(up*2)),
            glass_color
        )
        mc.setBlocks(
            *(window_depth+(cross*(width+2))),
            *(window_depth-(up*2)+(cross*(width+2))),
            glass_color
        )
    user_storage()[TUNNEL_CONTINUE_KEY] = (
        width,
        height,
        walls,
        floor,
        ceiling,
        track,
        start+(direction*depth),
        direction,
    )

TUNNEL_CONTINUE_KEY = '__current_tunnel__'
@expose.expose()
def tunnel_continue(
    depth=25,
    *, 
    user=None,
    user_storage=None,
    mc=None 
):
    """Continue the previously started tunnel"""
    log.info("Starring")
    storage = user_storage()
    params = storage.get(TUNNEL_CONTINUE_KEY)
    if not params:
        return 'Sorry, I have forgotten where the tunnel was'
    return tunnel(depth,*params,user=user,user_storage=user_storage,mc=mc)
