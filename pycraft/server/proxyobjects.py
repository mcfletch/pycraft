"""Models RPC proxied objects on the server"""
import typing
import uuid
import logging
import numpy as np

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
    "Set": typing.Set,
    "String[]": typing.List[str],
    "void": bool,
}
PROXY_TYPES = {
    # Namespace:str => ProxyObject class
}

RETURN_TYPES = {}


def type_name_to_type(name):
    """Given java class simple name find the associated type"""
    if name in SIMPLE_TYPES:
        return SIMPLE_TYPES[name]
    elif name in PROXY_TYPES:
        return PROXY_TYPES[name]
    return None


def type_coerce(value, typ):
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
    if isinstance(value, dict) and '__type__' in value and '__namespace__' in value:
        if value['__type__'] in PROXY_TYPES:
            typ = PROXY_TYPES[value['__type__']]
            # return type_coerce(value, typ)
        elif value['__namespace__'] in PROXY_TYPES:
            typ = PROXY_TYPES[value['__namespace__']]
            # return type_coerce(value, typ)
        else:
            log.warning("No type for dictionary: %s", value)

    # if typ == world.Inventory.__annotations__['contents']:
    #     import pdb

    #     pdb.set_trace()
    if isinstance(typ, type):
        if issubclass(typ, typing.List):
            sub_type = typ.__args__[0]  # YUCK!
            return [type_coerce(item, sub_type) for item in value]
        elif issubclass(typ, typing.Dict):
            key_typ, value_typ = typ.__args__
            result = {}
            for key, value in value.items():
                result[type_coerce(key, key_typ)] = type_coerce(value, value_typ)
            return result
        else:
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
        RETURN_TYPES.setdefault(self.description.get('returntype'), []).append(
            self.__doc__
        )

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
        log.info("Call method: %s(%s)", method, ",".join([repr(x) for x in args]))

        result = await self.channel.call_remote(
            method,
            *args,
        )
        return_type_name = self.description.get('returntype')
        if return_type_name:
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


class ServerObjectProxy(object):
    """Object reference on the server which we are proxying"""

    @classmethod
    def from_server(cls, struct):
        """Convert server-side structure to local object"""
        # log.info("%s from server: %s", cls.__name__, struct)
        if not struct:
            return None
        instance = cls(**struct)
        return instance

    @classmethod
    def inject_methods(cls, channel, method_descriptions):
        """Inject the methods the server reports are available for this namespace"""
        for description in method_descriptions.get('commands', ()):
            if description.get('type') != 'method':
                continue
            method = ProxyMethod(description, cls.__namespace__)
            setattr(cls, method.__name__, method)

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

    def __init__(self, key):
        self.key = key

    def get_key(self):
        return self.key

    @classmethod
    def from_server(cls, key):
        return cls(key)


def ProxyType(cls):
    """Register a particular class as an ObjectProxy sub-type"""
    PROXY_TYPES[cls.__namespace__] = cls
    for clsName in getattr(cls, '__known_classes__', ()):
        PROXY_TYPES[clsName] = cls
    return cls