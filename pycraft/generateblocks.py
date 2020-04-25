"""Generate block definitions from upstream datafile and introspection"""
from mcpi import minecraft, connection
import requests
import logging, os
from pycraft._eblock import Block
HERE = os.path.dirname(os.path.abspath(__file__))
UPSTREAM_URL = 'https://minecraft-ids.grahamedgecombe.com/items.tsv'
log = logging.getLogger(__name__)

def find_supported_blocks(records, mc=None):
    """Given list of all blocks, see what the server lets us create"""
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

def generate_eblocks(records):
    """Generate set of Enhanced Blocks in blocks.py"""
    TARGET = os.path.join(HERE,'blocks.py')
    blocks = [
        Block(id,data,name.replace("'","_"),type_name)
        for (id,data,name,type_name) in sorted(records)
    ]
    formatted = "\n".join([
        f'{block.name} = {repr(block)}'
        for block in blocks
    ])
    content = f'''"""Auto-generated set of enhanced blocks known to java edition servers
    
Upstream data-set: {UPSTREAM_URL}
"""
from ._eblock import Block, BLOCK_NAMES
{formatted}
'''
    with open(TARGET,'w') as fh:
        fh.write(content)

def generate_names():
    HERE = os.path.abspath(os.path.dirname(__file__))
    SOURCE = os.path.join(HERE,'items.tsv')
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
            full_name.upper()
            .replace("'",'_')
            .replace('-','_')
            .replace('(','')
            .replace(')','')
            .replace(' ','_'),
            type_name.upper()
        ))
    records = list(records)
    records = find_supported_blocks(records)
    return records

def main():
    logging.basicConfig(level=logging.INFO)
    generate_eblocks(
        generate_names()
    )
