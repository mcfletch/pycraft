Pycraft Installation 
=====================

.. note::

    You will need administrative permissions on the box when 
    you are setting up the code, and your user will need to
    be able to run `docker` containers.

The steps required to get Pycraft Running:

* Get a Docker + Linux environment
* Get Minecraft (Java Edition Preferred)
* [Download a release](https://github.com/mcfletch/pycraft/releases)
* Read the [Minecraft EULA](https://www.minecraft.net/en-us/eula)
* Run `pycraft-runner -e -d your-empty-folder-for-your-world`
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

    For Linux or Windows with WSL:

    .. code-block:: bash 

        wget https://github.com/mcfletch/pycraft/releases/download/version-3.0.1/pycraft-runner-linux-3.0.1.zip
        mkdir pycraft-runner 
        cd pycraft-runner 
        unzip ../pycraft-runner-linux-3.0.1.zip
    
    The actual script that is being run is in the root directory of the 
    pycraft repository and is called `run.py` there. If you don't have a 
    packaged repository, or want to develop pycraft itself:

    .. code-block:: bash 

        git clone --recursive https://github.com/mcfletch/pycraft.git
        cd pycraft
        python -m venv .env 
        source .env/bin/activate 
        pip install -r requirements.txt 
        ./run.py -e -d test-world
   
4) Start the containers using `pycraft-runner`

    .. code-block:: bash 

        ./pycraft-runner \
            -e \
            -d test-world
    
    where `-e` means "I have read and agreed to the Minecraft Server EULA" and 
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

      .. code-block:: pycon

        >>> echo("Hello world!")
        'Hello world!' (<class 'str'>)


.. TODO:: Debugging, showing running containers, etc