import random


class RandomChoice(object):
    def __init__(self, choices):
        self.choices = choices

    def __json__(self):
        return random.choice(self.choices)


RANDOM_STAINED_GLASS = RandomChoice(
    [
        'minecraft:white_stained_glass',
        'minecraft:orange_stained_glass',
        'minecraft:magenta_stained_glass',
        'minecraft:light_blue_stained_glass',
        'minecraft:yellow_stained_glass',
        'minecraft:lime_stained_glass',
        'minecraft:pink_stained_glass',
        'minecraft:gray_stained_glass',
        'minecraft:light_gray_stained_glass',
        'minecraft:cyan_stained_glass',
        'minecraft:purple_stained_glass',
        'minecraft:blue_stained_glass',
        'minecraft:brown_stained_glass',
        'minecraft:green_stained_glass',
        'minecraft:red_stained_glass',
        'minecraft:black_stained_glass',
    ]
)
RANDOM_STAINED_GLASS_PANE = RandomChoice(
    [
        'minecraft:white_stained_glass_pane',
        'minecraft:orange_stained_glass_pane',
        'minecraft:magenta_stained_glass_pane',
        'minecraft:light_blue_stained_glass_pane',
        'minecraft:yellow_stained_glass_pane',
        'minecraft:lime_stained_glass_pane',
        'minecraft:pink_stained_glass_pane',
        'minecraft:gray_stained_glass_pane',
        'minecraft:light_gray_stained_glass_pane',
        'minecraft:cyan_stained_glass_pane',
        'minecraft:purple_stained_glass_pane',
        'minecraft:blue_stained_glass_pane',
        'minecraft:brown_stained_glass_pane',
        'minecraft:green_stained_glass_pane',
        'minecraft:red_stained_glass_pane',
        'minecraft:black_stained_glass_pane',
    ]
)