#!/usr/bin/env python
# encoding: utf-8
"""
特殊方法研究
poker card

-
迭代器环境会先尝试__iter__方法，在尝试__getitem__.也就是如果对象不支持迭代协议，就会尝试索引运算

迭代环境是通过调用内置函数iter去尝试__iter__方法来实现的，这种方法返回一个迭代器对象，如果提供Python就会重复调用这个迭代器对象的next方法，知道发生StopIteration异常，如果没找到这类__iter__方法，Python就会改用__getitem__机制，通过偏移量重复索引，直至发生IndexError异常
---------------------
作者：aaronlyt
来源：CSDN
原文：https://blog.csdn.net/u012829152/article/details/41911497
版权声明：本文为博主原创文章，转载请附上博文链接！

@author: cbr
"""
from collections import namedtuple


card = namedtuple('Card', ('rank', 'suit'))


class PokerCard(object):
    ranks = [str(x) for x in range(2, 11)] + ['j', 'q', 'k', 'a']
    suits = ['spade', 'heart', 'diamond', 'club']

    def __init__(self):
        self.cards = [card(r, s) for r in self.ranks for s in self.suits]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, item):
        return self.cards[item]


if __name__ == '__main__':
    p = PokerCard()
    print(len(p))
    print(p[0])
    for i in p:
        print(i)