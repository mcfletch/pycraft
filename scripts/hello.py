# # import random
# names = ['alex', 'mike', 'lupin', 'clark']


# # random.shuffle(names)
# # for number in names:
# #     if number == 'alex':
# #         print('hello', number, 'the great')
# #     elif number == 'lupin':
# #         print('good boy', number)
# #     else:
# #         print('hello', number)
# def x2(value):
#     return value * 2


# print(x2(names))
# longnamez = [x2(name) for name in names]
# print(longnamez[::-1])
from pycraft import expose
import asyncio


@expose.expose()
def hello(*, player=None):
    return f'hide, {player.name} is coming!'


@expose.expose()
def whereami(*, player=None):
    return player.location


@expose.expose()
async def youspinmerightround(*, player=None):
    from asyncio import sleep

    location = player.location
    rotation = location.yaw
    incliation = location.pitch
    for angle in range(0, 360, 1):
        target = [
            location.world,
            location.x,
            location.y,
            location.z,
            rotation + angle,
            incliation,
        ]
        await player.teleport(target)
        await sleep(0.02)
