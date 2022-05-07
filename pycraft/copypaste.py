import re, os, json, logging
import numpy as np
from . import expose, directions
from .server.world import Vector

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATES = os.path.join(HERE, 'templates')
log = logging.getLogger(__name__)


@expose.expose()
async def copy(
    name='stamp',
    depth=5,
    width=5,
    height=5,
    position=None,
    direction=None,
    *,
    world=None,
    player=None,
):
    """Read blocks to create a template that can be stamped elsewhere

    name -- name that you can use to reference this copy when pasting
    depth, width, height -- dimensions of the cube to copy
    position, direction -- middle of the lowest slice of the cube will be just
                           in front of position with cube extending in direction

    returns message with name and the content copied
    """

    name = sanitize(name)

    if direction is None:
        direction = player.direction
    direction, cross = directions.forward_and_cross(direction)

    if not direction:
        raise RuntimeError("Unable to find direction")

    if position is None:
        position = player.tile_position + direction

    start = position - (cross * (width // 2))
    stop = (
        start
        + (cross * (width - 1))
        + (direction * (depth - 1))
        + (Vector(0, 1, 0) * (height - 1))
    )

    print(
        'Start=%s Stop=%s position=%s direction=%s cross=%s',
        start,
        stop,
        position,
        direction,
        cross,
    )

    layers = await world.getBlockArray(start, stop)

    save_template(player, name, layers)
    return f'Saved template to {name} with {layers}'


@expose.expose()
async def show_pastes(substring=None):
    """Show the name of pastes that are available

    If `substring` is passed, we will restrict to names that have that
    string (case insensitively) in their filename.
    """
    if substring:
        test = substring.lower()
        return sorted([x for x in list_templates() if test in x.lower()])
    return list_templates()


@expose.expose()
async def paste(
    name='stamp',
    position=None,
    direction=None,
    *,
    world=None,
    player=None,
):
    """Paste previously copied blocks into the current location (see copy)

    See: show_pastes for a list of available templates...

    position, direction -- template will be directly in front of this position in direction
    """

    name = sanitize(name)
    template = load_template(player, name)

    if not template:
        return f'No template {name} found'

    template_blocks = template.get('blocks')
    if not template_blocks:
        return f'Tempalte {name} has no blocks member'

    if direction is None:
        direction = player.direction
    direction, cross = directions.forward_and_cross(direction)

    if not direction:
        raise RuntimeError("Unable to find direction")

    if position is None:
        position = player.tile_position + direction

    if template.get('offset'):
        position += template['offset']

    up = Vector(0, 1, 0)

    height = len(template_blocks)
    depth = len(template_blocks[0])
    width = len(template_blocks[0][0])

    log.info("Template size: %s,%s,%s", depth, width, height)

    # the template doesn't rotate, so we need to decide our position relative to it
    # rather than its position
    if direction[2] > 0:
        # we are facing north, native format, so start is to our left
        start = position - (cross * (width // 2))
    elif direction[2] < 0:
        # we are facing south, so we need to make start the full depth and then to our right...
        start = position + (cross * (width // 2)) + (direction * (depth - 1))
    elif direction[0] > 0:
        # we are facing east, so we should start from depth//2 to our right
        start = position - (cross * (depth // 2))
    elif direction[0] < 0:
        # we are facing west, so we should start from depth//2 to our left + width
        start = position + (cross * (depth // 2)) + (direction * (depth - 1))
    else:
        return 'Unable to determine start position'

    locations, blocks = [], []
    for y, layer in enumerate(template_blocks):
        for z, row in enumerate(layer):
            for x, cell in enumerate(row):
                locations.append(start + (x, y, z))
                blocks.append(cell)
    await world.setBlockList(locations, blocks)


def sanitize(text):
    return ''.join(BAD_CHARS.split(text))


BAD_CHARS = re.compile(r'[^0-9a-zA-Z_]')


def template_filename(player, template_name):
    """Get the template filename for the given player

    names are restriced to A-Za-z0-9_ for both player and template
    """
    playername = sanitize(player.name)
    template_name = sanitize(template_name)
    return os.path.join(TEMPLATES, template_name) + '.json'


def save_template(player, name, template):
    """Save a template to a file using the proxy encoder to allow saving e.g. locations/directions"""
    from pycraft.server import channel

    filename = template_filename(player, name)
    log.info("Saving to file: %s", filename)
    struct = {
        'author': player.name,
        'name': name,
        'blocks': template,
        'location': player.location,
        'direction': player.direction,
    }

    result = json.dumps(
        struct,
        cls=channel.ProxyEncoder,
    )
    with open(filename, 'w') as fh:
        fh.write(result)


def load_template(player, name):
    filename = template_filename(player, name)
    log.info("Loading from file: %s", filename)
    if os.path.exists(filename):
        content = json.loads(open(filename).read())
        return content
    log.info("No such file: %s", filename)
    return None


def list_templates():
    return [
        x[0]
        for x in [os.path.splitext(x) for x in sorted(os.listdir(TEMPLATES))]
        if x[1] == '.json'
    ]
