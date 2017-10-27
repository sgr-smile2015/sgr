#!/usr/bin/env python
# _*_ coding: utf-8 _*_


def most_frequent(data):
    """
        determines the most frequently occurring string in the sequence.
    """

#    dic = dict((i, data.count(i)) for i in set(data))
#    num = max(dic.values())
#    for key, value in dic.items():
#        if value is num:
#            return key
    return max(data, key=data.count)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ])

    print most_frequent(['a', 'a', 'bi', 'bi', 'bi'])
    print('Done')