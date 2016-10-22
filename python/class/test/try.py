#! /usr/bin/python

try:
    f = file('no.txt')
    print 'File Opened!'
    f.close()
except:
    print 'file not exists.'
    
print 'done'
        
