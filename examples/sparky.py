from pycraft.expose import expose


@expose()
async def sparky(*, player):
    """Create some sparks in front of the player"""
    await player.spawnParticle('electric_spark', player.location + player.forward, 200)
