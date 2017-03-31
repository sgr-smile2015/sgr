#!/usr/bin/env python

count = 0 

set_num = input('You stop number?')

while count < 100:
#    print 'loop:', count
    count += 1
    if count == set_num:
        print 'you set number is %d ', set_num
        choice = raw_input('Do you want continue(y/n)')
        if choice == 'n':
            break
    while set_num <= count:
        print 'the nubmer is come over!!'
        set_num = input('You choice?')
    else:
        print "LOOP:",count
