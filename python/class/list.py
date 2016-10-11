#! /usr/bin/python

print range(1, 9)

x = range(1,9)
for i in x:
    print i,

list = [32, 'everyday', 0.8,True]
print 
print list[1]
list[3] = 98
print list[3]

list.append(234)
print list[-1]
