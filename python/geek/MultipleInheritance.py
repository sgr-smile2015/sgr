#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © Sgr
# CreateTime: 2017-08-14 16:52:55

class Init(object):
    def __init__(self, value):
        print "Init"
        self.val = value


class Add2(Init):
    def __init__(self, val):
        super(Add2, self).__init__(val)
        print "add2"
        self.val += 2


class Mul5(Init):
    def __init__(self, val):
        super(Mul5, self).__init__(val)
        print "mul5"
        self.val *= 5

class CCC(Init):
    def __init__(self, val):
        super(CCC, self).__init__(val)
        print "ccc"
        self.val += 4


class Pro(Mul5, Add2, CCC):
    pass


class Incr(Pro):
    csup = super(Pro)
    def __init__(self, val):
        self.csup.__init__(val)
        self.val += 1


p = Incr(4)
print(p.val)
