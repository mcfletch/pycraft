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

Why?
-----

* Creates a Dockerised Minecraft Java Edition server with reasonable defaults

   * Allows vanilla clients to connect, no plugins required client-side
   * Allows Java/Bedrock clients to interact in the same world
   * Start a server with: ``./run.py -d path-to-your-world``

* Lets you use (or learn) Python to interact with the rich `Bukkit API <https://hub.spigotmc.org/javadocs/bukkit/index.html>`_
* You can call your Python code directly from Minecraft using Python syntax

Quick Start 
------------
.. note::

   Keep in mind that you **SHOULD NOT** run this on the public internet!
   Pycraft is intended to give you a powerful environment where you can do 
   extremely powerful and cool things, but that power is available to 
   **anyone who connects to your server**.

If you are familiar with Docker and Linux, this should get you started.

* Get a Docker + Linux environment (e.g. WSL)
* `Download a release <https://github.com/mcfletch/pycraft/releases>`_
* Unzip into a directory in your Linux environment
* Read the `Minecraft EULA <https://www.minecraft.net/en-us/eula>`_
* Run `pycraft-runner -e -d your-empty-folder-for-your-world`

See: :doc:`installation` for details.

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
   :maxdepth: 5
   :caption: Contents:

   installation
   Python from Minecraft <chatserver>
   Extending Pycraft <scripts>
   Minecraft from Python <controlling>
   API Reference <api/pycraft>


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
