#!/usr/bin/env python
# _*_ coding: utf-8 _*_


def min(*args, **kwargs):
    key = kwargs.get("key", None)
    return None


def max1(*args, **kwargs):
    key = kwargs.get("key", None)
    t = max(3, 2)
    print t
    return 1


if __name__ == '__main__':
    print max1(3, 2)
#    assert min(3, 2) == 2
#    assert max([1, 2, 0, 3, 4]) == 4
#    assert min("hello") == "e"
#    assert max(2.2, 5.6, 5.9, key=int) == 5.6
#    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0]
#    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")