import typing
import uuid
import logging
import numpy as np
from .proxyobjects import ServerObjectProxy, ProxyType


log = logging.getLogger(__name__)


@ProxyType
class Vector(object):
    __namespace__ = 'Vector'
    vector: np.ndarray

    def get_key(self):
        return self.__json__()

    def __init__(self, record):
        self.vector = np.array(record, dtype='d')

    def __json__(self):
        return list(self.vector)

    @property
    def x(self):
        return self.vector[0]

    @x.setter
    def x(self, value):
        self.vector[0] = value

    @property
    def y(self):
        return self.vector[1]

    @x.setter
    def y(self, value):
        self.vector[1] = value

    @property
    def z(self):
        return self.vector[2]

    @x.setter
    def z(self, value):
        self.vector[2] = value


@ProxyType
class Location(object):
    __namespace__ = 'Location'
    world: str
    vector: np.ndarray

    def get_key(self):
        return self.__json__()

    def __init__(self, record):
        if len(record) == 6:
            world, x, y, z, yaw, pitch = record
        else:
            world, x, y, z = record
            yaw = pitch = 0.0
        self.world = world
        self.vector = np.array([x, y, z, yaw, pitch], dtype='d')

    def __json__(self):
        base = list(self.vector)
        base.insert(0, self.world)
        return base

    @property
    def x(self):
        return self.vector[0]

    @x.setter
    def x(self, value):
        self.vector[0] = value

    @property
    def y(self):
        return self.vector[1]

    @x.setter
    def y(self, value):
        self.vector[1] = value

    @property
    def z(self):
        return self.vector[2]

    @x.setter
    def z(self, value):
        self.vector[2] = value

    @property
    def yaw(self):
        return self.vector[3]

    @yaw.setter
    def yaw(self, value):
        self.vector[3] = yaw

    @property
    def pitch(self):
        return self.vector[4]

    @pitch.setter
    def pitch(self, value):
        self.vector[4] = value

    def __str__(self):
        return '[%s,%s]' % (
            repr(self.world),
            ','.join([str(x) for x in self.vector]),
        )

    __repr__ = __str__


@ProxyType
class Entity(ServerObjectProxy):
    """A particular entity, such as a mob, or item stack on the server"""

    def __json__(self):
        return self.uuid

    __namespace__ = 'Entity'
    world: str
    location: Location
    uuid: uuid.UUID
    type: str
    name: str
    display_name: str

    def get_key(self):
        return self.uuid


@ProxyType
class Player(Entity):
    """A particular player (potentially not currently logged in) on the server"""

    def __json__(self):
        return self.uuid

    __namespace__ = 'Player'

    world: str
    location: Location
    uuid: uuid.UUID
    type: str
    name: str
    display_name: str
    last_played: float

    def get_key(self):
        return self.uuid


@ProxyType
class OfflinePlayer(Player):
    __namespace__ = 'OfflinePlayer'


@ProxyType
class World(ServerObjectProxy):
    """A particular world on the server"""

    def __json__(self):
        return self.name

    __namespace__ = 'World'
    name: str
    players: typing.List[Player]
    type: str

    def get_key(self):
        return self.name


@ProxyType
class Server(ServerObjectProxy):
    """Proxy for the server API"""

    def get_key(self):
        return "server"

    def __json__(self):
        return self.version

    __namespace__ = 'Server'
    version: str
    pycraft_version: str
    worlds: typing.List[World]

    channel: object


@ProxyType
class ItemStack(ServerObjectProxy):
    __namespace__ = 'ItemStack'


@ProxyType
class BlockData(ServerObjectProxy):
    """Data describing a particular block (or a potential block)"""

    def __init__(self, string_value):
        super().__init__(string_value=string_value)

    def __json__(self):
        return self.string_value

    __namespace__ = 'BlockData'
    string_value: str

    def get_key(self):
        return self.string_value


@ProxyType
class Inventory(ServerObjectProxy):
    __namespace__ = 'Inventory'
    __known_classes__ = ['PlayerInventory']

    type: str
    inventoryType: str
    size: int
    contents: typing.List[ItemStack]
    holder: typing.Union[Entity, Player, BlockData, None]
    firstEmpty: int

    def get_key(self):
        if isinstance(self.holder, Player) or isinstance(self.holder, Entity):
            return self.holder.uuid
        elif isinstance(self.holder, BlockData):
            return self.holder.location
        raise RuntimeError(
            "Can't calculate the key of an inventory that doesn't belong to something",
            self,
        )


# @ProxyType
# class PlayerInventory(Inventory):
#     __namespace__ = 'PlayerInventory'
# @ProxyType
# class ChestInventory(Inventory):
#     __namespace__ = 'PlayerInventory'


class Enum(ServerObjectProxy):
    def __init__(self, name):
        super().__init__(name=name)

    def get_key(self):
        return self.name

    def __json__(self):
        return self.name


ENUM_CLASSES = [
    'BlockFace',
    'Material',
    'Difficulty',
    'EntityType',
    'EntityCategory',
    'Entity',
    'Advancement',
    'WeatherType',
    'WarningState',
    'Pose',
    'PistonMoveReaction',
    'PotionEffect',
]


def known_enums():
    for name in ENUM_CLASSES:
        enum_class = ProxyType(
            type(
                name,
                (Enum,),
                {
                    '__namespace__': name,
                },
            )
        )
        setattr(Enum, name, enum_class)
