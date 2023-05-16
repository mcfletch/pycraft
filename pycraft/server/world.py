import typing
import uuid
import logging
import numpy as np
from .proxyobjects import (
    PROXY_TYPES,
    ProxyMethod,
    ServerObjectProxy,
    OverrideType,
    ServerObjectEnum,
    KeyedServerObjectEnum,
)
from . import final
from pycraft.server import proxyobjects


log = logging.getLogger(__name__)


@OverrideType
class Art(KeyedServerObjectEnum):
    __namespace__ = 'Art'


@OverrideType
class Fluid(KeyedServerObjectEnum):
    __namespace__ = 'Fluid'


@OverrideType
class Sound(KeyedServerObjectEnum):
    __namespace__ = 'Sound'


@OverrideType
class Statistic(KeyedServerObjectEnum):
    __namespace__ = 'Statistic'


@OverrideType
class TreeType(ServerObjectEnum):
    __namespace__ = 'TreeType'


@OverrideType
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


@OverrideType
class Material(KeyedServerObjectEnum):
    __namespace__ = 'Material'


@OverrideType
class EntityType(KeyedServerObjectEnum):
    __namespace__ = 'EntityType'


@OverrideType
class Biome(KeyedServerObjectEnum):
    __namespace__ = 'Biome'


@OverrideType
class BlockFace(KeyedServerObjectEnum):
    __namespace__ = 'BlockFace'


@OverrideType
class PistonMoveReaction(KeyedServerObjectEnum):
    __namespace__ = 'PistonMoveReaction'


