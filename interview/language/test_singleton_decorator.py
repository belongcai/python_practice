#!/usr/bin/env python
# encoding: utf-8
"""
@author: cbr
"""

from functools import wraps


def singleton(cls):
    instances = {}

    @wraps(cls)
    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return getinstance


@singleton
class MyClass(object):
    a = 1


if __name__ == '__main__':
    ta = MyClass()
    tb = MyClass()
    print ta
    print tb
    print(ta is tb)

