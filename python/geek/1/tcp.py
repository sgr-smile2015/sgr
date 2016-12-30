#! /usr/bin/python

import socket

socket.setdefaulttimeout(3)

s = socket.socket()
s.connect(("192.168.1.81",22))
ans = s.recv(1024)
print ans
