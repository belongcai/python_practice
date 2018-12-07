#!/usr/bin/env python
# encoding: utf-8
"""
@author: cbr
"""


r"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法
"""


def flog_bt(n):
    if n < 2:
        return n
    return 2 * flog_bt(n-1)


def flog_jump(n):
    a, b = 1, 1
    while n > 1:
        # print a,
        a, b = b, a + b
        n -= 1
    print a


if __name__ == '__main__':
    # print flog_bt(4)
    flog_jump(2)
