"""Modify a World on the server using the Bukkit API"""
import asyncio
from pycraft.server import final, channel


async def get_server():
    """Get a connected :py:class:`pycraft.server.channel.Channel`"""
    server = channel.Channel(debug=False)
    await server.open()
    await server.introspect()
    return server


async def start_storm():
    """Get a reference to a :py:class:`pycraft.server.final.World` and modify that world using the Bukkit API"""
    await get_server()
    world = final.World('world')
    await world.setThundering(True)
    await world.setStorm(True)


if __name__ == "__main__":
    asyncio.run(start_storm())
