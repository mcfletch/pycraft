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

## WARNING

THE SERVER IS INSECURE BY DEFAULT. It is intended for 
developers to work with the API. It is *not* configured
such that it should be exposed on the internet!

The server is insecure by default due to the broken nature
of the Pocket Edition Minecraft client, where it will only
allow users to connect to an authenticating server with their
*java edition* login... and if they had a java edition login
they would use the java edition.

Additionally, the pycraft-chat-server gives players *in game*
incredible power, allowing them to do almost anything that
the Bukkit API allows you to do.

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
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
# NOTE: -e declares that you accept the Minecraft EULA (see link above)
./run.py -e -d YOURWORLDDIRECTORY
```

At this point, you have a vanilla Bukkit server running 
in docker with the Geyser bridge installed.

You can connect to your server by choosing Multiuser
in Minecraft Java Edition and typing in the 
IP of your docker host as the server to join.

The Java server is running on TCP and UDP on port `25565`
on your docker host. If enabled (default) the bedrock server
is running on port `19132`.

## Letting Pocket/iOS/Android/XBox/Windows Editions Connect

NOTE: Nintendo Switch editions of Minecraft cannot connect
to servers not on the Nintendo realms service, so you will
likely *not* be able to use Switch devices on your local
server.

NOTE: We are running a Geyser Proxy Plugin here, it is not
stable, and you should expect to have to restart the server,
particularly if a user lets their tablet/device go to sleep
while connected to the server.

By default the Geyser plugin will be installed and run from
within the Minecraft server. If you do not want it to run,
you need to pass `--no-bedrock` to the `./run.py` script.

## Talking to Minecraft from Python

The requirements for the demo scripts are declared
in the `requirements.txt` file you installed above.

To run a demo script:
```
source env/bin/activate
# install pycraft itself...
python3 setup.py develop 
# run your script
python3 scripts/helloworld.py
```

## Talking to Python from Minecraft

The `pycraft-chat-server` script is a larger example
of using the `mcpi` API. It allows you to expose 
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
commands. For instance:
```
  help() # shows all available commands with summary of purpose
  help('list-entities') # show all available entity names
  help('list-blocks') # show all available block types
  users() # get a python list of entities for each user

  bulldoze() # clears blocks in front of you
  pyramid(material='type') # creates a pyramid of blocks of given type
  block('iron_ore') # create a block in front of you
  hall() # creates a dining hall for a party
  p_dome() # creates a parabolic dome out of stained glass
  tunnel() # creates a tunnel with windows, torches and a rail track
  fr() # create a fast (powered) rail tunnel on the floor ahead

  echo( 2+3 ) # evaluates the thing you types and returns it
  echo( user.position ) # show's the calling user's position
  echo( user.get_nearby_entities() ) # show entities near you
  echo( user.remove_nearby_entities('creeper'))
  find_blocks('redstone')
  find_entities('creep')
  
  click_create('stone') # a sort of fake creative mode as long as you are holding a sword
  click_delete() # one-click removal
  click_cancel() # stop drawing with stone

  echo(user.position+V(0,1,1)) # position at waist-height in front of user

  # NOTE: the following are *extremely* slow due to working block-by-block
  copy(name='stamp',depth=5,width=5,height=5) # copy 5x5x5 block in front of you as a template named stamp
  paste(name='stamp') # paste back the template from a copy
```
You can also assign variables and use them later, 
for instance:
```
  pos = user.position
  # walk around for a bit...
  echo( 'You were standing at'% pos)
```
will cause the python server to respond with `ERR>` or `OUT>`
with the result of your function call. Note that
only function-calls with simple names will be 
interpreted.

Note: 
  All trademarks are the property of their respective owners.
