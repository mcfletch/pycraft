"""Entity (including player) manipulation and metadata"""
import functools, types, logging, typing
from mcpi import minecraft, vec3, connection
from .lockedmc import with_lock_held
log = logging.getLogger(__name__)

class Entity(object):
    """Hold a reference to an entity id on an EntityAPI"""
    def __init__(self, api: 'EntityAPI', id: int):
        self.api = api
        self.id = id 
    def __int__(self):
        return self.id
    def __eq__(self,rhs):
        return self.id == int(rhs)
    def __str__(self):
        return self.get_name()
    def get_name(self) -> str:
        return self.api.get_entity_name(self.id)
    def get_position(self) -> vec3.Vec3:
        return self.api.get_entity_position(self.id)
    def get_direction(self) -> vec3.Vec3:
        """On Java edition, get the direction the user is facing"""
        return self.api.get_entity_direction(self.id)
    def set_position(self):
        """On Java edition, set the entity's position"""
        self.api.set_entity_position(self.id)
    name = property(get_name)
    position = property(get_position,set_position)
    direction = property(get_direction,)

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


