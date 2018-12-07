#!/usr/bin/env python
# encoding: utf-8
"""
二维向量
vector(1,2)
具有方法
v1 + v2
v1 * 3
abs(v1)
@author: cbr
"""


class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vector(%r, %r)" % (self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, num):
        x = self.x * num
        y = self.y * num
        return Vector(x, y)


if __name__ == '__main__':
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    print(v1, v2, v1 + v2)