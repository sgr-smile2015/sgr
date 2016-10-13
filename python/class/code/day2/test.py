#! /usr/bin/python

import pickle

f = file('txt')
test = pickle.load(f)
f.close

print test

