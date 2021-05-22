import typing
import uuid
import logging
import numpy as np
from .proxyobjects import (
    PROXY_TYPES,
    ProxyMethod,
    ServerObjectProxy,
    ProxyType,
    ServerObjectEnum,
    KeyedServerObjectEnum,
)
from pycraft.server import proxyobjects


log = logging.getLogger(__name__)


@ProxyType
class Art(KeyedServerObjectEnum):
    __namespace__ = 'Art'


@ProxyType
class Fluid(KeyedServerObjectEnum):
    __namespace__ = 'Fluid'


@ProxyType
class Sound(KeyedServerObjectEnum):
    __namespace__ = 'Sound'


@ProxyType
class Statistic(KeyedServerObjectEnum):
    __namespace__ = 'Statistic'


@ProxyType
class Enchantment(KeyedServerObjectEnum):
    __namespace__ = 'Enchantment'
    __cached_methods__ = set(
        [
            'conflictsWith',
            'getItemTarget',
            'getKey',
            'getMaxLevel',
            'getName',
            'getStartLevel',
            'isTreasure',
            'toString',
        ]
    )


@ProxyType
class Material(KeyedServerObjectEnum):
    __namespace__ = 'Material'


@ProxyType
class EntityType(KeyedServerObjectEnum):
    __namespace__ = 'EntityType'


@ProxyType
class Biome(KeyedServerObjectEnum):
    __namespace__ = 'Biome'


@ProxyType
class BlockFace(KeyedServerObjectEnum):
    __namespace__ = 'BlockFace'


@ProxyType
class PistonMoveReaction(KeyedServerObjectEnum):
    __namespace__ = 'PistonMoveReaction'


@ProxyType
class Vector(ServerObjectProxy):
    __namespace__ = 'Vector'
    vector: np.ndarray

    @classmethod
    def from_server(cls, record):
        return cls(record)

    def get_key(self):
        return self.__json__()

    def __init__(self, record, *args):
        if isinstance(record, (int, float)) and args:
            record = (record,) + args
        self.vector = np.array(record[:3], dtype='d')

    def __json__(self):
        return list(self.vector)

    def __len__(self):
        return len(self.vector)

    def __getitem__(self, slice):
        return self.vector.__getitem__(slice)

    def __add__(self, other):
        return self.vector + other[:3]

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
class Location(ServerObjectProxy):
    __namespace__ = 'Location'
    world: str
    vector: np.ndarray

    @classmethod
    def from_server(cls, record):
        return cls(record)

    def get_key(self):
        return self.__json__()

    def get_world(self):
        return World(name=self.world)

    def __init__(self, record):
        if isinstance(record, Location):
            record = record.__json__()
        if len(record) == 2:  # world and vector..
            world = record[0]
            vector = record[1]
        elif len(record) == 6:
            world = record[0]
            vector = record[1:]
        elif len(record) == 4:
            world = record[0]
            vector = record[1:]
        else:
            raise TypeError(
                "Expected a Location, a [world,x,y,z,yaw,pitch], a [world,x,y,z], [world,[x,y,z]] or [world,[x,y,z,pitch,yaw]] value, got: %s"
                % (record)
            )
            world, x, y, z = record
            yaw = pitch = 0.0
        self.world = world.get_key() if hasattr(world, 'get_key') else world
        self.vector = np.zeros((5,), dtype='d')
        self.vector[: len(vector)] = vector

    def __json__(self):
        base = list(self.vector)
        base.insert(0, self.world)
        return base

    def __len__(self):
        return len(self.vector)

    def __getitem__(self, slice):
        return self.vector.__getitem__(slice)

    def __floor__(self):
        return Location([self.world, np.floor(self.vector)])

    @property
    def x(self):
        return self.vector[0]

    @x.setter
    def x(self, value):
        self.vector[0] = value

    @property
    def y(self):
        return self.vector[1]

    @y.setter
    def y(self, value):
        self.vector[1] = value

    @property
    def z(self):
        return self.vector[2]

    @z.setter
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

    def __add__(self, other):
        if isinstance(other, (Vector, Location)):
            other = other.vector[:3]
        new_vector = self.vector[:]
        new_vector[:3] += other
        return Location([self.world, new_vector])

    def block_location(self):
        """Get the block location (block address) for this location"""
        return Location([self.world, np.floor(self.vector[:3])])

    @property
    def direction(self):
        """Get the direction faced by this location"""
        angle_deg = self.yaw % 360
        angle_rad = -(angle_deg / 180 * np.pi)
        return np.array([np.sin(angle_rad), 0, np.cos(angle_rad)], dtype='d')

    def tilt(self):
        """Get the rise/run for the angle of the user's gaze

        This is basically "if you move forward 1 block, you should rise
        N blocks (or fall)
        """
        pitch = (self.pitch % 180) / 180 * np.pi
        if np.allclose(pitch, 0) or np.allclose(pitch, 180):
            return 0
        elif np.allclose(pitch, np.pi / 2) or np.allclose(pitch, -np.pi / 2):
            return 1
        return np.tan(pitch)


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

    def position(self):
        return self.location

    async def set_position(self, location):
        """Set the user's position to the given location or vector"""
        if not isinstance(location, Location):
            location = Location(location)
        self.teleport(location)

    def tile_position(self):
        return self.location.__floor__() - (0, 1, 0)

    def direction(self):
        """Get the direction (3-value array) the entity is facing"""
        return self.location.direction()

    def tilt(self):
        """Get the rise/run 1 value float telling how far the entity's gaze rises/falls per unit of run"""
        return self.location.tilt()


