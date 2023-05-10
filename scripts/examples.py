"""Sample script for pycraft"""
from pycraft.expose import expose
from pycraft.server import final
from pycraft.chatmessage import ChatMessage
import asyncio


@expose()
async def hello_world():
    return "Hello World! Let's Craft"


@expose()
async def whoami(*, player=None):
    """Echo back the user's name"""
    return player.name


# @expose()
# async def whereami(*, player=None):
#     """Echo back the user's location"""
#     return player.location


@expose()
async def cat(*, player=None, world=None):
    """Spawn a can in front of the player"""
    await world.spawnEntity(player.location + player.forward, 'minecraft:cat')


@expose()
async def box(material, *, player=None, world=None):
    """Create a 5x5 box around the player"""

    materials, positions = [], []
    # we start from a position 2 blocks left and back from the player's current position
    start = player.position + player.left + player.left + player.back + player.back
    # we want to make three layers
    for layer in start, start + (0, 1, 0), start + (0, 2, 0):
        # for each layer, draw the sides
        for i in range(0, 5):
            # left wall
            materials.append(material)
            positions.append(layer + (player.forward * i))
            # right wall
            materials.append(material)
            positions.append(layer + (player.right * 4) + (player.forward * i))

        # and draw the front and back walls...
        for j in range(1, 4):
            # back-wall
            materials.append(material)
            positions.append(layer + (player.right * j))
            # back-wall
            materials.append(material)
            positions.append(layer + (player.forward * 4) + (player.right * j))

    await world.setBlockList(positions, materials)


@expose()
async def vengence(*, player=None, listener=None, server=None):
    """Every hit for the next 50 hits does 100 damage"""

    async def v_watcher():
        async for event in listener.wait_for_events(
            'EntityDamageByEntityEvent',
            count=500,
            timeout=3600 * 2,
        ):
            if event.damager.get('name') == player.name:
                try:
                    target = final.Entity(**event.entity)
                    if target.type != 'Player':
                        await target.remove()
                        await server.broadcastMessage('Death to the %s' % (target.name))
                except Exception as err:
                    print(err)

    asyncio.ensure_future(v_watcher())
    return "Vengence shall be harsh"


@expose()
async def raw_chat_example():
    return ChatMessage('Moo')


@expose()
async def midas_touch(
    material='minecraft:gold_block',
    count=25,
    *,
    listener=None,
    player=None,
    interpreter=None,
):
    async def run_midas():
        converted = set()
        if not interpreter:
            return
        async for event in listener.wait_for_events(
            event_type='PlayerInteractEvent',
            player=player,
            count=count,
        ):
            if event.action == 'RIGHT_CLICK_BLOCK':
                block: final.Block = event.block_clicked
                location: final.Location = block.location
                key = location.world, int(location.x), int(location.y), int(location.z)
                if key in converted:
                    continue
                converted.add(key)
                await final.Block(location=location).setType(material)
            elif event.action == 'LEFT_CLICK_BLOCK':
                break
        await interpreter.broadcast_chat('Finished midas_touch')

    asyncio.ensure_future(run_midas())
    return 'Right click blocks with your empty hand to convert them'
