#!/usr/bin/env python
# _*_ coding: utf-8 _*_


def checkio(data):

#    ret = []
#    data_set = set(data)
#    print data_set
#    for i in data:
#        if data.count(i) > 1:
#            ret.append(i)
#    return ret

    #for item in data:
    #why return [2, 4] ???

    for item in data[:]:
        print item
        if data.count(item) is 1:
            data.remove(item)
    return data


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
#    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3]
#    assert list(checkio([1, 2, 3, 4, 5])) == []
#    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5]
#    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9]
    #print list(checkio([1, 2, 3, 1, 3]))
    print list(checkio([1, 2, 3, 4, 5]))
    #print list(checkio([5, 5, 5, 5, 5]))
    #print list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9]
