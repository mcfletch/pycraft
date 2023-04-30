# PyCraft: Python in Minecraft Chat

Pycraft is a dockerised Minecraft server that lets you
interactively use Python code from within the world to
manipulate the environment.

You can open a text-chat window and type code such as:

 ```
 paste('red_fortress')
 give('cooked_beef',count=64)
 ```

and the python server container will paste in a large
fortress complete with a redstone gate or give you a 
whole stack of steak.

[![Youtube Video Showing the Paste Command](http://img.youtube.com/vi/dM_s-SX_Vfg/0.jpg)](http://www.youtube.com/watch?v=dM_s-SX_Vfg "Create a Mansion for Exploring Minecraft in one Command")
[![Youtube Video Showing Paste Command with Redstone](http://img.youtube.com/vi/su93P0UlspY/0.jpg)](http://www.youtube.com/watch?v=su93P0UlspY "Tour the Red Fortress Paste with Pycraft in Minecraft 1.19.2")
[![Youtube Video Showing Inventory Manipulation](http://img.youtube.com/vi/6jTjcPHK2u0/0.jpg)](http://www.youtube.com/watch?v=6jTjcPHK2u0 "It's dangerous out there, cover yourself in debris with this command in Minecraft with Pycraft")
[![Youtube Video Showing More Inventory Manipulation](http://img.youtube.com/vi/szqi6IRF1Mo/0.jpg)](http://www.youtube.com/watch?v=szqi6IRF1Mo "Feeding yourself in Minecraft with Pycraft, food, food stacks, super-hoe and wheat farm")
[![Youtube Video Showing Bubble Columns](http://img.youtube.com/vi/CFb1FQ7Rz94/0.jpg)](http://www.youtube.com/watch?v=CFb1FQ7Rz94 "Up and Down Bubble Elevators for Mine Access in Pycraft with Minecraft 1.19")
[![Youtube Video Showing Block State Manipulation](http://img.youtube.com/vi/PLyHif5C7-c/0.jpg)](http://www.youtube.com/watch?v=PLyHif5C7-c "Manipulate Block State (new feature) using Bukkit API from Python in Minecraft 1.19")

The Python server supports a fairly large, but not 
complete subset of Python. The API that is exposed is
extensive, being most of the common features from the
Java Bukkit API.

## Quick Start

If you are familiar with Docker and Linux, this should get you started:

* Get a Docker + Linux environment (e.g. WSL)
* [Download a release](https://github.com/mcfletch/pycraft/releases)
* Unzip into a directory in your Linux environment
* Read the [Minecraft EULA](https://www.minecraft.net/en-us/eula)
* Run `pycraft-runner -e -d your-empty-folder-for-your-world`

In Minecraft, connect to the server running on your local machine's IP address.

## What is Here

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
they could use the java edition.

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

For a Windows Machine:

* Install Windows Subsystem for Linux (will require Administrator permissions)
* Install Docker in the WSL environment

For (Ubuntu) Linux machine(s):
* Install docker `apt-get install docker-ce`

For both:

* Download the Stand-Alone Linux Run-script, unpack to a directory
* Run `run --help` to see options
* Read the [Minecraft EULA](https://www.minecraft.net/en-us/eula)
* Run `run -e -d YOURWORLDDIRECTORY`


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

