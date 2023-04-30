
Pycraft: Python Code in Minecraft
==================================

Pycraft is a dockerised Minecraft server that lets you
interactively use Python code from within the Minecraft 
world to manipulate the environment.

You can open a text-chat window in-game and type code such as::
   
 player.teleport((23,200,0)) # move yourself
 find_player('vrplum').get_location() # find out where someone is
 join('vrplum') # join that person
 paste('red_fortress') # paste from library of structures
 give('cooked_beef',count=64) # manipulate your inventory

The code in-world is parsed by the Python interpreter, then
processed to result in calls to a server component `PyCraftServer <https://github.com/mcfletch/pycraft-server>`_ running 
in the Minecraft Java Edition Server (technically a Spigot/Bukkit server)
which is provided by the `itzg/minecraft-server docker image <https://github.com/itzg/docker-minecraft-server>`_ .

Quick Start 
------------
.. note::

   Keep in mind that you **SHOULD NOT** run this on the public internet!

If you are familiar with Docker and Linux, this should get you started.

* Get a Docker + Linux environment (e.g. WSL)
* `Download a release <https://github.com/mcfletch/pycraft/releases>`_
* Unzip into a directory in your Linux environment
* Read the `Minecraft EULA <https://www.minecraft.net/en-us/eula>`_
* Run `pycraft-runner -e -d your-empty-folder-for-your-world`

See: :doc:`installation` for details and :doc:`devsetup` for running 
the code on your host for development.

In Minecraft

* Connect to the server running on your local machine's IP address
* Start the chat window (T in Java Edition)
* Begin typing code::

   # show the available functions/classes
   dir() 
   # echo a value back to you
   echo(2+2)

Other machines on your local network will be able to connect to your Minecraft instance, and they
will be able to run nearly-arbitrary code from the chat window, so you should 
definitely *not* expose your machine to the internet while running this server.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   devsetup
   chatserver
   builtins
   api/modules


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
