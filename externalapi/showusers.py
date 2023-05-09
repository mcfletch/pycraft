"""This script demonstrates how to see the UUIDs of users who have connected to the server

You can add users to your whitelist.
"""
import asyncio
from pycraft.server import final, channel


async def get_server():
    """Get a connected :py:class:`pycraft.server.channel.Channel`"""
    server = channel.Channel(debug=False)
    await server.open()
    await server.introspect()
    return server


async def show_users():
    """Print out the set of users who have connected to the server"""
    channel = await get_server()
    for player in await final.Server().getOfflinePlayers():
        if isinstance(player, final.Player):
            print(
                f'{repr(player.name)} {player.uuid} {"🚫" if player.banned else "✓"} {"☑" if player.whitelisted else "☐"} currently at {player.location}'
            )
        else:
            print(
                f'{repr(player.name)} {player.uuid} {"🚫" if player.banned else "✓"} {"☑" if player.whitelisted else "☐"}'
            )


if __name__ == "__main__":
    asyncio.run(show_users())
