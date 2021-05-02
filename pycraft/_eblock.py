"""Slightly enhanced Block with name and parent tracking"""
from mcpi import block as mc_block
import random
from . import fuzzymatch

BLOCK_NAMES = {}
BLOCK_KEYS = {}


class Block(mc_block.Block, object):
    """Block that shows name and knows about sub-types

    Known block types are created in `eblocks.py`
    from introspecting on the server what is available
    Same-id-and-data blocks return the same block.
    A name passed as id will return the named block.
    """

    id = None
    data = None
    _sub_types = None
    name = None
    type_name = None

    @classmethod
    def as_instance(cls, id, data=None):
        """Coerce given value to an instance of the cls"""
        if isinstance(id, Block):
            return id
        if isinstance(id, str):
            if id in BLOCK_NAMES:
                return BLOCK_NAMES[id]
            else:
                return fuzzymatch.resolve_name(id, BLOCK_NAMES)
        elif hasattr(id, '__iter__') and data is None:
            id, data = id

        for possible_key in [(id, data), (id, 0)]:
            if possible_key in BLOCK_KEYS:
                return BLOCK_KEYS[possible_key]
        raise ValueError("Unable to find Block with type %s: %s" % (id, data))

    def __init__(self, id, data=0, name=None, type_name=None):
        super(Block, self).__init__(id, data)
        if name is not None:
            self.name = name
            BLOCK_NAMES[name] = self
        if type_name is not None:
            self.type_name = type_name
        key = (id, data)
        if key not in BLOCK_KEYS:
            # only do registration one time...
            BLOCK_KEYS[key] = self
            if data > 0:
                parent = self.parent
                if parent:
                    parent.add_child(self)
                else:
                    raise ValueError(
                        'Block %s %s %s does not have a parent block type'
                        % (
                            id,
                            data,
                            name,
                        )
                    )
            else:
                if type_name not in BLOCK_NAMES:
                    BLOCK_NAMES[type_name] = self

    def __repr__(self):
        return "%s(%d, %d, name=%r, type_name=%r)" % (
            self.__class__.__name__,
            self.id,
            self.data,
            self.name,
            self.type_name,
        )

    def add_child(self, child):
        """Add a child-type to this (root) type"""
        self.sub_types.append(child)

    @property
    def sub_types(self):
        if self._sub_types is None:
            if self.data == 0:
                self._sub_types = []
            else:
                return self.parent.sub_types
        return self._sub_types

    @sub_types.setter
    def sub_types(self, value):
        self._sub_types = value

    @property
    def parent(self):
        return BLOCK_KEYS.get((self.id, 0))

    def random_subtype(self):
        if not self.sub_types:
            parent = self.parent
            if parent and parent.sub_types:
                r = RandomSubtype(
                    self.id,
                    0,
                    self.type_name,
                )
                r.sub_types = parent.sub_types
                return
            return self
        r = RandomSubtype(
            self.id,
            0,
            self.type_name,
        )
        r.sub_types = self.sub_types
        return r


class RandomSubtype(Block):
    """Return a random sub-type of a Block"""

    @property
    def data(self):
        return random.choice(self.sub_types).data

    @data.setter
    def data(self, value):
        pass
