"""Entity (including player) manipulation and metadata"""
import functools, types, logging, typing
from mcpi import minecraft, vec3, connection, entity as mc_entity
from .lockedmc import with_lock_held
from . import fuzzymatch
import numpy as np
log = logging.getLogger(__name__)

ENTITY_NAMES = {}
ENTITY_IDS = {}
class Entity(object):
    """Hold a reference to an entity id on an EntityAPI
    
    type_id values can be found at:

        https://mcreator.net/wiki/entity-ids
    
    """
    @classmethod
    def as_instance(cls, id):
        """Coerce given value to an instance of the cls"""
        if isinstance(id, mc_entity.Entity):
            return cls(id.id)
        if isinstance(id, Entity):
            return id
        if isinstance(id, str):
            if id in ENTITY_NAMES:
                return ENTITY_NAMES[id]
            else:
                return fuzzymatch.resolve_name(
                    id,
                    ENTITY_NAMES
                )
        if id in ENTITY_IDS:
            return ENTITY_IDS[id]
        raise NameError(
            id,
            'Unable to find an Entity with an id of %r'%(id,)
        )
    def __init__(
        self, 
        id: int, 
        type_id: int=None, 
        type_name:str = None,
        position:vec3.Vec3 = None,
        name: str = None,
        *,
        api: 'EntityAPI' = None
    ):
        self.api = api
        self.id = id 
        self.type_id = type_id 
        self.type_name = type_name
        self._position = position
        self._name = name
    def __int__(self):
        return self.id
    def __eq__(self,rhs):
        return self.id == int(rhs)
    def __str__(self):
        if self.type_id:
            return self.type_name
        return self.get_name()
    def __repr__(self):
        return '%s(%s)'%(
            self.__class__.__name__,
            ", ".join([
                repr(x)
                for x in [
                    self.id,
                    self.type_id,
                    self.type_name,
                    self.position,
                    self.get_name(),
                ]
            ])
        )
    def get_name(self) -> str:
        if self._name:
            return self._name
        return self.api.get_entity_name(self.id)
    def get_position(self) -> vec3.Vec3:
        if self._position is not None:
            return self._position
        return self.api.get_entity_position(self.id)
    def get_direction(self) -> vec3.Vec3:
        """On Java edition, get the direction the user is facing"""
        return self.api.get_entity_direction(self.id)
    def set_direction(self, direction:vec3.Vec3):
        """On java edition, set the direction the user is facing"""
        return self.api.set_entity_direction(self.id,direction)
    def set_position(self, position: vec3.Vec3):
        """On Java edition, set the entity's position"""
        self.api.set_entity_position(self.id, position)
        self._position = position
    def get_rotation(self):
        """Get current rotation in radians"""
        return self.api.get_entity_rotation(self.id)
    def set_rotation(self,radians):
        """Set current rotation in radians"""
        self.api.set_entity_rotation(self.id,radians)
    name = property(get_name)
    position = property(get_position,set_position)
    direction = property(get_direction,set_direction)
    rotation = property(get_rotation,set_rotation)
    def get_nearby_entities(self, type_id:int=-1, distance:int=10 ):
        """Get the entities near this entity (e.g. Player)"""
        return self.api.get_nearby_entities(
            self.id,
            distance=distance,
            type_id=type_id,
        )
    def remove_nearby_entities(self, type_id:int=-1, distance:int=10):
        """Destroy all entities within distance blocks of the given type"""
        removed = []
        for entity in self.get_nearby_entities(type_id=type_id,distance=distance):
            removed.append(entity.name)
            self.api.remove_entity(entity.id)
        return removed


