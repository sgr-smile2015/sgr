#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


def checkio(text):
    data = list(filter(str.isalpha, text.lower()))
    #dic = dict((i, data.count(i)) for i in set(data))
    dic = dict((i, data.count(i)) for i in set(data))
    temp = max(dic.values())
    print temp

    big = []
    for key, value in dic.items():
        #print key, value
        if temp == 1:
            ret = min(dic.keys())
        elif value == temp:
            big.append(key)
#            ret = min(big)

    if len(big) == 1:
        ret = max(data, key=data.count)
    else:
        ret = min(big)
    return ret

#    text = text.lower()  # set all text to lower case
#    # Create a dictionary with keys as the letters in the string if they are alpha
#    # Set the valuse to the count of the letter in the text
#    data = {letter: text.count(letter) for letter in text if letter.isalpha()}
#    max_value = max(data.values())  # find the value in the dictionary
#    # make a list of the keys whos value is equal to the max
#    keys = [k for k, v in data.items() if v == max_value]
#    keys.sort()
#    return keys[0]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
#    assert checkio("Hello World!") == "l", "Hello test"
#    assert checkio("How do you do?") == "o", "O is most wanted"
#    assert checkio("One") == "e", "All letter only once."
#    assert checkio("Oops!") == "o", "Don't forget about lower case."
#    assert checkio("AAaooo!!!!") == "a", "Only letters."
#    assert checkio("abe") == "a", "The First."
#    print("Start the long test")
#    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
#    print checkio("a" * 9000 + "b" * 1000)
#    print checkio("Hello World!")
#    print checkio("m m M moo o O!!!!")
    print checkio("Lorem ipsum dolor sit amet!!!")
#    print("The local tests are done.")
