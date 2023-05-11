from pycraft.expose import expose


@expose()
async def hello_world():
    """Gives a cheerful hello"""
    return "Hello World!"
