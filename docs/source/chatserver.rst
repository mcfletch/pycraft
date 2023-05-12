Pycraft-Chat-Server: Talking to Python from Minecraft
======================================================

The `pycraft-chat-server` script is a larger example
of using the `pycraft` API. It allows you to expose 
commands to users on your server (remember, keep your
server away from the public). The implementation is in
:py:mod:`pycraft.achatserver`

.. note::

  The run-script normally starts the chat server in a container
  configured to talk to the Minecraft server. 

  See :doc:`./installation` for details on how to setup
  the server containers.

Calling Python from Minecraft
-----------------------------

Then from within your minecraft client, press `T`
to get the chat window, and type your Python code.

.. note::

    In iOS and similar Bedrock clients, you will find the chat 
    window is a button between the Health and Hunger bars.

The `pycraft-chat-server` is listening for chat commands that 
it can recognise as Python code. If it can parse your chat message
it will attempt to execute the code (here my username is 
VRPlumberMagic)::

    <VRPlumberMagic> echo('hello')
    'hello' (<class 'str'>)
    <VRPlumberMagic> echo( 2 + 3 )
    5 (<class 'int'>)
    <VRPlumberMagic> echo( 2 * 3 )
    6 (<class 'int'>)
    <VRPlumberMagic> echo( 2 ** 3 )
    8 (<class 'int'>)
    <VRPlumberMagic> echo( 2 / 3 )
    0.6666666666666666 (<class 'float'>)

    <VRPlumberMagic> echo( player.location )
    ['world',2128.4617685823027,93.0,-1681.4257264464052,-175.81409,4.1994276] (<class 'pycraft.server.world.Location'>)
    <VRPlumberMagic> player.teleport(player.location+player.direction*2)
    True (<class 'bool'>)
    <VRPlumberMagic> find_blocks('shulk')
    ['minecraft:shulker_box', 'minecraft:white_shulker_box', 'minecraft:orange_shulker_box', 'minecraft:magenta_shulker_box', 'minecraft:light_blue_shulker_box', 'minecraft:yellow_shulker_box', 'minecraft:lime_shulker_box', 'minecraft:pink_shulker_box', 'minecraft:gray_shulker_box', 'minecraft:light_gray_shulker_box', 'minecraft:cyan_shulker_box', 'minecraft:purple_shulker_box', 'minecraft:blue_shulker_box', 'minecraft:brown_shulker_box', 'minecraft:green_shulker_box', 'minecraft:red_shulker_box', 'minecraft:black_shulker_box', 'minecraft:shulker_spawn_egg', 'minecraft:shulker_shell'] (<class 'list'>)
    
    <VRPlumberMagic> echo([w.name for w in server.getWorlds()])
    ['world', 'world_nether', 'world_the_end'] (<class 'list'>)

    <VRPlumberMagic> x = 3+4
    7 (<class 'int'>)
    <VRPlumberMagic> y = 4+5
    9 (<class 'int'>)
    <VRPlumberMagic> echo(x+y)
    16 (<class 'int'>)


