#!/usr/bin/env python
# _*_ coding: utf-8 _*_


def checkio(number):

    ret = 1
    for i in str(number):
        if not int(i):
            continue
        else:
            ret *= int(i)
    return ret

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")