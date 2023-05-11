from pycraft.expose import expose


@expose()
async def super_jump(*, player):
    """Teleport the user 100m up"""
    await player.teleport(
        player.location
        + (
            0,
            100,
            0,
        )
    )
