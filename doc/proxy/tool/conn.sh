#!/bin/sh

do_conn() {
	ssh_c -o TCPKeepAlive=no -o ServerAliveInterval=30 -o ServerAliveCountMax=3 -o ExitOnForwardFailure=yes \
		-l sgr  -p $2 -N \
		-R :1002:localhost:22 $1 
	sleep 10
}

while true; do
	do_conn  12.18.1.4 22
done
