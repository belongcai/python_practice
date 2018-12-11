#!/usr/bin/env python
# encoding: utf-8
"""
用函数实现一个判断用户输入的年份是否是闰年的程序

normal leap: % 4 == 0 and % 100 != 0
decade leap: % 400 ==0
@author: cbr
"""


def judge_leap_year(year):
    # no consider input type
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False


if __name__ == '__main__':
    # 这里需要处理其他不符合正整数的数据
    input_year = int(raw_input("which year do you want to judge?"))
    print("your input year: %s, is lear year?(True,False) %s" % (input_year, judge_leap_year(input_year)))
