#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright © Sgr
# CreateTime: 2017-05-19 11:14:39


import sys
import os

if len(sys.argv) <4:
    print 'useage: python replice.py old new filename'

old, new = sys.argv[1], sys.argv[2]
file_name = sys.argv[3]

with open('passwd', 'r') as f:
    new_file = open('.%s.bak' % file_name, 'w+')

    for line in f.xreadlines():
        new_file.write(line.replace(old, new))
    f.close()
    new_file.close()

if '--bak' in sys.argv:
    os.rename(file_name, '%s.bak' % file_name)
    os.rename('.%s.bak' % file_name, '%s' % file_name)

else:
    None

