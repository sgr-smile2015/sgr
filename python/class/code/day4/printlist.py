#! /usr/bin/python

def ext(val, list=[]):
    list.append(val)
    return list

list1 = ext(10)
list2 = ext(12,[])
list3 = ext('a')

print "list1 = %s" % list1
print "list2 = %s" % list2
print "list3 = %s" % list3

print "\n" 

# output list1[10] list2[12] list3[a]

def ext(val, list=None):
    if list is None:
        list = []
    list.append(val)
    return list

list1 = ext(10)
list2 = ext(12,[])
list3 = ext('a')

print "list1 = %s" % list1
print "list2 = %s" % list2
print "list3 = %s" % list3
