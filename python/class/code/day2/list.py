#! /usr/bin/python

list1 = [1,2,3,4,5,6,13,22]
list2=[]
for i in list1:
    if i % 2 ==0:
        list2.append(i)
print list2

list3 = [i for i in list1 if i % 2 ==0]
print list3

#list4 = [i for i in range(1,21) if i%2==0 | if i%3==0 | if i%5==0]
print ';'.join([str(i) for i in range(1,102) if i%2==0 and i%3==0 and i%5==0])
#print list4

