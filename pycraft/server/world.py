import typing
import uuid
import logging
import numpy as np
from .proxyobjects import ProxyMethod, ServerObjectProxy, ProxyType, ServerObjectEnum


log = logging.getLogger(__name__)


@ProxyType
class Enchantment(ServerObjectEnum):
    __namespace__ = 'Enchantment'


@ProxyType
class Material(ServerObjectEnum):
    __namespace__ = 'Material'


@ProxyType
class EntityType(ServerObjectEnum):
    __namespace__ = 'EntityType'


@ProxyType
class Biome(ServerObjectEnum):
    __namespace__ = 'Biome'


@ProxyType
class BlockFace(ServerObjectEnum):
    __namespace__ = 'BlockFace'


@ProxyType
class PistonMoveReaction(ServerObjectEnum):
    __namespace__ = 'PistonMoveReaction'


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
        if isinstance(record, Location):
            record = record.__json__()
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
        other = np.array(other, dtype='d')
        x, y, z = self.vector[:3] + other
        return Location([self.world, x, y, z, self.yaw, self.pitch])

    def block_location(self):
        return Location(
            [self.world, round(self.x, 0), round(self.y, 0), round(self.z, 0)]
        )


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

    key = None

    def get_key(self):
        return self.key


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
    holder: typing.Union[Entity, Player, Block, BlockData, None]
    firstEmpty: int

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
