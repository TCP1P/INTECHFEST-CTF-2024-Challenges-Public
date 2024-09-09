#!/bin/bash

Xvfb :99 -screen 0 1280x720x24 &> /tmp/xvfb.log &

sleep 5

export DISPLAY=:99
export QT_QPA_PLATFORM=offscreen 
export XDG_RUNTIME_DIR=/tmp/runtime-root

python3 /app/src/main.py