class EntityAPI(object):
    """Provide a lock-protected API around mcpi connection"""
    def __init__(self, mc:minecraft.Minecraft):
        self.name_cache = {}
        self.mc = mc 
    
    @with_lock_held
    def players(self) -> typing.List[Entity]:
        """Retrieve the list of Player Entities from the server
        """
        try:
            return [
                Entity(id,api=self) 
                for id in self.mc.getPlayerEntityIds()
            ]
        except connection.RequestError as err:
            # unfortunately, not a lot of metadata provided by err...
            # and it produces an error even if there's just
            # no one currently connected...
            return []

    @functools.lru_cache(maxsize=256)
    @with_lock_held
    def get_entity_name(self, entity: int) -> str:
        """Get username for the given user"""
        current = self.mc.entity.getName(
            entity
        )
        log.debug("Entity %s => %s", entity, current)
        return current
    @with_lock_held
    def get_entity_position(self, entity: int):
        """Get entity position"""
        return self.mc.entity.getPos(entity)
    @with_lock_held
    def set_entity_position(self, entity: int, position: vec3.Vec3):
        """Get entity position"""
        return self.mc.entity.setPos(entity, position)
    @with_lock_held
    def get_entity_tile_position(self, entity: int) -> vec3.Vec3:
        return self.mc.entity.getTilePos(entity)
    @with_lock_held
    def get_entity_direction(self, entity: int) -> vec3.Vec3:
        return self.mc.entity.getDirection(entity)
    @with_lock_held
    def get_entity_rotation(self, entity: int) -> float:
        return self.mc.entity.getRotation(entity)/360*(np.pi*2)
    @with_lock_held
    def set_entity_rotation(self, entity: int, rotation:float):
        return self.mc.entity.setRotation(entity,rotation/(np.pi*2)*360)

    @with_lock_held
    def get_nearby_entities(self, entity:int, distance: int=10, type_id=-1):
        """Return the set of entities near given entity"""
        if type_id != -1:
            type_id = Entity.as_instance(
                type_id,
            )
        records = self.mc.entity.getEntities(
            entity,
            int(distance),
            type_id,
        )
        entities = [
            Entity(
                id=id,
                type_id=type_id,
                type_name=type_name,
                position=vec3.Vec3(x,y,z),
                api=self,
            )
            for (id,type_id,type_name,x,y,z) in records
        ]
        return entities

    @with_lock_held
    def remove_nearby_entities(self, entity:int, distance:int=10, type_id:int=-1):
        if type_id != -1:
            type_id = Entity.as_instance(
                type_id,
            )
        return self.mc.entity.removeEntities(entity,distance,type_id)

    @with_lock_held
    def remove_entity(self, entity:int):
        """Remove a specific entity from the game
        
        Note: is a *direct* operation on the connection,
        not going through mcpi
        """
        self.mc.conn.send(
            b'world.removeEntity',
            entity,
        )

for _key,_value in mc_entity.__dict__.items():
    if isinstance(_value,mc_entity.Entity):
        ENTITY_NAMES[_key] = _value

ENTITY_NAMES['ITEM'] = mc_entity.Entity(1,'ITEM')
ENTITY_NAMES['XP_ORB'] = ENTITY_NAMES['EXPERIENCE_ORB']
ENTITY_NAMES['LEASH_KNOT'] = ENTITY_NAMES['LEASH_HITCH']
ENTITY_NAMES['EYE_OF_ENDER_SIGNAL'] = ENTITY_NAMES['ENDER_SIGNAL']
ENTITY_NAMES['POTION'] = mc_entity.Entity(16,'POTION')
ENTITY_NAMES['XP_BOTTLE'] = ENTITY_NAMES['THROWN_EXP_BOTTLE']
ENTITY_NAMES['TNT'] = ENTITY_NAMES['PRIMED_TNT']
ENTITY_NAMES['FALLING_BLOCK'] = mc_entity.Entity(21,'FALLING_BLOCK')
ENTITY_NAMES['FIREWORKS_ROCKET'] = mc_entity.Entity(22,'FIREWORKS_ROCKET')
ENTITY_NAMES['EVOCATION_FANGS'] = ENTITY_NAMES['EVOKER_FANGS']
ENTITY_NAMES['EVOCATION_ILLAGER'] = ENTITY_NAMES['EVOKER']
ENTITY_NAMES['VINDICATION_ILLAGER'] = ENTITY_NAMES['VINDICATOR']
ENTITY_NAMES['ILLUSION_ILLAGER'] = ENTITY_NAMES['ILLUSIONER']
ENTITY_NAMES['COMMANDBLOCK_MINECART'] = ENTITY_NAMES['MINECART_COMMAND']
ENTITY_NAMES['CHEST_MINECART'] = ENTITY_NAMES['MINECART_CHEST']
ENTITY_NAMES['FURNACE_MINECART'] = ENTITY_NAMES['MINECART_FURNACE']
ENTITY_NAMES['TNT_MINECART'] = ENTITY_NAMES['MINECART_TNT']
ENTITY_NAMES['HOPPER_MINECART'] = ENTITY_NAMES['MINECART_HOPPER']
ENTITY_NAMES['SPAWNER_MINECART'] = ENTITY_NAMES['MINECART_MOB_SPAWNER']
ENTITY_NAMES['ZOMBIE_PIGMAN'] = ENTITY_NAMES['PIG_ZOMBIE']
ENTITY_NAMES['MOOSHROOM'] = ENTITY_NAMES['MUSHROOM_COW']
ENTITY_NAMES['VILLAGER_GOLEM'] = ENTITY_NAMES['IRON_GOLEM']


# ENTITY_IDS = {_value.id:_key for (_key,_value) in ENTITY_NAMES.items()}
# def check_missing_ids():
#     missing = False
#     for line in WIKI_DATA.splitlines():
#         try:
#             (_,name,_,type_id) = line.split('\t')
#             name = name.upper()
#             id = int(type_id)
#             if name not in ENTITY_NAMES:
#                 missing = True
#                 if id in ENTITY_IDS:
#                     print(f'ENTITY_NAMES[{repr(name)}] = ENTITY_NAMES[{repr(ENTITY_IDS[id])}]')
#                 else:
#                     print(f'ENTITY_NAMES[{repr(name)}] = mc_entity.Entity({id},{repr(name)})')
#         except Exception as err:
#             err.args += (line,)
#             raise
#     assert not missing
# check_missing_ids()
