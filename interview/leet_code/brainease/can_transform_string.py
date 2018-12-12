#!/usr/bin/env python
# encoding: utf-8
"""
在一个由 'L' , 'R' 和 'X' 三个字符组成的字符串（例如"RXXLRXRXL"）中进行移动操作。
一次移动操作指用一个"LX"替换一个"XL"，或者用一个"XR"替换一个"RX"。
现给定起始字符串start和结束字符串end，请编写代码，当且仅当存在一系列移动操作使得start可以转换成end时， 返回True。

1 <= len(start) = len(end) <= 10000。
start和end中的字符串仅限于'L', 'R'和'X'。

输入: start = "RXXLRXRXL", end = "XRLXXRRLX"
输出: True
解释:
我们可以通过以下几步将start转换成end:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX


分析：
    输入的字符串去除X后，顺序和长度是相等的；意味着在遍历到非X字符时候，start,end字符是相等的
    同时，题目涉及到移动顺序，start_str的字符串中 L只能往前移动， R只能往后移动

@author: cbr
"""


def can_transform_string(start, end):
    # 输入的字符串去除X后，顺序和长度是相等的
    if len(start) != len(end) and len(start) > 1000 or len(start) <= 0:
        return False
    end_index = len(start) - 1
    i, j = 0, 0

    while i <= end_index and j < end_index:
        # 找到第一个出现非X的元素，并比较该元素
        # 并且要注意循环可能导致的越界
        while start[i] == "X":
            if i != end_index:
                i += 1
            else:
                break

        while end[j] == "X":
            if j != end_index:
                j += 1
            else:
                break

        # 据题目意思，start_str的字符串中 L只能往前移动， R只能往后移动
        # 并且每次出现非X的字符都是相等的，一开始就过滤掉顺序不相等的字符串
        if start[i] != end[j]:
            return False

        if start[i] == "L" and i < j:
            return False

        if start[i] == "R" and i > j:
            return False

        # 继续往后走
        i += 1
        j += 1

    return True


def can_transform_string_2(start, end):
    i, j = 0, 0
    n = len(start)

    if len(start) != len(end) or n < 1:
        return False

    while i < n and j < n:

        # 找到第一个非X字符，
        while i < n - 1 and start[i] == "X":
            i += 1

        while j < n - 1 and end[j] == "X":
            j += 1

        if start[i] != end[j]:
            return False

        if start[i] == "L" and i < j:
            return False

        if start[i] == "R" and i > j:
            return False

        i += 1
        j += 1

    return True


if __name__ == '__main__':
    """
    测试用例
        无效
        "", ""
        XXLR, LLL
        
        False
        L, R
        XLXXRX, XXXRLX
        
        True
        XXXX, XXXX  这个不包含L，R的情况
        RXXLRXRXL， XRLXXRRLX
        "XXXLXXXXXX", "XXXLXXXXXX"
        "XXXXXLXXXX" "LXXXXXXXXX"
    """
    t_start_str = "XXXXXLXXXX"
    t_end_str = "LXXXXXXXXX"
    print(can_transform_string_2(t_start_str, t_end_str))