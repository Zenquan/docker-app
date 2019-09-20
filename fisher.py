# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     fish
   Description :
   Author :       zenquan
   date：          2019/9/12
-------------------------------------------------
   Change Activity:
                   2019/9/12:
-------------------------------------------------
"""
__author__ = 'zenquan'

from app import create_app

app = create_app()
app.run(port=app.config['PORT'],
        debug=app.config['DEBUG'])