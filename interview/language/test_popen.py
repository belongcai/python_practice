#!/usr/bin/env python
# encoding: utf-8
"""
@author: cbr
"""
from os import popen


if __name__ == '__main__':
    f = popen("calc", "w")
    print >>f, "abc"
    f.flush()
    f.close()