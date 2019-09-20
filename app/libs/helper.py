# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     helper
   Description :
   Author :       zenquan
   date：          2019/9/12
-------------------------------------------------
   Change Activity:
                   2019/9/12:
-------------------------------------------------
"""
__author__ = 'zenquan'

def is_isbn_or_key(word):
    """
    word: isbn或者key
    """
    # isbn13 是0-9组成的13位数字
    # isbn10 是0-9组成的10位数字，中间有-
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-'in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'

    return  isbn_or_key