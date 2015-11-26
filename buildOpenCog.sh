#!/bin/bash

cd ../opencog
if [git checkout "OpenCogMineCraft"]
then
    echo "Switched Branch to OpenCogMineCraft"
else
    echo "Creating new Branch 'OpenCogMineCraft'"
    git stash
    git checkout -b "OpenCogMineCraft"
    cd ../opencog-to-minecraft
    cp -r opencog/ ../.
fi

cd ../opencog
mkdir build
cd build
cmake ..
make
