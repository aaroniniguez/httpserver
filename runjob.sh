#!/bin/bash
#make-run.sh
#make sure a process is always running.

export DISPLAY=:0 #needed if you are running a simple gui app.

process=ssl_server2.py
makerun="python /ssl_server2.py"

while true
do
	if ! ps ax | grep -v grep | grep $process > /dev/null
	then
	    $makerun &
	fi
	sleep 5
done
