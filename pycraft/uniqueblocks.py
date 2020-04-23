import numpy as np

def unique_blocks_only(gen):
    """Filter generated blocks so that API only sees unique blocks"""
    seen = set()
    for item in gen:
        key = tuple([int(x) for x in item])
        if key not in seen:
            seen.add(key)
            yield item
