#!/usr/bin/env python
# encoding: utf-8
"""
在数组中寻找最小的K个数
@author: cbr
"""
from interview.program.sort.partition import partition


def find_k_small_num(s, k):
    p, r = 0, len(s) - 1
    index = partition(s, p, r)

    while index != k - 1:
        pass
