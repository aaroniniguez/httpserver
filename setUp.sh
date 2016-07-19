#!/bin/bash

cp ./ssl_server2.py /
cp ./rc.local /etc/
cp ./runjob.sh /
cp ./localhost.pem /
mkdir /cgi-bin
cp ./test.py /cgi-bin
cd /
openssl req -new -x509 -keyout localhost.pem -out localhost.pem -days 365 -nodes
nohup bash ./runjob.sh &
echo "https://yourip:8000/cgi-bin/test.py"
