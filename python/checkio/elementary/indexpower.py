#!/usr/bin/env python
# _*_ coding: utf-8 _*_


def index_power(array, n):
    """
        Find Nth power of the element with index N.
    """
    if len(array) >= n+1:
        return array[n]**n
    else:
        return -1


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
#    assert index_power([1, 2, 3, 4], 2) == 9
#    assert index_power([1, 3, 10, 100], 3) == 1000000
#    assert index_power([0, 1], 0) == 1
#    assert index_power([1, 2], 3) == -1
    print index_power([1, 2, 3, 4], 2)
    print index_power([1, 3, 10, 100], 3) == 1000000
    print index_power([0, 1], 0) == 1
    print index_power([1, 2], 3) == -1

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")