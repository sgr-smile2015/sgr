#! /usr/bin/python

import os
from random import randint

infolist = [
'\'testing file to scripts\'',
'\'change bug to python src\'',
'\'use new object\'',
'\'rm file to debug system\'']

word = infolist[randint(0,3)]
cmd = 'git commit -m ' + word # % infolist[randint(0,3)] 
print cmd
#file = os.system(cmd) 
#print file

os.system('touch testfile')
os.system('git add testfile')
ll = os.system(cmd)
print ll
