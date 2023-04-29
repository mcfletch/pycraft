"""Generate documentation by introspecting exposed API"""
import logging, asyncio, pprint, time, os, inspect, types
from pycraft.server.proxyobjects import ProxyMethod, type_coerce
from . import world, proxyobjects, channel

HERE = os.path.dirname(__file__)
DEFAULT_TARGET = os.path.join(HERE, '..', '..', 'docs', 'source', 'generated')
log = logging.getLogger(__name__)


async def setup():
    server = channel.Channel(debug=False)
    await server.open()
    await server.introspect()
    return server


def twrite(filename, content):
    tmp = filename + '~'
    with open(tmp, 'w') as fh:
        fh.write(content)
    os.rename(tmp, filename)


def javadoc_url(full_name: str) -> str:
    transformed = full_name.replace('.', '/')
    return f'https://hub.spigotmc.org/javadocs/spigot/{transformed}.html'


CLASS_NAME_LOOKUP = {
    'void': None,
    'String': 'str',
    'boolean': 'bool',
    'Boolean': 'bool',
    'int': 'int',
    'Integer': 'int',
    'Double': 'float',
    'Float': 'float',
    'double': 'float',
    'float': 'float',
    'UUID': 'uuid.UUID',
    'java.util.List<java.util.List<java.lang.String>>': '[[BlockData,BlockData,...]]'
    # 'Set': 'list',
}


def cls_link(name, sub_type=None):
    if name in CLASS_NAME_LOOKUP:
        return CLASS_NAME_LOOKUP[name]
    elif name in ('List', 'Collection', 'Set') or name.endswith('[]'):
        if name.endswith('[]'):
            sub_type = [name[:-2]]
        if sub_type:
            return f'typing.List[{" | ".join([cls_link(typ) for typ in sub_type])}]'
        else:
            return 'list'
    result = f':doc:`./{name}`'
    # log.info("cls_link(%s) => %s", name, result)
    return result


def describe_python_method(method, indent=0):
    signature = inspect.signature(method)
    if inspect.isawaitable(method) or inspect.iscoroutinefunction(method):
        async_mark = 'async '
    else:
        async_mark = ''
    docs = [f'{" "*indent}* {async_mark}{method.__name__}{str(signature)}']
    if method.__doc__:
        docs.append('')
        doc_lines = inspect.cleandoc(method.__doc__).splitlines()
        for line in doc_lines:
            if line.strip():
                docs.append(
                    f'{" "*indent} {line}',
                )
            else:
                docs.append('')
    return docs


def describe_java_method(description, indent=0):
    """Describe a proxied java method"""
    if description.get('static'):
        self_arg = 'cls'
    else:
        self_arg = 'self'
    arg_types = [cls_link(n) for n in description.get('argtypes', [])]
    arg_types.insert(0, self_arg)
    return_type = cls_link(
        description.get('returntype'), description.get('returntype_subtypes')
    )
    indent = ' ' * indent

    return f'{indent}* async {description["name"]}({", ".join(arg_types)}) => {return_type}'


def describe_proxy_method(key, method, cls):
    """Describe a single proxy method for the user"""
    description = []

    if getattr(method, 'multi', None):
        description.append(f'* {key}:')
        for sub in method.multi.get('commands', ()):
            description.append(describe_java_method(sub, indent=4))
    else:
        description.append(describe_java_method(method.description))
    return description


async def generate_docs(output=DEFAULT_TARGET):
    server = await setup()
    index = [
        'pycraft.server.final',
        '=====================',
        '',
        '''The pycraft.server.final module contains the final classes representing the server-side
        proxy objects which follow the Java Bukkit API. The classes described here are Python classes,
        but with special proxy methods for calling into the related Java objects. The documentation
        here is mostly a reference as to what is exposed, while the Bukkit API documentation linked
        from each Proxy class's page provides details and semantics of what the methods do.
        ''',
    ]

    for key, cls in sorted(proxyobjects.PROXY_TYPES.items()):
        index.append(
            f'* class {cls_link(cls.__name__)} ( {", ".join([cls_link(interface) for interface in cls.interfaces])} )'
        )
        if not isinstance(cls, proxyobjects.ServerObjectMeta):
            continue

        if cls.__interfaces__:
            interfaces = [
                'Implements',
                '-----------',
                '',
            ] + [f'* {cls_link(interface)}' for interface in cls.__interfaces__]
        else:
            interfaces = []

        methods = [
            'Methods',
            '---------',
            '',
        ]
        null_methods = len(methods)
        properties = [
            'Properties',
            '----------',
            '',
        ]
        null_properties = len(properties)
        proxy_methods = [
            'Proxy Methods',
            '--------------',
            '',
        ]
        null_proxy = len(proxy_methods)
        for key, value in inspect.getmembers(cls):
            if isinstance(value, proxyobjects.ProxyMethod):
                # print(f'    def {key}():')
                proxy_methods.extend(describe_proxy_method(key, value, cls))
            elif inspect.isfunction(value) or inspect.ismethod(value):
                methods.extend(describe_python_method(value, 0))
            elif isinstance(value, property):
                properties.append(f'* {key} -- {value.__doc__}')
            elif key == 'values' and hasattr(value, 'cache_clear'):
                methods.append(
                    f'* {key}() -- (cached) set of values defined for the enumeration'
                )
            elif (
                key.startswith('__')
                and key.endswith('__')
                or key in ('interfaces', '_prop_typ')
            ):
                continue
            elif isinstance(value, (int, float, str, bytes, tuple, list, type(None))):
                properties.append(f'* {key} = {repr(value)}')
            else:
                raise KeyError(key, value)
            # else:
            #     print('Not a method: %s %s' % (key, type(value)))
        declaration = getattr(cls, '__declaration__', None)
        header = [
            f'{cls.__name__}',
            '================',
            '',
        ]
        if declaration:
            class_declaration = declaration.get('cls')
            if class_declaration:
                full_name = class_declaration['fullName']
                javadoc = javadoc_url(full_name)
                if javadoc:
                    header.extend(
                        [
                            f'Python Proxy to `{full_name} <{javadoc}>`_ from :py:module:`pycraft.server.final`',
                            '',
                        ]
                    )
            else:
                log.info("No cls declaration for %s", declaration)
        if cls.__doc__:
            header.extend(inspect.cleandoc(cls.__doc__).splitlines())

        page = (
            header
            + interfaces
            + (methods if len(methods) > null_methods else [])
            + (properties if len(properties) > null_properties else [])
            + (proxy_methods if len(proxy_methods) > null_proxy else [])
        )
        twrite(os.path.join(output, f'{cls.__name__}.rst'), "\n".join(page))

    index.extend(['', f'Generated {time.strftime("%Y-%m-%d")}'])
    twrite(os.path.join(output, 'index.rst'), '\n'.join(index))


def main():
    logging.basicConfig(level=logging.DEBUG)
    asyncio.get_event_loop().run_until_complete(generate_docs())


if __name__ == "__main__":
    main()
