#!/usr/bin/env python
# encoding: utf-8
"""
输入递增的旋转数组，
1,2,3,4,5 -> 3,4,5,1,2
考虑以下测试用例
1. 移动0个元素
2. 基准值与首尾相等，无法判断属于前面递增的数组还是后面递增的数组
@author: cbr
"""


def min_in_arr(s):
    res = s[0]

    for i in range(1, len(s) - 1):
        if s[i] < res:
            res = s[i]

    return res


def find_smallest(spin_str):
    if len(spin_str) <= 0:
        return None

    i, j = 0, len(spin_str) - 1
    t = i

    while spin_str[i] >= spin_str[j]:
        if j - i == 1:
            t = j
            break
        mid = (i + j) / 2
        if spin_str[mid] == spin_str[i] == spin_str[j]:
            return min_in_arr(spin_str)
        if spin_str[mid] >= spin_str[i]:
            i = mid  # 移动后指针仍属于原本分组
        else:
            j = mid
    return spin_str[t]


if __name__ == '__main__':
    t1 = [3, 4, 5, 1, 2]
    t2 = [1, 2, 3]
    t3 = [1, 1, 1, 0, 1]
    print(find_smallest(t1))
    print(find_smallest(t2))
    print(find_smallest(t3))
