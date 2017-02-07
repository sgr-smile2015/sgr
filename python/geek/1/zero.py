#!/usr/bin/python
#add file testing by 2017
try:
    print "[+] 13/0" +str(13/0)
except Exception, e:
    print "[-] Error = " +str(e)
