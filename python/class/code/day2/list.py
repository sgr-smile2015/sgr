#! /usr/bin/python

list1 = [1,2,3,4,5,6,13,22]
list2=[]
for i in list1:
    if i % 2 ==0:
        list2.append(i)
print list2

list3 = [i for i in list1 if i % 2 ==0]
print list3

