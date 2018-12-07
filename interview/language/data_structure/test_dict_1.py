#!/usr/bin/env python
# encoding: utf-8
"""
@author: cbr
"""
import string


if __name__ == '__main__':
    count_by_letter = dict.fromkeys(string.ascii_lowercase)
    print(count_by_letter)
