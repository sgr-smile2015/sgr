#!/usr/bin/env python
# _*_ coding: utf-8 _*_

def find_message(text):
    """Find a secret message"""
#    size_str = len(text)
#    ret = ''
#    l = []
#    for i in range(size_str):
#        if text[i].isupper():
#            #print text[i]
#            l.append(text[i])
#    return ret.join(l)

    ret = ''
    for i in text:
        if i.isupper():
            ret += i
    return ret

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
#    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
#    assert find_message("hello world!") == "", "Nothing"
#    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
    print find_message("How are you? Eh, ok. Low or Lower? Ohhh.")
    print find_message("hello world!")
    print find_message("HELLO WORLD!!!")
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
