#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import re

def checkio(data):
    rt = 0
    if len(data) < 10:
        return False
    if re.search('[a-z]+', data) is not None:
        rt += 1
    if re.search('[A-Z]+', data) is not None:
        rt += 1
    if re.search('[0-9]+', data) is not None:
        rt += 1

    if rt is 3:
        return True
    else:
        return False

# return re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{10,}$", data) != None

if __name__ == '__main__':
#    assert checkio('A1213pokl') == False
#    assert checkio('bAse730onE4') == True
#    assert checkio('asasasasasasasaas') == False
#    assert checkio('QWERTYqwerty') == False
#    assert checkio('123456123456') == False
#    assert checkio('QwErTy911poqqqq') == True

    print checkio('A1213pokl') # False
    print checkio('bAse730onE4') # True
    print checkio('asasasasasasasaas') # False
    print checkio('QWERTYqwerty') # False
    print checkio('123456123456') # False
    print checkio('QwErTy911poqqqq') # True
