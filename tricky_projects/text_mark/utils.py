#!/usr/bin/env python
# encoding: utf-8
"""
封装了读取文件的接口
@author: cbr
"""


def lines(f):
    for line in f:
        yield line

    yield '\n'  # 文本最后一块输出


def blocks(descriptor):
    # 成块输出，块的临界值为空行
    block = []
    for line in lines(descriptor):
        if line.strip():
            block.append(line.strip())
        elif block:
            yield "".join(block).strip()
            block = []