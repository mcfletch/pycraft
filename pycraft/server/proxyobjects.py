"""Models RPC proxied objects on the server"""
import typing
import uuid
import logging
import sys
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
OVERRIDE_TYPES = {
    # Namespace:str => ProxyObject override class...
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
    if isinstance(typ, str):
        if typ.startswith('final.'):
            typ = typ[6:]
        typ = PROXY_TYPES.get(typ[6:], typ)
        if isinstance(typ, str):
            # test cases where we have not introspected...
            from . import world

            typ = getattr(world, typ)
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
        yield cls
        # if cls:
        #     for s_cls in _get_interfaces(cls, seen=seen):
        #         yield s_cls


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
                        ),
                        '__module__': 'pycraft.server.final',
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

    if value is None:
        return None
    if typ is None:
        return value
    elif typ in (str, float, int, uuid.UUID):
        return typ(value)
    elif typ in (np.ndarray,):
        # Not ideal to assume 'd' type
        return np.array(value, dtype='d')
    if hasattr(typing, 'ForwardRef') and isinstance(typ, typing.ForwardRef):
        # Yuck, why can't typing make an api that's actually usable???
        if sys.version_info >= (3, 10):
            typ = typ._evaluate(PROXY_TYPES, PROXY_CLASSES, set())
        else:
            typ = typ._evaluate(PROXY_TYPES, PROXY_CLASSES)
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
        self.__doc__ = description.get('__doc__')
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
        self.__name__ = method.__name__

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
        except Exception as e:
            e.args += (
                cls,
                struct,
            )
            raise
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
            typ = self._prop_typ(key)
            if typ:
                setattr(self, key, type_coerce(value, typ))
            else:
                setattr(self, key, value)

    @classmethod
    def _prop_typ(cls, key):
        for src in cls.mro():
            annot = getattr(src, '__annotations__', None)
            if annot and key in annot:
                return annot[key]
        return None

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
    def as_type(self, typ):
        """Return this object coerced to given type"""
        if isinstance(typ, str):
            if typ in PROXY_TYPES:
                typ = PROXY_TYPES[typ]
            elif typ in PROXY_CLASSES:
                typ = PROXY_CLASSES[typ]
        return type_coerce(self.__dict__.copy(), typ)


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


def OverrideType(cls):
    """Register a particular class as an ObjectProxy sub-type"""
    OVERRIDE_TYPES[cls.__namespace__] = cls
    for clsName in getattr(cls, '__known_classes__', ()):
        OVERRIDE_TYPES[clsName] = cls
    return cls


def filter_star_mro(superinterfaces):
    """If a super-interface is in the MRO of another superinterface, filter out that interface"""
    result = []
    reversed = superinterfaces[::-1]

    def is_duplicate(iface, rest):
        for other in rest:
            if issubclass(other, iface):
                return True
        return False

    for i, iface in enumerate(reversed):
        if not is_duplicate(iface, reversed[i + 1 :]):
            result.append(iface)
    return result


async def construct_one_interface(declaration, definition_map, seen_classes):
    """Construct a single class recursively defining any super-interfaces"""

    try:
        name = declaration['name']
    except KeyError:
        raise KeyError('name', declaration)

    if name in seen_classes:
        return seen_classes[name]
    # if declaration.get('cls') and declaration.get('cls').get('interfaces'):
    #     bases = declaration.get('cls').get('interfaces')
    # else:
    #     bases = []
    base = ServerObjectProxy
    clsDeclaration = declaration.get('cls')
    if clsDeclaration:
        if name == 'World':
            # TODO: broken introspection here, doesn't show up under test, but on real instance
            # World shows up as an isKeyed...
            clsDeclaration['isKeyed'] = False
        if clsDeclaration.get('isKeyed'):
            log.info("Keyed type: %s", name)
            base = KeyedServerObjectEnum
        elif clsDeclaration.get('isEnum'):
            base = ServerObjectEnum
        interface_names = [
            x
            for x in clsDeclaration.get('interfaces', ())
            if (x != name) and (x in definition_map)
        ]
        super_interfaces = [
            x
            for x in [
                await construct_one_interface(
                    definition_map.get(interface),
                    definition_map=definition_map,
                    seen_classes=seen_classes,
                )
                for interface in interface_names
            ]
        ]
    else:
        super_interfaces = []
    super_interfaces.append(base)
    overrides = OVERRIDE_TYPES.get(name)
    if overrides:
        super_interfaces.insert(0, overrides)

    try:
        cls = PROXY_TYPES[name] = type(
            name,
            tuple(super_interfaces),
            {
                '__namespace__': name,
                '__module__': 'pycraft.server.introspection',
                '__declaration__': declaration,
                '__interfaces__': clsDeclaration.get('interfaces', [])
                if clsDeclaration
                else [],
            },
        )
    except TypeError as err:
        raise TypeError(
            '%s Inheritence messed up: %s'
            % (name, '\n'.join([str(s.mro()) for s in super_interfaces]))
        )

    seen_classes[name] = cls
    return cls


async def construct_from_introspection(automatic: dict, channel):
    """Create introspected api from automatic query on server"""
    from . import final

    seen_classes = {}
    unfinished = [
        x
        for x in automatic.get('commands', [])
        if (isinstance(x, dict) and x.get('type') == 'namespace')
    ]

    definition_map = {}
    for declaration in unfinished:
        try:
            name = declaration['name']
        except KeyError:
            raise KeyError('name', declaration)
        else:
            definition_map[name] = declaration

    for declaration in unfinished:
        await construct_one_interface(
            declaration, definition_map=definition_map, seen_classes=seen_classes
        )

    ProxyMethod.set_channel(channel)
    for name, proxy in seen_classes.items():
        proxy.inject_methods(channel, proxy.__declaration__)
        PROXY_TYPES[name] = proxy
        setattr(final, name, proxy)

    for name, proxy in seen_classes.items():
        mapping = getattr(proxy, '__annotations__', {})
        for key, typ in list(mapping.items()):
            if isinstance(typ, str):
                if typ.startswith('final.'):
                    value = PROXY_TYPES[typ[6:]]
                    mapping[key] = value
