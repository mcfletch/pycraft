"""Generate documentation by introspecting exposed API"""
import logging, asyncio, pprint, time, os, inspect
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
    docs = [f'{" "*indent}* `{method.__name__}{str(signature)}`']
    if method.__doc__:
        docs.append('')
        doc_lines = inspect.cleandoc(method.__doc__).splitlines()
        for line in doc_lines:
            if line.strip():
                docs.append(
                    f'{" "*indent}  ```{line}```',
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
        'Pycraft Proxy Objects',
        '=====================',
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
        proxy_methods = [
            'Proxy Methods',
            '--------------',
            '',
        ]
        for key, value in sorted(cls.__dict__.items()):
            if isinstance(value, proxyobjects.ProxyMethod):
                # print(f'    def {key}():')
                proxy_methods.extend(describe_proxy_method(key, value, cls))
            elif inspect.isfunction(value):
                methods.extend(describe_python_method(value, 0))
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
                    header.extend([f'Python Proxy to `{full_name} <{javadoc}>`_ ', ''])
            else:
                log.info("No cls declaration for %s", declaration)

        page = header + methods + interfaces + proxy_methods
        page.extend(['', f'Generated {time.strftime("%Y-%m-%d")}'])
        twrite(os.path.join(output, f'{cls.__name__}.rst'), "\n".join(page))

    index.extend(['', f'Generated {time.strftime("%Y-%m-%d")}'])
    twrite(os.path.join(output, 'index.rst'), '\n'.join(index))


def main():
    logging.basicConfig(level=logging.DEBUG)
    asyncio.get_event_loop().run_until_complete(generate_docs())


if __name__ == "__main__":
    main()
