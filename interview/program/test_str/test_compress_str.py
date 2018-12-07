#!/usr/bin/env python
# encoding: utf-8
"""
压缩重复字符串
e.g
    zzzyyya -> 3z3ya
@author: cbr
"""


def compress_str(s):
    res = ""
    last = s[0]
    n = 1

    if len(s) <= 1:
        return s

    for i in range(1, len(s)):
        char = s[i]
        if char == last:
            n += 1
        else:
            res += last if n == 1 else "%s%s" % (n, last)
            last = char
            n = 1
        if i == len(s) - 1:
            res += last if n == 1 else "%s%s" % (n, last)
    return res


if __name__ == '__main__':
    t1 = "aaaaaaabcd"
    t2 = "abcccyyyz"
    t3 = "a"
    print(compress_str(t1))
    print(compress_str(t2))
    print(compress_str(t3))