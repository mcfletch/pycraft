import re, os, json, logging, glob, functools, time
import numpy as np
from . import expose, directions
from .server.world import Vector
from . import bulldozer, parsematerial, rotations

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATES = os.path.join(HERE, 'templates')
# When running from source, directly write into templates...
USER_TEMPLATES = os.path.abspath(os.environ.get('USER_DATA', './pycraft-templates'))
log = logging.getLogger(__name__)


@expose.expose()
async def copy(
    name='stamp',
    depth=5,
    width=5,
    height=5,
    position=None,
    direction=None,
    offset=None,
    *,
    world=None,
    player=None,
):
    """Read blocks to create a template that can be stamped elsewhere

    name -- name that you can use to reference this copy when pasting
    depth, width, height -- dimensions of the cube to copy
    position, direction -- middle of the lowest slice of the cube will be just
                           in front of position with cube extending in direction
    offset -- offset from the normal copy position to where that position should be when
              pasted; so if you want the paste to be 3m below where it would paste
              normally, use [0,-3,0]

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

    # BUGFIX: Copying an occupied bed makes it useless/broken...
    for layer in layers:
        for row in layer:
            for i, material in enumerate(row):
                if 'occupied=true' in material:
                    row[i] = material.replace('occupied=true', '')

    save_template(player, name, layers, offset=offset)
    return f'Saved template to {name} with {layers}'


@expose.expose()
async def show_pastes(substring=None, *, player=None):
    """Show the name of pastes that are available

    If `substring` is passed, we will restrict to names that have that
    string (case insensitively) in their filename.
    """
    if substring:
        test = substring.lower()
        return sorted([x for x in list_templates() if test in x.lower()])
    return list_templates()


def rotated_template(template, player):
    """Given a template, try to rotate to match the current orientation

    player.direction determines the rotation IFF there is a `direction`
    key in the original. We look at the major direction of the original
    and compare to the current, producing a number-of-CW-rotations
    to apply to the template. Each rotation transforms the X and Z such
    the first makes an AxB into a BxA and the second into an AxB again
    but with the order reversed (since it's a 180deg rotation then).
    """
    if not 'direction' in template:
        log.info("Template %s has no direction", template.get('name'))
        return template
    original_direction = bulldozer.roughly_forward(template['direction'])
    direction = bulldozer.roughly_forward(player.direction)
    if original_direction == direction:
        log.info("Direction matches copy")
        return template
    template = template.copy()
    blocks = template['blocks'][:]

    steps = rotations.steps_between(tuple(original_direction), tuple(direction))

    for layer in blocks:
        layer[:] = np.rot90(layer, steps, axes=(1, 0))

    for layer in blocks:
        layer[:] = [[rotations.rotate(m, steps) for m in row] for row in layer]

    template['blocks'] = blocks
    return template


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

    template = rotated_template(template, player)

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

    # log.info("Player location: %s Direction: %s", player.tile_position, direction)
    # log.info("Position: %s", position)
    # log.info("Template size: %s,%s,%s", depth, width, height)

    # The template's rotation is already applied, so we just need
    # to find the point forward one and to our left

    # start = position - (cross * (width // 2))
    if direction[2] > 0:
        # facing east, so width is really width
        start = position - (cross * (width // 2))
    elif direction[2] < 0:
        # we are facing south, so we need to make start the full depth and then to our right...
        start = position + (cross * (width // 2)) + (direction * (depth - 1))
    elif direction[0] > 0:
        # we are facing east (positive X), so we should start from depth//2 to our right
        start = position - (cross * (depth // 2))
    elif direction[0] < 0:
        # we are facing west, so we should start from depth//2 to our left + width
        start = position + (cross * (depth // 2)) + (direction * (width - 1))
    else:
        return 'Unable to determine start position'

    locations, blocks, specials = [], [], []
    for y, layer in enumerate(template_blocks):
        for z, row in enumerate(layer):
            for x, cell in enumerate(row):
                position = start + (x, y, z)
                if cell == None:
                    # explicitly don't replace...
                    continue
                elif isinstance(cell, dict):
                    special = cell
                    cell = special['material']
                    specials.append((position, special))
                locations.append(position)
                blocks.append(cell)
    await world.setBlockList(locations, blocks)


def sanitize(text):
    return ''.join(BAD_CHARS.split(text))


BAD_CHARS = re.compile(r'[^0-9a-zA-Z_]')


def template_filename(template_name, user=True):
    """Get the template filename for the given player

    names are restriced to A-Za-z0-9_ for both player and template
    """
    template_name = sanitize(template_name)
    if user:
        return os.path.join(USER_TEMPLATES, template_name) + '.json'
    else:
        return os.path.join(TEMPLATES, template_name) + '.json'


def save_template(player, name, template, **named):
    """Save a template to a file using the proxy encoder to allow saving e.g. locations/directions"""
    from pycraft.server import channel

    filename = template_filename(name, user=True)
    log.info("Saving to file: %s", filename)
    struct = {
        'author': player.name,
        'name': name,
        'blocks': template,
        'location': player.location,
        'direction': player.direction,
    }
    for key, value in named.items():
        if value is not None:
            struct[key] = value

    result = json.dumps(
        struct,
        cls=channel.ProxyEncoder,
    )
    dirname = os.path.dirname(filename)
    # TODO: do we care about the race condition?
    if os.path.exists(filename):
        os.rename(
            filename, filename + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
        )
    elif not os.path.exists(dirname):
        os.makedirs(dirname)

    with open(filename, 'w') as fh:
        fh.write(result)

    list_templates.cache_clear()


def load_template(player, name):
    for filename in [
        template_filename(name, True),
        template_filename(name, False),
    ]:
        log.info("Loading from file: %s", filename)
        if os.path.exists(filename):
            content = json.loads(open(filename).read())
            return content
    log.info("No such file: %s", filename)
    return None


@functools.lru_cache(maxsize=1)
def list_templates():
    result = []
    for pattern in [
        os.path.join(TEMPLATES, '*.json'),
        os.path.join(USER_TEMPLATES, '*.json'),
    ]:
        for filename in glob.glob(pattern):
            result.append(os.path.basename(filename)[:-5])
    return result
