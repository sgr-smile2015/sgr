#!/usr/bin/env python
# _*_ coding: utf-8 _*_


class Foo(object):

    def __init__(self, title):
        self.title = title

    @classmethod
    def class_mod(cls, title):
        book = cls(title=title)
        return book

book1 = Foo('python')
book2 = Foo.class_mod("I'm django")

print(book1.title)
print(book2.title)


class Father(object):

    x = 1
    y = 2

    @staticmethod
    def avg(*mixs):
        return sum(mixs) * 1.0 / len(mixs)

    @staticmethod
    def static_mod():
        return Father.avg(Father.x, Father.y)

    @classmethod
    def class_mod(cls):
        print cls
        return cls.avg(cls.x, cls.y)


class Son(Father):
    x = 3
    y = 5

    @staticmethod
    def avg(*mixs):
        return sum(mixs) / 3.0

p = Son()

print(p.static_mod())
print(p.class_mod())


def list_mod(*args):
    for ar in args:
        print ar


arg = ['hello', 'the', 'world']
arg0 = [3]

list_mod(arg, arg0)

