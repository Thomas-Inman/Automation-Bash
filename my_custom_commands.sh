#!/bin/bash


# Create notes and folder function
function nfe() {
    pwd | pbcopy
    cd ~
    cd /Users/thomasinman/coding
    python3 nfe_command.py $1 $2 $3
    cd ~
    cd $(pbpaste)
}


# TicTacToe game function
function TicTacToe() {
    pwd | pbcopy
    cd ~
    cd /Users/thomasinman/coding/TicTacToe
    python3 TicTacToe2.py
    cd ~
    cd $(pbpaste)
}


# Begin podcast function
function podcast() {
    pwd | pbcopy
    cd ~
    cd /Users/thomasinman/coding/Automation
    python3 PodcastFunction.py $1
    cd ~
    cd $(pbpaste)
}
