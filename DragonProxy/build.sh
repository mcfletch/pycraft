#!/bin/bash
ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

if [ ! -d $ROOT/DragonProxy ]; then
    git clone https://github.com/DragonetMC/DragonProxy .
    ln -s $ROOT/DragonProxy/config.yml $ROOT/config.yml
else
    ( cd $ROOT/DragonProxy && git pull )
fi
docker run -it -v $ROOT/DragonProxy:/code -w /code adoptopenjdk/maven-openjdk8:latest mvn clean package
