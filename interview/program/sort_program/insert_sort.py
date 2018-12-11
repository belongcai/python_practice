#!/usr/bin/env python
# encoding: utf-8
"""
@author: cbr
"""


def insert_sort(s):
    for i in range(1, len(s)):
        tmp = s[i]
        j = i-1
        while j >= 0 and s[j] > tmp:
            s[j+1] = s[j]
            j -= 1
        s[j+1] = tmp


if __name__ == '__main__':
    t1 = range(10)
    print(t1)
    insert_sort(t1)
    print(t1)
