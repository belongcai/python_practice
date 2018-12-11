#!/usr/bin/env python
# encoding: utf-8
"""
@author: cbr
"""


def is_all_char_included(l1, l2):
    l1 = sorted(l1)
    l2 = sorted(l2)

    a = 0
    for b in range(0, len(l2)):
        while (a < len(l1)) and l1[a] < l2[b]:  # 注意这两个表达式的顺序
            a += 1
        if a >= len(l1) or l1[a] > l2[b]:
            return False
    return True


def is_all_char_included_solution2(s1, s2):
    # force search
    for b in range(0, len(s2)):
        is_char_find = False
        for a in range(0, len(s1)):
            if s2[b] == s1[a]:
                is_char_find = True
                break
        if not is_char_find:
            return False
    return True


if __name__ == '__main__':
    test_1 = "abcd"
    test_2 = "aaae"
    print(is_all_char_included(test_1, test_2))
    print(is_all_char_included_solution2(test_1, test_2))