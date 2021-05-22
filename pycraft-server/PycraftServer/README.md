# PyCraft Backend Server Bukkit Plugin

This is a more modern backend server that does not 
attempt to provide support for older scripts written
to the mcpi api, instead it attempts to provide a 
solid foundation for writing Minecraft manipulation
code from Python.

## How it Works

Uses Java Reflection APIs (mostly) to provide a set of 
namespaces of methods which can be invoked over a network
socket. Uses hand-coded Converter classes which allow
for lookup of target classes via key, path, etc.

On the client side, uses the introspected API to provide 
a relatively directly exposure of the Java API to the Python
callers. The network protocol is very close to JSON, though
it is currently hand coded on the Java side (to avoid
a dependency that might not work under Bukkit Server).

On top of this, the pycraft-chat-server is written such
that users can invoke python-coded commands using Python
syntax from within the world. The chat server listens
for commands and responds in chat to those commands.

## Build/Install Process

```
mvn -e package
cp target/PycraftServer-1.0-SNAPSHOT.jar ${YOUR_WORLD}/plugins/
../run.py -e -d ${YOUR_WORLD}
```