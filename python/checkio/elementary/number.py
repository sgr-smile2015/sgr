#!/usr/bin/env python
# _*_ coding: utf-8 _*_

def checkio(str_number, radix):
    try:
        return int(str_number, radix)
    except ValueError:
        return -1

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print checkio("AF", 16)
    print checkio("102", 2) == 5
    #assert checkio("101", 5) == 26, "5 base"
    #assert checkio("Z", 36) == 35, "Z base"
    #assert checkio("AB", 10) == -1, "B > A = 10"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")