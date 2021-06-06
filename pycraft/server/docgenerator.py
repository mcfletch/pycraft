"""Generate documentation by introspecting exposed API"""
import logging, asyncio, pprint, time, os, inspect
from pycraft.server.proxyobjects import ProxyMethod, type_coerce
from . import world, proxyobjects, channel

HERE = os.path.dirname(__file__)
DEFAULT_TARGET = os.path.join(HERE, '..', '..', 'pycraft-server', 'docs')
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
    return f'[{name}](./{name}.md)'


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

    return f'{indent}* {description["name"]}({", ".join(arg_types)}) => {return_type}'


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
        '# [PycraftServer](https://github.com/mcfletch/pycraft-server) Exposed Namespaces',
        '',
    ]

    for key, cls in sorted(proxyobjects.PROXY_TYPES.items()):
        index.append(
            f'* class {cls_link(cls.__name__)}({", ".join([cls_link(interface) for interface in cls.interfaces])})'
        )
        if not isinstance(cls, proxyobjects.ServerObjectMeta):
            continue

        if cls.interfaces:
            interfaces = [
                '## Implements',
            ] + [f'* {cls_link(interface)}' for interface in cls.interfaces]
        else:
            interfaces = []

        page = (
            [
                f'# [PycraftServer](./README.md) Proxy {cls.__name__}',
                '',
            ]
            + interfaces
            + [
                '',
                '## Proxy Methods',
                '',
            ]
        )
        for key, value in sorted(cls.__dict__.items()):
            if isinstance(value, proxyobjects.ProxyMethod):
                # print(f'    def {key}():')
                page.extend(describe_proxy_method(key, value, cls))
            elif inspect.ismethod(value):
                page.append(f'* {key} = {value.__doc__}')
        page.extend(['', f'Generated {time.strftime("%Y-%m-%d")}'])
        twrite(os.path.join(output, f'{cls.__name__}.md'), "\n".join(page))

    index.extend(['', f'Generated {time.strftime("%Y-%m-%d")}'])
    twrite(os.path.join(output, 'README.md'), '\n'.join(index))


def main():
    logging.basicConfig(level=logging.DEBUG)
    asyncio.get_event_loop().run_until_complete(generate_docs())


if __name__ == "__main__":
    main()
