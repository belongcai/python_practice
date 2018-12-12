#!/usr/bin/env python
# encoding: utf-8
"""
封装了读取文件的接口
@author: cbr
"""


def blocks(descriptor):
    # 成块输出，块的临界值为空行
    block = []
    for line in descriptor:
        if line.strip():
            block.append(line.strip())
        elif block:
            yield "".join(block).strip()
            block = []