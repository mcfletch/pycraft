#! /usr/bin/env python3
# Minecraft api reference
#  https://www.stuffaboutcode.com/p/minecraft-api-reference.html

# Get the collection of code that the minecraft people
# have given us that lets us talk to minecraft, the
# "library" or "module" provides lots of functions for
# manipulating the minecraft server.
from mcpi import minecraft, block, connection

# Create a "thing" which is a `minecraft.Minecraft` instance
# which lets us talk to the local minecraft server
mc = minecraft.Minecraft.create()
# Call a "method" on the minecraft server that lets us
# post a message to the chat window...
mc.postToChat("Hello from python")

# Ask the server for a list of identifiers (ids) that let us
# talk about the users with the server. Internally the server
# thinks of the user as a number, with their name just a thing
# attached to that user-number
# TODO: This command actually crashes (raises an exception)
# rather than returning an empty list when there are no logged-in
# users
try:
    users = mc.getPlayerEntityIds()
except connection.RequestError:
    users = []
else:
    # Call the function `print` to print the *list* of user ids that 
    # are logged in the minecraft server tracks users, mobs and villagers 
    # as things called "entities"
    print(
        "Users: %s are online"%(users)
    )
# *if* users is not empty, do the things that are "inside" the if
# if there are more than one users logged in, then users will be
# a list of integer values such as [23,45,55]
if users:
    # for every user in users, assign the variable `user` to that user id
    # then do everything "inside" the for loop with `user` referring
    # to that number (id)
    for user in users:
        # for this *particular* user, find their current position
        position = mc.entity.getPos(user)
        # position is now a Vector, which is a sequence of 3 floating-point values
        # which defines a position in 3D space
        # x => how far East/West
        # y => how far up/down
        # z => how far North/South
        name = mc.entity.getName(user)
        # name is now a string of characters which is the user's name
        # as they entered it in their Minecraft client
        print('User #%d %s at %s'%( user, name, position))
        # Unpack the 3 values (x,y,z) of the position vector into separate values
        # so that we can manipulate *just* one of them
        x,y,z = position
        # Set the position of the player to the same x and z, but 
        # y increased by 1m (y is up-and-down)
        # The effect of this is to make the user jump up 1m
        mc.player.setPos(x,y+1,z)
        # We are going to create a vein of diamond blocks
        # starting 1m North of the player and stretching 100m
        # North from there...
        # For every number in the range 0-100 (not including the end)
        # assign the number to the variable offset, then do this
        # block of statements (so here we will do the statements 100 
        # times)
        for offset in range(100):
            # offset is 0, then 1, then 2, then 3
            # In minecraft you "create" a block by "setting"
            # it to a particular block-type. Some block-types
            # such as wood have sub-types like Oak, Pine, etc
            mc.setBlock(
                x,
                y,
                z+1+offset, # user's z (north/south) plus 1 plus [0,1,2,3,4,...,99]
                block.DIAMOND_BLOCK.id # what we want to set it to...
            )
