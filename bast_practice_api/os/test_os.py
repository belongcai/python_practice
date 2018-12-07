#!/usr/bin/env python
# encoding: utf-8
"""
@author: cbr
"""
from os import walk


if __name__ == '__main__':
    top = r"F:\DEV\test_obj"
    for root, dirs, names in walk(top, topdown=False):
        print root, dirs, names