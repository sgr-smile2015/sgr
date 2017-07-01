#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright © Sgr
# CreateTime: 2017-07-01 11:56:39


from threading import Thread
import time

def counter():
    i = 0
    for x in range(100000000):
        i = i + 1
    return True

def main():
    thread_array = {}
    start = time.time()

    for tid in range(2):
        t = Thread(target=counter)
        t.start()
        t.join()
    end = time.time()
    print "Totail time: %s sec" % (end - start)

if __name__ == '__main__':
    main()
