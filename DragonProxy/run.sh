#!/bin/bash

ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
docker run -it -v $ROOT/DragonProxy:/code -p 19132:19132/udp -w /code adoptopenjdk/maven-openjdk8:latest java -jar bootstrap/standalone/target/DragonProxy.jar
