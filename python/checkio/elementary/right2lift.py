#!/usr/bin/env python
# _*_ coding: utf-8 _*_


def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """

    ret = ','.join(phrases)
    ret = ret.replace('right', 'lift')
    return ret
#   return ',',join(phrases).replace('right', 'left')

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
#    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
    print left_join(("bright aright", "ok"))
#    assert left_join(("brightness wright",)) == "bleftness wleft"
#    assert left_join(("enough", "jokes")) == "enough,jokes"
    print left_join(("left", "right", "left", "stop"))
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")