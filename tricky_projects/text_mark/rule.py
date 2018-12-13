#!/usr/bin/env python
# encoding: utf-8
"""
规则处理器，如何对文本做跟细致的处理
这里简单设计了
    condition:
    action
    满足condition,则执行action
    action的行为有模块handler负责

当前rule设置：
    添加的时候需要注意顺序
    paragraph: p
    list: ul
    list_item: li
    heading: h2
    title: h1
存在问题：
    TODO： 当前规则处理方式过于简单
@author: cbr
"""


class Rule(object):
    type = "paragraph"  # 默认是段落

    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)
        return True

    @classmethod
    def condition(cls, block):
        return True


class ParagraphRule(Rule):
    pass


class HeadingRule(Rule):
    type = "heading"

    @classmethod
    def condition(cls, block):
        # heading 定义：
        return '\n' not in block and len(block) <= 30 and block[-1] != ":"


class TitleRule(HeadingRule):
    #  TODO 定义
    pass


class ListItemRule(Rule):

    type = "list_item"

    @classmethod
    def condition(cls, block):
        #  TODO： 多个的话
        return block.strip()[0] == "-"

    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block[1:].strip())
        handler.end(self.type)
        return True  # 当前块不需要继续由其他规则处理


class ListRule(ListItemRule):

    type = "list"
    is_inside = False

    @classmethod
    def condition(cls, block):
        # 需要该条件
        return True

    def action(self, block, handler):
        if not self.is_inside and super(ListRule, self).condition(block):
            handler.start(self.type)
            self.is_inside = True
        elif self.is_inside and not super(ListRule, self).condition(block):
            handler.end(self.type)
            self.is_inside = False

        return False


