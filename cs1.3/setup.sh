#!/bin/sh -e

# This script will install dependencies.

sudo apt-get update
sudo apt-get install -y wmctrl xdotool libxdo3 python3-xlib python3-xdo

pip install -r requirements.txt
