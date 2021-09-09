#!/bin/bash

# This program moves all of the files from one directory (src) to another (dst)

function printCorrectInput {
    echo "Correct execution of this program is $0 <source-path> <destination-path>"
}

# Start by checking input:
# Check if we have enough arguments
if [ ! $# -eq 2 ]; then
    echo "The number of arguments is wrong."
    printCorrectInput $0
    exit 1
fi

# Check and save source
src=$1
if [ ! -d $src ]; then
    echo "The source-path given as input doesn't exist."
    printCorrectInput $0
    exit 1
fi 

# Check and save destination
dst=$2
if [ ! -d $dst ]; then
    echo "The destination-path given as input doesn't exist."
    printCorrectInput $0
    exit 1
fi 



# Perform the actual task:
# Move all of the files from source to destination
mv $src/* $dst 