"""Draw a parabolic dome over the user"""
from mcpi import block, minecraft
import numpy as np
from . import expose, uniqueblocks

@expose.expose(name='circle')
def draw_circle(
    center,
    radius,
    block=block.STONE,
    start_angle=0,
    stop_angle=np.pi*2,
    steps = None,
    *,
    mc=None
):
    """Draw a horizontal circle around center with radius"""
    x,y,z = center
    steps = steps or radius * 20
    def coord(angle):
        return (
            x+(np.sin(angle)*radius),
            y,
            z+(np.cos(angle)*radius),
        )
    positions = uniqueblocks.unique_blocks_only([
        coord(angle)
        for angle in np.arange(
            0,
            2*np.pi,
            (2*np.pi)/(steps)
        )
    ])
    for (x,y,z) in positions:
        # print([round(x),round(y),round(z)])
        mc.setBlock(
            x,y,z,
            block,
        )

@expose.expose(name='p_dome')
def parabolic_dome(
    center=None, 
    height=10, 
    relaxation=4, 
    material=block.STAINED_GLASS,
    start_angle=0,
    stop_angle=np.pi*2,
    steps = None,
    *,
    mc=None,
    user=None,
):
    """Draw a parabolic dome at given bottom-center and height
    
    A parabolic dome is created with:

        radius = sqrt(y*relaxation)
    
    where each y-level is rendered with circle() and
    with invert the whole structure to get a dome
    instead of a cup...

    center defaults to the user's current position
    """
    if center is None:
        center = user.position
    yes  = np.arange(1,height+1)
    zes = np.sqrt(yes*relaxation)
    yes = yes
    x,y,z = center
    for h,rad in zip(yes,zes):
        draw_circle((x,y+height-h,z),rad,block=material,mc=mc)

@expose.expose()
def dome(
    center=None,
    radius=10, 
    material=block.STAINED_GLASS,
    start_angle=0,
    stop_angle=np.pi*2,
    steps = None,
    *,
    mc=None,
    user=None,
):
    if center is None:
        center = user.position
    height = radius
    yes  = np.arange(1,radius+1)
    angles = np.arcsin(yes/radius)
    zes = np.cos(angles*radius)
    x,y,z = center
    for h,rad in zip(yes,zes):
        draw_circle((x,y+height-h,z),rad,block=material,mc=mc)


def main():
    mc = minecraft.Minecraft.create()
    # players = [1,2,3]
    for player in mc.getPlayerEntityIds():
        position = mc.entity.getPos(player)
        draw_parabolic_dome(position,20, mc=mc)
    
if __name__ == "__main__":
    main()
