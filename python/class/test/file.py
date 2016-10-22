#! /usr/bin/python

f = file('int.py')
data =f.read()
print data
#data1 =f.readlines()
#print data1
f.close()

string = 'i am begin write to file ^_^\n'
out = open('out.txt', 'w')
out.write(data)
out.close()


