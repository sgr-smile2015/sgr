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

#def check(banner,filename):
#    f.filename.readlines()
def check(banner):
    if 'Ubuntu-2ubuntu2.8' in banner:
        print "[*] is OK"
    elif 'Ubunt' in banner:
        print "[-] is NO"
    else:
        return


def main():
    host=retBanner("192.168.1.46",22)
    check(host)

if __name__=='__main__':
    main()
