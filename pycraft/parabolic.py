"""Draw a parabolic dome over the user"""
from mcpi import block, minecraft
import numpy as np
from . import expose

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
    positions = [
        coord(angle)
        for angle in np.arange(
            0,
            2*np.pi,
            (2*np.pi)/(steps)
        )
    ]
    for (x,y,z) in positions:
        # print([round(x),round(y),round(z)])
        mc.setBlock(
            x,y,z,
            block,
        )

@expose.expose(name='p_dome')
def draw_parabolic_dome(
    center, 
    height, 
    relaxation=4, 
    material=block.STAINED_GLASS,
    start_angle=0,
    stop_angle=np.pi*2,
    steps = None,
    *,
    mc=None
):
    """Draw a parabolic dome at given bottom-center and height
    
    A parabolic dome is created with:

        radius = sqrt(y*relaxation)
    
    where each y-level is rendered with circle() and
    with invert the whole structure to get a dome
    instead of a cup...
    """
    yes  = np.arange(1,height+1)
    zes = np.sqrt(yes*relaxation)
    yes = yes
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
