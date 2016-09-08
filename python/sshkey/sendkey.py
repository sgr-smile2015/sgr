#!/usr/bin/python
 
import sys 
import pexpect
 
ip = sys.argv[1]
password = sys.argv[2]
expect_list = ['(yes/no)', 'password:']
 
p = pexpect.spawn('ssh-copy-id ipin@%s' % ip)
try:
    while True:
        idx = p.expect(expect_list)
        print p.before + expect_list[idx],
        if idx == 0:
            print "yes"
            p.sendline('yes')
        elif idx == 1:
            print password
            p.sendline(password)
except pexpect.TIMEOUT:
    print >>sys.stderr, 'timeout'
except pexpect.EOF:
    print p.before
    print >>sys.stderr, '<the end>'
