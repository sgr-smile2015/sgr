#! /usr/bin/python

def mult():
    return [lambda x :i*x for i in range(4)]

print [m(2) for m in mult()]

# output list [0,2,4,6]

def mult():
    return [lambda x , i=i :i*x for i in range(4)]

print [m(2) for m in mult()]