`pycraft-chat-server`` will respond to your requests in chat if the command
returns a non-None result.


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

.. container:: video-list

  .. youtube:: dM_s-SX_Vfg

  .. youtube:: 6jTjcPHK2u0

  .. youtube:: szqi6IRF1Mo

  .. youtube:: CFb1FQ7Rz94

  .. youtube:: PLyHif5C7-c

  .. youtube:: su93P0UlspY


Meta Commands
--------------

These commands allow you to figure out how to work with other commands 
or objects. They allow you to ask the `pycraft-chat-server` what you 
can do from within the chat window.

.. list-table::
    :header-rows: 1
    :width: 100%

    * - Implementation 
      - Chat Call
      - Description 
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
    * - :py:func:`pycraft.acommands.this_guy`
      - ``this_guy() => right-click-on-entity``
      - Returns a reference to the next Entity that the user `interacts`
        with; normally by right-clicking on e.g. a Villager.

Shelter and Gear 
-----------------

These commands let you set up a world where kids can be ready-to-adventure as soon 
as they log in (e.g. for birthday parties and the like). You can easily setup 
houses, grant advanced equipment and let new players "catch up" with more 
advanced players.

.. list-table:: Basic Shelter
    :header-rows: 1
    :width: 100%

    * - Implementation 
      - Chat Call
      - Description 
      - 
    * - :py:func:`pycraft.acommands.bed`
      - ``bed(color='black')``
      - Creates a bed in front of the user
      - .. image:: _static/img/bed.png
          :width: 256
          :alt: Image of a bed
      
    * - :py:func:`pycraft.buildings.hall`
      - ``hall()``
      - Build a stone hall with bed, crafting table, furnace and the like.
       
        .. note::

            Note: there are nicer buildings available with :py:func:`pycraft.copypaste.paste`
            hall is more of an example of programatically setting up a building.
      - .. image:: _static/img/hall.png
          :width: 256
          :alt: Image of the generated hall
    * - :py:func:`pycraft.buildings.temple`
      - ``temple()``
      - Build an empty stone temple in front of the user. The inside of the temple is 
        empty and there are no doors on the structure.
      - .. image:: _static/img/temple.png
          :width: 256
          :alt: Image of the generated temple

.. list-table:: paste() Shelter
    :header-rows: 1
    :width: 100%

    * - Implementation 
      - Chat Call
      - Description 
      - 

    * - :py:func:`pycraft.copypaste.paste`
      - paste('dark_house')
      - Deepslate and Iron Bar Pavilion Style house with lanterns, bed, crafting table and furnace.
        Does not provide complete shelter, as the iron grill can be shot through and Creepers
        can get close enough to blow up. Use within a larger complex.
      - .. image:: _static/img/dark_house.png
          :width: 256
          :alt: Image of the pasted dark house
    
    * - :py:func:`pycraft.copypaste.paste`
      - paste('lantern_mansion')
      - Large well-appointed house with shulker boxes, multiple beds, crafting table, music box,
        and bookshelves.
      - .. image:: _static/img/lantern_mansion.png
          :width: 256
          :alt: Image of the pasted lantern_mansion

    * - :py:func:`pycraft.copypaste.paste`
      - paste('red_fortress')
      - Large well-appointed red-sandstone fortress with enchanting area, bed, crafting table, furnace,
        redstone powered large gate.
      - .. image:: _static/img/red_fortress.png
          :width: 256
          :alt: Image of the pasted red_fortress

.. list-table:: Gear
    :header-rows: 1
    :width: 100%

    * - Implementation 
      - Chat Call
      - Description 

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
The 

.. list-table:: Construction
    :header-rows: 1
    :width: 100%

    * - Implementation 
      - Chat Call
      - Description 

    * - :py:func:`pycraft.acommands.block`
      - ``block('iron_block')``
      - Create the given block in front of the player's legs.
        Note: py:meth:`pycraft.server.final.World.setBlockList` is more 
        efficient and flexible than setting individual blocks with `block`
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
    * - :py:func:`pycraft.parabolic.parabolic_dome`
      - ``p_dome()``
      - Creates a loosely-parabolic dome with stained glass blocks centered
        around the player's position. The dome has an oculus at the top
        but makes a pleasant super-structure for setting up a base.

    * - :py:func:`pycraft.parabolic.draw_circle`
      - ``circle()``
      - Creates a loosely-circular set of blocks around the user's position
    
    * - :py:func:`pycraft.tunnels.tunnel`
      - ``tunnel(depth=25, width=3, height=3)``
      - Create a well-lit tunnel with stained-glass walls forward from the
        player's position. Useful for tunneling through mountains, underwater,
        or otherwise setting up a passage.
    * - :py:func:`pycraft.tunnels.tunnel_continue`
      - ``tunnel_continue()``
      - Extends the previously created tunnel.

    * - :py:func:`pycraft.tunnels.fast_rail`
      - ``fr(depth=100, base='glass')``
      - Create a fast-rail (minecart rails with power) that continues for depth blocks in the 
        direction the user is facing. Specify ``base`` to have the fast rail 
        construct a base on which the rails will be placed, otherwise the 
        rails will be placed, but may immediately fall.

Manipulating Entities and Players
-----------------------------------

.. list-table:: Players and Teleporting
    :header-rows: 1
    :width: 100%

    * - Implementation 
      - Chat Call
      - Description 

    * - :py:func:`pycraft.acommands.keep_inventory`
      - ``keep_inventory(True)``
      - Turns world's keep-inventory flag on so that novice players aren't 
        frustrated with losing everything every time they die.
    * - :py:func:`pycraft.acommands.players`
      - ``players()``
      - Retrieves :py:class:`pycraft.server.final.Player` references 
        for all players in the world of the player making the call.
    * - :py:func:`pycraft.acommands.find_player`
      - ``find_player(fragment:str)``
      - Returns the first online :py:class:`pycraft.server.final.Player` whose name contains the given 
        fragment. The player does not need to be in the same world as 
        the caller.
    * - :py:func:`pycraft.acommands.join`
      - ``join('vr')``
      - Searches for the (first) player with the fragment 'vr' in their name and teleports to their location
    * - :py:func:`pycraft.acommands.bring`
      - ``bring('vr')``
      - Brings the (first) player with the fragment 'vr' in their name and teleports them to your location
    * - :py:func:`pycraft.acommands.unjoin`
      - ``unjoin()``
      - Returns you to the location you were at before a ``join`` or ``bring`` teleported you.
     
    * - :py:func:`pycraft.acommands.back_to_bed`
      - ``back_to_bed()``
      - Returns you to the location of your ``Bed Spawn Location`` which is basically the location 
        of the bed in which you last slept (note that breaking that bed means you no longer have that location)

.. list-table:: Entities and Spawning
    :header-rows: 1
    :width: 100%

    * - Implementation 
      - Chat Call
      - Description 

    * - :py:func:`pycraft.acommands.spawn`
      - ``villager = spawn('villager')``
      - Creates a new entity and returns a reference to them
    * - :py:func:`pycraft.acommands.spawn_drop`
      - ``spawn_drop('cow')``
      - Creates a new entity 50 blocks over your current location, when you are 
        standing on the surface this has the effect of dropping that entity in 
        front of you, normally dropping some resources.
    * - :py:func:`pycraft.acommands.spawn_shower`
      - ``spawn_shower('experience_bottle', count=50)``
      - Showers entities with ``spawn_drop`` every 1/10th of a second until 
        the number of entities specified are dropped. You can specify the 
        height of the drop (e.g. if the height is 1 most mobs will survive).

Templates and Copying
----------------------

Copy and paste in minecraft makes it easier to build large and
complex structures. You can create a repeating element, copy it
and then paste it many times.


.. list-table:: Entities and Spawning
    :header-rows: 1
    :width: 100%

    * - Implementation 
      - Chat Call
      - Description 
    * - :py:func:`pycraft.copypaste.copy`
      - copy('my_template', width=10,depth=8, height=7)
      - Copies a rectangular prism of blocks into a template 
        which can be pasted later.

    * - :py:func:`pycraft.copypaste.paste`
      - paste('my_template')
      - Pastes a previously-copied prism of blocks into a the world 
    
    * - :py:func:`pycraft.copypaste.show_pastes`
      - show_pastes('my')
      - Lists the names of pastes which contain the given fragment

    * - :py:meth:`pycraft.server.final.World.getBlocks`
      - world.getBlocks(start_location, (x_size,y_size,z_size))
      - Returns the materials in the prism with x,y,z sizes
        core operation on which copy is based

    * - :py:meth:`pycraft.server.final.World.getBlockArray`
      - world.getBlockArray(start_location, end_location)
      - Returns the materials in the prism from start to end location 
        as a list of lists of materials

