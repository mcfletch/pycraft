import numpy as np
import logging 
log = logging.getLogger(__name__)

def unique_blocks_only(gen):
    """Filter generated blocks so that API only sees unique blocks"""
    seen = set()
    count = 0
    for item in gen:
        key = tuple([int(x) for x in item])
        if key not in seen:
            seen.add(key)
            yield item
        count += 1
    # log.info("%s/%s were unique blocks",len(seen),count)