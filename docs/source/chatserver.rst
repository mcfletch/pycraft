Pycraft-Chat-Server: Talking to Python from Minecraft
======================================================

The `pycraft-chat-server` script is a larger example
of using the `pycraft` API. It allows you to expose 
commands to users on your server (remember, keep your
server away from the public). The implementation is in
:py:mod:`pycraft.achatserver`

Starting the Server
--------------------

The run-script normally starts the chat server in a container
configured to talk to the Minecraft server. If you'd like to 
run the server directly you can do so with::

    virtualenv -p python3 env
    source env/bin/activate
    pip install -r requirements.txt -e .
    pycraft-chat-server

See :doc:`./devsetup` for details

Calling Python from Minecraft
-----------------------------

Then from within your minecraft client, press `T`
to get the chat window, and type your Python code.

.. note::

    In iOS and similar Bedrock clients, you will find the chat 
    window is a button between the Health and Hunger bars.

.. youtube:: dM_s-SX_Vfg

The `pycraft-chat-server` is listening for chat commands that 
it can recognise as Python code. If it can parse your chat message
it will attempt to execute the code (here my username is 
VRPlumberMagic)::

    [03:01:50 INFO]: <VRPlumberMagic> echo('hello')
    [03:01:51 INFO]: 'hello' (<class 'str'>)
    [03:10:18 INFO]: <VRPlumberMagic> echo( 2 + 3 )
    [03:10:18 INFO]: 5 (<class 'int'>)
    [03:10:23 INFO]: <VRPlumberMagic> echo( 2 * 3 )
    [03:10:23 INFO]: 6 (<class 'int'>)
    [03:10:28 INFO]: <VRPlumberMagic> echo( 2 ** 3 )
    [03:10:28 INFO]: 8 (<class 'int'>)
    [03:10:36 INFO]: <VRPlumberMagic> echo( 2 / 3 )
    [03:10:36 INFO]: 0.6666666666666666 (<class 'float'>)
    [03:10:59 INFO]: <VRPlumberMagic> echo( player.location )
    [03:11:00 INFO]: ['world',2128.4617685823027,93.0,-1681.4257264464052,-175.81409,4.1994276] (<class 'pycraft.server.world.Location'>)
    [03:16:20 INFO]: <VRPlumberMagic> player.teleport(player.location+player.direction*2)
    [03:16:20 INFO]: True (<class 'bool'>)
    [03:36:25 INFO]: [Not Secure] <VRPlumberMagic> find_blocks('shulk')
    [03:36:26 INFO]: ['minecraft:shulker_box', 'minecraft:white_shulker_box', 'minecraft:orange_shulker_box', 'minecraft:magenta_shulker_box', 'minecraft:light_blue_shulker_box', 'minecraft:yellow_shulker_box', 'minecraft:lime_shulker_box', 'minecraft:pink_shulker_box', 'minecraft:gray_shulker_box', 'minecraft:light_gray_shulker_box', 'minecraft:cyan_shulker_box', 'minecraft:purple_shulker_box', 'minecraft:blue_shulker_box', 'minecraft:brown_shulker_box', 'minecraft:green_shulker_box', 'minecraft:red_shulker_box', 'minecraft:black_shulker_box', 'minecraft:shulker_spawn_egg', 'minecraft:shulker_shell'] (<class 'list'>)



.. note:: 
   
    The chat server does *not* support all of Python, the subset it 
    supports mostly focusses on function calls and basic math.  Major 
    features not supported:

    * imports 
    * function definitions 
    * list comprehensions at the top-level (you can pass them as parameters)

    If you find yourself wanting these features, consider making your 
    code a function and using :py:func:`pycraft.expose.expose` to make 
    it usable from the chat server.
    
Meta Commands
--------------

These commands allow you to figure out how to work with other commands 
or objects. They allow you to ask the `pycraft-chat-server` what you 
can do from within the chat window.

.. list-table::

    * - :py:func:`pycraft.acommands.dir_`
      - ``dir()``
      - Reports all of the functions, classes and data in the global namespace
    * - :py:func:`pycraft.acommands.help`
      - ``help(object)``
      - Reports the python docstring for the given object/type
    * - :py:func:`pycraft.acommands.echo`
      - ``echo(expression)``
      - Prints the result of evaluating the expression to the chat
    * - :py:func:`pycraft.acommands.find_blocks`
      - ``find_blocks(fragment:str)``
      - Searches for blocks whose name contain the fragment 
    * - :py:func:`pycraft.acommands.find_entities`
      - ``find_entities(fragment:str)``
      - Searches for entities whose Entity Type Name contains fragment
    * - :py:func:`pycraft.acommands.findall`
      - ``findall(fragment:str)``
      - Searches for entities whose Individual Name contains fragment
    * - :py:func:`pycraft.acommands.users`
      - ``users()``
      - Retrieves :py:class:`pycraft.server.final.Player` references 
        for all players in the world of the player making the call.
    * - :py:func:`pycraft.acommands.find_player`
      - ``find_player(fragment:str)``
      - Returns the first online :py:class:`pycraft.server.final.Player` whose name contains the given 
        fragment. The player does not need to be in the same world as 
        the caller.
    * - :py:func:`pycraft.acommands.this_guy`
      - ``this_guy() => right-click-on-entity``
      - Returns a reference to the next entity that the user `interacts`
        with; normally by right-clicking on e.g. a Villager.

Shelter and Gear 
-----------------

These commands let you set up a world where kids can be ready-to-adventure as soon 
as they log in (e.g. for birthday parties and the like). You can easily setup 
houses, grant advanced equipment and let new players "catch up" with more 
advanced players.

