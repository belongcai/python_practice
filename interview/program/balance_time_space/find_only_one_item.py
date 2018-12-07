#!/usr/bin/env python
# encoding: utf-8
"""
寻找字符串中最早出现一次的字符
solution1:
    遍历，o(n2)
solution2:
    hash
    o(n)
@author: cbr
"""


def find_first_only_one(input_str):
    if len(input_str) <= 0 or not isinstance(input_str, str):
        raise ValueError

    # iter 2 times
    char_hash = dict()
    for i in input_str:
        if i not in char_hash:
            char_hash[i] = 1
        else:
            char_hash[i] += 1

    for i in input_str:
        if char_hash[i] == 1:
            return i

    return None


if __name__ == '__main__':
    data1 = "abcbcbc"
    data2 = "aabcbcbc"
    data3 = "bcbcdbc"
    for d in data1, data2, data3:
        print(find_first_only_one(d))