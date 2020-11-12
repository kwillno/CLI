#!/bin/bash

export DISPLAY=':0.0'
export XAUTHORITY=/home/kwill/.Xauthority

if [ "$1" = "term" ]; then
        xdotool key --clearmodifiers ctrl+alt+F4
fi

if [ "$1" = "home" ];then
        chvt 7
fi      
