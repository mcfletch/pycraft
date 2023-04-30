"""Generate documentation by introspecting exposed API"""
import logging, asyncio, pprint, time, os, inspect, types, textwrap
from pycraft.server.proxyobjects import ProxyMethod, type_coerce
from . import world, proxyobjects, channel

HERE = os.path.dirname(__file__)
DEFAULT_TARGET = os.path.join(HERE, '..', '..', 'docs', 'source', 'api', 'generated')
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
    result = f':py:class:`{name}`'
    # log.info("cls_link(%s) => %s", name, result)
    return result


def describe_python_method(method, indent=0):
    signature = inspect.signature(method)
    if inspect.isawaitable(method) or inspect.iscoroutinefunction(method):
        async_mark = ':async:'
    else:
        async_mark = ''
    docs = [
        f'{" "*indent}.. py:method:: {method.__name__}{str(signature)}',
        f'{" "*indent}   {async_mark}',
    ]
    docstring = inspect.getdoc(method)
    if docstring:
        docs.append('')
        docstring = textwrap.indent(inspect.cleandoc(docstring), ' ' * (indent + 3))
        docs.append(docstring)
        docs.append('')
    return "\n".join(docs)


def describe_java_method(description, indent=0, no_index=False):
    """Describe a proxied java method"""
    if description.get('static'):
        self_arg = 'cls'
    else:
        self_arg = 'self'
    arg_types = [f'_{i}:{n}' for i, n in enumerate(description.get('argtypes', []))]
    arg_types.insert(0, self_arg)
    return_type = cls_link(
        description.get('returntype'), description.get('returntype_subtypes')
    )
    tags = [':async:']
    if self_arg == 'cls':
        tags.append(':classmethod:')
    if no_index:
        tags.append(':noindex:')
    return textwrap.indent(
        "\n".join(
            [
                f'.. py:method:: {description["name"]}({", ".join(arg_types)}) -> {return_type}',
            ]
            + [f'{" "*(3)}{tag}' for tag in tags]
            + ['']
        ),
        ' ' * indent,
    )


def describe_proxy_method(key, method, cls, indent=0):
    """Describe a single proxy method for the user"""
    description = []

    if getattr(method, 'multi', None):
        description.append(f'{" "*indent}.. py:method:: {key}')
        description.append('')
        for sub in method.multi.get('commands', ()):
            description.append(
                describe_java_method(sub, indent=indent + 4, no_index=True)
            )
    else:
        description.append(describe_java_method(method.description, indent=indent))
    return "\n".join(description)


def class_ref(cls):
    return f':py:class:`{cls.__module__}.{cls.__name__}`'


def class_methods(cls):
    for key, value in inspect.getmembers(cls):
        if isinstance(value, proxyobjects.ProxyMethod):
            # print(f'    def {key}():')
            yield (key, value)
        elif inspect.isfunction(value) or inspect.ismethod(value):
            yield (key, value)


def describe_method(cls, key, method, indent=0):
    if isinstance(method, proxyobjects.ProxyMethod):
        return describe_proxy_method(key, method, cls, indent=indent)
    elif inspect.ismethod(method) or inspect.isfunction(method):
        return describe_python_method(method, indent=indent)
    else:
        raise TypeError(method.__class__)


SKIP_METHODS = set(
    [
        '__str__',
        '__json__',
        '_prop_typ',
        'as_type',
    ]
)


