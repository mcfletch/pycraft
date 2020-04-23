"""Entity (including player) manipulation and metadata"""
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


def generate_names():
    if not os.path.exists('items.tsv'):
        import requests
        response = requests.get(UPSTREAM_URL)
        response.raise_for_status()
        content = response.text 
        with open('items.tsv','w') as fh:
            fh.write(content)
    import csv, pprint
    records = []
    for id,data,full_name,type_name in csv.reader(open('items.tsv'),delimiter='\t'):
        records.append((
            int(id),
            int(data),
            full_name.upper().replace('(','').replace(')','').replace(' ','_'),
            type_name.upper()
        ))
    content = f'''
# Generated from {UPSTREAM_URL}
_DATA = {pprint.pformat(records)}'''
    with open('_blocknames.py','w') as fh:
        fh.write(content)

if __name__ == "__main__":
    generate_names()
else:
    _fill_in_names()
