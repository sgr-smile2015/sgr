#!/usr/bin/env python
# _*_ coding: utf-8 _*_


def checkio(numbers_array):
#    return sorted(numbers_array, key=lambda x: abs(numbers_array[3]))
    return sorted(numbers_array, key=abs)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def check_it(array):
        if not isinstance(array, (list, tuple)):
            raise TypeError("The result should be a list or tuple.")
        return list(array)

#    assert check_it(checkio((-20, -5, 10, 15))) == [-5, 10, 15, -20]
    print check_it(checkio((1, 2, 3, 0))) == [0, 1, 2, 3]
    print check_it(checkio((-1, -2, -3, 0))) == [0, -1, -2, -3]
    print check_it(checkio((-20, -5, 10, 15)))
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")