#!/usr/bin/env python
# _*_ coding: utf-8 _*_


def count_words(text, words):
    count = 0
    for word in words:
        if word in text.lower():
            count += 1
    return count


if __name__ == '__main__':
    print count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"})
    print count_words("Bananas, give me bananas!!!", {"banana", "bananas"})
    print count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"})
