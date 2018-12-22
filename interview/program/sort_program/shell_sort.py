#!/usr/bin/env python
# encoding: utf-8
"""
希尔排序
    增量采取常规的N/2,N/4 ...
@author: cbr
"""


def _insert_sort(arr, gap, i):
    """
        插入排序
    :param arr:
    :param gap: 组内元素间隔
    :param i: 待插入元素
    """
    inserted_ele = arr[i]
    j = i - gap

    while j >= 0 and arr[j] > inserted_ele:
        # 插入排序
        arr[j + gap] = arr[j]
        j -= gap

    arr[j + gap] = inserted_ele


def shell_sorted(arr):
    """

    :param arr:
    :return: sorted arr
    """
    arr_len = len(arr)
    # 增量分组 N / 2
    gap = arr_len / 2

    while gap > 0:

        i = gap
        # 组内排序
        while i < arr_len:
            _insert_sort(arr, gap, i)
            i += 1
        gap = gap / 2

    return arr


if __name__ == '__main__':
    test_lists = [
        [],
        [0],
        [0, 1],
        [-1, 0, 1, 2, 3],
        [4, 0, 3, 2, 2, 5, -1]
    ]
    for idx, t in enumerate(test_lists):
        print("test case #{}\n\tunsorted list: {}, \n\tsorted list : {}".format(idx, t, shell_sorted(t)))
