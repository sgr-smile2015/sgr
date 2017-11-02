#!/usr/bin/env python
# _*_ coding: utf-8 _*_


def checkio(result):
    rows = result
    cols = map(''.join, zip(*rows))
    diags = map(''.join, zip(*[(r[i], r[2-i]) for i, r in enumerate(rows)]))
    lines = rows + list(cols) + list(diags)
    print lines

    return 'X' if ('XXX' in lines) else 'O' if ('OOO' in lines) else 'D'

if __name__ == '__main__':
    print checkio([
        "X.O",
        "XX.",
        "XOO"]) # "X"
    print checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O"
    print checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D"
    print checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X"
    #print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
