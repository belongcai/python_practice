#!/usr/bin/env python
# encoding: utf-8
"""
规则处理器，如何对文本做跟细致的处理
这里简单设计了
    condition:
    action
    满足condition,则执行action
    action的行为有模块handler负责

存在问题：
    TODO： 当前规则处理方式过于简单，处理文本中，嵌套等较为复杂的情况，会乱套。
@author: cbr
"""


class Rule(object):
    type = "paragraph"  # 默认是段落

    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block)
        handler.start(self.type)

    @classmethod
    def condition(cls, block):
        return True


class ParagraphRule(Rule):
    pass
