#!/usr/bin/env python
# encoding: utf-8
"""
合并两个有序列表
@author: cbr
"""


def merge_sorted_list(l1, l2):
    tmp = []
    while len(l1) > 0 and len(l2) > 0:
        if l1[0] < l2[0]:
            tmp.append(l1.pop(0))
        else:
            tmp.append(l2.pop(0))
    tmp.extend(l1)
    tmp.extend(l2)
    return tmp


if __name__ == '__main__':
    l1 = range(1, 10, 2)
    l2 = range(2, 10, 2)
    print(merge_sorted_list(l1, l2))