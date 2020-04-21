#!/bin/bash

ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
DRAGON_DOCKER_ARGS="-v $ROOT/DragonProxy:/code -w /code adoptopenjdk/maven-openjdk8:latest java -jar bootstrap/standalone/target/DragonProxy.jar"

if [ -z $1 ]; then
    echo "Usage: $0 <proxy destination ip>"
    exit
elif [ ! -d $ROOT/DragonProxy ]; then
    echo "Run build.sh first"
    exit
elif [ ! -f $ROOT/DragonProxy/config.yml ]; then
    # Generate a default config
    echo 'stop' | docker run -i -a STDIN $DRAGON_DOCKER_ARGS
fi

# Start!
sed -i -e "s/^\(remote-address\):.*/\1: '$1'/" $ROOT/config.yml
docker run -it -p 19132:19132/udp $DRAGON_DOCKER_ARGS
