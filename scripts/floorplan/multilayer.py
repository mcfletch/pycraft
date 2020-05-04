#!/usr/bin/env python3

from mcpi.minecraft import Minecraft
from PIL import Image
from numpy import asarray
import sys

if len(sys.argv) < 2:
    print("Usage: %s <filename> ..." % sys.argv[0])
    sys.exit(-1)

filenames = sys.argv[1:]
craft = Minecraft.create()
(x, y, z) = (0, 0, 0)
floor_height = 4

def read_image(filename):
    print("Rending %s to Minecraft" % filename)
    image = Image.open(filename).convert('LA')
    image.thumbnail((64,64))
    data = asarray(image)
    return data

def column(x, y, z, type):
    # Wall / Not Wall
    craft.setBlocks(x, y, z, x, y+floor_height-1, z, type)
    # Roof
    craft.setBlock(x, y+floor_height, z, 2)
    # Floor
    craft.setBlock(x, y-1, z, 2)

def render_map(data, level):
    current_level = y + level * floor_height
    for j, line in enumerate(data):
        for k, cell in enumerate(line):
            if cell[0] > 200:
                column(j, current_level, k, 0)
                sys.stdout.write("  ")
            else:
                column(j, current_level, k, 1)
                sys.stdout.write("[]")
        sys.stdout.write("\n")

def main():
    for level, filename in enumerate(filenames):
        data = read_image(filename)
        render_map(data, level)

if __name__ == "__main__":
    main()
