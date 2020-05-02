from pycraft.expose import expose
from mcpi import minecraft 
from pycraft import blocks, fuzzymatch
import os, glob, logging 
log = logging.getLogger(__name__)
HERE=os.path.dirname(os.path.abspath(__file__)) 
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
TEMPLATES = {}
def scan_templates():
    """Look in the directory templates for all files named *.csv"""
    pattern = os.path.join(HERE,'templates','*.csv')
    log.debug("Scanning %s for templates", pattern)
    for filename in glob.glob(pattern):
        base = os.path.basename(filename)[:-4] # Take off the .csv
        log.info("Found template: %r", base)
        TEMPLATES[base] = filename
scan_templates()
TEMPLATE_NAMESPACE = fuzzymatch.FuzzyNamespace(TEMPLATES)

@expose()
def template(template='farm',position=None,*,mc=None,user=None):
    if position==None:
        position=user.position
    slices=[]
    slice=[]
    slices.append(slice)
    filename = getattr( TEMPLATE_NAMESPACE, template)
    for line in open(filename):
        columns=line.strip().split(',')
        if columns[0]=='-':
            print('slice')
            slice=[]
            slices.append(slice)
        else:
            t=[]
            for block in columns:
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
    template('farm',position=(-5,1,-67),mc=mc,)