#!/usr/bin/env python
# encoding: utf-8
"""
@author: cbr
"""
name = "lzl"


def f1():
    print(name)


def f2():
    name = "eric"
    f1()


if __name__ == '__main__':
    f2()