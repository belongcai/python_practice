#!/usr/bin/env python
# encoding: utf-8
"""
查找一个有序重复数组，比如，t1 = [1, 2, 2, 2, 3, 4],找出2在数组中最后的位置,要求时间复杂度为logn
@author: cbr
"""


def find_last_shown_index(l, num):
    last_shown_index = None
    if l[0] > num or num > l[-1]:
        return None

    low = 0
    high = len(l) - 1

    while low <= high:
        mid = (low + high) / 2
        guess = l[mid]

        if guess == num:
            last_shown_index = mid
            low = mid + 1
        elif guess > num:
            high = mid - 1
        else:
            low = mid + 1

    return last_shown_index


if __name__ == '__main__':
    t1 = [1, 2, 2, 2, 2, 3, 4]
    t2 = [1, 1, 1, 1]
    print(find_last_shown_index(t1, 2))
    print(find_last_shown_index(t1, 1))
    print(find_last_shown_index(t1, 5))
    print(find_last_shown_index(t2, 1))
