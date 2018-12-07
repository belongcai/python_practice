#!/usr/bin/env python
# encoding: utf-8
"""\
丑数,只包含 2,3,5的因子
@author: cbr
"""


#  蛮力
def is_ugly_num(num):
    while num % 2 == 0:
        num = num / 2

    while num % 3 == 0:
        num = num / 3

    while num % 5 == 0:
        num = num / 5

    return num == 1


def get_ugly_number(index):
    # 获取第几个丑数
    if index <= 0:
        raise ValueError
    ugly_found = 0
    num = 0

    while ugly_found < index:
        num += 1

        if is_ugly_num(num):
            ugly_found += 1

    return num


#  规律法， 使用辅助的数组作为丑数的推导容器
def get_ugly_num_solution2(index):
    if index <= 0:
        raise ValueError
    ugly_num = [0] * int(index)
    ugly_num[0] = 1

    pos_factor_2, pos_factor_3, pos_factor_5 = 0, 0, 0
    next_index = 1

    while next_index < index:
        num = min(ugly_num[pos_factor_2] * 2, ugly_num[pos_factor_3] * 3, ugly_num[pos_factor_5] * 5)
        ugly_num[next_index] = num

        # factor_pos update
        while ugly_num[pos_factor_2] * 2 <= num:
            pos_factor_2 += 1
        while ugly_num[pos_factor_3] * 3 <= num:
            pos_factor_3 += 1
        while ugly_num[pos_factor_5] * 5 <= num:
            pos_factor_5 += 1

        next_index += 1

    return ugly_num[index - 1]


if __name__ == '__main__':
    # print(get_ugly_num_solution2(0))
    print(get_ugly_number(10))
    print(get_ugly_num_solution2(10))