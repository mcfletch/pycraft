#! /usr/bin/env python3
# We use asynchronous operations to wait for the server
# to complete the things we've asked it to do, asynchronous
# functions have an "async" in front of them and they tell
# the interpreter to wait for something to finish by using
# the "await" keyword
import asyncio
import logging
from pycraft.server import channel


async def hello_world():
    # We'll get a connection (channel) to the server, here we're
    # using the default (localhost) server and port
    chan = channel.Channel()
    # We're waiting for the connection to the server to open
    await chan.open()
    # Now we ask the PycraftServer plugin in the server to
    # poke around and tell us what APIs are available. This
    # process will take a while (seconds) and will send a huge
    # gob of data (MBs) to us that describes what we can do
    # with the server
    await chan.introspect()

    from pycraft.server import final
    from pycraft import acommands

    # name= here can be any string, the server actually does have
    # a name, but the api will ignore it because there's only
    # one server on the far side of the connection...
    server_api = world.Server(name='server')

    # Again, we have to await the call, otherwise Python will
    # never get around to running the operation...
    await server_api.broadcastMessage("Hello from Python")

    # Print out a list of every player that has ever connected
    # to this server
    # offline_players = await server_api.getOfflinePlayers()
    # print("Known players")
    # for player in offline_players:
    #     print(f'{player.name}: {player.uuid}')
    for world in await server_api.getWorlds():
        print(f"In world: {world.name}")
        print("Online players:")
        for player in await world.getPlayers():
            print(f'    {player.name}: {player.uuid} at {player.location}')
            try:
                await acommands.give('elytra', player=player)
            except channel.MethodInvocationError as err:
                print(f"  Could not give elytra to {player.name}: {err}")


def main():
    """This regular function just starts the asyncio event loop"""
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(hello_world())


if __name__ == "__main__":
    main()
