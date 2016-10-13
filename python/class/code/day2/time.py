#! /usr/bin/python

import time
starttime = time.time()
print type(starttime)
print 'start: %s' % starttime

for i in range(20):
    print i,
print 
endtime = time.time()
print 'end: %f' % endtime

print 'total time:-> %f' % (endtime - starttime)
