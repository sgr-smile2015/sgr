#!/bin/bash
# CreateTime: 2018-05-05 14:53:33
set -x

mkdaemon -r -p /home/sgr/daemons/ssh.harbor_local.pid -o /home/sgr/logs/ssh.harbor_local.log ssh -N -o TCPKeepAlive=no -o ServerAliveInterval=30 -o ServerAliveCountMax=3 -o ExitOnForwardFailure=yes  -L 0:5002:vps:80 sgr@dev11
