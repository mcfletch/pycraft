# PyCraft: Python API to Minecraft Java Edition Setup

This repository includes the following:

* dockerised setup to allow developers to easily create a 
  Minecraft Java Edition Server (using [Docker Minecraft Server](https://github.com/itzg/docker-minecraft-server))
* dockerised setup to allow BedRock clients (that is,
  tablet, game console, pocket edition, and Windows native
  clients) to be proxied into the game using
  [Geyser](https://geysermc.org/)
* a sample daemon `pycraft-chat-server` that lets you
  write simple scripts that users can call from the
  text chat in-game via "magic commands"

Note: All trademarks are the property of their respective owners.

## WARNING

THE SERVER IS INSECURE BY DEFAULT. It is intended for 
developers to play with the API with their kids. It is *not* configured
such that it should be exposed on the internet!

The server does not require logins due to the broken nature
of the Pocket Edition Minecraft client, where it will only
allow users to connect to an authenticating server with their
*java edition* login... and if they had a java edition login
they would use the java edition.

Additionally, the `pycraft-chat-server` gives players *in game*
incredible power, allowing them to do almost anything that
the Bukkit API allows you to do. You should only allow people
you trust to connect to your server if you're running
`pycraft-chat-server` against it.

## Creating a Minecraft Java Edition Server with API

Important Note: Do *not* run this install outside
of a firewalled network. By default the server allows
anyone to connect. Particularly if you are going
to allow API access you should not allow untrusted
users to connect.

You have to abide by the [Minecraft EULA](https://www.minecraft.net/en-us/eula)

On your (Ubuntu) Linux machine:

```
apt-get install docker python3 git
git clone https://github.com/mcfletch/pycraft.git
cd pycraft
# Note the --no-install-recommends, this prevents installing
# 300MB of unneeded compilation dependencies
apt-get install python3-virtualenv --no-install-recommends
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
# NOTE: -e declares that you accept the Minecraft EULA (see link above)
./run.py -e -d YOURWORLDDIRECTORY
```

At this point, you have a vanilla Bukkit server running 
in docker with the Geyser bridge and PycraftServer plugins 
installed.

You can connect to your server by choosing Multiuser
in Minecraft Java Edition and typing in the 
IP of your docker host as the server to join.

The Java server is running on TCP and UDP on port `25565`
on your docker host. If enabled (default) the bedrock server
is running on port `19132`. These are the application default
ports.

## Letting Pocket/iOS/Android/XBox/Windows Editions Connect

NOTE: Nintendo Switch editions of Minecraft cannot connect
to servers not on the Nintendo realms service, so you will
likely *not* be able to use Switch devices on your local
server.

By default the Geyser plugin will be installed and run from
within the Minecraft server. If you do not want it to run,
you need to pass `--no-bedrock` to the `./run.py` script.

## Pycraft Server: Talking to Minecraft from Python

The requirements for the demo scripts are declared
in the `requirements.txt` file you installed above.
These instructions assume you already know how to program
in Python3.

To run a demo script:
```
source env/bin/activate
# install pycraft itself...
python3 setup.py develop 
# run your script
python3 scripts/helloworld.py
```

## Pycraft-Chat-Server: Talking to Python from Minecraft

The `pycraft-chat-server` script is a larger example
of using the `pycraft` API. It allows you to expose 
commands to users on your server (remember, keep your
server away from the public).

To run the server:
```
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt -e .
pycraft-chat-server
```
Then from within your minecraft client, press `T`
to get the chat window, and type one of the known
commands.

### Meta Commands
```
  help() # shows all available commands with summary of purpose
  help(command) # show help for that command
  echo( 2+3 ) # evaluates the thing you types and returns it
  echo( player.position ) # show's the calling player's position
  find_blocks('redstone') # search for a block by name-fragment
  find_entities('creep') # search for an entity by name-fragment
  pos = player.position
  # walk around for a bit...
  echo( 'You were standing at'% pos)
  world # reference to the world the user is currently in
  player # reference to the speaking player
  server # reference to the server on which the player is talking
```

### Shelter and Gear
```
  bed() # create a bed in front of you
  hall() # creates a hall in which you can rest, craft, enchant etc.
  give('netherite_sword') # give the indicated item in your inventory
  nice_item('netherite_sword') # give the indicated item and enchant it with lots of enchantments
  nice_gear() # give ridiculously overpowered selection of adventuring gear
```

### Construction
```
  bulldoze() # clears blocks in front of you
  pyramid(material='type') # creates a pyramid of blocks of given type
  block('iron_ore') # create a block in front of you
  p_dome() # creates a parabolic dome out of stained glass
  circle() # creates a circle of material around you
  tunnel() # creates a tunnel with windows and torches
  fr() # create a fast (powered) rail tunnel on the floor ahead
  stairs() # create stairs going up in front of you
  stairs(material='obsidian',ystep=-1) # create stairs going down ahead of you
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



## Bukkit API Access

[PycraftServer](https://github.com/mcfletch/pycraft-server) (the plugin we are using) exposes a significant fraction
of the Bukkit/Spigot/Paper API. It does this using Java reflection
at run-time against the running Spigot server. As a result, there is 
little code in Pycraft or PycraftServer, it just proxies the API through
a JSON RPC mechanism.

Each type that will be supported by PycraftServer has to have a Converter
registered that defines how the type will be converted to and from JSON
structures.  Common types and their conversions are below:

| Class               | Key Specifications                                                                                            |
| ------------------- | ------------------------------------------------------------------------------------------------------------- |
| Server              | any: ignored (is always the server you've connected to but is required, a string such as "server" works fine) |
| World               | str: "name"                                                                                                   |
| Player              | str: "name", str: "uuid"                                                                                      |
| Location            | ["world",0,1,2], ["world",0,1,2,3,4]                                                                          |
| Vector              | [0,1,2]                                                                                                       |
| Entity              | str: "uuid", str: "name"                                                                                      |
| Keyed (Enum)        | str: "namespace:key"                                                                                          |
| Enum                | str: "name"                                                                                                   |
| Material, BlockData | (see: Keyed)                                                                                                  |
| Entity              | (see: Keyed)                                                                                                  |
| Enchantment         | (see: Keyed)                                                                                                  |
| Block               | Location                                                                                                      |
| Inventory           | Entity \| Block reference                                                                                     |
| ItemStack           | [Material,count] (new ItemStack), [index,Inventory] (ItemStack in an Inventory)                               |

You can use `pycraft-chat-server` to directly call Bukkit API from
within the Minecraft server like so (T to chat):

```
# world is the world you are currently standing in...
<VRPlumber> world.generateTree(player.position+(0,0,1), 'MEGA_REDWOOD')
```

```
# show all defined worlds on the server
<VRPlumber> echo([w.name for w in server.getWorlds()])
['world', 'world_nether', 'world_the_end'] (<class 'list'>)
```
```
<VRPlumber> player.position.getBlock().getBlockData()
BlockData(string_value='minecraft:red_carpet',interfaces=['BlockData'],__namespace__='BlockData',__type__='CraftBlockData') (<class 'pycraft.server.world.BlockData'>)
```
Note: if you've read this far, you may be asking "How did that work, where
were the `await` keywords? The interpreter, being asynchronous itself, awaits
partial values and then passes the results to the calling context.

