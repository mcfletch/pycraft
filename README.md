# PyCraft: Python API to Minecraft Java Edition Setup

This repository includes the following:

* dockerised setup to allow developers to easily create a 
  Minecraft Java Edition Server that includes the 
  [RaspberryJuice](https://github.com/zhuowei/RaspberryJuice) 
  remote API that follows the Minecraft Pi Edition API
* dockerised setup to allow BedRock clients (that is,
  tablet, game console, pocket edition, and Windows native
  clients) to be proxied into the game using
  [Geyser](https://geysermc.org/)
* a bunch of sample code for using the mcpi python
  library to construct simple tools
* a nice image-to-maze tool that lets children draw a 
  low-resolution maze on paper and turn it into a 3D
  maze/building
* a sample daemon `pycraft-chat-server` that lets you
  write simple scripts that users can call from the
  text chat in-game via "magic commands"

## WARNING

THE SERVER IS INSECURE BY DEFAULT. It is intended for 
developers to work with the API. It is *not* configured
such that it should be exposed on the internet!

## Creating a Minecraft Java Edition Server with API

Important Note: Do *not* run this install outside
of a firewalled network. By default the server allows
anyone to connect. Particularly if you are going
to allow API access you should not allow untrusted
users to connect.

On your (Ubuntu) Linux machine:

```
apt-get install docker python3 git
git clone https://github.com/mcfletch/pycraft.git
cd pycraft
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
# NOTE: -e declares that you accept the server EULA
# NOTE: -b installs the Geyser plugin to allow BedRock clients to connect
./run.py -e -b -d YOURWORLDDIRECTORY
```

At this point, you have a vanilla Bukkit server running 
in docker with the RaspberryJuice API bridge installed.

You can connect to your server by choosing Multiuser
in Minecraft Java Edition and typing in the 
IP of your docker host as the server to join.

The server is running on TCP and UDP on port 25565
on your docker host.

## Letting Pocket/iOS/Android/XBox/Windows Editions Connect

NOTE: Nintendo Switch editions of Minecraft cannot connect
to servers not on the Nintendo realms service, so you will
likely *not* be able to use Switch devices on your local
server.

NOTE: We are running an experimental DragonProxy here, do 
not expect it to be particularly robust/stable. Expect that
you may need to delete the data directory and restart 
a few times.

The `DragonProxy` subdirectory contains an experimental
setup for letting `BedRock` or `Pocket` editions
of Minecraft connect to a Java Edition server.
The `-b` flag to the top-level `run.py` runs the
DragonProxy setup in such a way that it *should*
be configured to talk to the Minecraft server 
and be exposed on the default BedRock server port.

To manually run or restart the DragonProxy instance,
for instance, to choose a minecraft server other than
the one running in docker as `minecraft`:

```
cd DragonProxy
./run.py -t 192.168.15.32
```

Will run the server with UDP Port 19132 exposed on
your docker host.

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
  players() # shows all current players

  dir() # Tells you what commands are defined
  bulldoze() # clears blocks in front of you
  pyramid(material='type') # creates a pyramid of blocks of given type
  block('iron_ore') # create a block in front of you
  hall() # creates a dining hall for a party
  p_dome() # creates a parabolic dome out of stained glass

  echo( 2+3 ) # evaluates the thing you types and returns it
  echo( user.position ) # show's the calling user's position
  echo( user.get_nearby_entities() ) # show entities near you
  echo( user.remove_nearby_entities('creeper'))
  find_blocks('redstone')
  find_entities('creep')
  
  click_create('stone') # a sort of fake creative mode as long as you are holding a swort
  click_delete() # one-click removal
  click_cancel() # stop drawing with stone

  echo(user.position+V(0,1,1)) # position at waist-height in front of user
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
