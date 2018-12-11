#!/usr/bin/env python
# encoding: utf-8
"""
@author: cbr
"""


def is_char_include(src_str, test_str):
    """s1,s2 are upper char"""
    # bit union opr
    tmp = 0

    for i in src_str:
        n = ord(i) - ord('A')
        tmp |= 1 << n

    for j in test_str:
        n = ord(j) - ord('A')
        if (tmp & 1 << n) == 0:
            return False
    return True


if __name__ == '__main__':
    s1 = "ABC"
    s2 = "AD"
    print(is_char_include(s1, s2))