proxyobjects.SIMPLE_TYPES["EntityType[]"] = typing.List[Entity]


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

    @property
    def id(self):
        return self.uuid

    @property
    def position(self):
        return self.location

    @property
    def direction(self):
        return self.location.direction


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

    async def setBlock(self, vector, material_or_blockdata):
        """Set a specific block in this world to given material (blockdata)"""
        return await ProxyMethod.channel.call_remote(
            "World.setBlock", [self.name] + vector, material_or_blockdata
        )


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
    material: Material
    amount: int
    enchantments: typing.Dict[Enchantment, int]

    def __json__(self):
        return self.key

    key = None

    def get_key(self):
        return self.key


@ProxyType
class BlockData(ServerObjectProxy):
    """Data describing a particular block (or a potential block)"""

    @classmethod
    def from_server(cls, named):
        interfaces = named.get('interfaces')
        if interfaces:
            for interface in interfaces:
                if interface in PROXY_TYPES and PROXY_TYPES[interface] is not cls:
                    return PROXY_TYPES[interface].from_server(named)
        return cls(**named)

    def __init__(self, string_value, **named):
        super().__init__(string_value=string_value, **named)

    def __json__(self):
        return self.string_value

    __namespace__ = 'BlockData'
    string_value: str

    def get_key(self):
        return self.string_value


for _name in [
    "Bamboo",
    "Bed",
    "Beehive",
    "Bell",
    "BrewingStand",
    "BubbleColumn",
    "Cake",
    "Campfire",
    "Chain",
    "Chest",
    "Cocoa",
    "CommandBlock",
    "Comparator",
    "CoralWallFan",
    "DaylightDetector",
    "Dispenser",
    "Door",
    "EnderChest",
    "EndPortalFrame",
    "Farmland",
    "Fence",
    "Fire",
    "Furnace",
    "Gate",
    "GlassPane",
    "Grindstone",
    "Hopper",
    "Jigsaw",
    "Jukebox",
    "Ladder",
    "Lantern",
    "Leaves",
    "Lectern",
    "NoteBlock",
    "Observer",
    "Piston",
    "PistonHead",
    "RedstoneRail",
    "RedstoneWallTorch",
    "RedstoneWire",
    "Repeater",
    "RespawnAnchor",
    "Sapling",
    "Scaffolding",
    "SeaPickle",
    "Sign",
    "Slab",
    "Snow",
    "Stairs",
    "StructureBlock",
    "Switch",
    "TechnicalPiston",
    "TNT",
    "TrapDoor",
    "Tripwire",
    "TripwireHook",
    "TurtleEgg",
    "Wall",
    "WallSign",
]:
    globals()[_name] = ProxyType(
        type(
            _name,
            (BlockData,),
            {
                '__namespace__': _name,
            },
        )
    )


@ProxyType
class Block(ServerObjectProxy):
    __namespace__ = 'Block'

    def get_key(self):
        return self.location

    data: BlockData
    location: Location


@ProxyType
class Inventory(ServerObjectProxy):
    __namespace__ = 'Inventory'
    __known_classes__ = ['PlayerInventory', 'CraftInventoryPlayer']

    type: str
    inventoryType: str
    size: int
    contents: typing.List[ItemStack]
    holder: typing.Union[Entity, Player, Block, BlockData, Location, None]
    firstEmpty: int

    def empty_slots(self):
        """Local introspection to find empty content slots"""
        empty = []
        for index, stack in enumerate(self.contents):
            if stack is None:
                empty.append(index)
        return empty

    def __init__(self, *args, **named):
        super().__init__(*args, **named)
        for index, stack in enumerate(self.contents):
            if stack is not None:
                stack.key = [index, self.get_key()]

    def get_key(self):
        if isinstance(self.holder, Player) or isinstance(self.holder, Entity):
            return self.holder.uuid
        elif isinstance(self.holder, Block):
            return self.holder.location
        elif isinstance(self.holder, Location):
            return self.holder
        raise RuntimeError(
            "Can't calculate the key of an inventory that doesn't belong to something",
            self,
        )

    def get_stack(self, index):
        stack = self.contents[index]
        if stack is None:
            stack = ItemStack(key=[index, self.holder.get_key()])
        return stack


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

    __cached__ = None


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
KEYED_CLASSES = []


def _known_enums():
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


# _known_enums()


@ProxyType
class AsyncPlayerChatEvent(ServerObjectProxy):
    __namespace__ = 'Event'
    type: str
    message: str
    player: Player
