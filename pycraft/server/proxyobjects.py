"""Models RPC proxied objects on the server"""
import typing
import uuid
import logging
import numpy as np
from asyncstdlib.functools import lru_cache
from functools import wraps

log = logging.getLogger(__name__)

SIMPLE_TYPES = {
    "long": int,
    "int": int,
    "short": int,
    "double": float,
    "float": float,
    "boolean": bool,
    "String": str,
    # "Set": set,
    # "Map": dict,
    "UUID": uuid.UUID,
    "List": typing.List,
    "Collection": typing.List,
    "Set": typing.Set,
    "String[]": typing.List[str],
    "void": bool,
    'java.util.List<java.util.List<java.lang.String>>': typing.List[typing.List[str]],
}
PROXY_CLASSES = {
    # Implementation Class name (CraftSkeleton) => final python class with all interfaces...
}
PROXY_TYPES = {
    # Namespace:str => ProxyObject class
}
PROXY_RELATIONS = {
    # Name: {ParentName...}
}

# RETURN_TYPES = {}


def type_name_to_type(name):
    """Given java class simple name find the associated type"""
    if name in SIMPLE_TYPES:
        return SIMPLE_TYPES[name]
    elif name in PROXY_TYPES:
        return PROXY_TYPES[name]
    return None


def type_coerce(value, typ):
    try:
        return _type_coerce(value, typ)
    except Exception as err:
        err.args += (typ, value)
        raise


def _get_interfaces(base, seen=None):
    """Given an interface, iteratively find all super-interfaces"""
    seen = seen or set()
    yield base
    for iface_name in getattr(base, 'interfaces'):
        if iface_name in seen:
            continue
        seen.add(iface_name)
        cls = PROXY_TYPES.get(iface_name)
        if cls:
            for s_cls in _get_interfaces(cls, seen=seen):
                yield s_cls


def _dict_cls(value):
    if isinstance(value, dict) and '__type__' in value and '__namespace__' in value:
        cls_key = value['__type__']
        if cls_key not in PROXY_CLASSES:
            # Construct a new class with the interfaces as parents...
            base = _dict_typ(value)
            if base:
                PROXY_CLASSES[cls_key] = type(
                    cls_key,
                    tuple(
                        _get_interfaces(base),
                    ),
                    {
                        '__doc__': '''Server Side Proxy object representing a %s instance with %s interface'''
                        % (
                            cls_key,
                            base.__name__,
                        )
                    },
                )
            else:
                log.warning(
                    "Unable to create a wrapper class for %s from %s", cls_key, value
                )
                return None
        return PROXY_CLASSES[cls_key]
    else:
        return None


def _dict_typ(value):
    typ = None

    if isinstance(value, dict) and '__type__' in value and '__namespace__' in value:
        if value['__type__'] in PROXY_TYPES:
            typ = PROXY_TYPES[value['__type__']]
            # return type_coerce(value, typ)
        elif '.' in value['__type__'] and value['__type__'].split('.') in PROXY_TYPES:
            typ = PROXY_TYPES[value['__type__'].split('.')]
        elif value['__namespace__'] in PROXY_TYPES:
            typ = PROXY_TYPES[value['__namespace__']]
            # return type_coerce(value, typ)
        else:
            log.warning("No type for dictionary: %s", value)
    return typ


def is_a_typing_list(typ):
    if typ.__class__ == getattr(typing, '_GenericAlias', None):
        if typ._name == 'List':
            # YUCK!
            # Python 3.8, using internal damn class name
            return True
    elif isinstance(typ, type) and issubclass(typ, typing.List):
        # Python 3.6, but crashes on Python 3.8
        return True
    return False


def is_a_typing_dict(typ):
    if typ.__class__ == getattr(typing, '_GenericAlias', None):
        if typ._name == 'Dict':
            # YUCK!
            # Python 3.8, using internal damn class name
            return True
    elif isinstance(typ, type) and issubclass(typ, typing.Dict):
        # Python 3.6, but crashes on Python 3.8
        return True
    return False


def is_a_typing_union(typ):
    if typ.__class__ == getattr(typing, '_GenericAlias', None):
        if typ._name == None and hasattr(typ, '__args__'):
            return True
    return False


