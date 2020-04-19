#! /bin/bash
HERE=`pwd`
mkdir -p data/plugins
if [ ! -d "RaspberryJuice" ]; then
    git submodule update --init 
    cp RaspberryJuice/jars/raspberryjuice-1.12.1.jar data/plugins/
fi
docker run -d -p4711:4711 -p25565:25565 -v`pwd`/data:/data -e TYPE=BUKKIT -eEULA=TRUE --name minecraft itzg/minecraft-server


