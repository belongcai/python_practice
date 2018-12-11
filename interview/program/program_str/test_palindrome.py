#!/usr/bin/env python
# encoding: utf-8
"""
检测一个字符串是否为回文字符串
@author: cbr
"""


def is_palindrome_str(s1):
    if not isinstance(s1, str) or len(s1) < 1:
        return False

    s = list(s1)
    begin = 0
    end = len(s) - 1

    while begin < end:
        if s[begin] != s[end]:
            return False
        begin += 1
        end -= 1
    return True


if __name__ == '__main__':
    t1 = "aba"
    t2 = "abba"
    t3 = "bc"
    for t in t1, t2, t3:
        print(is_palindrome_str(t))