def _type_coerce(value, typ):
    """Attempt to coerce value to the given typ"""
    from . import world

    if value is None:
        return None
    if typ is None:
        return value
    elif typ in (str, float, int, uuid.UUID):
        return typ(value)
    elif typ in (np.ndarray,):
        # Not ideal to assume 'd' type
        return np.array(value, dtype='d')
    # typ = _dict_typ(value) or typ
    typ = _dict_cls(value) or typ

    if is_a_typing_list(typ):
        if typ.__args__:
            sub_type = typ.__args__[0]  # YUCK!
            return [type_coerce(item, sub_type) for item in value]
        else:
            log.warning("No sub-type on %s; dispatching on dict-types", typ)
            return [
                (type_coerce(item, _dict_typ(item)) if _dict_typ(item) else item)
                for item in value
            ]
    elif is_a_typing_dict(typ):
        key_typ, value_typ = typ.__args__
        result = {}
        for key, value in value.items():
            result[type_coerce(key, key_typ)] = type_coerce(value, value_typ)
        return result
    elif is_a_typing_union(typ):
        # WTF? Why can't I test for "is this a union"
        for possible in typ.__args__:
            if isinstance(value, possible):
                return value
        for possible in typ.__args__:
            try:
                return type_coerce(value, possible)
            except (ValueError, TypeError) as err:
                log.exception("Failed to convert")
        raise ValueError(
            "Union type %s we don't know how to convert %r"
            % (
                typ,
                value,
            )
        )

    elif isinstance(typ, type):
        if hasattr(typ, 'from_server'):
            return typ.from_server(value)
        else:
            return typ(value)
    raise ValueError(
        "Do not know how to convert type %s with value %r"
        % (
            typ,
            value,
        )
    )


class ProxyMethod(object):
    """Represents a callable entry point on the server"""

    @classmethod
    def set_channel(cls, channel):
        """Set the (singleton) channel reference"""
        cls.channel = channel

    def __init__(self, description, namespace):
        self.namespace = namespace
        self.description = description
        # self.__doc__ = description.get('__doc__')
        self.__name__ = description.get('name')
        # RETURN_TYPES.setdefault(self.description.get('returntype'), []).append(
        #     self.__doc__
        # )

    @property
    def return_type(self):
        return_type_name = self.description.get('returntype')
        if return_type_name:
            if return_type_name.endswith('[]'):
                base_type = type_name_to_type(return_type_name[:-2])
                return typing.List[base_type]
            return_type = type_name_to_type(return_type_name)
            if 'returntype_subtypes' in self.description:
                sub_types = tuple(
                    type_name_to_type(t)
                    for t in self.description['returntype_subtypes']
                )
                if None not in sub_types:
                    return_type = return_type[sub_types]
            return return_type
        return None

    @property
    def is_classmethod(self):
        return self.description.get('static')

    @property
    def argument_types(self):
        return self.description.get()

    def __get__(self, obj, objType=None):
        if self.description.get('static'):
            return self
        if obj is not None:
            return BoundProxyMethod(obj, self)
        else:
            return self

    def get_full_method(self):
        return '%s.%s' % (self.namespace, self.description.get('name'))

    async def __call__(self, *args):
        method = self.get_full_method()
        log.debug("Call method: %s(%s)", method, ",".join([repr(x) for x in args]))

        result = await self.channel.call_remote(
            method,
            *args,
        )
        return_type_name = self.description.get('returntype')
        if return_type_name:
            if return_type_name.endswith('[]'):
                base_type = type_name_to_type(return_type_name[:-2])
                return [type_coerce(r, base_type) for r in result]
            return_type = type_name_to_type(return_type_name)
            if 'returntype_subtypes' in self.description:
                sub_types = tuple(
                    type_name_to_type(t)
                    for t in self.description['returntype_subtypes']
                )
                if None not in sub_types:
                    return_type = return_type[sub_types]
            if return_type:
                result = type_coerce(result, return_type)
            else:
                log.warning(
                    "Return type %r unknown on %s %s",
                    return_type_name,
                    self.get_full_method(),
                    sorted(PROXY_TYPES.keys()),
                )
        return result


class MultiMethod(ProxyMethod):
    def __init__(self, description, namespace):
        self.multi = description
        super().__init__(description['commands'][0], namespace)


class BoundProxyMethod(object):
    def __init__(self, instance, method):
        if not hasattr(instance, 'get_key'):
            raise TypeError(
                "Can only operate on proxy objects with get_key() defined, got %s"
                % (instance,)
            )
        self.instance = instance

        self.method = method
        self.__doc__ = method.__doc__

    async def __call__(self, *args):
        return await self.method(
            self.instance.get_key(),
            *args,
        )


