import re, os, json
import numpy as np
from . import expose
from .bulldozer import roughly_forward

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATES = os.path.join(HERE, 'templates')


@expose.expose()
def copy(
    name='stamp',
    depth=5,
    height=5,
    width=5,
    position=None,
    direction=None,
    *,
    mc=None,
    user=None,
):
    """Read blocks to create a template that can be stamped elsewhere"""

    name = sanitize(name)

    if direction is None:
        direction = user.direction
    direction = roughly_forward(direction)

    if not direction:
        raise RuntimeError("Unable to find direction")

    if position is None:
        position = user.tile_position + direction

    direction = np.array(tuple(direction))
    position = np.array(tuple(position))

    cross = np.array((direction[2], 0, direction[0]))
    up = np.array((0, 1, 0))

    start = position - (cross * width // 2)

    layers = []
    for lindex in range(height):
        layer_start = start + (up * lindex)
        layer = []
        for rindex in range(depth):
            row_start = layer_start + (rindex * direction)
            row = []
            for cindex in range(width):
                cellpos = row_start + (cindex * cross)
                block, data = 0, 0
                for attempt in range(20):
                    try:
                        block, data = mc.getBlockWithData(*cellpos)
                        break
                    except ValueError:
                        pass
                print(f'{cellpos} => {block},{data}')
                row.append((block, data))
            layer.append(row)
        layers.append(layer)
    save_template(user, name, layers)
    return f'Saved template to {name}'


@expose.expose()
def paste(
    name='stamp',
    position=None,
    direction=None,
    *,
    mc=None,
    user=None,
):
    """Paste previously copied blocks into the current location"""

    name = sanitize(name)

    if direction is None:
        direction = user.direction
    direction = roughly_forward(direction)

    if not direction:
        raise RuntimeError("Unable to find direction")

    if position is None:
        position = user.tile_position + direction

    direction = np.array(tuple(direction))
    position = np.array(tuple(position))

    cross = np.array((direction[2], 0, direction[0]))
    up = np.array((0, 1, 0))

    template = load_template(user, name)
    if not template:
        return f'No template {name} found'

    row = template[0][0]
    width = len(row)
    start = position - (cross * width // 2)

    for lindex, layer in enumerate(template):
        layer_start = start + (up * lindex)
        for rindex, row in enumerate(layer):
            row_start = layer_start + (rindex * direction)
            for cindex, cell in enumerate(row):
                cellpos = row_start + (cindex * cross)
                id, data = cell
                # block = blocks.Block.as_instance(id,data)
                mc.setBlock(*cellpos, id, data)


def sanitize(text):
    return ''.join(BAD_CHARS.split(text))


BAD_CHARS = re.compile(r'[^0-9a-zA-Z_]')


def template_filename(user, template_name):
    """Get the template filename for the given user

    names are restriced to A-Za-z0-9_ for both user and template
    """
    username = sanitize(user.get_name())
    template_name = sanitize(template_name)
    return os.path.join(TEMPLATES, template_name)


def save_template(user, name, template):
    filename = template_filename(user, name)
    struct = {
        'author': user.get_name(),
        'name': name,
        'blocks': template,
    }
    result = json.dumps(struct)
    with open(filename, 'w') as fh:
        fh.write(result)


def load_template(user, name):
    filename = template_filename(user, name)
    if os.path.exists(filename):
        content = json.loads(open(filename).read())
        return content['blocks']
    return None
