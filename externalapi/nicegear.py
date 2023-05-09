"""Uses chat-server tools to manipulate the world"""
import asyncio
from pycraft.server import final, channel
from pycraft import acommands


async def get_server():
    """Get a connected :py:class:`pycraft.server.channel.Channel`"""
    server = channel.Channel(debug=False)
    await server.open()
    await server.introspect()
    return server


def get_options():
    import argparse

    parser = argparse.ArgumentParser(description='Give nice gear to a user')
    parser.add_argument('name', metavar='NAME_OR_FRAGMENT')
    return parser


async def nice_gear(name):
    """Use pycraft-chat-server exposed code from scripts"""
    await get_server()
    # the server is a singleton, so final.Server() is always "the server"
    # many chat-server commands will need a server and/or a world
    player = await acommands.find_player(name, server=final.Server())
    world = final.World(name=player.location.world)

    if player:
        await acommands.nice_gear(player=player)
        print(f"Gave {player.name} some nice gear")


if __name__ == "__main__":
    options = get_options().parse_args()
    asyncio.run(nice_gear(options.name))
