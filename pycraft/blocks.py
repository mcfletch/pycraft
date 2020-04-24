"""More extensive Block definitions"""
import logging, os
from mcpi import block as mc_block
log = logging.getLogger(__name__)

UPSTREAM_URL = 'https://minecraft-ids.grahamedgecombe.com/items.tsv'
BLOCK_NAMES = {}
def _fill_in_names():
    from . import _blocknames
    mc_names = {}
    for name,value in mc_block.__dict__.items():
        if isinstance(value,mc_block.Block):
            mc_names.setdefault((value.id,value.data),[]).append(name)
    for (id,data,full_name,type_name) in _blocknames._DATA:
        typ = mc_block.Block(id,data) # It really should store the name...
        BLOCK_NAMES[full_name] = typ 
        if data == 0:
            BLOCK_NAMES[type_name] = typ 
        key = (id,data)
        if key in mc_names:
            for name in mc_names[key]:
                BLOCK_NAMES[name] = typ 

def find_supported_blocks(records, mc=None):
    """Given list of all blocks, see what the server lets us create"""
    from mcpi import minecraft, connection
    if mc is None:
        mc = minecraft.Minecraft.create()
    result = []
    for (id,data,full_name,type_name) in records:
        position = (0,0,0)
        debug = '%s (%s,%s)'%(full_name,id,data)
        try:
            mc.setBlock(*position,id,data)
        except connection.RequestError as err:
            log.info("Cannot create: %s", debug)
        else:
            try:
                current = mc.getBlockWithData(*position)
            except connection.RequestError as err:
                log.info("Cannot retrieve: %s (likely legacy)", debug)
            else:
                if current.id != id:
                    log.info("No error, but didn't change: %s", debug)
                elif current.data != data:
                    log.info("No error, data doesn't match %s", debug)
                else:
                    result.append((id,data,full_name,type_name))
    return result


def generate_names():
    HERE = os.path.abspath(os.path.dirname(__file__))
    SOURCE = os.path.join(HERE,'items.tsv')
    TARGET = os.path.join(HERE,'_blocknames.py')
    log = logging.getLogger('generate-names')
    if not os.path.exists(SOURCE):
        import requests
        response = requests.get(UPSTREAM_URL)
        response.raise_for_status()
        content = response.text 
        with open(SOURCE,'w') as fh:
            fh.write(content)
    import csv, pprint
    records = []
    for id,data,full_name,type_name in csv.reader(open(SOURCE),delimiter='\t'):
        records.append((
            int(id),
            int(data),
            full_name.upper().replace('-','_').replace('(','').replace(')','').replace(' ','_'),
            type_name.upper()
        ))
    records = list(records)
    unfiltered = len(records)
    records = find_supported_blocks(records)
    if len(records) == unfiltered:
        import pdb;pdb.set_trace()
    content = f'''
# Generated from {UPSTREAM_URL}
_DATA = {pprint.pformat(records)}'''
    with open(TARGET,'w') as fh:
        fh.write(content)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    generate_names()
else:
    _fill_in_names()
