#! /usr/bin/env python
# Minecraft api reference
#  https://www.stuffaboutcode.com/p/minecraft-api-reference.html
from mcpi import minecraft, block
mc = minecraft.Minecraft.create()
mc.postToChat("Hello from python")
users = mc.getPlayerEntityIds()
print("Users: %s"%(users))
if users:
    position = None
    for user in users:
        position = mc.entity.getPos(user)
        print('User #%d at %s'%( user, position))
    if position:
        x,y,z = position
        mc.player.setPos(x,y+1,z)
    
else:
    print("No users currently")
