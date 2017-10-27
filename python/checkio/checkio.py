#!/usr/bin/env python
# _*_ coding: utf-8 _*_

def checkio(number):
    # Your code here
    # It's main function. Don't remove this function
    # It's using for auto-testing and must return a result for check.

    if number % 15 is 0:
        number = 'Fizz Buzz'
    elif number % 3 is 0:
        number = 'Fizz'
    elif number % 5 is 0:
        number = 'Buzz'
    else:
        number = 7

    return str(number)


# Some hints:
# Convert a number in the string with str(n)

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
    print checkio(15)
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")