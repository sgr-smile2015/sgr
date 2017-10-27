#!/usr/bin/env python
# _*_ coding: utf-8 _*_


def checkio(words):
    count = 0
    for word in words.split():
        if word.isalpha():
            count += 1
            if count is 3:
                return True
        else:
            count = 0
    else:
        return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    #assert checkio("Hello World hello") == True
    print checkio("He is 123 man")
    #assert checkio("1 2 3 4") == False
    #assert checkio("bla bla bla bla") == True
    #assert checkio("Hi") == False
    print checkio("Hello World hello")
    print checkio("one two 3 four five six 7 eight 9 ten eleven 12")

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")