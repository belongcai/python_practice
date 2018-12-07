#!/usr/bin/env python
# encoding: utf-8
"""
@author: cbr
"""


li = [x for x in range(10)]
li2 = [lambda:x for x in range(10)]


if __name__ == '__main__':
    print(li)
    print li2[0]()