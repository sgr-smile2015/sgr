#! /usr/bin/python

import socket

socket.setdefaulttimeout(3)

s = socket.socket()
try:    
    s.connect(("192.168.1.46",21))
except Exception,e:
    print "[-] Error = " +str(e)
ans = s.recv(1024)
print ans
