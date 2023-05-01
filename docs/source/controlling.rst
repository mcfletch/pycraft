Controlling Minecraft from Python
==================================

The ``pycraft-chat-server`` allows you to run Python code from within
Minecraft, but to do anything useful, the code you run needs to be able
to affect the Minecraft worlds. The API we use to control Minecraft
is provided by the `PycraftServer <https://github.com/mcfletch/pycraft-server>`_
plugin which the runner script has injected into the server container.

PycraftServer's API is based on the `Bukkit/Spigot API <https://hub.spigotmc.org/javadocs/spigot/index.html>`_
which it exposed via a JSON based RPC mechanism. The API exposes many, but 
not all of the Bukkit APIs.

Creating a Channel
------------------

To interact with the PycraftServer API, we create a :py:class:`pycraft.server.channel.Channel`
instance and ask it to introspect the APIs available from the server.

.. code:: python 

    from pycraft.server import final, channel

    async def get_server():
        server = channel.Channel(debug=False)
        await server.open()
        await server.introspect()
        return server

Controlling the Server
-------------------------

After we have the server Channel, we can start making calls on the PycraftServer API.
The normal way to do that is to use one of the Proxy classes that are added to the 
:py:mod:`pycraft.server.final` namespace during the :py:meth:`pycraft.server.channel.Channel.introspect` call.

.. literalinclude :: ../../scripts/showusers.py
   :language: python

Getting Access to a World 
--------------------------

.. literalinclude :: ../../scripts/startstorm.py
   :language: python

Reusing ChatServer Code
--------------------------

There is a lot of code in the `pycraft-chat-server` which is useful
but relies on having references to objects or records:

.. list-table:: 

    * - :py:class:`pycraft.server.final.Server`
      - ``server = final.Server()``
    * - :py:class:`pycraft.server.final.World`
      - ``world = final.World(name='world')``
    * - :py:class:`pycraft.server.final.Player`
      - ``player = await acommands.find_player('name',server=server)``

.. literalinclude :: ../../scripts/nicegear.py
   :language: python
