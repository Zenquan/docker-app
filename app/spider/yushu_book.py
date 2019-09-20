# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     yushu_book
   Description :
   Author :       zenquan
   date：          2019/9/12
-------------------------------------------------
   Change Activity:
                   2019/9/12:
-------------------------------------------------
"""
__author__ = 'zenquan'

from app.libs.httper import HTTP
from flask import current_app

class YushuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.total = 0
        self.books = []

    def search_by_isbn(self, isbn):
        url = self.isbn_url.format(isbn)
        result = HTTP.get(url)
        # print('result', result)
        self.__fill_single(result)

    def search_by_keyword(self, keyword, page=1):
        url = self.keyword_url.format(keyword,
                                     current_app.config['PER_PAGE'], self.cal_start(page))
        result = HTTP.get(url)
        self.__fill_conllection(result)

    def __fill_single(self, data):
        if data:
            self.total = 1
            # print('data', data)
            self.books.append(data)

    def __fill_conllection(self, data):
        self.total = data['total']
        self.books = data['books']

    def cal_start(self, page):
        return (page-1)*current_app.config['PER_PAGE']