#!/usr/bin/env python
# encoding: utf-8
"""
给定字符串的全排列
@author: cbr
"""


def permutation(s, f, t):
    if t <= 1:
        return
    if f == t:
        print(s)
    else:
        for j in range(f, t+1):
            s[j], s[f] = s[f], s[j]
            permutation(s, f+1, t)
            s[j], s[f] = s[f], s[j]


def is_swap(s, f, j):
    if s[j] in s[f:j]:
        return False
    return True


def permutation_mature(s, f, t):
    """去除重复排列"""
    if t < 1:
        return
    if f == t:
        print(s)
    else:
        for j in range(f, t+1):
            if is_swap(s, f, j):
                s[j], s[f] = s[f], s[j]
                permutation_mature(s, f+1, t)
                s[j], s[f] = s[f], s[j]


if __name__ == '__main__':
    # ts = list("abcde")
    # permutation(ts, 0, len(ts) - 1)
    ts2 = list("abbd")
    # permutation(ts2, 0, len(ts2) - 1)
    permutation_mature(ts2, 0, len(ts2) - 1)