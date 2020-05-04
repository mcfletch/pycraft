#! /usr/bin/env python3
"""Query the server to pull all entity types/names"""
from mcpi import minecraft, entity
def main():
    mc = minecraft.Minecraft.create()
    ids = mc.getEntityTypes()
    known = set()
    for key,value in entity.__dict__.items():
        if isinstance(value,entity.Entity):
            known.add(value.id)
    unknown = [id for id in ids if id.id not in known]
    if unknown:
        print('Entity types supported on server but not known: %r'%(unknown))
if __name__ == "__main__":
    main()
    