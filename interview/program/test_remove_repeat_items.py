#!/usr/bin/env python
# encoding: utf-8
"""
@author: cbr
"""


def remove_rep_items(l):
    return list(set(l))


def remove_rep_2(l):
    return dict.fromkeys(l).keys()


if __name__ == '__main__':
    l1 = ['b', 'c', 'd', 'b', 'c', 'a', 'a']
    l2 = list(set(l1))
    l2.sort()
    print l2