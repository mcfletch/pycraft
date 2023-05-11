from pycraft.expose import expose


@expose()
async def whereami(*, player):
    """Return the player's location"""
    return player.location
