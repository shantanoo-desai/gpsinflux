#!/bin/bash

# TMUX Session for GPS Acquisition
sleep 1;

/usr/bin/tmux new-session -d -s gps

/usr/bin/tmux set-option set-remain-on-exit on

# Change path to your home directory here....
/usr/bin/tmux -d -n 'gpsInflux' -t gps:1 'sleep 1; cd /home/root/gpsinflux; until /usr/bin/python3 /home/root/gpsinflux/run.py; do echo $(date) 2>&1; sleep 1; done'