@OverrideType
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

    def __json__(self) -> np.ndarray:
        return list(self.vector)

    def __len__(self) -> int:
        return len(self.vector)

    def __iter__(self) -> np.ScalarType:
        for item in self.vector:
            yield item

    def __getitem__(self, slice):
        return self.vector.__getitem__(slice)

    def __add__(self, other) -> 'Vector':
        return Vector(self.vector.copy() + other[:3])

    def __sub__(self, other) -> 'Vector':
        return Vector(self.vector.copy() - other[:3])

    def __eq__(self, other) -> bool:
        if isinstance(other, (Vector, Location)):
            return np.allclose(self.vector, other.vector[:3])
        else:
            return np.allclose(self.vector, other)

    def __neg__(self) -> 'Vector':
        return Vector(-self.vector)

    def __mul__(self, other) -> 'Vector':
        if isinstance(other, (Vector, Location)):
            other = other.vector[:3]
        return Vector(self.vector * other)

    def __div__(self, other) -> 'Vector':
        if isinstance(other, (Vector, Location)):
            other = other.vector[:3]
        return Vector(self.vector / other)

    def __floordiv__(self, other) -> 'Vector':
        if isinstance(other, (Vector, Location)):
            other = other.vector[:3]
        return Vector(self.vector // other)

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


@OverrideType
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
        return (
            final.World(name=self.world)
            if hasattr(final, 'World')
            else World(name=self.world)
        )

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
                "Expected a Location, a [world,x,y,z,yaw,pitch], a [world,x,y,z], [world,[x,y,z]] or [world,[x,y,z,pitch,yaw]] value, got: %s (length %s)"
                % (record, len(record))
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

    def __hash__(self):
        return hash((self.world, tuple(self.vector)))

    def __getitem__(self, slice):
        return self.vector.copy().__getitem__(slice)

    def __floor__(self):
        return self.__class__([self.world, np.floor(self.vector)])

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
        return '[%s, %s]' % (
            repr(self.world),
            ', '.join([str(round(x, 3)) for x in self.vector]),
        )

    def __repr__(self):
        return '[%s,%s]' % (
            repr(self.world),
            ','.join([str(x) for x in self.vector]),
        )

    def __add__(self, other):
        if isinstance(other, (Vector, Location)):
            other = other.vector[:3]
        new_vector = self.vector.copy()
        new_vector[:3] += other[:3]
        return self.__class__([self.world, new_vector])

    def __sub__(self, other):
        if isinstance(other, (Vector, Location)):
            other = other.vector[:3]
        new_vector = self.vector.copy()
        new_vector[:3] -= other
        return self.__class__([self.world, new_vector])

    def block_location(self):
        """Get the block location (block address) for this location"""
        return self.__class__([self.world, np.floor(self.vector[:3])])

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


@OverrideType
class Entity(ServerObjectProxy):
    """A particular entity, such as a mob, or item stack on the server"""

    @classmethod
    def from_server(cls, named):
        interfaces = named.get('interfaces')
        if interfaces:
            subclass = cls.get_subclass(interfaces)
            if subclass:
                cls = subclass
        return cls(**named)

    def __json__(self):
        return self.uuid

    __namespace__ = 'Entity'
    world: str
    location: 'final.Location'
    uuid: uuid.UUID
    type: str
    name: str
    display_name: str

    def get_key(self):
        return self.uuid

    def position(self):
        return self.location

    async def set_location(self, location):
        """Set the user's position to the given location or vector"""
        if not isinstance(location, Location):
            location = Location(location)
        await self.teleport(location)

    @property
    def tile_position(self):
        return self.location.__floor__() - (0, 1, 0)

    @property
    def direction(self):
        """Get the direction (3-value array) the entity is facing"""
        return self.location.direction

    def tilt(self):
        """Get the rise/run 1 value float telling how far the entity's gaze rises/falls per unit of run"""
        return self.location.tilt()


proxyobjects.SIMPLE_TYPES["EntityType[]"] = typing.List[Entity]


@OverrideType
class OfflinePlayer(ServerObjectProxy):
    """Represents a user who is known to the server, but isn't necessarily online right now"""

    __namespace__ = 'OfflinePlayer'

    uuid: uuid.UUID
    name: str
    first_played: float
    last_played: float
    banned: bool
    online: bool
    whitelisted: bool

    def __json__(self):
        """Return the user's UUID as a reference"""
        return self.uuid

    @property
    def id(self):
        """Get our local unique key for referencing (uuid)"""
        return self.uuid


@OverrideType
class Player(Entity):
    """A particular player (potentially not currently logged in) on the server"""

    def __json__(self):
        """Return the user's UUID as a reference"""
        return self.uuid

    __namespace__ = 'Player'

    world: str
    location: 'final.Location'
    uuid: uuid.UUID
    type: str
    name: str
    banned: bool
    online: bool
    display_name: str
    first_played: float
    last_played: float

    def get_key(self):
        """Return our unique key for lookup on the server (uuid)"""
        return self.uuid

    @property
    def id(self):
        """Get our local unique key for referencing (uuid)"""
        return self.uuid

    @property
    def position(self):
        """Retrieve the location reported when this record was retrieved (not necessarily the *current* location)"""
        return self.location

    @property
    def direction(self):
        """Retrieve the direction reported when this record was retrieved (not necessarily the *current* direction)"""
        return self.location.direction

    @property
    def forward_and_cross(self):
        """Calculate the ordinal directions ahead and right for block-oriented operations"""
        from pycraft import directions

        forward, cross = directions.forward_and_cross(self.direction)
        return forward, cross

    @property
    def forward(self):
        """The cardinal x,z vector which is most closely aligned to forward from the player's current orientation"""
        return self.forward_and_cross[0]

    @property
    def back(self):
        """The cardinal x,z vector which is most closely aligned to backward from the player's current orientation"""
        return -self.forward_and_cross[0]

    backward = back

    @property
    def left(self):
        """The cardinal x,z vector which is most closely aligned to left from the player's current orientation"""
        return -self.forward_and_cross[1]

    @property
    def right(self):
        """The cardinal x,z vector which is most closely aligned to left from the player's current orientation"""
        return self.forward_and_cross[1]


@OverrideType
class OfflinePlayer(Player):
    __namespace__ = 'OfflinePlayer'


@OverrideType
class World(ServerObjectProxy):
    """A particular world on the server

    Worlds are referenced by their name, with the common worlds being:

    * 'world' -- known as the Overworld, this is the main world you start in
    * 'world_nether' -- the Nether is full of lava, magma and Piglins
    * 'world_the_end' -- the End is the boss-level for the Ender Dragon and is full of Endermen

    When referring to a world, you can use the string name of the world,
    or get a world with :py:meth:`pycraft.server.final.Server.getWorld`
    or :py:meth:`pycraft.server.final.Server.getWorlds`

    Example usage:

        server.getWorld('world')

    """

    def __json__(self):
        """Return the world's name as a reference"""
        return self.name

    def __init__(self, name=None, **named):
        """Initialise the world record, normally by name"""
        named['name'] = name
        super(World, self).__init__(**named)

    __namespace__ = 'World'
    name: str
    players: typing.List['Player']
    type: str

    def get_key(self):
        """Get the unique value which looks up the world (name)"""
        return self.name

    # Provide old-style apis to ease code reuse
    async def setBlock(self, x, y, z, material_or_blockdata):
        """Set a specific block in this world to given material (blockdata)

        Note: there is a far more flexible mechanism in
        async world.setBlockList(locations, materials) which
        should likely be preferred for any non-trivial tasks.
        """
        return await final.Block(
            location=Location([self.name, x, y, z]).block_location()
        ).setBlockData(material_or_blockdata)

    async def oldSetBlocks(self, sx, sy, sz, ex, ey, ez, material):
        """Use old style code for mcpi setBlocks

        Note: there is a far more flexible mechanism in
        async world.setBlockList(locations, materials) which
        should likely be preferred for any non-trivial tasks.
        """
        from ..directions import as_cube

        start, size = as_cube((sx, sy, sz), (ex, ey, ez))
        return await self.setBlocks(start, size, material)

    async def getBlockArray(self, start, end):
        """Get block array by start and end coordinates"""
        from .. import directions

        start, size = directions.as_cube(start, end)

        return await self.getBlocks(start, size)


@OverrideType
class Server(ServerObjectProxy):
    """Proxy for the server API"""

    def get_key(self):
        """Get the key to lookup the server (literal 'server')"""
        return "server"

    def __json__(self):
        return self.version

    __namespace__ = 'Server'
    version: str
    pycraft_version: str
    worlds: typing.List['World']

    channel: object


@OverrideType
class ItemStack(ServerObjectProxy):
    __namespace__ = 'ItemStack'
    material: 'Material'
    amount: int
    enchantments: typing.Dict['Enchantment', int]

    def __json__(self):
        return self.key

    key = None

    def get_key(self):
        return self.key

    async def getMeta(self):
        """Retrieve the ItemMeta and set it's key to our key..."""
        result = await self.getItemMeta()
        if result:
            result.key = self.key
        return result


@OverrideType
class ItemMeta(ServerObjectProxy):
    __namespace__ = 'ItemMeta'
    key: object = None

    def get_key(self):
        return self.key


@OverrideType
class AttributeModifier(ServerObjectProxy):
    __namespace__ = 'AttributeModifier'
    name: str
    amount: float
    operation: str
    uuid: uuid.UUID
    slot: str

    def __json__(self):
        base = {
            'name': self.name,
            'amount': self.amount,
            'operation': self.operation,
        }
        if hasattr(self, 'uuid'):
            base['uuid'] = self.uuid
        if hasattr(self, 'slot'):
            base['slog'] = self.slot
        return base


@OverrideType
class BlockData(ServerObjectProxy):
    """Data describing a particular block (or a potential block)"""

    @classmethod
    def from_server(cls, named):
        interfaces = named.get('interfaces')
        if interfaces:
            subclass = cls.get_subclass(interfaces)
            if subclass:
                cls = subclass
        return cls(**named)

    def __init__(self, string_value=None, **named):
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
    globals()[_name] = OverrideType(
        type(
            _name,
            (BlockData,),
            {
                '__namespace__': _name,
            },
        )
    )


@OverrideType
class Block(ServerObjectProxy):
    __namespace__ = 'Block'

    def get_key(self):
        return self.location

    data: BlockData
    location: Location


@OverrideType
class Inventory:
    __namespace__ = 'Inventory'
    __known_classes__ = []

    type: str
    inventoryType: str
    size: int
    contents: typing.List['ItemStack']
    holder: typing.Union['Entity', 'Player', 'Block', 'BlockData', 'Location', None]
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
            stack = final.ItemStack(key=[index, self.holder.get_key()])
        return stack


# @OverrideType
# class PlayerInventory(Inventory):
#     __namespace__ = 'PlayerInventory'
# @OverrideType
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
    # 'Entity',
    'Advancement',
    'WeatherType',
    'WarningState',
    'Pose',
    'PistonMoveReaction',
    'PotionEffect',
    'EquipmentSlot',
    'Action',
]
KEYED_CLASSES = []


