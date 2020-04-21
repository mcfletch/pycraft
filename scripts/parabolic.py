"""Draw a parabolic dome over the user"""
from mcpi import block, minecraft
import numpy as np

def draw_circle(
    mc:minecraft.Minecraft,
    center,
    radius,
    block=block.STONE,
    start_angle=0,
    stop_angle=np.pi*2,
    steps = None
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
        print([round(x),round(y),round(z)])
        mc.setBlock(
            x,y,z,
            block,
        )

def draw_parabolic_dome(
    mc,
    center, 
    height, 
    relaxation=4, 
    material=block.STAINED_GLASS,
    start_angle=0,
    stop_angle=np.pi*2,
    steps = None
):
    """Draw a parabolic dome of given bottom-radius and height"""
    yes  = np.arange(1,height+1)
    zes = np.sqrt(yes*relaxation)
    yes = yes
    x,y,z = center
    for h,rad in zip(yes,zes):
        draw_circle(mc,(x,y+height-h,z),rad,block=material)

def main():
    mc = minecraft.Minecraft.create()
    for player in mc.getPlayerEntityIds():
        x,y,z = position = mc.entity.getPos(player)
        draw_parabolic_dome(mc,(x,y,z),20)
    
if __name__ == "__main__":
    main()
