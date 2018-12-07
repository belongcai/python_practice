#!/usr/bin/env python
# encoding: utf-8
"""
实现快速排序的partition函数
@author: cbr
"""


def partition(s, start, end):
    # 返回 index of pivot
    p, r = start, end
    i = p - 1
    x = s[r]

    for j in range(r):
        if s[j] <= x:
            i += 1
            s[i], s[j] = s[j], s[i]
    s[i+1], s[r] = s[r], s[i+1]
    return i + 1


if __name__ == '__main__':
    t = [1, 5, 2, 6, 10, 3]
    print(partition(t, 0, len(t) - 1))
    print(t)