#!/bin/bash

cp ./ssl_server2.py /
cp ./rc.local /etc/
cp ./runjob.sh /
cp ./test.pem /
cp ./test.py /cgi-bin
cd /
nohup bash ./runjob.sh &
