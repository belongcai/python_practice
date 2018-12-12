#!/usr/bin/env python
# encoding: utf-8
"""
handler
    执行句柄
    提供，start_xxx, end_xxx, feed 等接口
HtmlRender
    提供标签输出，包括头部，尾部标签的接口
    start_xxx, end_xxx
    sub_xxx 替换成全标签形式，比如url替换成 <a href=url>url</a>
@author: cbr
"""


class Handler(object):

    def callback(self, prefix, name, *args):
        name = prefix + name
        method = getattr(self, name, None)
        if callable(method): method(*args)

    def start(self, name):
        self.callback('start_', name)

    def end(self, name):
        self.callback('end_', name)

    def sub(self, name):
        def substitution(match):
            # TODO 匹配失败处理
            self.callback('sub_', name, match)
        return substitution


class HtmlRender(Handler):

    @classmethod
    def start_paragraph(cls):
        print("<p>")

    @classmethod
    def end_paragraph(cls):
        print("</p>")

    @classmethod
    def sub_emphasise(cls, match):
        print("<em>%s</em>" % match.group(1))

    @classmethod
    def feed(cls, data):
        print(data)