.. list-table:: Basic Shelter

    * - :py:func:`pycraft.acommands.bed`
      - ``bed(color='black')``
      - Creates a bed in front of the user
    * - :py:func:`pycraft.buildings.hall`
      - ``hall()``
      - Build a stone hall with bed, crafting table, furnace and the like.
       
        .. note::

            Note: there are nicer buildings available with :py:func:`pycraft.copypaste.paste`
            hall is more of an example of programatically setting up a building.
    * - :py:func:`pycraft.buildings.temple`
      - ``temple()``
      - Build an empty stone temple in front of the user. The inside of the temple is 
        empty and there are no doors on the structure.


.. list-table:: paste() Shelter

    * - paste('dark_house')
      - Deepslate and Iron Bar Pavilion Style house with lanterns, bed, crafting table and furnace.
        Does not provide complete shelter, as the iron grill can be shot through and Creepers
        can get close enough to blow up. Use within a larger complex.
    
    * - paste('lantern_mansion')
      - Large well-appointed house with shulker boxes, multiple beds, crafting table, music box,
        and bookshelves.

    * - paste('red_fortress')
      - Large well-appointed red-sandstone fortress with enchanting area, bed, crafting table, furnace,
        redstone powered large gate.

.. list-table:: Gear

    * - :py:func:`pycraft.acommands.give`
      - ``give('cooked_beef',count=64)``
      - Attempt to give the player an :py:class:`pycraft.server.final.ItemStack` with the 
        indicated amount of the indicated material.

    * - :py:func:`pycraft.acommands.nice_item`
      - ``nice_item('leather_leggings')``
      - Give the player the indicated item, then attempt to apply to that item every :py:class:`pycraft.server.final.Enchantment`
        that can be applied to the item. The result is a very nice version of the item.

    * - :py:func:`pycraft.acommands.nice_gear`
      - ``nice_gear()``
      - Give the player a set of `nice_item()` gear for adventuring.

Construction 
-------------

These functions allow you to create large or complex structures quickly.

    * - :py:func:`pycraft.bulldozer.bulldoze`
      - ``bulldoze(depth=20,height=-3,width=10,material='tnt')``
      - Fills the area in front of the player with the given material.
        Material defaults to 'air', so by default the bulldozer "clears"
        the area.
    * - :py:func:`pycraft.buildings.pyramid`
      - ``pyramid(width=9,depth=9,material='iron_block')``
      - Creates a stepped pyramid using the given blocks. The Pyramid can 
        be used to create a beacon so that players can find an area in 
        which you've setup e.g. an shared event.
    * - :py:func:`pycraft.acommands.stairs`
      - ``stairs(depth=25,ystep=1,material='stone_stairs[facing=north]')``
      - Creates a stairway with the given block going 25 blocks deep and 
        going up/down by ystep every block.
    * - :py:func:`pycraft.buildings.elevator_up`
      - ``elevator_up(base='magma_block',to_surface=True, to_air=False)``
      - Creates a bubble column that allows you to rapidly ascend/descend,
        this is the same kind of elevator you can create by stacking kelp
        in the water column and then breaking it.
    * - :py:func:`pycraft.buildings.elevators`
      - ``elevators(to_surface=True)``
      - Creates a two-way elevator bank with up and down columns, signs 
        telling users which way to go to travel, lighting, and a set of 
        walls to prevent flooding of nearby blocks.

        

```

### Construction
```
  block('iron_ore') # create a block in front of you
  p_dome() # creates a parabolic dome out of stained glass
  circle() # creates a circle of material around you
  tunnel() # creates a tunnel with windows and torches
  fr() # create a fast (powered) rail tunnel on the floor ahead
```
### Users and Entities
```
  users() # get a python list of Player references
  join('name') # Jump to the current world/position of user with name starting with name
  bring('name') # Jump user with name starting with name to your current position
  unjoin() # Jump back to where you were before you were brought or joined
  back_to_bed() # Jump back to your bed spawn location (last place you slept, normally)
  find_player('name') # search for first player with name-prefix e.g. `find_player('vr').set_location(player.location)` is `bring('vr')`
  spawn('blaze') # spawn an entity right in front of you
  spawn_drop('cow') # spawn an entity 50m above you (it will normally drop dead in front of you if it can't fly)
  spawn_shower('experience_bottle') # drop 30 of the entity in a shower in front of you
```

### Templates and Copying

Copy and paste in minecraft makes it easier to build large and
complex structures. You can create a repeating element, copy it
and then paste it many times.

```  
  getBlocks(8,6,5) # get array of array of block-data for area specified
  copy(name='stamp',depth=5,width=5,height=5) # copy 5x5x5 block in front of you as a template named stamp
  paste(name='stamp') # paste back the template from a copy
```

Pycraft will respond to your requests in chat if the command
returns a non-None result.

### Adding New Commands

The whole point of the project is to let you and your kids create new
"magic" bits that you can add to the game. The commands are generally
fairly short Python functions that e.g. manipulate inventories or blocks.

To make a function available, decorate it with `@pycraft.expose.expose`
and give it keyword-only parameters for accessing the `player`, `world`
etc. You can see examples in `pycraft.acommands` and `pycraft.buildings`

```
@expose()
async def spawn(
    type_name, position=None, *, player: Player = None, world: World = None
):
    """Spawn a new entity of type_id at position (default in front of player)

    type_name -- full minecraft ID for the entity to spawn
    """
    if position is None:
        position = player.position + player.direction
    if not ':' in type_name:
        type_name = 'minecraft:%s' % (type_name,)
    await world.spawnEntity(position, type_name)
```

If you want to create large numbers of blocks, the `world.setBlockList` command
should likely be used, this takes a pair of `Location[]` and `BlockData[]` lists
which are set in a single request.
