#!/usr/bin/env python
# encoding: utf-8
"""
@author: cbr
"""


class Borg(object):
    _state = {}

    def __new__(cls, *args, **kw):
        ob = super(Borg, cls).__new__(cls, *args, **kw)
        ob.__dict__ = cls._state
        return ob


class MyClass2(Borg):
    a = 1


if __name__ == '__main__':
    a = MyClass2()
    b = MyClass2()
    print a
    print b