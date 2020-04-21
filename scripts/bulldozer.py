from mcpi import block, minecraft
import numpy as np

def bulldozer(mc, position, size=8):
    x,y,z = position
    top_left = x-size,y+1+size,z+size
    bottom_right = x+size,y+1,z-size
    mc.setBlocks(*top_left,*bottom_right,block.AIR)

def main():
    mc = minecraft.Minecraft.create()
    # players = [1,2,3]
    for player in mc.getPlayerEntityIds():
        position = mc.entity.getPos(player)
        bulldozer(mc,position)
    
if __name__ == "__main__":
    main()
