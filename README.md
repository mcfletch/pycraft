# PyCraft: Python API to Minecraft(TM) Java Edition Setup

This repository includes the following:

* a dockerised setup to allow you to easily create a 
  Minecraft Java Edition Server that includes the 
  RaspberryJuice remote API
* a bunch of sample code for using the mcpi python
  library to construct simple tools

## Creating a Minecraft Java Edition Server with API

Important Note: Do *not* run this install outside
of a firewalled network. By default the server allows
anyone to connect. Particularly if you are going
to allow API access you should not allow untrusted
users to connect.

On your linux machine:

```
apt-get install docker
git clone https://github.com/mcfletch/pycraft.git
cd pycraft
git submodule update --init --remote
# NOTE: the following declares that you agree to
# the Minecraft Server API EULA
./run.sh
```

At this point, you have a vanilla server running in docker
with the RaspberryJuice API bridge installed.

You can connect to your server by choosing Multiuser
in Minecraft Java Edition and typing in the 
IP of your docker host as the server to join.

## Talking to Minecraft from Python

The requirements for the demo scripts are declared
in the `requirements.txt` file. Use standard Python
setup to create a Python 3.6+ virtualenv and
`pip install -r requirements.txt` into that 
environment.

See the files in the `scripts` directory which include
simple stand-alone commands that can be run with:

```
source venv/bin/activate
python3 scripts/helloworld.py
```

## Talking to Python from Minecraft

The `pycraft.chatcommands` script is a larger example
of using the `mcpi` API. It allows you to expose 
commands to users on your server (remember, keep your
server away from the public).

To run the server:
```
source venv/bin/activate
python3 setup.py develop
pycraft-chat-server
```
Then from within your minecraft client, press `T`
to get the chat window, and type one of the known
commands. For instance:
```
    sin(pi)
    dir()
    help(p_dome)
    p_dome(user.position,30)
    help(bulldoze)
    bulldoze(10,10,3)
    echo(user.position+V(0,1,1))
    echo(user.position+user.direction)
    echo(user.name)
```
will cause the python server to respond as `<Bot>`
with the result of your function call. Note that
only function-calls with simple names will be 
interpreted.


All trademarks are the property of their respective
owners.