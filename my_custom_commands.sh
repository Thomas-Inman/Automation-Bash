#!/bin/bash


# Create notes and folder function
function nfe() {
    pwd | pbcopy
    cd ~
    # Replace the path below with the path to the nfe_command.py script
    cd # Your PATH
    python3 nfe_command.py $1 $2 $3
    cd ~
    cd $(pbpaste)
}


# Begin podcast function
function podcast() {
    pwd | pbcopy
    cd ~
    # Replace the path below with the path to the PodcastFunction.py script
    cd # Your PATH
    python3 PodcastFunction.py $1
    cd ~
    cd $(pbpaste)
}
