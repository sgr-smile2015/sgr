#! /usr/bin/python

import socket

def retBanner(ip,port):
    try:
        socket.setdefaulttimeout(3)
        s = socket.socket()
        s.connect((ip,port))
        banner = s.recv(1024)
        return banner
    except:
        return
def main():
    print retBanner("192.168.1.46",22)

if __name__=='__main__':
    main()
