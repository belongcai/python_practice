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
import sys


class Handler(object):

    def __init__(self, output_fp=None):
        if output_fp is None:
            output_fp = sys.stdout
        self.output_fp = output_fp

    def output(self, cont):
        # 打开句柄异常由上层处理
        self.output_fp.write(cont + "\n")

    def callback(self, prefix, name, *args):
        name = prefix + name
        method = getattr(self, name, None)
        if callable(method):
            return method(*args)  # !!! 返回结果

    def start(self, name):
        self.callback('start_', name)

    def end(self, name):
        self.callback('end_', name)

    def sub(self, name):
        def substitution(match):
            # TODO 匹配失败处理
            return self.callback('sub_', name, match)  # !!!: 这里返回结果
        return substitution


class HtmlRender(Handler):

    def start_document(self):
        self.output('<html><head><meta charset="UTF-8"><title>test</title></head><body>')

    def end_document(self):
        self.output('</body></html>')

    def start_heading(self):
        self.output("<h2>")

    def end_heading(self):
        self.output("</h2>")

    def start_paragraph(self):
        self.output("<p>")

    def end_paragraph(self):
        self.output("</p>")

    def start_list(self):
        self.output("<ul>")

    def end_list(self):
        self.output("</ul>")

    def start_list_item(self):
        self.output("<li>")

    def end_list_item(self):
        self.output("</li>")

    @classmethod
    def sub_emphasise(cls, match):
        return "<em>%s</em>" % match.group(1)

    @classmethod
    def sub_url(cls, match):
        return '<a href="%s">%s</a>' % (match.group(1), match.group(1))

    @classmethod
    def sub_mail(cls, match):
        return '<a href="mailto:%s">%s</a>' % (match.group(1), match.group(1))

    def feed(self, data):
        self.output(data)
