#!/use/bin/env python
# -*- conding:utf-8 -*-

import string
import random

def active_code(id,length=10):
    head = hex(int(id))[2:] + '@'
    #print head
    length = length - len(head)
    chars = string.ascii_letters + string.digits
    #print chars
    return head + ''.join(random.choice(chars) for i in range(length))
    
def get_id(hex_id):
    return str(int(hex_id.upper(),base=16))

if __name__=="__main__":
    for i in range(10,200,4):
        code = active_code(i)
        hex_id = code.split('@')[0]
        id = get_id(hex_id)
        print code,id

