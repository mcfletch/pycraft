#! /bin/bash

while true; do
    echo "Making html..."
    make html
    inotifywait -r -qq ./source
    sleep 1
done
