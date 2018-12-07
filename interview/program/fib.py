#!/usr/bin/env python
# encoding: utf-8
"""
@author: cbr
"""


def fib(n):
    a, b = 1, 1
    while n > 0:
        print a,
        a, b = b, a + b
        n -= 1


def fib_recursive(n, a=1, b=1):
    print a,
    if n > 1:
        fib_recursive(n-1, a=b, b=a + b)


if __name__ == '__main__':
    fib(3)
    # print "\n"
    # fib_recursive(10)