def class_page(cls):
    """Generate a Sphinx-style class description page"""
    header = [
        '.. currentmodule:: pycraft.server.final',
        '',
        f'{cls.__name__}',
        '=' * len(cls.__name__),
        '',
    ]
    inheritance = []
    for parent in cls.__mro__:
        if parent is not object:
            if parent is not cls:
                inheritance.append(f'* {class_ref(parent)}')
            else:
                inheritance.append(f'* {parent.__module__}.{parent.__name__}')
    if inheritance:
        header.extend(
            [
                'Inheritance',
                '------------',
            ]
        )
        header.extend(inheritance)
        header.append('')

    declaration = getattr(cls, '__declaration__', None)
    if declaration:
        class_declaration = declaration.get('cls')
        if class_declaration:
            full_name = class_declaration['fullName']
            javadoc = javadoc_url(full_name)
            if javadoc:
                header.extend(
                    [
                        f'Python Proxy to `{full_name} <{javadoc}>`_ from :py:mod:`pycraft.server.final`',
                        '',
                    ]
                )
        else:
            log.info("No cls declaration for %s", declaration)

    # Now the actual sphinx definition...
    if hasattr(cls, '__init__'):
        init_signature = inspect.signature(cls.__init__)
    else:
        init_signature = '()'
    header.extend(
        [
            f'.. py:class:: {cls.__name__}{init_signature}',
            f'   :canonical: {cls.__module__}.{cls.__name__}',
            '',
        ]
    )

    indent = 3
    doc = inspect.getdoc(cls)
    if doc:
        header.append(textwrap.indent(doc, ' ' * indent))
        header.append('')

    methodset = sorted(class_methods(cls))
    if methodset:
        methods = []
        for key, value in methodset:
            if key not in SKIP_METHODS:
                description = describe_method(cls, key, value, indent=indent)
                methods.append(description)
                methods.append('')
    else:
        methods = []
    # null_methods = len(methods)
    # properties = [
    #     'Properties',
    #     '----------',
    #     '',
    # ]
    # null_properties = len(properties)
    # proxy_methods = [
    #     'Proxy Methods',
    #     '--------------',
    #     '',
    # ]
    # null_proxy = len(proxy_methods)
    # for key, value in inspect.getmembers(cls):
    #     if isinstance(value, proxyobjects.ProxyMethod):
    #         # print(f'    def {key}():')
    #         proxy_methods.extend(describe_proxy_method(key, value, cls))
    #     elif inspect.isfunction(value) or inspect.ismethod(value):
    #         methods.extend(describe_python_method(value, 0))
    #     elif isinstance(value, property):
    #         properties.append(f'* {key} -- {value.__doc__}')
    #     elif key == 'values' and hasattr(value, 'cache_clear'):
    #         methods.append(
    #             f'* {key}() -- (cached) set of values defined for the enumeration'
    #         )
    #     elif (
    #         key.startswith('__')
    #         and key.endswith('__')
    #         or key in ('interfaces', '_prop_typ')
    #     ):
    #         continue
    #     elif isinstance(value, (int, float, str, bytes, tuple, list, type(None))):
    #         properties.append(f'* {key} = {repr(value)}')
    #     else:
    #         raise KeyError(key, value)
    #     # else:
    #     #     print('Not a method: %s %s' % (key, type(value)))

    page = (
        header
        + methods
        # + (properties if len(properties) > null_properties else [])
        # + (proxy_methods if len(proxy_methods) > null_proxy else [])
    )
    return page


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
        '',
        '.. :py:module: pycraft.server.final',
        '.. toctree::',
        '   :maxdepth: 1',
        '   :caption: Contents:',
        '',
    ]

    for key, cls in sorted(proxyobjects.PROXY_TYPES.items()):
        index.append(
            f'   class {cls.__name__}({", ".join(cls.interfaces)}) <./generated/{cls.__name__}>'
        )
        if not isinstance(cls, proxyobjects.ServerObjectMeta):
            continue

        page = class_page(cls)
        twrite(os.path.join(output, f'{cls.__name__}.rst'), "\n".join(page))

    index.extend(['', f'Generated {time.strftime("%Y-%m-%d")}'])
    twrite(os.path.join(output, '..', 'pycraft.server.final.rst'), '\n'.join(index))


def main():
    logging.basicConfig(level=logging.DEBUG)
    asyncio.get_event_loop().run_until_complete(generate_docs())


if __name__ == "__main__":
    main()
