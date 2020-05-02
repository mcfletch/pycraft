from pycraft.expose import expose
from mcpi import minecraft 
from pycraft import blocks
import os
HERE=os.path.dirname(os.path.abspath(__file__)) 
FARM=os.path.join(HERE,'THOMSONS B-DAY FARM - Sheet1.csv')
legend={
    'S':'STONE',
    'F':'OAK_FENCE',
    'G':'GLASS',
    'GP':'GLASS_PANE',
    'LL':'LAPIS_LAZULI_BLOCK',
    'W':'OAK_WOOD',
    'D':'ACACIA_DOOR_BLOCK',
    '':'AIR',
    'T':'TORCH',
    'CH--':'CHEST',
    'FUR':'FURNACE',
    'CT':'CRAFTING_TABLE',
}

@expose()
def bday_farm(*,mc=None,position=None,user=None,file=FARM):
    if position==None:
        position=user.position
    slices=[]
    slice=[]
    slices.append(slice)
    for line in open(file):
        collums=line.strip().split(',')
        if collums[0]=='-':
            print('slice')
            slice=[]
            slices.append(slice)
        else:
            t=[]
            for block in collums:
                tb=legend[block]
                t.append(tb)
            slice.append(t)
    # print(slices)
    x,y,z=position
    for yup,slice in enumerate(slices):
        for zup,row in enumerate(slice):
            for xup,block in enumerate(row):
                bee=getattr(blocks,block)
                mc.setBlock(x+xup,y+yup,z+zup,bee)
if __name__=='__main__':
    mc=minecraft.Minecraft.create('192.168.15.32')
    bday_farm(mc,position=(-5,1,-67))