#!/usr/bin/env python
# encoding: utf-8
"""
@author: cbr
"""


class Solution(object):

    @staticmethod
    def get_value(l, r, c):
        return l[r][c]

    @classmethod
    def search_matrix(cls, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) < 1 or len(matrix[0]) < 1:
            return False
        m = len(matrix) - 1
        n = len(matrix[0]) - 1
        r = 0
        c = n

        while r <= m and c >= 0:
            if cls.get_value(matrix, r, c) == target:
                return True
            elif cls.get_value(matrix, r, c) < target:
                r += 1
            else:
                c -= 1
        return False

    @classmethod
    def search_matrix_2(cls, matrix, target):
        # 取左下角
        if len(matrix) < 1 or len(matrix[0]) < 1:
            return False
        m = len(matrix) - 1
        n = len(matrix[0]) - 1
        r = m
        c = 0

        while r >= 0 and c <= n:
            if cls.get_value(matrix, r, c) == target:
                return True
            elif cls.get_value(matrix, r, c) < target:
                c += 1
            else:
                r -= 1
        return False


if __name__ == '__main__':
    t_m = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    t = 3
    print(Solution.search_matrix(t_m, t))
    print(Solution.search_matrix_2(t_m, t))
