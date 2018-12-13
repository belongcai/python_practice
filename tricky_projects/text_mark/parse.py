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
from handler import HtmlRender
from rule import *


class Parser(object):
    """
        Parser:
        实例化， handler为执行句柄，如本app体现到在html tag 输出的执行句柄
        filters 为 需要加载的过滤器
        rules 为 需要加载的规则处理器，如何对文本做跟细致的处理
            - condition
            - action
    """
    def __init__(self, handler, input_fp):
        self.handler = handler
        self.input_fp = input_fp
        self.filters = []
        self.rules = []

    def add_filter(self, pattern, name):
        def text_filter(block, handler):
            return re.sub(pattern, handler.sub(name), block)
        self.filters.append(text_filter)

    def add_rule(self, rule):
        self.rules.append(rule)

    def parse(self):
        # 调用 过滤器，规则处理器完成文本解析，并输出
        self.handler.start("document")
        for block in blocks(self.input_fp):
            for fil in self.filters:
                block = fil(block, self.handler)
            for r in self.rules:
                if r.condition(block):
                    last = r.action(block, self.handler)
                    if last:  # 表示应用的规则会最后，可直接退出
                        break
        self.handler.end("document")


class BaseTextParser(Parser):

    emphasise_pattern = r'\*(.+?)\*'
    url_pattern = r'(https?://[\.a-zA-Z0-9/]+)'  # TODO
    mail_pattern = r'([\.a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]+)'  # TODO

    def __init__(self, handler, input_fp):
        super(BaseTextParser, self).__init__(handler, input_fp)
        self.add_rule(ListRule())
        self.add_rule(ListItemRule())
        self.add_rule(HeadingRule())
        self.add_rule(ParagraphRule())
        self.add_filter(self.emphasise_pattern, "emphasise")
        self.add_filter(self.url_pattern, "url")
        self.add_filter(self.mail_pattern, "mail")


if __name__ == '__main__':
    from os import path
    cur_dir = path.dirname(path.abspath(__file__))
    test_file = path.join(cur_dir, "test_data")
    output_file = path.join(cur_dir, "output.html")
    with open(test_file) as fp:
        with open(output_file, "w") as output_fp:
            hd = HtmlRender(output_fp)
            btp = BaseTextParser(hd, fp)
            btp.parse()

