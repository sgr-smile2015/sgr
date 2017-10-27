#!/usr/bin/env python
# _*_ coding: utf-8 _*_


def easy_unpack(elements):
    """
        returns a tuple with 3 elements - first, third and second to the last
    """
#    ret = []
#    temp = [tuple(elements[x: x + 3]) for x in range(0, len(elements), 3)]
#    ret.append(temp[0][0])
#    ret.append(temp[0][2])
#    for i in range(len(temp)):
#        if len(temp[i]) % 3 is not 0:
#            ret.append(temp[i][0])
#    if len(elements) % 3 is 0:
#        ret.append(temp[0][1])
#    return ret
    return tuple(elements[i] for i in (0, 2, -2))
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print easy_unpack((1, 2, 3, 4, 5, 6, 7, 9))
    print easy_unpack((1, 1, 1, 1))
    print easy_unpack((6, 3, 7))
    print easy_unpack((5, 5, 5, 5, 5, 5))
    print('Done! Go Check!')
