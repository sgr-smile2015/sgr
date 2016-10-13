#! /usr/bin/python

import pickle
data = ['save me!',12.34,True]

f = file('txt','w')
pickle.dump(data,f)
f.close