def _known_enums():
    for name in ENUM_CLASSES:
        enum_class = OverrideType(
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


@OverrideType
class Event(ServerObjectProxy):
    __namespace__ = 'Event'
    type: str
    message: str
    block: 'Block'
    player: 'Player'
    item_in_hand: 'ItemStack'
    # hand: 'EquipmentSlot'
    exp_to_drop: int
    will_drop: bool
    can_build: bool
    block_against: 'Block'
    block_clicked: 'Block'
    block_face: 'BlockFace'
    block_placement: bool
    # action: 'Action'
    material: 'Material'
    # bed: 'Bed'
    # advancement: 'Advancement'

    entity: 'Entity'
    clicked_position: 'Location'


@OverrideType
class EntityEvent(ServerObjectProxy):
    __namespace__ = 'EntityEvent'
    entity: 'Entity'


@OverrideType
class EntityDamageByEntityEvent(ServerObjectProxy):
    __namespace__ = 'EntityDamageByEntityEvent'
    damager: 'Entity'


@OverrideType
class GameRule(ServerObjectProxy):
    __namespace__ = 'GameRule'

    @classmethod
    def from_server(cls, struct):
        """Convert server-side structure to local object"""
        if isinstance(struct, str):
            return cls(name=struct)
        else:
            return cls(**struct)

    def __init__(self, name):
        super().__init__(name=name)

    def get_key(self):
        return self.name

    def __json__(self):
        return self.name


# @OverrideType
# class Axolotl(Entity):
#     __namespace__ = 'Axolotl'

#     def get_key(self):
#         return self.uuid


@OverrideType
class PotionData(ServerObjectProxy):
    __namespace__ = 'PotionData'
    type: str
    upgraded: bool
    extended: bool

    def __json__(self):
        return {'type': self.type, 'upgraded': self.upgraded, 'extended': self.extended}
