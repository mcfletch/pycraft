Developer Setup 
================

Developing code for Pycraft will require a Python development
environment, preferably using Python 3.10+ . Pycraft's source 
code is stored in git on github and can be cloned to your 
local machine.

These command assume an Ubuntu Linux image, such as you can install
using Windows Subsystem for Linux, or running directly on a Linux 
desktop.

.. code:: shell

    apt-get install git python3
    git clone https://github.com/mcfletch/pycraft.git
    cd pycraft

Normally you will want to create a venv to isolate your work
from other Python projects:

.. code:: shell

    # create the virtualenv (only the first time)
    python3 -m venv .env 
    # enter the virtualenv (every time you want to work on the code)
    source .env/bin/activate 
    # install dependencies to make the code work,
    # run this from the `pycraft` top-level directory
    pip install -r requirements.txt -e .

At this point, you should be able to start the minecraft server,
(assuming you have docker setup properly to allow your user to
create containers).

.. code:: shell
    
    # --no-chat is used so that we can run the chat server locally from this directory
    ./run.py -e -d path-to-scratch-world --no-chat

Now you are ready to start your local chat server with:

.. code:: shell

    source .env/bin/activate 
    pycraft-chat-server -H localhost 
