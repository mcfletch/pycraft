Pycraft Installation 
=====================

.. note::

    You will need administrative permissions on the box when 
    you are setting up the code, and your user will need to
    be able to run `docker` containers.

The steps required to get Pycraft Running:

    * Get a Docker + Linux environment
    * Get Minecraft (Java Edition Preferred)
    * Get the Runner Script:
    * Read the `Minecraft EULA <https://www.minecraft.net/en-us/eula>`_
    * Run ``pycraft-runner -e -d your-empty-folder-for-your-world``
    * In Minecraft, connect to the server running on your local machine's IP address.

Prerequisites
--------------

We assume you'll be running in a Linux/Unix like environment where docker 
is easily available. The common environments where the code should work are:

* Linux (should work on any native linux machine)
* Windows with Windows Subsystem for Linux (WSL)
* Mac OS-X (in theory)

each of these environments will have a different method for installing the 
prerequisites needed to run.


1) Install Docker (Community Edition)

    For Ubuntu Linux (should also work in Windows+WSL):

    .. code-block:: bash 

        sudo apt-get update
        sudo apt-get install ca-certificates curl gnupg
        sudo mkdir -m 0755 -p /etc/apt/keyrings
        curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
        echo \
            "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
            "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
            sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
        sudo apt-get update
        sudo apt-get install docker-ce docker-ce-cli containerd.io
        sudo usermod -a -G docker $USER 

    Test that you have docker running capability (note: you may need to log out and back in to get your new group to be active):

    .. code-block:: bash 

        docker run -it hello-world


2) Install Minecraft Java (or Windows (Bedrock)) Edition (Requires License from Microsoft)

    Known to work:

        * Java Edition (preferred, native client)
        * Windows Bedrock Edition (works fine, but uses the proxy)
        * iOS Pocket/Bedrock Edition (works fine, but uses the proxy, does not have chat history, so lots more typing)
  
    Known **not** to work:

        * Nintendo Switch Edition (cannot join a non-realms host)

    The Minecraft launcher can be downloaded from Microsoft and requires that you
    purchase a license. The Java Edition gives you "native" support for the server 
    we run here, while Bedrock editions have to use the Geyser plugin to connect.
   
3) Install a `pycraft-runner <https://github.com/mcfletch/pycraft/releases>`_ release

    .. note:: 

        The `pycraft-runner` script is a `pyinstaller` wrapped copy of the script 
        `run.py <https://raw.githubusercontent.com/mcfletch/pycraft/master/run.py>`_ 
        in the root of the pycraft repository. If you are comfortable with Python 
        code, you can download the script, install the two dependencies and run 
        directly from Python.

    For Linux or Windows with WSL, use one of these approaches:

    A) Use the packaged ``pycraft-runner`` executable (for novices):

        .. code-block:: bash 

            wget https://github.com/mcfletch/pycraft/releases/download/version-3.0.1/pycraft-runner-linux-3.0.1.zip
            mkdir pycraft-runner 
            cd pycraft-runner 
            unzip ../pycraft-runner-linux-3.0.1.zip

    B) Clone the pycraft repository and run from the code checkout (for development or coders comfortable with git and Python):

        .. code-block:: bash 

            apt-get install git python3
            git clone --recursive https://github.com/mcfletch/pycraft.git
            cd pycraft
            python -m venv .env 
            source .env/bin/activate 
            pip install -r requirements.txt -e .
            ./run.py -e -d test-world
        
        If you want to develop pycraft itself, or just want to run pycraft on the host, rather than in a container,
        you can pass ``--no-chat`` to the runner script and run the pycraft-chat-server from this checkout:

        .. code-block:: bash

            source .env/bin/activate 
            ./run.py -e -d path-to-scratch-world --no-chat
            pycraft-chat-server 

    
    C) Copy just the runner script and manually setup dependencies:

        .. code-block:: bash 

            wget https://raw.githubusercontent.com/mcfletch/pycraft/master/run.py
            python -m venv .env 
            source .env/bin/activate 
            pip install yaml requests
            ./run.py -e -d test-world

   
4) Start the containers using `pycraft-runner`

    .. code-block:: bash 

        ./pycraft-runner \
            -e \
            -d test-world
    
    or, if running from source code:

        ./run.py \
            -e \
            -d test-world
    
    where `-e` means "I have read and agreed to the `Minecraft EULA <https://www.minecraft.net/en-us/eula>`_" and 
    `-d test-world` means use (and/or create) a world data directory in `test-world`

5) Connect using Minecraft (Java or Bedrock/Pocket Edition)

    Java edition: (Linux, OS-X, Windows)

    * Multiplayer | Add Server

        * Give the server any name you like, such as "Coding Server"

        * Put the IP address of your Docker host as the server address.

    * Click on the blue/purple "Play" triangle next to your newly added server

    Bedrock edition: (Windows)

    .. TODO:: Need to look at what the process is on bedrock

6) Test that the Server is Listening

    * Start the chat window (T on Java Edition, Button in the middle of HUD on Bedrock)
    * Ask the server to echo some text:

      .. code-block:: python

        >>> echo("Hello world!")
        'Hello world!' (<class 'str'>)
    
    * If the server doesn't respond, check:

        * Did you pass the --no-chat flag to the runner?
        * Did the container crash?

Docker Commands
---------------

.. code-block:: shell 

    # show running containers (here the --no-chat was used, so the minecraft-chatserver container isn't running)
    $ docker ps
    CONTAINER ID   IMAGE                          COMMAND    CREATED      STATUS                PORTS                                                                                                                                     NAMES
    867558c2d87e   itzg/minecraft-server:java19   "/start"   2 days ago   Up 2 days (healthy)   0.0.0.0:4712->4712/tcp, :::4712->4712/tcp, 0.0.0.0:25565->25565/tcp, :::25565->25565/tcp, 0.0.0.0:19132->19132/udp, :::19132->19132/udp   minecraft
    # watch the log output from a container
    docker logs -f minecraft
    # stop a container manually 
    docker stop minecraft
