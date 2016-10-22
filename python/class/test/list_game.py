#! /usr/bin/python

from random import choice
score = [0,0]
direction = [1,2,3]

def kick():
    print '==Round  you kick! =='
    print 'choose one'
    print '1,2,3'
    you = input()
    print 'you kicked->' + str(you)
    com = choice(direction)
    print 'computer saved_.' + str(com)
    if you != com:
        print "Good"
        score[0] += 1
    else:
        print "Oo00..."
        score[1] += 1
    print 'score:%d(you) - %d(com)\n' %(score[0],score[1])  

#    print '==Round - you saved! ==' 
#    print 'choose one'
#    print '1,2,3'
#    you = input()
#    print 'you saved->' + str(you)
#    com = choice(direction)
#    print 'computer kicked_.' + str(com)
#    if you == com:
#        print "saved!"
#    else:
#        print "Oo00..."
#        score[1] += 1
#    print 'score:%d(you) - %d(com)\n' %(score[0],score[1])  

for i in range(3):
    print '--- Round %d ---' %(i+1)
    kick()

#while(score[0] == score[1]):
#    i += 1
#    kick()

    if score[0] > score[1]:
        print 'you win!'
    else:
        print 'you lose.'


