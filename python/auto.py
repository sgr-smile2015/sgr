#! /usr/bin/python

import os
import time
from random import randint

infolist = [
'\'testing file to scripts\'',
'\'change bug to python src\'',
'\'use new object\'',
'\'rm file to debug system\'']

word = infolist[randint(0,3)]
cmd = 'git commit -m ' + word # % infolist[randint(0,3)] 
#print cmd

os.system('touch testfile')
os.system('git add testfile')
os.system(cmd)
os.system('git push')

time.sleep(5)

print 'time is coming'

os.system('git rm testfile')
os.system(cmd)

