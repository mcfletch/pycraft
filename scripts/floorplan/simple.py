#!/usr/bin/env python3

from mcpi.minecraft import Minecraft
from PIL import Image
from numpy import asarray
import sys

if len(sys.argv) < 2:
    print("Usage: %s <filename>" % sys.argv[0])
    sys.exit(-1)

filename = sys.argv[1]
print("Rending %s to Minecraft" % filename)
image = Image.open(filename).convert('LA')
image.thumbnail((64,64))
data = asarray(image)

craft = Minecraft.create()
(x, y, z) = (0, 0, 0)

def column(x, y, z, type):
    # Wall / Not Wall
    craft.setBlocks(x, y, z, x, y+3, z, type)
    # Roof
    craft.setBlock(x, y+4, z, 2)
    # Floor
    craft.setBlock(x, y-1, z, 2)

for j, line in enumerate(data):
    for k, cell in enumerate(line):
        if cell[0] > 200:
            column(j, y, k, 0)
            sys.stdout.write("  ")
        else:
            column(j, y, k, 1)
            sys.stdout.write("[]")
    sys.stdout.write("\n")
