# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     config
   Description :
   Author :       zenquan
   date：          2019/9/12
-------------------------------------------------
   Change Activity:
                   2019/9/12:
-------------------------------------------------
"""
__author__ = 'zenquan'

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:root@localhost:3306/fisher'
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = True