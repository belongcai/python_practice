#!/usr/bin/env python
# encoding: utf-8
"""
@author: cbr
"""


class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance


class MyClass(Singleton):
    a = 1

    def __init__(self, kk=1):
        self.a = kk


class SubMyClass(MyClass):
    pass


if __name__ == '__main__':
    ta = MyClass(kk=1)
    tb = MyClass(kk=2)
    print ta
    print tb
    print(ta is tb)
    tc = SubMyClass()
    print tc
    print ta is tb
    print tc is ta

