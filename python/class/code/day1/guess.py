#! /usr/bin/python

from random import randint 
num = randint(1,10)

f = open('game.txt')
score = f.read().split()

game_time = int(score[0])
min_time = int(score[1])
total_time = int(score[2])

if game_time > 0:
    avg_time = float (total_time) / game_time
else:
    avg_time = 0

#print 'play time %d s, min time %d s, avg time %0.2f s' % (game_time,min_time,total_time)
print 'play time %d s, min time %d s, avg time %0.2f s' \
% (game_time,min_time,total_time) 


times = 0
print 'guess number ?'

bingo = False
while bingo == False:
    times += 1
    answer = input()

    if answer < num:
        print 'too small'
    if answer > num:
        print 'too big'
    if answer == num:
        print 'bingo'
        bingo = True

if game_time == 0 or times < min_time:
    min_time = times

total_time += times
game_time += 1
result = '%d %d %d' %(game_time,min_time,total_time)
f = open('game.txt','w')
f.write(result)
f.close()
