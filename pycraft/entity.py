"""Entity (including player) manipulation and metadata"""
import functools, types, logging, typing
from mcpi import minecraft, vec3, connection, entity as mc_entity
from .lockedmc import with_lock_held
log = logging.getLogger(__name__)

class Entity(object):
    """Hold a reference to an entity id on an EntityAPI
    
    type_id values can be found at:

        https://mcreator.net/wiki/entity-ids
    
    """
    def __init__(
        self, 
        api: 'EntityAPI', 
        id: int, 
        type_id: int=None, 
        type_name:str = None,
        position:vec3.Vec3 = None,
        name: str = None,
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
        return self.type_name or self.get_name()
    def __repr__(self):
        return '%s(%s)'%(
            self.__class__.__name__,
            ", ".join([
                repr(x)
                for x in [
                    self.id,
                    self.type_id,
                    self.type_name,
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
    def set_position(self, position: vec3.Vec3):
        """On Java edition, set the entity's position"""
        self.api.set_entity_position(self.id, position)
        self._position = position
    name = property(get_name)
    position = property(get_position,set_position)
    direction = property(get_direction,)
    def get_nearby_entities(self, distance:int=10, type_id:int=-1):
        """Get the entities near us"""
        return self.api.get_nearby_entities(
            self.id,
            distance=distance,
            type_id=type_id,
        )
    def remove_nearby_entities(self, distance:int=10, type_id:int=-1):
        """Destroy all entities within distance blocks"""
        return self.api.remove_nearby_entities(
            self.id,
            distance=distance,
            type_id=type_id,
        )


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
                Entity(id) for id in self.mc.getPlayerEntityIds()
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
    def get_nearby_entities(self, entity:int, distance: int=10, type_id=-1):
        """Return the set of entities near given entity"""
        records = self.mc.entity.getEntities(
            entity,
            int(distance),
            type_id,
        )
        entities = [
            Entity(
                self,id,
                type_id=type_id,
                type_name=type_name,
                position=vec3.Vec3(x,y,z),
            )
            for (id,type_id,type_name,x,y,z) in records
        ]
        return entities

    @with_lock_held
    def remove_nearby_entities(self, entity:int, distance:int=10, type_id:int=-1):
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