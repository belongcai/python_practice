#!/usr/bin/env python
# encoding: utf-8
"""
语法解析器，也是app入口的地方

类：
    Parser
    HtmlParser0
主要功能：
    对输入文本进行处理，
    过滤指定格式的文本，并进行替换，替换方式为子类实现，比如，html 就替换为 对应的标签
    对文本进行规则处理，规则匹配与输出为子类实现

@author: cbr
"""
import re
from utils import blocks


class Parser(object):
    """
        Parser:
        实例化， handler为执行句柄，如本app体现到在html tag 输出的执行句柄
        filters 为 需要加载的过滤器
        rules 为 需要加载的规则处理器，如何对文本做跟细致的处理
            - condition
            - action
    """
    def __init__(self, handler):
        self.handler = handler
        self.filters = []
        self.rules = []

    def add_filter(self, pattern, name):
        def text_filter(block, handler):
            return re.sub(pattern, handler.sub(name), block)
        self.filters.append(text_filter)

    def add_rule(self, rule):
        self.rules.append(rule)

    def parse(self, descriptor):
        # 调用 过滤器，规则处理器完成文本解析，并输出
        self.handler.start("document")
        for block in blocks(descriptor):
            for fil in self.filters:
                block = fil(block, self.handler)

            for r in self.rules:
                pass
        self.handler.end("document")


class BaseTextParser(Parser):

    emphasise_pattern = r'\*(.+?)\*', 'emphasis'

    def __init__(self, handler):
        super(BaseTextParser, self).__init__(handler)
        self.add_filter(self.emphasise_pattern, "emphasise")
        # self.add_rule()


if __name__ == '__main__':
    pass
