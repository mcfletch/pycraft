Extending Pycraft with Scripts
================================

You can create and expose a new command to `pycraft-chat-server` by
adding a new Python file (a file with the extension `.py`) to the 
`scripts` directory.

.. note:: 

    **Where is the `scripts` Directory?**

    If you've started `pycraft-chat-server` from the 
    runner and the server is running in a container, you'll find the scripts 
    folder in the directory where you started `pycraft-chat-server`.

    If you've run `pycraft-chat-server` from a git checkout, then the scripts 
    directory will have defaulted to `/var/pycraft/scripts`. You can re-run 
    the server and pass `--scripts path-you-wish-to-use` if you'd like to 
    use a different location.

Hello World 
-----------

This is the simplest example of a script. You don't have to type any line 
that starts with a `#` as those are just comments to other programmers.
Most programs don't have quite as many comments as this, particularly for 
such a small program.

Create a file in your editor, and save it into the `scripts` directory
as `helloworld.py`.

Add the lines that do *not* have # at the start to the file and save.
`pycraft-chat-server` will print a message in chat telling you that it
is reloading your script.

.. literalinclude:: ../../examples/helloworld.py 

All you really need in your file is:

.. literalinclude:: ../../examples/helloworldclean.py

In chat, call your script with::

  hello_world()

You will get back a message saying `"Hello World!" (type str)` which 
is the chat server telling you about the result you returned from 
your function.

Parameters and Players 
-----------------------

Most of the time, you want to be able to actually do something with 
your function. The set of parameters you function takes can be thought 
of as the "things it works with", so if you want to work with a player,
then you need to pass that player into the function.

`pycraft-chat-server` has a quirk (thing that isn't common) in that it 
will look at your function and check to see if you've said you need a 
player, a world, etc as a parameter, and will provide that automatically 
from the default namespace when it goes to run your function.

Let's look at a function that takes the current player (the one chatting
with the chat-server) and returns their :py:class:`pycraft.server.final.Location`
which includes the `world, x, y, z, yaw, pitch` defining where in the game 
the player currently is.

We can save this function in a file in the `scripts` directory:

.. literalinclude:: ../../examples/whereami.py

In chat, call your script with::

  whereami()

and it will return the `Location` object describing where you are currently 
standing.

Waiting for Changes 
---------------------

We can find in the :py:class:`pycraft.server.final.Player` that is has 
a method :py:meth:`pycraft.server.final.Player.teleport` that can take 
a :py:class:`pycraft.server.final.Location` and move the player to 
that location.

Let's try to make a `super_jump` function that moves the player 100m
straight up.

When we actually want to interact with the game, we need to wait for the 
communication with the server. You'll recall that we've been adding a
word `async` in front of our function definitions (`def`). The reason for 
this `asynchronous` marker is to make it possible for our functions to 
wait for changes from the server.

If we **don't** wait for the changes, **nothing** will happen.

.. code:: python 

    @expose()
    async def super_jump(*, player):
        # this is *broken* because we don't wait for the change to be applied!
        player.teleport(
            player.location
            + (
                0,
                100,
                0,
            )
        )

So when we are trying to ask the server to do something, we have to **await**
the results of the change. It is very easy to forget to do this, so if you 
find yourself trying to debug why something didn't happen, check that you've
`await`'d the operation.

.. literalinclude:: ../../examples/superjump.py 
    