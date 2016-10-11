#! /usr/bin/python

from random import choice
score_you = 0
score_com = 0
direction = ['1','2','3']

for i in range(3):
    print '==Round %d - you kick! ==' % (i+1)
    print 'choose one'
    print '1,2,3'
    you = input()
    print 'you kicked->' + str(you)
    com = choice(direction)
    print 'computer saved_.' + str(com)
    if you != com:
        print "Good"
        score_you += 1
    else:
        print "Oo00..."
    print 'score:%d(you) - %d(com)\n' %(score_you,score_com)  

    print '==Round %d - you saved! ==' % (i+1)
    print 'choose one'
    print '1,2,3'
    you = input()
    print 'you saved->' + str(you)
    com = choice(direction)
    print 'computer kicked_.' + str(com)
    if you == com:
        print "saved!"
    else:
        print "Oo00..."
        score_com += 1
    print 'score:%d(you) - %d(com)\n' %(score_you,score_com)  


