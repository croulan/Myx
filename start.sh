#!/bin/bash

sudo mongod &

cd Downloads/Senior\ Design/MyxService/Webapp/
sudo iptables -A INPUT -p tcp --dport 3000 -j ACCEPT

nodemon server.js
