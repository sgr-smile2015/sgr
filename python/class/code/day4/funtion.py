#! /usr/bin/python

def div1(x,y):
    print("%s/%s = %s" % (x,y,x/y))

def div2(x,y):
    print("%s//%s = %s" % (x,y,x//y))

div1(5,2)
div1(5.,2)

div2(5,2)
div2(5.,2.)
