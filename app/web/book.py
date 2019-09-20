# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     book
   Description :
   Author :       zenquan
   date：          2019/9/16
-------------------------------------------------
   Change Activity:
                   2019/9/16:
-------------------------------------------------
"""
__author__ = 'zenquan'
from flask import jsonify, request, render_template
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YushuBook
from . import web
from app.forms.book import SearcgForm
from app.view_model.book import BookCollection
import json

@web.route('/book/search', methods=['GET'])
def search():
    form = SearcgForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        book = YushuBook()

        if isbn_or_key == 'isbn':
            book.search_by_isbn(q)
        else:
            book.search_by_keyword(q,page)

        books.fill(book, q)
        # return jsonify(books.__dict__)
        # print('books', books)
        # return json.dumps(books, default=lambda o:o.__dict__)
        return render_template('index.html', data = books)
    else:
        # return jsonify({'meg': '参数校验错误'})
        return jsonify(form.errors)

@web.route('/test')
def test():
    result = {
        'name': 'zenquam',
        'age': 18
    }
    # return jsonify(result)
    return render_template('test.html', result = result)