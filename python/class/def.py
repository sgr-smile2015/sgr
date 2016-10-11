#! /usr/bin/python

from random import randint
num = randint(1,12)

def equal(num1,num2):
    if num1 < num2:
        print 'too small'
        return False;
    if num1 > num2:
        print 'too big ^_^'
        return False;
    if num1 == num2:
        print 'bingo !!'
        return True


print 'guess numbers "?"'
bingo = False
while bingo == False:
    answer = input()
    bingo = equal(answer, num)

def hello(someone):
    print someone + ' say hello'

hello('tom')


