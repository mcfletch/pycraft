#! /bin/bash 

mvn -e package
cp target/PycraftServer-1.0-SNAPSHOT.jar ../../scratch-world/plugins/
cp target/PycraftServer-1.0-SNAPSHOT.jar ../../moosh-world/plugins/
cp target/PycraftServer-1.0-SNAPSHOT.jar ../../slime-world/plugins/
