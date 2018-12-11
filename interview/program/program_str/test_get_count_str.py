#!/usr/bin/env python
# encoding: utf-8
"""

统计输入字符串包含制定字符串的方式
题目：在一个字符串中查找子字符串的个数。
要求：两个字符串之间以空格隔开，前一个为字符串，后一个为要查找的子字符串。结果输出字符串中包含的子字符串的个数。
例如：输入：abcdssdfabc abc
输出：2
先把测试用例写出来：
1：输入：abdsdjkflsdjkabdsdjk abd 输出：2
2：输入：a abc 输出：0
3：输入：&%jskdl&%sdfjkl *&% 输出：2
---------------------
@author: cbr
"""


s1 = "%abc%"


def get_count2(s):
    if not (isinstance(s, str) or isinstance(s, unicode)):
        raise TypeError("s must be a string")
    return len(s.split(s1)) - 1


def get_count_2(m_str, s_str):
    """使用c方法实现"""
    m_len, s_len = len(m_str), len(s_str)
    if m_len <= 0 or s_len <= 0 or m_len < s_len:
        return False

    i, j = 0, 0
    count = 0

    while i <= m_len - s_len:
        flag = 1
        for j in range(0, s_len):
            if m_str[i + j] == s_str[j]:
                flag = 1
            else:
                flag = 0
                break
        if flag == 1:
            count += 1
        i += 1

    return count


def get_count_3(m_str, s_str):
    """使用python 切片比较"""


if __name__ == '__main__':
    test_str = "%abc%defg"
    test_str2 = "123"
    test_str3 = "abc"
    test_str4 = "%abc%"
    sub = "abc"
    print(get_count_2(test_str2, sub))
