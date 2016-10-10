#! /usr/bin/python

from random import randint 
num = randint(1,10)

print 'guess number ?'

bingo = False
while bingo == False:
    answer = input()

    if answer < num:
        print 'too small'
    if answer > num:
        print 'too big'
    if answer == num:
        print 'bingo'
        bingo = True