class ServerObjectMeta(type):
    # def __getattr__(cls, key):
    #     interfaces = cls.__interfaces__
    #     for interface_name in interfaces:
    #         src_cls = PROXY_TYPES.get(interface_name)
    #         if src_cls is not None and src_cls is not cls:
    #             result = getattr(src_cls, key, None)
    #             if result is not None:
    #                 log.info('Found in method on %s: %s', interface_name, key)
    #                 return result
    #     raise AttributeError(key)

    def implements(cls, interface):
        """Does the given cls implement interface name?"""
        if isinstance(interface, type):
            interface = interface.__namespace__
        if interface in cls.__interfaces__:
            return True
        for implemented in cls.__interfaces__:
            target = PROXY_TYPES.get(implemented)
            if target is not None:
                if target.implements(interface):
                    return True
        return False

    def get_subclass(cls, interfaces):
        """Given a cls, determine if interfaces contains a subclass we can prefer to this cls"""

        for interface_name in interfaces:
            interface = PROXY_TYPES.get(interface_name)
            if interface and interface.implements(cls):
                return interface
        return cls


class ServerObjectProxy(metaclass=ServerObjectMeta):
    """Object reference on the server which we are proxying"""

    # __metaclass__ = ServerObjectMeta

    @classmethod
    def from_server(cls, struct):
        """Convert server-side structure to local object"""
        # log.info("%s from server: %s", cls.__name__, struct)
        if not struct:
            return None
        try:
            instance = cls(**struct)
        except TypeError as err:
            import pdb

            pdb.set_trace()
            raise
        else:
            return instance

    __interfaces__ = ()
    __cached_methods__ = None

    @classmethod
    def inject_methods(cls, channel, method_descriptions):
        """Inject the methods the server reports are available for this namespace"""
        to_cache = cls.__cached_methods__ or set()
        for description in method_descriptions.get('commands', ()):
            if description.get('type') not in ('method', 'multidispatch'):
                continue
            if description.get('type') == 'multidispatch':
                method = MultiMethod(description, cls.__namespace__)
            else:
                method = ProxyMethod(description, cls.__namespace__)
            # if description.get('name') in to_cache:
            #     method = lru_cache(maxsize=1024)(method)
            setattr(cls, method.__name__, method)
        if 'cls' in method_descriptions:
            cls.interfaces = method_descriptions['cls'].get('interfaces', [])
            if cls.__namespace__ != cls.__name__:
                cls.interfaces.append(cls.__namespace__)
            for interface in cls.interfaces:
                PROXY_RELATIONS.setdefault(interface, set()).add(cls.__namespace__)
                # log.info(
                #     "Class %s implements %s",
                #     cls.__namespace__,
                #     interface,
                # )

    def __init__(self, **named):
        """Set each named key/value as an attribute on object"""
        for key, value in named.items():
            typ = getattr(self, '__annotations__', {}).get(key)
            if typ:
                setattr(self, key, type_coerce(value, typ))
            else:
                setattr(self, key, value)

    def __str__(self):
        return '%s(%s)' % (
            self.__class__.__name__,
            ','.join(
                [
                    '%s=%r'
                    % (
                        key,
                        value if not isinstance(value, uuid.UUID) else str(value),
                    )
                    for key, value in self.__dict__.items()
                ]
            ),
        )

    __repr__ = __str__
    # def __repr__(self):
    #     return repr(self.get_key())


class ServerObjectEnum(ServerObjectProxy):
    """Holder for an enumeration where the enumeration's key is used to lookup the value"""

    key: str

    @classmethod
    @lru_cache(maxsize=1)
    async def values(cls):
        """Get the enumerated values in this class"""
        result = []
        for key in await ProxyMethod.channel.call_remote(
            "%s.values" % (cls.__namespace__,),
        ):
            result.append(cls(key=key))
        return result

    def __init__(self, key):
        self.key = key

    def get_key(self):
        return self.key

    @classmethod
    def from_server(cls, key):
        return cls(key)

    __cached__ = None

    @classmethod
    async def cached_values(cls):
        """Get the cached values for the given enumeration"""
        if cls.__cached__ is None:
            cls.__cached__ = await cls.values()
        return cls.__cached__

    @classmethod
    async def loosely_match(cls, name):
        possible = []
        for value in await cls.cached_values():
            key = getattr(value, 'key', None)
            if key and name in key:
                possible.append(value)
        return possible


class KeyedServerObjectEnum(ServerObjectEnum):
    """Namespaced/keyed enumerations"""

    def __init__(self, key):
        if ':' not in key:
            key = 'minecraft:%s' % (key,)
        return super().__init__(key)

    def __json__(self):
        return self.key


def ProxyType(cls):
    """Register a particular class as an ObjectProxy sub-type"""
    PROXY_TYPES[cls.__namespace__] = cls
    for clsName in getattr(cls, '__known_classes__', ()):
        PROXY_TYPES[clsName] = cls
    return cls
